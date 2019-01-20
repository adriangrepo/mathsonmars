import random

from mathsonmars.marslogger import logger
from mathsonmars.utils.numberutils import NumberUtils
from mathsonmars.utils.stringutils import StringUtils
from mathsonmars.mathslogic.messenger import Messenger
from mathsonmars.constants.modelconstants import OperatorTypes, RoleTypes
from mathsonmars.models import Role, Student, Completed
from mathsonmars.constants.userconstants import ImageTypePostfixes,\
    ProfileConstants

class AppViewUtils(object):
    
    @classmethod
    def selectFromList(cls, data_list, total_questions):
        '''data selection from a list based on questions length
        @param data_list: list of data
        @param total_questions: int
        '''
        new_list = []
        if data_list is not None and len(data_list)>0:
            new_list = data_list.copy()
            data_list_len = len(data_list)
            if data_list_len > total_questions:
                random.shuffle(new_list)
                questions_to_remove = data_list_len-total_questions 
                for i in range(questions_to_remove): 
                    new_list.pop()
            elif data_list_len < total_questions:
                questions_to_add = total_questions - data_list_len
                for i in range(questions_to_add):
                    new_list.append(random.choice(data_list))
        return new_list
         
    @classmethod
    def checkDataValidity(cls, session_id, elapsed, table_name, question_id, result, hint, help_on_question):
        session_id = NumberUtils.convertToInt(session_id)
        elapsed= NumberUtils.convertToFloat(elapsed)
        table_name= StringUtils.convertToString(table_name)
        question_id= NumberUtils.convertToInt(question_id)
        if not isinstance(result, bool) and isinstance(result, str):
            result = StringUtils.strToBool(result)
        if not isinstance(hint, bool) and isinstance(result, str):
            hint = StringUtils.strToBool(hint)
        if not isinstance(help_on_question, bool) and isinstance(result, str):
            help_on_question = StringUtils.strToBool(help_on_question)
        if (not (isinstance(question_id, int))) or (not (isinstance(session_id, int))) or (not (isinstance(elapsed,float))) or (not (isinstance(table_name, str))) \
        or (not (isinstance(question_id, int))) or (not (isinstance(result, bool))) or (not (isinstance(hint, bool))) or (not (isinstance(help_on_question, bool))):
            m = Messenger(valid=False, session=session_id, elapsed=elapsed, table=table_name, question=question_id, result=result, hint=hint, help=help_on_question)
            return m
        else:
            m = Messenger(valid=True, session=session_id, elapsed=elapsed, table=table_name, question=question_id, result=result, hint=hint, help=help_on_question)
            return m

    @classmethod
    def calcAnswers(cls, numVars, var1List, var2List, var3List, op1List, op2List):
        answers=[]
        if (numVars == 2):
            totalValues = len(var1List)
            for i in range(totalValues): 
                answer = AppViewUtils.calcAnswer2Ints(var1List[i], var2List[i], op1List[i])
                answers.append(answer)
        logger.debug("--calcAnswers() answers:{0}".format(answers))
        return answers;

    
    @classmethod
    def calcAnswer2Ints(cls, var1, var2, op):
        logger.debug(">>calcAnswer2Ints() var1:{0}, var2:{1}, op:{2}".format(var1, var2, op))
        answer = 0;
        pt1 = NumberUtils.convertToInt(var1)
        pt2 = NumberUtils.convertToInt(var2)
        if (op == OperatorTypes.MULTIPLY):
            answer = pt1*pt2
            logger.debug("--calcAnswer2Ints()  MULTIPLY answer:{0}".format(answer))
        elif (op == OperatorTypes.DIVIDE):
            if pt2 != 0:
                answer = pt1/pt2
            else:
                answer = 0
        elif (op == OperatorTypes.ADD):
            answer = pt1+pt2
        elif (op == OperatorTypes.SUBTRACT):
            answer = pt1-pt2
        return answer;
    
    @classmethod
    def getRandomListPairFromTwoLists(cls, list1, list2):
        flip = random.randint(0, 1)
        if (flip == 0):
            part_names = [random.choice(list1), random.choice(list2)]
        else:
            part_names = [random.choice(list2), random.choice(list1)]
        return part_names
    
    @classmethod
    def getRandomListTripleFromTwoLists(cls, list1, list2):
        flip = random.randint(0, 1)
        flip2 = random.randint(0, 1)
        m1 = random.choice(list1)
        m2 = random.choice(list1)
        f1 = random.choice(list2)
        f2 = random.choice(list2)
        if (flip == 0):
            if (flip2 == 0):
                if (m1 == m2):
                    index = list1.index(m1)
                    if (index< len(list1)-1):
                        m2 = list1[index+1]
                    elif (len(list1)==1):
                        m2 = m1+'a'
                    elif (index== len(list1)-1):
                        f2 = list2[index-1]
                part_names = [m1, f1, m2]
            else:
                if (f1 == f2):
                    index = list2.index(f1)
                    if (index< len(list2)-1):
                        f2 = list2[index+1]
                    elif (len(list2)==1):
                        f2 = f1+'a'
                    elif (index== len(list2)-1):
                        f2 = list2[index-1]
                part_names = [m1, f1, f2]
        else:
            if (flip2 == 0):
                if (f1 == f2):
                    index = list2.index(f1)
                    if (index< len(list2)-1):
                        f2 = list2[index+1]
                    elif (len(list2)==1):
                        f2 = f1+'a'
                    elif (index== len(list2)-1):
                        f2 = list2[index-1]
                part_names = [f1, f2, m1]
            else:
                if (m1 == m2):
                    index = list1.index(m1)
                    if (index< len(list1)-1):
                        m2 = list1[index+1]
                    elif (len(list1)==1):
                        m2 = m1+'a'
                    elif (index== len(list1)-1):
                        f2 = list2[index-1]
                part_names = [f1, m1, m2]
        return part_names
    
    @classmethod
    def getLevel(cls, db, user):
        role = db.session.query(Role).filter(Role.id == user.role_id).first()
        if role.role_name == RoleTypes.STUDENT:
            student = db.session.query(Student).filter(Student.user_id == user.id).first()
            if student is not None:
                return student.level
        return 0
    
    @classmethod
    def getPet(cls, db, user):
        role = db.session.query(Role).filter(Role.id == user.role_id).first()
        if role.role_name == RoleTypes.STUDENT:
            student = db.session.query(Student).filter(Student.user_id == user.id).first()
            if student is not None:
                return student.pet
        return ""
    
    @classmethod
    def getPetFileName(cls, db, user):
        pet_name = AppViewUtils.getPet(db, user)
        if pet_name is not None:
            pet_filename = ProfileConstants.PET_LOCATION +pet_name+ ImageTypePostfixes.PNG
            return pet_filename
        return ""
    
    @classmethod
    def getAvatarFileName(cls, user):
        avatar_name = user.avatar
        if avatar_name is not None:
            avatar_filename = ProfileConstants.AVATAR_LOCATION +avatar_name+ ImageTypePostfixes.PNG
            return avatar_filename
        return ""
    
    @classmethod
    def getProfileProperties(cls, db, user):
        pet_name = AppViewUtils.getPet(db, user)
        pet_filename = AppViewUtils.getPetFileName(db, user)       
        avatar_filename = AppViewUtils.getAvatarFileName(user)
        return {'pet_name': pet_name, 'pet_filename': pet_filename, 'avatar_filename': avatar_filename}
    
    @classmethod
    def getCompleted(cls, db, user, activities):
        activity_ids = []
        for activ in activities:
            activity_ids.append(activ.id)
        valueCounts = {}
        completed_activity_ids = []
        completed = db.session.query(Completed).filter(Completed.user_id==user.id).filter(Completed.activity_id.in_(activity_ids)).all()
        for complete in completed:
            completed_activity_ids.append(complete.activity_id)
        valueCounts = {x:completed_activity_ids.count(x) for x in completed_activity_ids}
        return valueCounts
