from urllib.parse import urlparse, urljoin
from sqlalchemy import exc, desc
from flask import render_template, flash, g, request, redirect, url_for, json, jsonify
from flask.ext.login import login_required, current_user
from mathsonmars.models import db, Activity, BoxMethod,\
    Role, Student, FunChunks, Topic, Category, Strategy, FriendlyAndFix, Results,\
    UserSessionTracker, NumberBonds, Memorize, BoxModelMADS, User, Completed
from mathsonmars.marslogger import logger
from mathsonmars.constants.modelconstants import CategoryConstants,\
    ActivityTypeConstants, RoleTypes, StrategyNames, StrategyDescriptions,\
    StrategyNameQualifiers, ResultClassification
from mathsonmars.mathslogic.problemgenerator import ProblemGenerator
from mathsonmars.utils.numberutils import NumberUtils
from mathsonmars.application import appl_view
from mathsonmars.mathslogic.messenger import Messenger
import random
import datetime
from mathsonmars.constants import modelconstants
import itertools
from mathsonmars.application.applviewutils import AppViewUtils
from mathsonmars.utils.listutils import ListUtils
from mathsonmars.constants.namesstr import NamesStrConstants
from mathsonmars.constants.userconstants import ProfileConstants,\
    ImageTypePostfixes

#see https://security.openstack.org/guidelines/dg_avoid-unvalidated-redirects.html
def is_safe_redirect_url(target):
  host_url = urlparse(request.host_url)
  redirect_url = urlparse(urljoin(request.host_url, target))
  return redirect_url.scheme in ('http', 'https') and \
    host_url.netloc == redirect_url.netloc


def get_safe_redirect():
  url =  request.args.get('next')
  if url and is_safe_redirect_url(url):
    return url

  url = request.referrer
  if url and is_safe_redirect_url(url):
    return url

  return '/'
        
@appl_view.before_request
def before_request():
    g.user = current_user
        
@appl_view.route('/student_home')
@login_required
def student_home():
    logger.debug(">>student_home")
    avatar_filename = AppViewUtils.getAvatarFileName(g.user)
    return render_template('user/student_home.html', avatar_filename=avatar_filename)

@appl_view.route('/user_area')
@login_required
def user_area():
    logger.debug(">>user_area")
    user = g.user
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    if role.role_name == RoleTypes.STUDENT:
        return redirect(url_for("appl_view.student_home"))
    elif role.role_name == RoleTypes.PARENT or role.role_name == RoleTypes.GUARDIAN or role.role_name == RoleTypes.TEACHER:
        return redirect(url_for("report_view.report"))
    return redirect(url_for("main_view.index"))

@appl_view.route('/level')
@login_required
def level():
    logger.debug(">>level")
    user = g.user
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    avatar_filename = AppViewUtils.getAvatarFileName(g.user)
    if role.role_name == RoleTypes.STUDENT:
        student = db.session.query(Student).filter(Student.user_id == user.id).first()
        level_value=student.level
        #first filter by logged in user properties
    
        activities = db.session.query(Activity).filter(Activity.level==level_value).all()
        topics = []
        for activity in activities:
            topic = db.session.query(Topic).filter(Topic.id==activity.topic_id).first()
            topics.append(topic)
        
        topics_set = list(set(topics))
        #sort list in place
        topics_set.sort(key=lambda x: x.order, reverse=False)
        logger.debug("--level() level_value:{0}, topics_set:{1}".format(level_value, topics_set))
        for topic in topics_set:
            logger.debug("--level() topic.id:{0}, topic.name:{1}".format(topic.id, topic.name))
        logger.debug("--level() return render_template('core/level_topics.html")
        return render_template('core/level_topics.html', level = level_value, topics=topics_set, avatar_filename=avatar_filename)
    else:
        logger.debug("--level() return render_template('user/student_home.html")
        return render_template('user/student_home.html', avatar_filename=avatar_filename)


    
@appl_view.route('/topic/<int:level_value>/<int:topic_id>')
@login_required
def activities(level_value, topic_id):
    logger.debug(">>activities level:{0}, category_id:{1}".format(level_value, topic_id))
    avatar_filename = AppViewUtils.getAvatarFileName(g.user)
    category_ids = []

    categories = db.session.query(Category).filter(Category.topic_id==topic_id).all()
    for category in categories:
        category_ids.append(category.id)
    activities = db.session.query(Activity).filter(Activity.level==level_value).filter(Activity.category_id.in_(category_ids)).order_by(Activity.topic_progress).all()
    #sort list in place
    activities.sort(key=lambda x: x.topic_progress, reverse=False)
    activity_strategy_list = []
    valueCounts = AppViewUtils.getCompleted(db, g.user, activities)
    values = valueCounts.keys()
    for activity in activities:
        count = 0
        strategy_id = activity.strategy_id
        strategy = db.session.query(Strategy).filter(Strategy.id==strategy_id).first()
        if activity.id in values:
            count = valueCounts[activity.id]
        activity_strategy_list.append((activity, strategy, count))
    if (activity.level == 1):
        return render_template('core/category_activities_level1.html', activity_strategy_list=activity_strategy_list, avatar_filename=avatar_filename) 
    elif(activity.level == 2):
        return render_template('core/category_activities_level2.html', activity_strategy_list=activity_strategy_list, avatar_filename=avatar_filename) 
    elif (activity.level == 3):
        return render_template('core/category_activities_level3.html', activity_strategy_list=activity_strategy_list, avatar_filename=avatar_filename) 
    elif(activity.level == 4):
        return render_template('core/category_activities_level4.html', activity_strategy_list=activity_strategy_list, avatar_filename=avatar_filename) 
    else:
        logger.error("category_activities for level:{0} not found".format(level_value))
        return render_template('user/student_home.html', avatar_filename=avatar_filename)

    
@appl_view.route('/activity/<string:activity_url>')
@login_required
def activity(activity_url):
    activity = db.session.query(Activity).filter(Activity.url_name==activity_url).first()
    if activity is not None:
        avatar_filename = AppViewUtils.getAvatarFileName(g.user)
        pet_filename = AppViewUtils.getPetFileName(db, g.user)
        activity_title = "";
        activity_description = "";
        strategy = db.session.query(Strategy).filter(Strategy.id==activity.strategy_id).first()
        category = db.session.query(Category).filter(Category.id==activity.category_id).first()
        start_time = datetime.datetime.utcnow()
        session_tracker = db.session.query(UserSessionTracker).filter(UserSessionTracker.user_id==current_user.id).order_by(desc(UserSessionTracker.login)).first()
        if session_tracker is None:
            session_tracker_id = 0
        else:
            session_tracker_id = session_tracker.id
        logger.debug("--activity() strategy.name: "+strategy.name)
        if strategy.name == StrategyNames.BOX_METHOD:
            activity_json = getBoxMethodData(session_tracker_id, start_time, activity, category, strategy)
            if activity_json is not None:
                logger.debug("--activity() BOX_METHOD activity_json: "+activity_json)
                activity_title = StrategyNames.BOX_METHOD
                activity_description = StrategyDescriptions.BOX_BASIC
                return render_template('core/activity.html', activity_json = activity_json, activity_title=activity_title, activity_description=activity_description, pet_filename=pet_filename, avatar_filename=avatar_filename)    
        elif strategy.name == StrategyNames.FUN_CHUNKS:
            activity_json = getFunChunksData(session_tracker_id, start_time, activity, category, strategy)
            if activity_json is not None:
                activity_title = StrategyNames.FUN_CHUNKS
                if category.name == CategoryConstants.ADDITION:
                    if strategy.qualifier == StrategyNameQualifiers.SINGLE_DIGIT:
                        activity_description = StrategyDescriptions.FUN_CHUNKS_SINGLE_DIGIT
                    else:
                        activity_description = StrategyDescriptions.FUN_CHUNKS_ADDITION
                elif category.name == CategoryConstants.SUBTRACTION:
                    activity_description = StrategyDescriptions.FUN_CHUNKS_SUBTRACTION
                return render_template('core/activity.html', activity_json = activity_json, activity_title=activity_title, activity_description=activity_description, pet_filename=pet_filename, avatar_filename=avatar_filename)    
        elif strategy.name == StrategyNames.FRIENDLY_AND_FIX:
            activity_json = getFriendyAndFixData(session_tracker_id, start_time, activity, category, strategy)
            if activity_json is not None:
                activity_title = StrategyNames.FRIENDLY_AND_FIX
                if category.name == CategoryConstants.ADDITION:
                    activity_description = StrategyDescriptions.FRIENDLY_AND_FIX_ADDITION
                elif category.name == CategoryConstants.SUBTRACTION:
                    activity_description = StrategyDescriptions.FRIENDLY_AND_FIX_SUBTRACTION
                return render_template('core/activity.html', activity_json = activity_json, activity_title=activity_title, activity_description=activity_description, pet_filename=pet_filename, avatar_filename=avatar_filename)    
        elif strategy.name == StrategyNames.NUMBER_BONDS:
            activity_json = getNumberBondsData(session_tracker_id, start_time, activity, category, strategy)
            if activity_json is not None:
                return render_template('core/activity.html', activity_json = activity_json, activity_title=activity_title, activity_description=activity_description, pet_filename=pet_filename, avatar_filename=avatar_filename)    
        elif strategy.name == StrategyNames.MEMORIZE:
            activity_json = getMemorizeActivityData(session_tracker_id, start_time, activity, category, strategy)
            if activity_json is not None:
                return render_template('core/activity.html', activity_json = activity_json, activity_title=activity_title, activity_description=activity_description, pet_filename=pet_filename, avatar_filename=avatar_filename)    
        return render_template('core/activity_pending.html', avatar_filename=avatar_filename)
    else:    
        return render_template('error/404.html')
    
@appl_view.route('/activity_summary/<int:corrects>/<int:total>/<time_expired>')
@login_required
def activity_summary(corrects, total, time_expired):  
    assert isinstance(corrects, int), "corrects is int"
    assert isinstance(total, int), "total is int"
    logger.debug(">>activity_summary  corrects:{0} total:{1}, corrects/total:{2}".format(corrects, total, corrects/total) )
    message = ""
    if total != 0:
        avatar_filename = AppViewUtils.getAvatarFileName(g.user)
        logger.debug(">>activity_summary total != 0 total:{0}".format(total))
        if (time_expired == True):
            message = ResultClassification.TIME_EXPIRED+"\n "
        if (corrects/total) == 0:
            message = message+ResultClassification.KEEP_TRYING
        elif (corrects/total) <= 0.1:
            message = message+ResultClassification.YOU_ARE_LEARNING
        elif (corrects/total) <= 0.3:
            message = message+ResultClassification.GOOD_TRY
        elif (corrects/total) <= 0.5:
            message = message+ResultClassification.WELL_DONE
        elif (corrects/total) <= 0.7:
            message = message+ResultClassification.GREAT_WORK
        elif (corrects/total) <= 0.8:
            message = message+ResultClassification.GREAT_WORK
        elif (corrects/total) <= 0.9:
            message = message+ResultClassification.EXCELLENT
        elif (corrects/total) <= 1.01:
            message = message+ResultClassification.PERFECT
        else:
            logger.debug(">>activity_summary not picked up total:{0}, corrects:{1}, corrects/total:{2}".format(total, corrects, corrects/total))
        return render_template('core/activity_summary.html', congrats = message, ncorrect = corrects, ntotal = total, avatar_filename=avatar_filename);  
    else:
        logger.error("--activity_summary() error total == 0")
        return url_for("appl_view.level")
    
@appl_view.route('/activity_completed/', methods=['POST'])
@login_required
def activity_completed():
    logger.debug(">>activity_completed()")
    #for h in request.headers:
    #    logger.debug("--activity_completed() Header:{0} ".format(h)) 
    if (request.headers['Content-Type'].startswith('application/json')):
        logger.debug(">>activity_completed() JSON Message:{0}".format(json.dumps(request.json)))
        corrects = []
        time_expired = False;
        avatar_filename = AppViewUtils.getAvatarFileName(g.user)
        try:
        
            session_id = request.json['session_id']
            start_time = request.json['start_time']
            results = request.json['results']
            elapsed_times = request.json['elapsed_times']
            hints = request.json['hints']
            helps = request.json['helps']
            category_name = request.json['category_name']
            activity_id = request.json['activity_id']
            activity_name = request.json['activity_name']
            strategy_name = request.json['strategy_name']
            activity_level_progress = request.json['activity_level_progress']
            activity_level = request.json['activity_level']
            question_ids = request.json['question_ids']
            time_expired = request.json['time_expired']
            if question_ids is None:
                logger.error("--activity_completed question_ids is None")
            elif len(question_ids)==0:
                logger.error("--activity_completed len(question_ids)==0")
            #too many sessions have an id of zero, just allowing it
            if NumberUtils.representsInt(session_id):
                persistResults(session_id, start_time, results, elapsed_times, question_ids, hints, helps, \
                               category_name, activity_id, activity_name, strategy_name, activity_level_progress, activity_level)
            else:
                logger.error("--activity_completed() invalid session_id:{0}".format(session_id))
                #redirect(url_for("auth_view.logout"))
            for result in results:
                if result == True:
                    corrects.append(True)
        except TypeError as te:
            logger.error("--activity_completed() error: {0}".format(te))
        except KeyError as ke:
            logger.error("--activity_completed() error: {0}".format(ke))
        return url_for("appl_view.activity_summary", corrects = len(corrects), total = len(question_ids), time_expired = time_expired, avatar_filename=avatar_filename) 
    else:
        return url_for('error/404.html')
    
def persistResults(session_id, start_time, results, elapsed_times, question_ids, hints, helps, category_name, \
                   activity_id, activity_name, strategy_name, activity_level_progress, activity_level):
    '''
    @param session_id
    @param start_time
    @param results
    @param elapsed_times
    @param question_ids_list: python list 
    @param hints
    @param helps
    @param category_name
    @param activity_id
    @param activity_name
    @param strategy_name
    @param activity_level_progress
    @param activity_level
    '''
    assert isinstance(session_id, int), "Wrong type: {0}".format(session_id)
    assert isinstance(results, list), "Wrong type: {0}".format(results)
    assert isinstance(elapsed_times, list), "Wrong type: {0}".format(elapsed_times)
    assert isinstance(question_ids, list), "Wrong type: {0}".format(question_ids)
    assert isinstance(hints, list), "Wrong type: {0}".format(hints)
    assert isinstance(helps, list), "Wrong type: {0}".format(helps)
    assert isinstance(category_name, str), "Wrong type: {0}".format(category_name)
    assert isinstance(activity_id, int), "Wrong type: {0}".format(activity_id)
    assert isinstance(activity_name, str), "Wrong type: {0}".format(activity_name)
    assert isinstance(strategy_name, str), "Wrong type: {0}".format(strategy_name)
    assert isinstance(activity_level_progress, int), "Wrong type: {0}".format(activity_level_progress)
    assert isinstance(activity_level, int), "Wrong type: {0}".format(activity_level)
    assert len(question_ids)>=len(hints)
    assert len(question_ids)>=len(helps)
    table_name = modelconstants.getTableNameForStrategy(strategy_name);
    if NumberUtils.representsInt(session_id):
        hint_vals = NumberUtils.reconstructBooleanList(len(question_ids), hints)
        help_vals = NumberUtils.reconstructBooleanList(len(question_ids), helps)
        time_completed = datetime.datetime.now()
        logger.debug("--persistResults() results:{0}, elapsed_times:{1}, question_ids:{2}".format(results, elapsed_times, question_ids))
        for i, (result, elapsed, question_id) in enumerate(zip(results, elapsed_times, question_ids)):
            hint = hint_vals[i]
            help_on_question = help_vals[i]
            if NumberUtils.representsInt(question_id):
                messenger = AppViewUtils.checkDataValidity(session_id, elapsed, table_name, question_id, result, hint, help_on_question)
                if (messenger.valid == True):
                    results = Results(user_id=current_user.id, session_tracker_id=messenger.session, \
                                      time_spent=messenger.elapsed, activity_id=activity_id, table_name=messenger.table, question_id=messenger.question, correct=messenger.result, \
                                      hint=messenger.hint, help=messenger.help, time_completed=time_completed)
                    try:
                        db.session.add(results)
                        db.session.commit()
                    except exc.SQLAlchemyError as e:
                        logger.error("--persistResults() error commiting data:{0}".format(e))
                else:
                    logger.error("--persistResults() invalid (messenger) data")
            else:
                logger.error("--persistResults() question_id invalid:{0}".format(question_id))
        completed = Completed(user_id=current_user.id, activity_id=activity_id, time_completed=time_completed)
        try:
            db.session.add(completed)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            logger.error("--persistResults() error commiting data:{0}".format(e))
    else:
      logger.error("--persistResults() error session_id:{0}".format(session_id))  
    
@appl_view.route('/methods')
@login_required
def methods():
    avatar_filename = AppViewUtils.getAvatarFileName(g.user)
    return render_template('core/methods.html', avatar_filename=avatar_filename)

@appl_view.route('/profile')
@login_required
def profile():
    user = g.user
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    if role.role_name == RoleTypes.STUDENT:
        student = db.session.query(Student).filter(Student.user_id == user.id).first()
        if student is not None:
            level_value=student.level
            petProperties = AppViewUtils.getProfileProperties(db, user)
            return render_template('core/profile.html', level_value=level_value, pet=petProperties['pet_name'], pet_filename = petProperties['pet_filename'], avatar_filename=petProperties['avatar_filename'])
        else:
            return redirect(url_for("appl_view.user_area"))
    else:
        return redirect(url_for("appl_view.user_area"))
    
@appl_view.route('/set_avatar/<string:avatar_name>')
@login_required
def set_avatar(avatar_name):
    logger.debug(">>set_avatar")
    user = g.user
    try:
        db.session.query(User).filter(User.id == user.id).update({'avatar': avatar_name})
        db.session.commit()
    except AttributeError as e:
            logger.debug(">>set_avatar() error:{0}".format(e))
    level = AppViewUtils.getLevel(db, user)
    petProperties = AppViewUtils.getProfileProperties(db, user)
    return render_template('core/profile.html', level_value=level, pet=petProperties['pet_name'], pet_filename = petProperties['pet_filename'], avatar_filename=petProperties['avatar_filename'])

@appl_view.route('/set_pet/<string:pet_name>')
@login_required
def set_pet(pet_name):
    logger.debug(">>set_pet")
    user = g.user
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    if role.role_name == RoleTypes.STUDENT:
        try:
            db.session.query(Student).filter(Student.user_id == user.id).update({'pet': pet_name})
            db.session.commit()
        except AttributeError as e:
            logger.debug(">>set_pet() error:{0}".format(e))
    level = AppViewUtils.getLevel(db, user)
    petProperties = AppViewUtils.getProfileProperties(db, user)
    return render_template('core/profile.html', level_value=level, pet=petProperties['pet_name'], pet_filename = petProperties['pet_filename'], avatar_filename=petProperties['avatar_filename'])


@appl_view.route('/set_level/<string:level_value>')
@login_required
def set_level(level_value):
    logger.debug(">>set_level")
    user = g.user
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    if role.role_name == RoleTypes.STUDENT:
        if NumberUtils.representsInt(level_value):
            if (int(level_value) >= 1) and (int(level_value) <= 6):
                try:
                    db.session.query(Student).filter(Student.user_id == user.id).update({'level': int(level_value)})
                    db.session.commit()
                except AttributeError as e:
                    logger.debug(">>set_level() error:{0}".format(e))
            petProperties = AppViewUtils.getProfileProperties(db, user)
            return render_template('core/profile.html', level_value=int(level_value), pet=petProperties['pet_name'], pet_filename = petProperties['pet_filename'], avatar_filename=petProperties['avatar_filename'])
    return redirect(url_for("appl_view.user_area"))

#Data gatherers
def getMemorizeActivityData(session_tracker_id, start_time, activity, category, strategy):
    logger.debug("--getMemorizeActivityData()")
    activity_json = None
    total_questions = activity.total_questions
    memorize = db.session.query(Memorize).filter(Memorize.activity_id==activity.id).all()
    if (memorize is not None) and (len(memorize)>0):
        memorize_list = AppViewUtils.selectFromList(memorize, total_questions)
        var1_list = []
        var2_list = []
        var3_list = []
        operator1_list = []
        operator2_list = []
        question_ids = []     
        num_vars = memorize[0].variables    
        for item in memorize_list:
            var1_list.append(item.var1)
            var2_list.append(item.var2)
            operator1_list.append(item.operator1)
            question_ids.append(item.id)
        if memorize[0].variables == 3:
            var3_list.append(item.var3)
            operator2_list.append(item.operator2)
        answers = AppViewUtils.calcAnswers(num_vars, var1_list, var2_list, var3_list, operator1_list, operator2_list)
        answers_result = ','.join(map(str, answers))
        var1_result = ','.join(map(str, var1_list))
        var2_result = ','.join(map(str, var2_list))
        var3_result = ','.join(map(str, var3_list))
        operator1_result = ','.join(map(str, operator1_list))
        operator2_result = ','.join(map(str, operator2_list))
        activity_title = StrategyNames.MEMORIZE
        if category.name == CategoryConstants.MULTIPLICATION:
            activity_description = StrategyDescriptions.MEMORIZE
        question_result = [activity_description];
        obj = {'session_id': session_tracker_id, 'start_time' : start_time, 'category_name' : category.name, \
               'activity_name' : activity.name, \
                'strategy_name' : strategy.name, 'activity_level' : activity.level, \
                'activity_progress' : activity.topic_progress, 'time_limit' : activity.time_limit, \
                'total_questions' : activity.total_questions, 'answer_format' : activity.answer_format, \
                'questions' : question_result, 'answers' : answers_result, 'activity_variables' : '',\
                'question_ids' : question_ids, \
                'strategy_qualifier' : strategy.qualifier, 'activity_id' : activity.id, \
                'data1' : var1_result, \
                'data2' : var2_result, 'data3' : var3_result, 'data4' : operator1_result, \
                'data5' : operator2_result, 'data6' : num_vars, 'data7' : '', 'data8' : '', 'data9' : '', 'data10' : ''}
        activity_json = json.dumps(obj)
    return activity_json

def getNumberBondsData(session_tracker_id, start_time, activity, category, strategy):
    logger.debug("--activity() NUMBER_BONDS")
    activity_json = None
    total_questions = activity.total_questions
    number_bonds = db.session.query(NumberBonds).filter(NumberBonds.activity_id==activity.id).all()
    if (number_bonds is not None) and (len(number_bonds)>0):
        number_bonds_list = AppViewUtils.selectFromList(number_bonds, total_questions)
        numberbond_type = number_bonds[0].numberbond_type
        whole_list = []
        part1_list = []
        part2_list = []     
        question_ids = []          
        for number_bond in number_bonds_list:
            whole_list.append(number_bond.whole)
            part1_list.append(number_bond.part1)
            part2_list.append(number_bond.part2)
            question_ids.append(number_bond.id)
        whole_result = ','.join(map(str, whole_list))
        part1_result = ','.join(map(str, part1_list))
        part2_result = ','.join(map(str, part2_list))
        activity_title = StrategyNames.NUMBER_BONDS
        if category.name == CategoryConstants.ADDITION:
            if strategy.qualifier == StrategyNameQualifiers.COUNTERS:
                activity_description = StrategyDescriptions.NUMBER_BONDS_COUNTERS
            elif strategy.qualifier == StrategyNameQualifiers.WHOLE_PART:
                activity_description = StrategyDescriptions.NUMBER_BONDS_WHOLE_PART
            elif strategy.qualifier == StrategyNameQualifiers.PART_PART:
                activity_description = StrategyDescriptions.NUMBER_BONDS_PART_PART
        elif category.name == CategoryConstants.SUBTRACTION:
            logger.debug("Number bond subtraction not implemented")
        question_result = [activity_description];
        obj = {'session_id': session_tracker_id, 'start_time' : start_time, 'category_name' : category.name, \
               'activity_name' : activity.name, \
                'strategy_name' : strategy.name, 'activity_level' : activity.level, \
                'activity_progress' : activity.topic_progress, 'time_limit' : activity.time_limit, \
                'total_questions' : activity.total_questions, 'answer_format' : activity.answer_format, \
                'questions' : question_result, 'answers' : '', 'activity_variables' : '',\
                'question_ids' : question_ids, \
                'strategy_qualifier' : strategy.qualifier, 'activity_id' : activity.id, \
                'data1' : whole_result, \
                'data2' : part1_result, 'data3' : part2_result, 'data4' : '', \
                'data5' : '', 'data6' : '', 'data7' : '', 'data8' : '', 'data9' : '', 'data10' : ''}
        activity_json = json.dumps(obj)
    return activity_json

def getFunChunksData(session_tracker_id, start_time, activity, category, strategy):
    logger.debug("--activity() FUN_CHUNKS")
    activity_json = None
    total_questions = activity.total_questions
    fun_chunks = db.session.query(FunChunks).filter(FunChunks.activity_id==activity.id).all()
    if fun_chunks is not None:
        fun_chunk_list = AppViewUtils.selectFromList(fun_chunks, total_questions)
        question_list = []
        line_positions_list = []
        jump_values_list = []
        stage1_question_list = []
        answer_list = []
        flip_list = []
        question_ids = []
        num_variables = activity.num_variables
        
        for fun_chunk in fun_chunk_list:
            question_list.append(fun_chunk.question)
            line_positions_list.append(fun_chunk.line_positions)
            jump_values_list.append(fun_chunk.jump_values)
            stage1_question_list.append(fun_chunk.stage1_question)
            answer_list.append(fun_chunk.answer)
            flip_list.append(fun_chunk.flip)
            question_ids.append(fun_chunk.id)
        question_result = ','.join(map(str, question_list))
        line_positions_result = ','.join(map(str, line_positions_list))
        jump_values_result = ','.join(map(str, jump_values_list))
        stage1_question_result = ','.join(map(str, stage1_question_list))
        answer_result = ','.join(map(str, answer_list))
        flip_result = ','.join(map(str, flip_list))
        
        obj = {'session_id': session_tracker_id, 'start_time' : start_time, 'category_name' : category.name, \
               'activity_name' : activity.name, \
                'strategy_name' : strategy.name, 'activity_level' : activity.level, \
                'activity_progress' : activity.topic_progress, 'time_limit' : activity.time_limit, \
                'total_questions' : activity.total_questions, 'answer_format' : activity.answer_format, \
                'questions' : question_result, 'answers' : answer_result, 'activity_variables' : num_variables,\
                'question_ids' : question_ids, 'activity_id' : activity.id, \
                'data1' : jump_values_result, \
                'data2' : stage1_question_result, 'data3' : line_positions_result, 'data4' : flip_result, \
                'data5' : "", 'data6' : '', 'data7' : '', 'data8' : '', 'data9' : '', 'data10' : ''}
        activity_json = json.dumps(obj)
    return activity_json

def getFriendyAndFixData(session_tracker_id, start_time, activity, category, strategy):
    logger.debug("--activity() FRIENDLY_AND_FIX")
    activity_json = None
    total_questions = activity.total_questions
    friendly_and_fixes = db.session.query(FriendlyAndFix).filter(FriendlyAndFix.activity_id==activity.id).all()
    if friendly_and_fixes is not None:
        friendly_and_fix_list = AppViewUtils.selectFromList(friendly_and_fixes, total_questions)
        question_list = []
        line_positions_list = []
        jump_values_list = []
        stage1_question_list = []
        answer_list = []
        flip_list = []
        question_ids = []
        num_variables = activity.num_variables
        activity_description = ""
        for friendly_and_fix in friendly_and_fix_list:
            question_list.append(friendly_and_fix.question)
            line_positions_list.append(friendly_and_fix.line_positions)
            jump_values_list.append(friendly_and_fix.jump_values)
            stage1_question_list.append(friendly_and_fix.stage1_question)
            answer_list.append(friendly_and_fix.answer)
            flip_list.append(friendly_and_fix.flip)
            question_ids.append(friendly_and_fix.id)
            
        question_result = ','.join(map(str, question_list))
        line_positions_result = ','.join(map(str, line_positions_list))
        jump_values_result = ','.join(map(str, jump_values_list))
        stage1_question_result = ','.join(map(str, stage1_question_list))
        answer_result = ','.join(map(str, answer_list))
        flip_result = ','.join(map(str, flip_list))
        
        obj = {'session_id': session_tracker_id, 'start_time' : start_time, 'category_name' : category.name, \
               'activity_name' : activity.name, \
                'strategy_name' : strategy.name, 'activity_level' : activity.level, \
                'activity_progress' : activity.topic_progress, 'time_limit' : activity.time_limit, \
                'total_questions' : activity.total_questions, 'answer_format' : activity.answer_format, \
                'questions' : question_result, 'answers' : answer_result, 'activity_variables' : num_variables,\
                'question_ids' : question_ids, 'activity_id' : activity.id, \
                'data1' : jump_values_result, \
                'data2' : stage1_question_result, 'data3' : line_positions_result, 'data4' : flip_result, \
                'data5' : "", 'data6' : '', 'data7' : '', 'data8' : '', 'data9' : '', 'data10' : ''}
        activity_json = json.dumps(obj)
    return activity_json
            
def getBoxMethodData(session_tracker_id, start_time, activity, category, strategy):
    logger.debug("--getBoxMethodData()")
    total_questions = activity.total_questions
    activity_json = None
    question_list = []
    hints_list = []
    total_values = []
    part_values = []
    part_name_associations = []
    answer_list = []
    flip_list = []
    question_ids = []
    num_variables = activity.num_variables
    part_value_types = []
    part_names_list = []
    part_name_association_result = []
    box_things_list = []
    
    if (strategy.qualifier == StrategyNameQualifiers.BASIC_ADDITION) or (strategy.qualifier == StrategyNameQualifiers.BASIC_SUBTRACTION) \
    or (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_ADDITION) or (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION) \
    or (strategy.qualifier == StrategyNameQualifiers.BASIC_MULTIPLICATION) or (strategy.qualifier == StrategyNameQualifiers.BASIC_DIVISION) \
    or (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION):
        box_models = db.session.query(BoxModelMADS).filter(BoxModelMADS.activity_id==activity.id).all()
        box_models_list = AppViewUtils.selectFromList(box_models, total_questions)
        
        if box_models is not None:
            if (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_ADDITION) or \
                (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION) or \
                (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION):
                male_names = NamesStrConstants.MALE_NAMES_STR
                female_names = NamesStrConstants.FEMALE_NAMES_STR
                male_names_list = male_names.split(",")
                female_names_list = female_names.split(",")
                
            if (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION):
                box_things = NamesStrConstants.BOX_ACTIVITY_THINGS.split(",")
                logger.debug("box_things:{0}".format(box_things))
            
            for model in box_models_list:
                question_list.append(model.question)
                hints_list.append(model.hint)
                total_values.append(model.total_value)
                part_value_types.append(model.part_value_types)
                answer_list.append(model.answer)
                question_ids.append(model.id)
                part_values.append(model.part_values)
                part_name_associations.append(model.part_name_association)
                if (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_ADDITION) or \
                (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION) or \
                (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION):
                    if (num_variables==2):
                          part_names = AppViewUtils.getRandomListPairFromTwoLists(male_names_list, female_names_list)
                    elif (num_variables==3):
                          part_names = AppViewUtils.getRandomListTripleFromTwoLists(male_names_list, female_names_list)  
                    #Use extend rather than append-Extends list by appending elements from the iterable
                    part_names_list.extend(part_names)
                if (strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION):
                    box_things_list.append(random.choice(box_things))
            
            question_result = ','.join(map(str, question_list))
            hints_result = ','.join(map(str, hints_list))
            total_values_result = ','.join(map(str, total_values))
            part_value_types_result = ','.join(map(str, part_value_types))
            answer_result = ','.join(map(str, answer_list))
            part_names_result = ','.join(map(str, part_names_list))
            part_values_result = ','.join(map(str, part_values))
            part_name_association_result = ','.join(map(str, part_name_associations))
            logger.debug("--activity() box_things_list:{0}".format(box_things_list))
            box_things_result = ','.join(map(str, box_things_list))
            logger.debug("--activity() box_things_result:{0}".format(box_things_result))
            
            logger.debug("--activity() question_result:{0}, len(part_names_result):{1}, len(part_values_result):{2}".format(question_result, len(part_names_result), len(part_values_result)))
            obj = {'session_id': session_tracker_id, 'start_time' : start_time, 'category_name' : category.name, \
                   'activity_name' : activity.name, \
                    'strategy_name' : strategy.name, 'activity_level' : activity.level, \
                    'activity_progress' : activity.topic_progress, 'time_limit' : activity.time_limit, \
                    'total_questions' : activity.total_questions, 'answer_format' : activity.answer_format, \
                    'questions' : question_result, 'answers' : answer_result, 'activity_variables' : num_variables,\
                    'question_ids' : question_ids, \
                    'strategy_qualifier' : strategy.qualifier, 'activity_id' : activity.id, \
                    'data1' : hints_result, \
                    'data2' : total_values_result, 'data3' : part_value_types_result, 'data4' : part_names_result, \
                    'data5' : part_values_result, 'data6' : part_name_association_result, 'data7' : box_things_result, 'data8' : '', 'data9' : '', 'data10' : ''}
            activity_json = json.dumps(obj)
    return activity_json