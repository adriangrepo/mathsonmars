'''
Created on 4 Feb 2016

@author: a
'''
from mathsonmars.models import Activity, BoxMethod, \
    User, Role, Student, FunChunks, Strategy, Topic, Category, \
    FriendlyAndFix, NumberBonds, Memorize, BoxModelMADS
from mathsonmars.constants.modelconstants import StrategyNames, StrategyDescriptions,\
    StrategyExamples, ConstraintConstants,\
    ActivityTypeConstants, AnswerFormat, RoleTypes,\
    DefaultUserName, CategoryConstants, TopicConstants, StrategyNameQualifiers,\
    NumberBondTypes

import logging
import os
import random
import datetime
from mathsonmars.constants.userconstants import ProfileConstants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def setup_strategies(db):
    logger.debug(">>setup_strategies()")
    strategy_count = Strategy(name = StrategyNames.COUNT, qualifier = "",\
                                 description = StrategyDescriptions.COUNT)
    db.session.add(strategy_count)

    strategy_number_bonds_counters = Strategy(name = StrategyNames.NUMBER_BONDS, qualifier = StrategyNameQualifiers.COUNTERS,\
                                 description = StrategyDescriptions.NUMBER_BONDS_COUNTERS)
    db.session.add(strategy_number_bonds_counters)
    
    strategy_number_bonds_whole_part = Strategy(name = StrategyNames.NUMBER_BONDS, qualifier = StrategyNameQualifiers.WHOLE_PART,\
                                 description = StrategyDescriptions.NUMBER_BONDS_WHOLE_PART)
    db.session.add(strategy_number_bonds_whole_part)
    
    strategy_number_bonds_part_part = Strategy(name = StrategyNames.NUMBER_BONDS, qualifier = StrategyNameQualifiers.PART_PART,\
                                 description = StrategyDescriptions.NUMBER_BONDS_PART_PART)
    db.session.add(strategy_number_bonds_part_part)
    
    strategy_patterns = Strategy(name = StrategyNames.PATTERNS, \
                                  description = StrategyDescriptions.PATTERNS)
    db.session.add(strategy_patterns)
    
    example_csv = ",".join(StrategyExamples.COUNT_ON)
    strategy_count_on = Strategy(name = StrategyNames.COUNT_ON, description = StrategyDescriptions.COUNT_ON, examples=example_csv)
    db.session.add(strategy_count_on)
    
    example_csv = ",".join(StrategyExamples.COUNT_BACK)
    strategy = Strategy(name = StrategyNames.COUNT_BACK, description = StrategyDescriptions.COUNT_BACK, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FUN_CHUNKS_SINGLE_DIGIT)
    strategy = Strategy(name = StrategyNames.FUN_CHUNKS, qualifier = StrategyNameQualifiers.SINGLE_DIGIT, description = StrategyDescriptions.FUN_CHUNKS_SINGLE_DIGIT, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FUN_CHUNKS_SINGLE_AND_SINGLE)
    strategy = Strategy(name = StrategyNames.FUN_CHUNKS, qualifier = StrategyNameQualifiers.SINGLE_AND_SINGLE, description = StrategyDescriptions.FUN_CHUNKS_ADDITION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FUN_CHUNKS_SINGLE_AND_DOUBLE)
    strategy = Strategy(name = StrategyNames.FUN_CHUNKS, qualifier = StrategyNameQualifiers.SINGLE_AND_DOUBLE, description = StrategyDescriptions.FUN_CHUNKS_ADDITION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FUN_CHUNKS_SUBTRACTION_SINGLE_AND_DOUBLE)
    strategy = Strategy(name = StrategyNames.FUN_CHUNKS, qualifier = StrategyNameQualifiers.SINGLE_AND_DOUBLE, description = StrategyDescriptions.FUN_CHUNKS_SUBTRACTION, examples="")
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FRIENDLY_AND_FIX_ADDITION)
    strategy = Strategy(name = StrategyNames.FRIENDLY_AND_FIX, qualifier = StrategyNameQualifiers.SINGLE_AND_SINGLE, description = StrategyDescriptions.FRIENDLY_AND_FIX_ADDITION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FRIENDLY_AND_FIX_ADDITION)
    strategy = Strategy(name = StrategyNames.FRIENDLY_AND_FIX, qualifier = StrategyNameQualifiers.SINGLE_AND_DOUBLE, description = StrategyDescriptions.FRIENDLY_AND_FIX_ADDITION, examples=example_csv)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.MEMORIZE, qualifier = StrategyNameQualifiers.COUNTERS, description = StrategyDescriptions.MEMORIZE)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.ADD_TEN_OR_HUNDRED)
    strategy = Strategy(name = StrategyNames.TEN_OR_HUNDRED, description = StrategyDescriptions.ADD_TEN_OR_HUNDRED, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FRIENDLY_PAIRS)
    strategy = Strategy(name = StrategyNames.FRIENDLY_PAIRS, description = StrategyDescriptions.FRIENDLY_PAIRS, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.SUBTRACT_TEN_OR_HUNDRED)
    strategy = Strategy(name = StrategyNames.TEN_OR_HUNDRED, description = StrategyDescriptions.SUBTRACT_TEN_OR_HUNDRED, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FRIENDLY_AND_FIX_SUBTRACTION)
    strategy = Strategy(name = StrategyNames.FRIENDLY_AND_FIX, qualifier = StrategyNameQualifiers.SINGLE_AND_SINGLE, description = StrategyDescriptions.FRIENDLY_AND_FIX_SUBTRACTION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.FRIENDLY_AND_FIX_SUBTRACTION)
    strategy = Strategy(name = StrategyNames.FRIENDLY_AND_FIX, qualifier = StrategyNameQualifiers.SINGLE_AND_DOUBLE, description = StrategyDescriptions.FRIENDLY_AND_FIX_SUBTRACTION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.ADDITION_BY_PLACE)
    strategy = Strategy(name = StrategyNames.BY_PLACE, description = StrategyDescriptions.ADDITION_BY_PLACE, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.REPEATED_ADDITION)
    strategy = Strategy(name = StrategyNames.REPEATED, description = StrategyDescriptions.REPEATED_ADDITION, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.DIVIDED_GROUPS)
    strategy = Strategy(name = StrategyNames.GROUPS, description = StrategyDescriptions.DIVIDED_GROUPS, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ''
    for strat_example in StrategyExamples.ADDING_FRACTIONS:
        example_csv = example_csv+strat_example
    strategy = Strategy(name = StrategyNames.FRACTIONS, description = StrategyDescriptions.ADDING_FRACTIONS, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.SUBTRACTING_FRACTIONS)
    strategy = Strategy(name = StrategyNames.FRACTIONS, description = StrategyDescriptions.SUBTRACTING_FRACTIONS, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.MULTIPLYING_FRACTIONS)
    strategy = Strategy(name = StrategyNames.FRACTIONS, description = StrategyDescriptions.MULTIPLYING_FRACTIONS, examples=example_csv)
    db.session.add(strategy)
    
    example_csv = ",".join(StrategyExamples.DIVIDING_FRACTIONS)
    strategy = Strategy(name = StrategyNames.FRACTIONS, description = StrategyDescriptions.DIVIDING_FRACTIONS, examples=example_csv)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_ADDITION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_NAMED_ADDITION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_SUBTRACTION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_MULTIPLICATION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_DIVISION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    strategy = Strategy(name = StrategyNames.BOX_METHOD, qualifier = StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION, description = StrategyDescriptions.BOX_BASIC)
    db.session.add(strategy)
    
    db.session.flush()
    db.session.commit()
    
def createURL(level, level_progress, name):
    logger.debug(">>createURL name:{0}".format(name))
    name.replace(',', '')
    url_name = "level"+"_"+str(level)+"_"+str(level_progress)+"_"+name.replace(" ","_")
    return url_name

def setup_topics_and_categories(db):
    logger.debug(">>setup_topics_and_categories()")
    topic_number_and_patterns = Topic(name = TopicConstants.NUMBERS_AND_PATTERNS.getName(), order = 1)
    db.session.add(topic_number_and_patterns)  
    topic_addition_and_subtraction = Topic(name = TopicConstants.ADDITION_AND_SUBTRACTION.getName(), order = 2)
    db.session.add(topic_addition_and_subtraction)  
    topic_multiplication_and_division = Topic(name = TopicConstants.MULTIPLICATION_AND_DIVISION.getName(), order = 3)
    db.session.add(topic_multiplication_and_division)  
    topic_fractions_and_decimals = Topic(name = TopicConstants.FRACIONS_AND_DECIMALS.getName(), order = 4)
    db.session.add(topic_fractions_and_decimals)  
    topic_powers_and_roots = Topic(name = TopicConstants.POWERS_AND_ROOTS.getName(), order = 5)
    db.session.add(topic_powers_and_roots)  
    topic_percentages_and_proportions = Topic(name = TopicConstants.PERCENTAGES_AND_PROPORTIONS.getName(), order = 6)
    db.session.add(topic_percentages_and_proportions)  
    topic_statistics = Topic(name = TopicConstants.STATISTICS.getName(), order = 7)
    db.session.add(topic_statistics)  
    topic_measurement_and_geometry = Topic(name = TopicConstants.MEASUREMENT_AND_GEOMETRY.getName(), order = 8)
    db.session.add(topic_measurement_and_geometry)  
    db.session.flush()
    
    category = Category(topic_id= topic_number_and_patterns.id, name = CategoryConstants.PATTERNS, order = 1)
    db.session.add(category)
    category = Category(topic_id= topic_number_and_patterns.id, name = CategoryConstants.NUMBERS, order = 2)
    db.session.add(category)
    category = Category(topic_id= topic_addition_and_subtraction.id, name = CategoryConstants.ADDITION, order = 3)
    db.session.add(category)
    category = Category(topic_id= topic_addition_and_subtraction.id, name = CategoryConstants.SUBTRACTION, order = 4)
    db.session.add(category)
    category = Category(topic_id= topic_multiplication_and_division.id, name = CategoryConstants.MULTIPLICATION, order = 5)
    db.session.add(category)
    category = Category(topic_id= topic_multiplication_and_division.id, name = CategoryConstants.DIVISION, order = 6)
    db.session.add(category)
    category = Category(topic_id= topic_fractions_and_decimals.id, name = CategoryConstants.FRACTIONS, order = 7)
    db.session.add(category)
    category = Category(topic_id= topic_fractions_and_decimals.id, name = CategoryConstants.DECIMALS, order = 8)
    db.session.add(category)
    category = Category(topic_id= topic_powers_and_roots.id, name = CategoryConstants.POWERS, order = 9)
    db.session.add(category)
    category = Category(topic_id= topic_powers_and_roots.id, name = CategoryConstants.ROOTS, order = 10)
    db.session.add(category)
    category = Category(topic_id= topic_percentages_and_proportions.id, name = CategoryConstants.PERCENTAGE, order = 11)
    db.session.add(category)
    category = Category(topic_id= topic_percentages_and_proportions.id, name = CategoryConstants.RATIO, order = 12)
    db.session.add(category)
    category = Category(topic_id= topic_statistics.id, name = CategoryConstants.AVERAGE, order = 13)
    db.session.add(category)    
    category = Category(topic_id= topic_measurement_and_geometry.id, name = CategoryConstants.MEASUREMENT, order = 14)
    db.session.add(category)  
    category = Category(topic_id= topic_measurement_and_geometry.id, name = CategoryConstants.GEOMETRY, order = 15)
    db.session.add(category)  
    db.session.flush()
    db.session.commit()
    
def setup_users(db):
    logger.debug(">>setup_users()")
    admin_role = Role(role_name = RoleTypes.ADMIN)
    student_role = Role(role_name = RoleTypes.STUDENT)
    parent_role = Role(role_name = RoleTypes.PARENT)
    teacher_role = Role(role_name = RoleTypes.TEACHER)

    db.session.add(admin_role)
    db.session.add(student_role)
    db.session.add(parent_role)
    db.session.add(teacher_role)
    db.session.flush()
    # Add a admin user.
    admin_user_name = os.environ.get('MARS_DB_ADMIN_USER_NAME')
    admin_user_password = os.environ.get('MARS_DB_ADMIN_PASSWORD')
    admin_user_email = os.environ.get('MARS_DB_ADMIN_USER_EMAIL')
    admin_first_name = os.environ.get('MARS_DB_ADMIN_FIRST_NAME')
    admin_last_name = os.environ.get('MARS_DB_ADMIN_LAST_NAME')
    admin_user = User(role_id = admin_role.id, first_name=admin_first_name, last_name=admin_last_name, user_name = admin_user_name, 
                email=admin_user_email, avatar=ProfileConstants.DEFAULT_AVATAR_NAME,
                password=admin_user_password)
    db.session.add(admin_user)
    db.session.flush()
    #add a public test parent
    parent1_user_name = os.environ.get('MARS_DB_PARENT1_USER_NAME')
    parent1_user_password = os.environ.get('MARS_DB_PARENT1_PASSWORD')
    parent1_user_email = os.environ.get('MARS_DB_PARENT1_USER_EMAIL')
    parent1_first_name = os.environ.get('MARS_DB_PARENT1_FIRST_NAME')
    parent1_last_name = os.environ.get('MARS_DB_PARENT1_LAST_NAME')
    parent1_user = User(role_id = parent_role.id, first_name=parent1_first_name, last_name=parent1_last_name, user_name = parent1_user_name, 
                email=parent1_user_email, avatar=ProfileConstants.DEFAULT_AVATAR_NAME,
                password=parent1_user_password)
    db.session.add(parent1_user)
    db.session.flush()
    #add a fist student
    student_user_name = os.environ.get('MARS_DB_STUDENT_USER_NAME')
    student_user_password = os.environ.get('MARS_DB_STUDENT_PASSWORD')
    student_first_name = os.environ.get('MARS_DB_STUDENT_FIRST_NAME')
    student_last_name = os.environ.get('MARS_DB_STUDENT_LAST_NAME')
    student_school = os.environ.get('MARS_DB_STUDENT_SCHOOL')
    student_user = User(role_id = student_role.id, first_name=student_first_name, \
                        last_name=student_last_name, user_name = student_user_name, avatar=ProfileConstants.DEFAULT_AVATAR_NAME, \
                        password=student_user_password)
    db.session.add(student_user)
    db.session.flush()
    
    student = Student(user_id = student_user.id, parentid = admin_user.id, age = 10,
                grade = 5, school = student_school,
                level = 2,
                country = 'Australia',
                goal_session_time = 10,
                goal_session_frequency = 5, pet=ProfileConstants.DEFAULT_PET_NAME)
    db.session.add(student)
    db.session.flush()
    

    
    

    
def setup_level_1_add_sub(db):
    logger.debug(">>persist_numberbond_addition_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    level = 1
    #stage is dependent on operation 
    stage = 1
    topic_progress = 1
    name = "Recognise number bond patterns up to 6"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_counters.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.COUNTERS
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='1', part2='5')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='1', part2='3')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    topic_progress = 2
    name = "Recognise number bond patterns up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_counters.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.COUNTERS
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    topic_progress = 3
    name = "Find the missing whole up to 6"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_part_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.PART_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='1', part2='5')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='1', part2='3')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    topic_progress = 4
    name = "Find the missing whole up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_part_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.PART_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    numberbond_whole_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.WHOLE_PART).first()
    topic_progress = 5
    name = "Find the missing part up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_whole_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.WHOLE_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    numberBonds21 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds22 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds23 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds24 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds25 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds26 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds27 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds28 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds29 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds30 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.add(numberBonds21)
    db.session.add(numberBonds22)
    db.session.add(numberBonds23)
    db.session.add(numberBonds24)
    db.session.add(numberBonds25)
    db.session.add(numberBonds26)
    db.session.add(numberBonds27)
    db.session.add(numberBonds28)
    db.session.add(numberBonds29)
    db.session.add(numberBonds30)
    db.session.commit()
    
def setup_level_2_add_sub(db):
    logger.debug(">>setup_level_2_add_sub()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_ADDITION).first()
    variables = 2
    
    level = 2
    stage = 1
    topic_progress = 1
    name = "box model addition up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    for i in range(1, 10):
        for j in range(1, 10):
            if j + i <=10:
                logger.debug("--setup_box_model_addition() add I:{0}, j:{1}".format(i, j))
                boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(j) + ' + ' + str(i) +' = ?', answer=str(j+i), num_variables=2, total_value=str(j+i), part_values=str(j)+','+str(i), part_value_types='cc') 
                db.session.add(boxModelAddSubtract)
                db.session.flush()
    db.session.commit()
          
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_SUBTRACTION).first()
    variables = 2
    level = 2
    stage = 1
    topic_progress = 2
    name = "box model subtraction up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    for i in range(1, 10):
        for j in range(1, 10):
            if j > i:
                logger.debug("--setup_box_model_addition() sub I:{0}, j:{1}".format(i, j))
                boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(j) + ' - ' + str(i) +' = ?', answer=str(j-i), num_variables=2, total_value=str(j), part_values=str(j)+','+str(i), part_value_types='cc') 
                db.session.add(boxModelAddSubtract)
                db.session.flush()
    db.session.commit()

    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
 
    level = 2
    stage = 1
    topic_progress = 3
    name = "Add two numbers, up to 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_single.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '6 + 5', line_positions = '6, 10, 11', jump_values = '4, 1', stage1_question = '6 + 4 + 1', answer = '11', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '6 + 6', line_positions = '6, 10, 12', jump_values = '4, 2', stage1_question = '6 + 4 + 2', answer = '12', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '6 + 7', line_positions = '7, 10, 13', jump_values = '3, 3', stage1_question = '7 + 3 + 3', answer = '13', flip = True)
    funChunks4 = FunChunks(activity_id = activity.id, question = '6 + 8', line_positions = '8, 10, 14', jump_values = '2, 4', stage1_question = '8 + 2 + 4', answer = '14', flip = True)
    funChunks5 = FunChunks(activity_id = activity.id, question = '6 + 9', line_positions = '9, 10, 15', jump_values = '1, 5', stage1_question = '9 + 1 + 5', answer = '15', flip = True)
    funChunks6 = FunChunks(activity_id = activity.id, question = '7 + 5', line_positions = '7, 10, 12', jump_values = '3, 2', stage1_question = '7 + 3 + 2', answer = '12', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '7 + 6', line_positions = '7, 10, 13', jump_values = '3, 3', stage1_question = '7 + 3 + 3', answer = '13', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '7 + 7', line_positions = '7, 10, 14', jump_values = '3, 4', stage1_question = '7 + 3 + 4', answer = '14', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '7 + 8', line_positions = '8, 10, 15', jump_values = '2, 5', stage1_question = '8 + 2 + 5', answer = '15', flip = True)
    funChunks10 = FunChunks(activity_id = activity.id, question = '7 + 9', line_positions = '9, 10, 16', jump_values = '1, 6', stage1_question = '9 + 1 + 6', answer = '16', flip = True)
    funChunks11 = FunChunks(activity_id = activity.id, question = '8 + 5', line_positions = '8, 10, 13', jump_values = '2, 3', stage1_question = '8 + 2 + 5', answer = '13', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '8 + 6', line_positions = '8, 10, 14', jump_values = '2, 4', stage1_question = '8 + 2 + 4', answer = '14', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '8 + 7', line_positions = '8, 10, 15', jump_values = '2, 5', stage1_question = '8 + 2 + 5', answer = '15', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '8 + 8', line_positions = '8, 10, 16', jump_values = '2, 6', stage1_question = '8 + 2 + 6', answer = '16', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '8 + 9', line_positions = '9, 10, 17', jump_values = '1, 7', stage1_question = '9 + 1 + 7', answer = '17', flip = True)
    funChunks16 = FunChunks(activity_id = activity.id, question = '9 + 5', line_positions = '9, 10, 14', jump_values = '1, 4', stage1_question = '9 + 1 + 4', answer = '14', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '9 + 6', line_positions = '9, 10, 15', jump_values = '1, 5', stage1_question = '9 + 1 + 5', answer = '15', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '9 + 7', line_positions = '9, 10, 16', jump_values = '1, 6', stage1_question = '9 + 1 + 6', answer = '16', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '9 + 8', line_positions = '9, 10, 17', jump_values = '1, 7', stage1_question = '9 + 1 + 7', answer = '17', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '9 + 9', line_positions = '9, 10, 18', jump_values = '1, 8', stage1_question = '9 + 1 + 8', answer = '18', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_friendly_and_fix_single_n_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    db.session.flush()
    level = 2
    stage = 1
    topic_progress = 4
    name = "Add two numbers, up to 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_single.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '6 + 7', line_positions = '6, 16, 13', jump_values = '10, -3', stage1_question = '6 + 10 - 3', answer = '13', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '6 + 8', line_positions = '6, 16, 14', jump_values = '10, -2', stage1_question = '6 + 10 - 2', answer = '14', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '6 + 9', line_positions = '6, 16, 15', jump_values = '10, -1', stage1_question = '6 + 10 - 1', answer = '15', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '7 + 7', line_positions = '7, 17, 14', jump_values = '10, -3', stage1_question = '7 + 10 - 3', answer = '14', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '7 + 8', line_positions = '7, 17, 15', jump_values = '10, -2', stage1_question = '7 + 10 - 2', answer = '15', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '7 + 9', line_positions = '7, 17, 16', jump_values = '10, -1', stage1_question = '7 + 10 - 1', answer = '16', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '8 + 7', line_positions = '8, 18, 15', jump_values = '10, -3', stage1_question = '8 + 10 - 3', answer = '15', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '8 + 8', line_positions = '8, 18, 16', jump_values = '10, -2', stage1_question = '8 + 10 - 2', answer = '16', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '8 + 9', line_positions = '8, 18, 17', jump_values = '10, -1', stage1_question = '8 + 10 - 1', answer = '17', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '9 + 7', line_positions = '9, 19, 16', jump_values = '10, -3', stage1_question = '9 + 10 - 3', answer = '16', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '9 + 8', line_positions = '9, 19, 17', jump_values = '10, -2', stage1_question = '9 + 10 - 2', answer = '17', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '9 + 9', line_positions = '9, 19, 18', jump_values = '10, -1', stage1_question = '9 + 10 - 1', answer = '18', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    #stage is dependent on operation 
    stage = 1
    topic_progress = 5
    name = "Subtract two numbers, maximum of 15"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '11 - 2', line_positions = '11, 10, 9', jump_values = '-1, -1', stage1_question = '11 - 1 - 1', answer = '9', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '11 - 3', line_positions = '11, 10, 8', jump_values = '-1, -2', stage1_question = '11 - 1 - 2', answer = '8', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '11 - 4', line_positions = '11, 10, 7', jump_values = '-1, -3', stage1_question = '11 - 1 - 3', answer = '7', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '11 - 5', line_positions = '11, 10, 6', jump_values = '-1, -4', stage1_question = '11 - 1 -4', answer = '6', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '11 - 6', line_positions = '11, 10, 5', jump_values = '-1, -5', stage1_question = '11 - 1 -5', answer = '5', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '12 - 3', line_positions = '12, 10, 9', jump_values = '-2, -1', stage1_question = '12 - 2 -1', answer = '9', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '12 - 4', line_positions = '12, 10, 8', jump_values = '-2, -2', stage1_question = '12 - 2 -2', answer = '8', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '12 - 5', line_positions = '12, 10, 7', jump_values = '-2, -3', stage1_question = '12 - 2 -3', answer = '7', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '12 - 6', line_positions = '12, 10, 6', jump_values = '-2, -4', stage1_question = '12 - 2 -4', answer = '6', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '13 - 4', line_positions = '13, 10, 9', jump_values = '-3, -1', stage1_question = '13 - 3 -1', answer = '9', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '13 - 5', line_positions = '13, 10, 8', jump_values = '-3, -2', stage1_question = '13 - 3 -2', answer = '8', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '13 - 6', line_positions = '13, 10, 7', jump_values = '-3, -3', stage1_question = '13 - 3 -3', answer = '7', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '14 - 5', line_positions = '14, 10, 9', jump_values = '-4, -1', stage1_question = '14 - 4 -1', answer = '9', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '14 - 6', line_positions = '14, 10, 8', jump_values = '-4, -2', stage1_question = '14 - 4 -2', answer = '8', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '15 - 6', line_positions = '15, 10, 9', jump_values = '-5, -1', stage1_question = '15 - 5 -1', answer = '9', flip = False) 
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    stage = 1
    topic_progress = 6
    name = "Subtract two numbers, maximum of 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '18 - 9', line_positions = '18, 8, 9', jump_values = '-10, 1', stage1_question = '18 - 10 + 1', answer = '9', flip = False)                                                                                                      
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '17 - 9', line_positions = '17, 7, 8', jump_values = '-10, 1', stage1_question = '17 - 10 + 1', answer = '8', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '17 - 8', line_positions = '17, 7, 9', jump_values = '-10, 2', stage1_question = '17 - 10 + 2', answer = '9', flip = False)                                                                                                         
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '16 - 9', line_positions = '16, 6, 7', jump_values = '-10, 1', stage1_question = '16 - 10 + 1', answer = '7', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '16 - 8', line_positions = '16, 6, 8', jump_values = '-10, 2', stage1_question = '16 - 10 + 2', answer = '8', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '16 - 7', line_positions = '16, 6, 9', jump_values = '-10, 3', stage1_question = '16 - 10 + 3', answer = '9', flip = False)                                                                                                       
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '15 - 9', line_positions = '15, 5, 6', jump_values = '-10, 1', stage1_question = '15 - 10 + 1', answer = '6', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '15 - 8', line_positions = '15, 5, 7', jump_values = '-10, 2', stage1_question = '15 - 10 + 2', answer = '7', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '15 - 7', line_positions = '15, 5, 8', jump_values = '-10, 3', stage1_question = '15 - 10 + 3', answer = '8', flip = False)   
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '14 - 9', line_positions = '14, 4, 5', jump_values = '-10, 1', stage1_question = '14 - 10 + 1', answer = '5', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '14 - 8', line_positions = '14, 4, 6', jump_values = '-10, 2', stage1_question = '14 - 10 + 2', answer = '6', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '14 - 7', line_positions = '14, 4, 7', jump_values = '-10, 3', stage1_question = '14 - 10 + 3', answer = '7', flip = False)                                                                                                       
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '13 - 9', line_positions = '13, 3, 4', jump_values = '-10, 1', stage1_question = '13 - 10 + 1', answer = '4', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '13 - 8', line_positions = '13, 3, 5', jump_values = '-10, 2', stage1_question = '13 - 10 + 2', answer = '5', flip = False)
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '13 - 7', line_positions = '13, 3, 6', jump_values = '-10, 3', stage1_question = '13 - 10 + 3', answer = '6', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.commit()
          
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()      
    stage = 2
    topic_progress = 7
    name = "Add two numbers, up to 58"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '46 + 5', line_positions = '46, 50, 51', jump_values = '4, 1', stage1_question = '46 + 4 + 1', answer = '51', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '36 + 6', line_positions = '36, 40, 42', jump_values = '4, 2', stage1_question = '36 + 4 + 2', answer = '42', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '26 + 7', line_positions = '26, 30, 33', jump_values = '4, 3', stage1_question = '26 + 4 + 3', answer = '33', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '16 + 8', line_positions = '16, 20, 24', jump_values = '4, 4', stage1_question = '16 + 4 + 4', answer = '24', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '46 + 9', line_positions = '46, 50, 55', jump_values = '4, 5', stage1_question = '46 + 4 + 5', answer = '55', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '47 + 5', line_positions = '47, 50, 52', jump_values = '3, 2', stage1_question = '47 + 3 + 2', answer = '52', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '17 + 6', line_positions = '17, 20, 23', jump_values = '3, 3', stage1_question = '17 + 3 + 3', answer = '23', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '37 + 7', line_positions = '37, 40, 44', jump_values = '3, 4', stage1_question = '37 + 3 + 4', answer = '44', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '27 + 8', line_positions = '27, 30, 35', jump_values = '3, 5', stage1_question = '27 + 3 + 5', answer = '35', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '37 + 9', line_positions = '37, 40, 46', jump_values = '3, 6', stage1_question = '37 + 3 + 6', answer = '46', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '28 + 5', line_positions = '28, 30, 33', jump_values = '2, 3', stage1_question = '28 + 2 + 5', answer = '33', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '48 + 6', line_positions = '48, 50, 54', jump_values = '2, 4', stage1_question = '48 + 2 + 4', answer = '54', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '18 + 7', line_positions = '18, 20, 25', jump_values = '2, 5', stage1_question = '18 + 2 + 5', answer = '25', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '38 + 8', line_positions = '38, 40, 46', jump_values = '2, 6', stage1_question = '38 + 2 + 6', answer = '46', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '28 + 9', line_positions = '28, 30, 37', jump_values = '2, 7', stage1_question = '28 + 2 + 7', answer = '37', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '19 + 5', line_positions = '19, 20, 24', jump_values = '1, 4', stage1_question = '19 + 1 + 4', answer = '24', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '29 + 6', line_positions = '29, 30, 35', jump_values = '1, 5', stage1_question = '29 + 1 + 5', answer = '35', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '49 + 7', line_positions = '49, 50, 56', jump_values = '1, 6', stage1_question = '49 + 1 + 6', answer = '56', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '39 + 8', line_positions = '39, 40, 47', jump_values = '1, 7', stage1_question = '39 + 1 + 7', answer = '47', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '19 + 9', line_positions = '19, 20, 28', jump_values = '1, 8', stage1_question = '19 + 1 + 8', answer = '28', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
    
    stage = 2
    topic_progress = 8
    name = "Subtract two numbers, maximum of 55"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '41 - 2', line_positions = '41, 40, 39', jump_values = '-1, -1', stage1_question = '41 - 1 - 1', answer = '39', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '31 - 3', line_positions = '31, 30, 28', jump_values = '-1, -2', stage1_question = '31 - 1 - 2', answer = '28', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '31 - 4', line_positions = '31, 30, 27', jump_values = '-1, -3', stage1_question = '31 - 1 - 3', answer = '27', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '51 - 5', line_positions = '51, 50, 46', jump_values = '-1, -4', stage1_question = '51 - 1 -4', answer = '46', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '21 - 6', line_positions = '21, 20, 15', jump_values = '-1, -5', stage1_question = '21 - 1 -5', answer = '15', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '52 - 3', line_positions = '52, 50, 49', jump_values = '-2, -1', stage1_question = '52 - 2 -1', answer = '49', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '22 - 4', line_positions = '22, 20, 18', jump_values = '-2, -2', stage1_question = '22 - 2 -2', answer = '18', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '32 - 5', line_positions = '32, 30, 27', jump_values = '-2, -3', stage1_question = '32 - 2 -3', answer = '27', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '42 - 6', line_positions = '42, 40, 36', jump_values = '-2, -4', stage1_question = '42 - 2 -4', answer = '36', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '23 - 4', line_positions = '23, 20, 19', jump_values = '-3, -1', stage1_question = '23 - 3 -1', answer = '19', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '53 - 5', line_positions = '53, 50, 48', jump_values = '-3, -2', stage1_question = '53 - 3 -2', answer = '48', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '33 - 6', line_positions = '33, 30, 27', jump_values = '-3, -3', stage1_question = '33 - 3 -3', answer = '27', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '24 - 5', line_positions = '24, 20, 19', jump_values = '-4, -1', stage1_question = '24 - 4 -1', answer = '19', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '44 - 6', line_positions = '44, 40, 38', jump_values = '-4, -2', stage1_question = '44 - 4 -2', answer = '38', flip = False)    
    funChunks15 = FunChunks(activity_id = activity.id, question = '55 - 6', line_positions = '55, 50, 49', jump_values = '-5, -1', stage1_question = '55 - 5 -1', answer = '49', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_friendly_and_fix_single_n_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    stage = 2
    topic_progress = 9
    name = "Add two numbers, up to 108"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '36 + 7', line_positions = '36, 46, 43', jump_values = '10, -3', stage1_question = '36 + 10 - 3', answer = '43', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '46 + 8', line_positions = '46, 56, 54', jump_values = '10, -2', stage1_question = '46 + 10 - 2', answer = '54', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '56 + 9', line_positions = '56, 66, 65', jump_values = '10, -1', stage1_question = '56 + 10 - 1', answer = '65', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '66 + 7', line_positions = '66, 76, 73', jump_values = '10, -3', stage1_question = '66 + 10 - 3', answer = '73', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '76 + 8', line_positions = '76, 86, 84', jump_values = '10, -2', stage1_question = '76 + 10 - 2', answer = '84', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '86 + 9', line_positions = '86, 96, 95', jump_values = '10, -1', stage1_question = '86 + 10 - 1', answer = '95', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '67 + 7', line_positions = '67, 77, 74', jump_values = '10, -3', stage1_question = '67 + 10 - 3', answer = '74', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '77 + 8', line_positions = '77, 87, 85', jump_values = '10, -2', stage1_question = '77 + 10 - 2', answer = '85', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '87 + 9', line_positions = '87, 97, 96', jump_values = '10, -1', stage1_question = '87 + 10 - 1', answer = '96', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '17 + 7', line_positions = '17, 27, 24', jump_values = '10, -3', stage1_question = '17 + 10 - 3', answer = '24', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '27 + 8', line_positions = '27, 37, 35', jump_values = '10, -2', stage1_question = '27 + 10 - 2', answer = '35', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '37 + 9', line_positions = '37, 47, 46', jump_values = '10, -1', stage1_question = '37 + 10 - 1', answer = '46', flip = False)
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '98 + 7', line_positions = '98, 108, 105', jump_values = '10, -3', stage1_question = '98 + 10 - 3', answer = '105', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '18 + 8', line_positions = '18, 28, 26', jump_values = '10, -2', stage1_question = '18 + 10 - 2', answer = '26', flip = False)
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '28 + 9', line_positions = '28, 38, 37', jump_values = '10, -1', stage1_question = '28 + 10 - 1', answer = '37', flip = False)
    friendlyAndFix16 = FriendlyAndFix(activity_id = activity.id, question = '48 + 7', line_positions = '48, 58, 55', jump_values = '10, -3', stage1_question = '48 + 10 - 3', answer = '55', flip = False)
    friendlyAndFix17 = FriendlyAndFix(activity_id = activity.id, question = '58 + 8', line_positions = '58, 68, 66', jump_values = '10, -2', stage1_question = '58 + 10 - 2', answer = '66', flip = False)
    friendlyAndFix18 = FriendlyAndFix(activity_id = activity.id, question = '68 + 9', line_positions = '68, 78, 77', jump_values = '10, -1', stage1_question = '68 + 10 - 1', answer = '77', flip = False)
    friendlyAndFix19 = FriendlyAndFix(activity_id = activity.id, question = '39 + 7', line_positions = '39, 49, 46', jump_values = '10, -3', stage1_question = '39 + 10 - 3', answer = '46', flip = False)
    friendlyAndFix20 = FriendlyAndFix(activity_id = activity.id, question = '49 + 8', line_positions = '49, 59, 57', jump_values = '10, -2', stage1_question = '49 + 10 - 2', answer = '57', flip = False)
    friendlyAndFix21 = FriendlyAndFix(activity_id = activity.id, question = '59 + 9', line_positions = '59, 69, 68', jump_values = '10, -1', stage1_question = '59 + 10 - 1', answer = '68', flip = False)
    friendlyAndFix22 = FriendlyAndFix(activity_id = activity.id, question = '69 + 7', line_positions = '69, 79, 76', jump_values = '10, -3', stage1_question = '69 + 10 - 3', answer = '76', flip = False)
    friendlyAndFix23 = FriendlyAndFix(activity_id = activity.id, question = '79 + 8', line_positions = '79, 89, 87', jump_values = '10, -2', stage1_question = '79 + 10 - 2', answer = '87', flip = False)
    friendlyAndFix24 = FriendlyAndFix(activity_id = activity.id, question = '89 + 9', line_positions = '89, 99, 98', jump_values = '10, -1', stage1_question = '89 + 10 - 1', answer = '98', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.add(friendlyAndFix16)
    db.session.add(friendlyAndFix17)
    db.session.add(friendlyAndFix18)
    db.session.add(friendlyAndFix19)
    db.session.add(friendlyAndFix20)
    db.session.add(friendlyAndFix21)
    db.session.add(friendlyAndFix22)
    db.session.add(friendlyAndFix23)
    db.session.add(friendlyAndFix24)
    db.session.commit()

    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()   
    stage = 3
    topic_progress = 10
    name = "Add two numbers, up to 108"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '56 + 5', line_positions = '56, 60, 61', jump_values = '4, 1', stage1_question = '56 + 4 + 1', answer = '61', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '76 + 6', line_positions = '76, 80, 82', jump_values = '4, 2', stage1_question = '76 + 4 + 2', answer = '82', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '86 + 7', line_positions = '86, 90, 93', jump_values = '4, 3', stage1_question = '86 + 4 + 3', answer = '93', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '96 + 8', line_positions = '96, 100, 104', jump_values = '4, 4', stage1_question = '96 + 4 + 4', answer = '104', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '56 + 9', line_positions = '56, 60, 65', jump_values = '4, 5', stage1_question = '56 + 4 + 5', answer = '65', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '67 + 5', line_positions = '67, 70, 72', jump_values = '3, 2', stage1_question = '67 + 3 + 2', answer = '72', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '87 + 6', line_positions = '87, 90, 93', jump_values = '3, 3', stage1_question = '87 + 3 + 3', answer = '93', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '97 + 7', line_positions = '97, 100, 104', jump_values = '3, 4', stage1_question = '97 + 3 + 4', answer = '104', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '57 + 8', line_positions = '57, 60, 65', jump_values = '3, 5', stage1_question = '57 + 3 + 5', answer = '65', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '77 + 9', line_positions = '77, 80, 86', jump_values = '3, 6', stage1_question = '77 + 3 + 6', answer = '86', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '78 + 5', line_positions = '78, 80, 83', jump_values = '2, 3', stage1_question = '78 + 2 + 5', answer = '83', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '88 + 6', line_positions = '88, 90, 94', jump_values = '2, 4', stage1_question = '88 + 2 + 4', answer = '94', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '98 + 7', line_positions = '98, 100, 105', jump_values = '2, 5', stage1_question = '98 + 2 + 5', answer = '105', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '58 + 8', line_positions = '58, 60, 66', jump_values = '2, 6', stage1_question = '58 + 2 + 6', answer = '66', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '68 + 9', line_positions = '68, 70, 77', jump_values = '2, 7', stage1_question = '68 + 2 + 7', answer = '77', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '89 + 5', line_positions = '89, 90, 94', jump_values = '1, 4', stage1_question = '89 + 1 + 4', answer = '94', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '99 + 6', line_positions = '99, 100, 105', jump_values = '1, 5', stage1_question = '99 + 1 + 5', answer = '105', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '79 + 7', line_positions = '79, 80, 86', jump_values = '1, 6', stage1_question = '79 + 1 + 6', answer = '86', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '69 + 8', line_positions = '69, 70, 77', jump_values = '1, 7', stage1_question = '69 + 1 + 7', answer = '77', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '59 + 9', line_positions = '59, 60, 68', jump_values = '1, 8', stage1_question = '59 + 1 + 8', answer = '68', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
    
    stage = 3
    topic_progress = 11
    name = "Subtract two numbers, maximum of 95"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '61 - 2', line_positions = '61, 60, 59', jump_values = '-1, -1', stage1_question = '61 - 1 - 1', answer = '59', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '71 - 3', line_positions = '71, 70, 68', jump_values = '-1, -2', stage1_question = '71 - 1 - 2', answer = '68', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '81 - 4', line_positions = '81, 80, 77', jump_values = '-1, -3', stage1_question = '81 - 1 - 3', answer = '77', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '91 - 5', line_positions = '91, 90, 86', jump_values = '-1, -4', stage1_question = '91 - 1 -4', answer = '86', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '61 - 6', line_positions = '61, 60, 55', jump_values = '-1, -5', stage1_question = '61 - 1 -5', answer = '55', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '92 - 3', line_positions = '92, 90, 89', jump_values = '-2, -1', stage1_question = '92 - 2 -1', answer = '89', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '82 - 4', line_positions = '82, 80, 78', jump_values = '-2, -2', stage1_question = '82 - 2 -2', answer = '78', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '72 - 5', line_positions = '72, 70, 67', jump_values = '-2, -3', stage1_question = '72 - 2 -3', answer = '67', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '62 - 6', line_positions = '62, 60, 56', jump_values = '-2, -4', stage1_question = '62 - 2 -4', answer = '56', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '63 - 4', line_positions = '63, 60, 59', jump_values = '-3, -1', stage1_question = '63 - 3 -1', answer = '59', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '73 - 5', line_positions = '73, 70, 68', jump_values = '-3, -2', stage1_question = '73 - 3 -2', answer = '68', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '83 - 6', line_positions = '83, 80, 77', jump_values = '-3, -3', stage1_question = '83 - 3 -3', answer = '77', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '74 - 5', line_positions = '74, 70, 69', jump_values = '-4, -1', stage1_question = '74 - 4 -1', answer = '69', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '94 - 6', line_positions = '94, 90, 88', jump_values = '-4, -2', stage1_question = '94 - 4 -2', answer = '88', flip = False)    
    funChunks15 = FunChunks(activity_id = activity.id, question = '85 - 6', line_positions = '85, 80, 79', jump_values = '-5, -1', stage1_question = '85 - 5 -1', answer = '79', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    stage = 3
    topic_progress = 12
    name = "Subtract two numbers, maximum of 98"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '28 - 9', line_positions = '28, 18, 19', jump_values = '-10, 1', stage1_question = '28 - 10 + 1', answer = '19', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '68 - 9', line_positions = '68, 58, 59', jump_values = '-10, 1', stage1_question = '68 - 10 + 1', answer = '59', flip = False)                                                                                                  
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '37 - 9', line_positions = '37, 27, 28', jump_values = '-10, 1', stage1_question = '37 - 10 + 1', answer = '28', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '47 - 8', line_positions = '47, 37, 39', jump_values = '-10, 2', stage1_question = '47 - 10 + 2', answer = '39', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '87 - 8', line_positions = '87, 77, 79', jump_values = '-10, 2', stage1_question = '87 - 10 + 2', answer = '79', flip = False)                                                                                                     
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '56 - 9', line_positions = '56, 46, 47', jump_values = '-10, 1', stage1_question = '56 - 10 + 1', answer = '47', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '66 - 8', line_positions = '66, 56, 58', jump_values = '-10, 2', stage1_question = '66 - 10 + 2', answer = '58', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '76 - 7', line_positions = '76, 66, 69', jump_values = '-10, 3', stage1_question = '76 - 10 + 3', answer = '69', flip = False)                                                                                                            
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '85 - 9', line_positions =  '85, 75, 76',  jump_values = '-10, 1', stage1_question = '85 - 10 + 1', answer = '76', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '95 - 8', line_positions = '95, 85, 87', jump_values = '-10, 2', stage1_question = '95 - 10 + 2', answer = '87', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '25 - 7', line_positions = '25, 15, 18', jump_values = '-10, 3', stage1_question = '25 - 10 + 3', answer = '18', flip = False)                                                                                                          
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '34 - 9', line_positions = '34, 24, 25', jump_values = '-10, 1', stage1_question = '34 - 10 + 1', answer = '25', flip = False)
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '44 - 8', line_positions = '44, 34, 36', jump_values = '-10, 2', stage1_question = '44 - 10 + 2', answer = '36', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '54 - 7', line_positions = '54, 44, 47', jump_values = '-10, 3', stage1_question = '54 - 10 + 3', answer = '47', flip = False)                                                                                                    
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '63 - 9', line_positions = '63, 54, 53', jump_values = '-10, 1', stage1_question = '63 - 10 + 1', answer = '54', flip = False)
    friendlyAndFix16 = FriendlyAndFix(activity_id = activity.id, question = '73 - 8', line_positions = '73, 65, 63', jump_values = '-10, 2', stage1_question = '73 - 10 + 2', answer = '65', flip = False)
    friendlyAndFix17 = FriendlyAndFix(activity_id = activity.id, question = '83 - 7', line_positions = '83, 76, 73', jump_values = '-10, 3', stage1_question = '83 - 10 + 3', answer = '76', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.add(friendlyAndFix16)
    db.session.add(friendlyAndFix17)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    stage = 4
    topic_progress = 13
    name = "Add two numbers, up to 208"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '146 + 5', line_positions = '146, 150, 151', jump_values = '4, 1', stage1_question = '146 + 4 + 1', answer = '151', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '136 + 6', line_positions = '136, 140, 142', jump_values = '4, 2', stage1_question = '136 + 4 + 2', answer = '142', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '186 + 7', line_positions = '186, 190, 193', jump_values = '4, 3', stage1_question = '186 + 4 + 3', answer = '193', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '176 + 8', line_positions = '176, 180, 184', jump_values = '2, 4', stage1_question = '176 + 2 + 4', answer = '184', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '156 + 9', line_positions = '156, 160, 165', jump_values = '1, 5', stage1_question = '156 + 1 + 5', answer = '165', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '157 + 5', line_positions = '157, 160, 162', jump_values = '3, 2', stage1_question = '157 + 3 + 2', answer = '162', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '177 + 6', line_positions = '177, 180, 183', jump_values = '3, 3', stage1_question = '177 + 3 + 3', answer = '183', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '167 + 7', line_positions = '167, 170, 174', jump_values = '3, 4', stage1_question = '167 + 3 + 4', answer = '174', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '137 + 8', line_positions = '137, 140, 145', jump_values = '2, 5', stage1_question = '137 + 2 + 5', answer = '145', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '197 + 9', line_positions = '197, 200, 206', jump_values = '1, 6', stage1_question = '197 + 1 + 6', answer = '206', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '158 + 5', line_positions = '158, 160, 163', jump_values = '2, 3', stage1_question = '158 + 2 + 5', answer = '163', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '168 + 6', line_positions = '168, 170, 174', jump_values = '2, 4', stage1_question = '168 + 2 + 4', answer = '174', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '188 + 7', line_positions = '188, 190, 195', jump_values = '2, 5', stage1_question = '188 + 2 + 5', answer = '195', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '148 + 8', line_positions = '148, 150, 156', jump_values = '2, 6', stage1_question = '148 + 2 + 6', answer = '156', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '128 + 9', line_positions = '128, 130, 137', jump_values = '1, 7', stage1_question = '128 + 1 + 7', answer = '137', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '119 + 5', line_positions = '119, 120, 124', jump_values = '1, 4', stage1_question = '119 + 1 + 4', answer = '124', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '129 + 6', line_positions = '129, 130, 135', jump_values = '1, 5', stage1_question = '129 + 1 + 5', answer = '135', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '169 + 7', line_positions = '169, 170, 176', jump_values = '1, 6', stage1_question = '169 + 1 + 6', answer = '176', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '139 + 8', line_positions = '139, 140, 147', jump_values = '1, 7', stage1_question = '139 + 1 + 7', answer = '147', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '149 + 9', line_positions = '149, 150, 158', jump_values = '1, 8', stage1_question = '149 + 1 + 8', answer = '158', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
    
def setup_level_2_mult(db):
    logger.debug(">>persist_multiplication_tables()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    memorize = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MEMORIZE).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    variables = 2
    level = 2
    stage = 1
    topic_progress = 1
    name = "2 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1='2', var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1='2', var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1='2', var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1='2', var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1='2', var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1='2', var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1='2', var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1='2', var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1='2', var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1='2', var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1='2', var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1='2', var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1='2', var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)  
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    stage = 1
    topic_progress = 2
    name = "10 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    var1="10"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_MULTIPLICATION).first()
    num_variables = 2
    level = 2
    stage = 1
    topic_progress = 3
    name = "box model multiplication 2 and 10 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()

    level_2_md_numbers = [2, 10]
    for i in level_2_md_numbers:
        for j in range(2, 10):
            boxModelMultiply = BoxModelMADS(activity_id = activity.id, question= str(i) + ' &#215; ' + str(j) +' = ?', answer=str(j*i), num_variables=2, total_value=str(j*i), part_values=str(i)+','+str(j), part_value_types='cc') 
            db.session.add(boxModelMultiply)
            db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.DIVISION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_DIVISION).first()
    num_variables = 2
    level = 2
    stage = 1
    topic_progress = 4
    name = "box model division for 2 and 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    for i in level_2_md_numbers:
        for j in range(2, 10):
            boxModelDivide = BoxModelMADS(activity_id = activity.id, question= str(i*j) + ' &#247; ' + str(i) +' = ?', answer=str(j), num_variables=2, total_value=str(j*i), part_values=str(i*j)+','+str(i), part_value_types='cc') 
            db.session.add(boxModelDivide)
            db.session.flush()
    db.session.commit()
    
def setup_level_3_add_sub(db):
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION).first()
    variables = 2
    level = 3
    stage = 1
    topic_progress = 1
    name = "(named) box model addition up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    for i in range(1, 10):
        for j in range(1, 10):
            if j + i <=10:
                boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(j) + ' + ' + str(i) +' = ?', answer=str(j+i), num_variables=2, total_value=str(j+i), part_values=str(j)+','+str(i), part_value_types='cc') 
                db.session.add(boxModelAddSubtract)
                db.session.flush()
    db.session.commit()
    
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_SUBTRACTION).first()
    variables = 2
    level = 3
    stage = 1
    topic_progress = 2
    name = "(named) box model subtraction up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    for i in range(1, 10):
        for j in range(1, 10):
            if j > i:
                boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(j) + ' - ' + str(i) +' = ?', answer=str(j-i), num_variables=2, total_value=str(j), part_values=str(j)+','+str(i), part_value_types='cc') 
                db.session.add(boxModelAddSubtract)
                db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_ADDITION).first()
    variables = 3
    level = 3
    stage = 1
    topic_progress = 3
    name = "(3 numbers) box model addition up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if j + i + k <=10:
                    boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(i) + ' + ' + str(j)+' + ' + str(k) +' = ?', \
                        answer=str(i+j+k), num_variables=variables, total_value=str(j+i+k), part_values=str(i)+','+str(j)+','+str(k), part_value_types='ccc') 
                    db.session.add(boxModelAddSubtract)
                    db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_ADDITION).first()
    variables = 3
    level = 3
    stage = 1
    topic_progress = 4
    name = "(3 numbers) box model addition up to 20"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    for i in range(1, 20):
        for j in range(1, 20):
            for k in range(1, 20):
                if j + i + k <=20:
                    boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(i) + ' + ' + str(j)+' + ' + str(k) +' = ?', \
                        answer=str(i+j+k), num_variables=variables, total_value=str(j+i+k), part_values=str(i)+','+str(j)+','+str(k), part_value_types='ccc') 
                    db.session.add(boxModelAddSubtract)
                    db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_SUBTRACTION).first()
    variables = 3
    level = 3
    stage = 1
    topic_progress = 5
    name = "(3 numbers) box model subtraction up to 20"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    for i in range(2, 20):
        for j in range(1, 10):
            for k in range(1, 10):
                if i > (j + k):
                    boxModelAddSubtract = BoxModelMADS(activity_id = activity.id, question= str(i) + ' - ' + str(j)+' - ' 
                            + str(k) +' = ?', \
                        answer=str(i-j-k), num_variables=variables, total_value=str(i), part_values=str(i)+','+str(j)+','
                        +str(k), part_value_types='ccc') 
                    db.session.add(boxModelAddSubtract)
                    db.session.flush()
    db.session.commit()
    
def setup_level_3_mult(db):
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    memorize = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MEMORIZE).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    variables = 2
    level = 3
    stage = 1
    topic_progress = 1
    name = "3 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var1="3"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()

    stage = 1
    topic_progress = 2
    name = "4 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var1="4"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()

    stage = 1
    topic_progress = 3
    name = "5 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    var1="5"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    stage = 1
    topic_progress = 4
    name = "11 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    var1="11"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_MULTIPLICATION).first()
    num_variables = 2
    level = 3
    stage = 1
    topic_progress = 5
    name = "box model multiplication 2, 3, 4, 5, 10, 11 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()

    level_3_md_numbers = [2, 3, 4, 5, 10, 11]
    for i in level_3_md_numbers:
        for j in range(2, 10):
            boxModelMultiply = BoxModelMADS(activity_id = activity.id, question= str(i) + ' &#215; ' + str(j) +' = ?', answer=str(j*i), num_variables=2, total_value=str(j*i), part_values=str(i)+','+str(j), part_value_types='cc') 
            db.session.add(boxModelMultiply)
            db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.DIVISION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_DIVISION).first()
    num_variables = 2
    level = 3
    stage = 1
    topic_progress = 6
    name = "box model division for 2, 3, 4, 5, 10 and 11"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()

    for i in level_3_md_numbers:
        for j in range(2, 10):
            boxModelDivide = BoxModelMADS(activity_id = activity.id, question= str(i*j) + ' &#247; ' + str(i) +' = ?', answer=str(j), num_variables=2, total_value=str(j*i), part_values=str(i*j)+','+str(i), part_value_types='cc') 
            db.session.add(boxModelDivide)
            db.session.flush()
    db.session.commit()

    
    #named box model method
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    box_method = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION).first()
    variables = 2
    level = 3
    stage = 1
    topic_progress = 7
    name = "(named) box model multiplication 2, 3, 4, 5, 10, 11 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = box_method.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    level_3_md_numbers = [2, 3, 4, 5, 10, 11]
    for i in level_3_md_numbers:
        for j in range(2, 10):
            boxModelMultiply = BoxModelMADS(activity_id = activity.id, question= str(i) + ' &#215; ' + str(j) +' = ?', answer=str(j*i), num_variables=2, total_value=str(j*i), part_values=str(i)+','+str(j), part_value_types='cc') 
            db.session.add(boxModelMultiply)
            db.session.flush()
    db.session.commit()
    
    
def setup_level_4_mult(db):
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    memorize = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MEMORIZE).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    variables = 2    

    #Level 4
    level = 4
    stage = 1
    topic_progress = 1
    name = "6 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var1="6"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
            
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    stage = 1
    topic_progress = 2
    name = "7 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var1="7"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()

    stage = 1
    topic_progress = 3
    name = "8 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    var1="8"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()

    stage = 1
    topic_progress = 4
    name = "9 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    var1="9"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    stage = 1
    topic_progress = 5
    name = "12 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = memorize.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    var1="12"
    var3=""
    operator1 = "*"
    operator2 = ""
    memorize1 = Memorize(activity_id = activity.id, var1=var1, var2='0', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize2 = Memorize(activity_id = activity.id, var1=var1, var2='1', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize3 = Memorize(activity_id = activity.id, var1=var1, var2='2', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize4 = Memorize(activity_id = activity.id, var1=var1, var2='3', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize5 = Memorize(activity_id = activity.id, var1=var1, var2='4', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize6 = Memorize(activity_id = activity.id, var1=var1, var2='5', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize7 = Memorize(activity_id = activity.id, var1=var1, var2='6', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize8 = Memorize(activity_id = activity.id, var1=var1, var2='7', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize9 = Memorize(activity_id = activity.id, var1=var1, var2='8', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize10 = Memorize(activity_id = activity.id, var1=var1, var2='9', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize11 = Memorize(activity_id = activity.id, var1=var1, var2='10', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize12 = Memorize(activity_id = activity.id, var1=var1, var2='11', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    memorize13 = Memorize(activity_id = activity.id, var1=var1, var2='12', var3=var3, operator1=operator1, operator2=operator2, variables=variables)
    db.session.add(memorize1)
    db.session.add(memorize2)
    db.session.add(memorize3)
    db.session.add(memorize4)
    db.session.add(memorize5)
    db.session.add(memorize6)
    db.session.add(memorize7)
    db.session.add(memorize8)
    db.session.add(memorize9)
    db.session.add(memorize10)
    db.session.add(memorize11)
    db.session.add(memorize12)
    db.session.add(memorize13)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_MULTIPLICATION).first()
    num_variables = 2
    level = 4
    stage = 1
    topic_progress = 6
    name = "box model multiplication up to 12 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()

    for i in range(2, 12):
        for j in range(2, 12):
            boxModelMultiply = BoxModelMADS(activity_id = activity.id, question= str(i) + ' &#215; ' + str(j) +' = ?', answer=str(j*i), num_variables=2, total_value=str(j*i), part_values=str(i)+','+str(j), part_value_types='cc') 
            db.session.add(boxModelMultiply)
            db.session.flush()
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.DIVISION).first() 
    BOX_METHOD = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_DIVISION).first()
    num_variables = 2
    level = 4
    stage = 1
    topic_progress = 7
    name = "box model division up to 144"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = BOX_METHOD.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = num_variables, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()

    for i in range(2, 12):
        for j in range(2, 12):
            boxModelDivide = BoxModelMADS(activity_id = activity.id, question= str(i*j) + ' &#247; ' + str(i) +' = ?', answer=str(j), num_variables=2, total_value=str(j*i), part_values=str(i*j)+','+str(i), part_value_types='cc') 
            db.session.add(boxModelDivide)
            db.session.flush()
    db.session.commit()
    

    #named box model method
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.MULTIPLICATION_AND_DIVISION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    box_method = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).filter(Strategy.qualifier == StrategyNameQualifiers.BASIC_NAMED_MULTIPLICATION).first()
    variables = 2
    level = 4
    stage = 1
    topic_progress = 8
    name = "(named) box model multiplication 2 to 12 times tables"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = box_method.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    
    for i in range(2, 12):
        for j in range(2, 12):
            boxModelMultiply = BoxModelMADS(activity_id = activity.id, question= str(i) + ' &#215; ' + str(j) +' = ?', answer=str(j*i), num_variables=2, total_value=str(j*i), part_values=str(i)+','+str(j), part_value_types='cc') 
            db.session.add(boxModelMultiply)
            db.session.flush()
    db.session.commit()
    
#TODO
#eg 46-7, add 3 to 7 to make 10, subtract 6 from 46 to make 40, add the differences.
def persist_chunk_differnce_subtraction_activities(db):
    logger.debug(">>persist_chunk_differnce_subtraction_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.CHUNK_DIFFERENCES).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    #stage is dependent on operation 
    stage = 1
    topic_progress = 3
    name = "Subtract two numbers, maximum of 15"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '11 - 2', line_positions = '11, 10, 9', jump_values = '-1, -1', stage1_question = '11 - 1 - 1', answer = '9', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '11 - 3', line_positions = '11, 10, 8', jump_values = '-1, -2', stage1_question = '11 - 1 - 2', answer = '8', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '11 - 4', line_positions = '11, 10, 7', jump_values = '-1, -3', stage1_question = '11 - 1 - 3', answer = '7', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '11 - 5', line_positions = '11, 10, 6', jump_values = '-1, -4', stage1_question = '11 - 1 -4', answer = '6', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '11 - 6', line_positions = '11, 10, 5', jump_values = '-1, -5', stage1_question = '11 - 1 -5', answer = '5', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '12 - 3', line_positions = '12, 10, 9', jump_values = '-2, -1', stage1_question = '12 - 2 -1', answer = '9', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '12 - 4', line_positions = '12, 10, 8', jump_values = '-2, -2', stage1_question = '12 - 2 -2', answer = '8', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '12 - 5', line_positions = '12, 10, 7', jump_values = '-2, -3', stage1_question = '12 - 2 -3', answer = '7', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '12 - 6', line_positions = '12, 10, 6', jump_values = '-2, -4', stage1_question = '12 - 2 -4', answer = '6', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '13 - 4', line_positions = '13, 10, 9', jump_values = '-3, -1', stage1_question = '13 - 3 -1', answer = '9', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '13 - 5', line_positions = '13, 10, 8', jump_values = '-3, -2', stage1_question = '13 - 3 -2', answer = '8', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '13 - 6', line_positions = '13, 10, 7', jump_values = '-3, -3', stage1_question = '13 - 3 -3', answer = '7', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '14 - 5', line_positions = '14, 10, 9', jump_values = '-4, -1', stage1_question = '14 - 4 -1', answer = '9', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '14 - 6', line_positions = '14, 10, 8', jump_values = '-4, -2', stage1_question = '14 - 4 -2', answer = '8', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '15 - 6', line_positions = '15, 10, 9', jump_values = '-5, -1', stage1_question = '15 - 5 -1', answer = '9', flip = False)  
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.commit()
    
def setup_activities_level_1(db):
    logger.debug(">>setup_activities_level_1()")
    category_numbers = db.session.query(Category).filter(Category.name == CategoryConstants.NUMBERS).first() 
    category_patterns = db.session.query(Category).filter(Category.name == CategoryConstants.PATTERNS).first() 
    category_addition = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    category_subtraction = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    level = 1
    level_progress = 1
    #name = "counting numbers"
    #1 show coloured number rods get student to type number of blocks
    name = "Count up to 9"
    strategy_count = db.session.query(Strategy).filter(Strategy.name == StrategyNames.COUNT).first() 
    madsActivity = MadsActivity(num_variables = 2, value_mins = '1', value_maxs = '9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_numbers.id, \
                        strategy_id = strategy_count.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    name = "Number patterns up to 9"
    #2 show single blocks/dots oriented around screen, get student to type number of blocks
    strategy_sequence = db.session.query(Strategy).filter(Strategy.name == StrategyNames.PATTERNS).first()
    madsActivity = MadsActivity(num_variables = 1, value_mins = '1', value_maxs = '9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_patterns.id, \
                        strategy_id = strategy_sequence.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)

    level_progress += 1
    name = "Add up to 6"
    #2 show two coloured rods next to each other
    #empty rod of total length below
    
    strategy_count_on = db.session.query(Strategy).filter(Strategy.name == StrategyNames.COUNT_ON).first()
    madsActivity = MadsActivity(num_variables = 2, value_mins = '0,0', value_maxs = '6,6', constraint_type = ConstraintConstants.ADD_TO_MAX_OF, constraint_value = "6", \
                        constraint_value_type = 'int', value_positions_to_apply_contraint_on="2")
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_count_on.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    name = "Count back from 6"
    strategy_count_back = db.session.query(Strategy).filter(Strategy.name == StrategyNames.COUNT_BACK).first()
    madsActivity = MadsActivity(num_variables = 2, value_mins = '0,0', \
                        value_maxs = '6,6')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name) 
    activity = Activity(category_id = category_subtraction.id, \
                        strategy_id = strategy_count_back.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
 
    level_progress += 1
    #2 show two coloured rods next to each other
    #empty rod of total length below
    name = "Add up to 10"
    strategy_count_on = db.session.query(Strategy).filter(Strategy.name == StrategyNames.COUNT_ON).first()
    madsActivity = MadsActivity(num_variables = 2, value_mins = '0,0', \
                        value_maxs = '9,9', constraint_type = ConstraintConstants.ADD_TO_MAX_OF, \
                        constraint_value = "10", \
                        constraint_value_type = 'int', value_positions_to_apply_contraint_on="2")
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_count_on.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    name = "Count back from 10"
    strategy_count_back = db.session.query(Strategy).filter(Strategy.name == StrategyNames.COUNT_BACK).first()
    madsActivity = MadsActivity(num_variables = 2, value_mins = '0,0', \
                        value_maxs = '9,9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name) 
    activity = Activity(category_id = category_subtraction.id, \
                        strategy_id = strategy_count_back.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)

    level_progress += 1
    #eg SGP Math Level 2 pg 6 Number Bond
    name = "Count up to 10"
    
    strategy_chunking_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_DIGIT).first()
    madsActivity = MadsActivity(num_variables = 1, value_mins = '2', \
                        value_maxs = '10')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_chunking_single.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
def setup_activities_level_2(db):
    '''Level 2 table setup '''
    logger.debug(">>setup_activities_level_2")
    
    category_addition = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    category_subtraction = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    db.session.flush()
    level = 2
    level_progress = 7
    
    '''
    level = 2
    level_progress = 1
    name = "Add two numbers, up to 18"
    strategy_chunking_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_SINGLE).first()
    funChunksOrFrieldyAndFixActivity = FunChunksOrFrieldyAndFixActivity(num_variables = 2, \
                        value_mins = '5, 1', \
                        value_maxs = '9, 9', \
                        value_position_to_split_or_fix = '1')
    db.session.add(funChunksOrFrieldyAndFixActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_chunking_single_single.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = funChunksOrFrieldyAndFixActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    '''
    level_progress += 1
    #friendly and fix, two single digits to 9
    name = "Add two numbers, up to 18"
    #iMaths 2 pg 163, Friend;ly and Fix 1
    strategy_friendly_and_fix = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '5, 6', \
                        value_maxs = '9, 9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_friendly_and_fix.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    #add two numbers, up to 18
    name = "Add two numbers,up to 18"
    strategy_friendly_and_fix = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '1, 7', \
                        value_maxs = '9, 9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)   
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_friendly_and_fix.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    #friendly and fix, one double digit up to 48
    name = "Add two numbers, up to 48"
    #iMaths 2 pg 163, Friend;ly and Fix 1
    url_name = createURL(level, level_progress, name)
    strategy_friendly_and_fix = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '5, 6', \
                        value_maxs = '39, 9')
    db.session.add(madsActivity)
    db.session.flush()
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_friendly_and_fix.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    '''
    level_progress += 1
    #name = "friendly and fix, one double digit up to 98"
    name = "Add two numbers, up to 98"
    
    strategy_chunking_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_DOUBLE).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '15, 6', \
                        value_maxs = '89, 9', constraint_type = ConstraintConstants.ONES_COLUMN_GREATER_THAN_N, \
                        constraint_value = "4",\
                        constraint_value_type = 'int', value_positions_to_apply_contraint_on="0")
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_chunking_single_double.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    '''
    level_progress += 1
    name = "Add two numbers, up to 99"
     
    strategy_friendly_and_fix = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '11, 7', \
                        value_maxs = '89, 9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)   
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_friendly_and_fix.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    '''
    level_progress += 1
    name = "Subtract two numbers,maximum of 18"
    strategy_subtraction_chunking_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_DOUBLE).first()
    madsActivity = MadsActivity(num_variables = 2, value_mins = '11,2', \
                        value_maxs = '18,9', \
                        constraint_type = ConstraintConstants.ONES_COLUMN_VALUE1_MINUS_VALUE0_NEGATIVE)
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name) 
    activity = Activity(category_id = category_subtraction.id, \
                        strategy_id = strategy_subtraction_chunking_single_double.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)

    level_progress += 1
    name = "Subtract two numbers,maximum of 88"
    strategy_subtraction_chunking_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_DOUBLE).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '21, 2', \
                        value_maxs = '88, 9', \
                        constraint_type = ConstraintConstants.ONES_COLUMN_VALUE1_MINUS_VALUE0_NEGATIVE)
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)    
    activity = Activity(category_id = category_subtraction.id, \
                        strategy_id = strategy_subtraction_chunking_single_double.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    '''
    
    #memorize only specific 'anchor points'
    #ie  multiples of 2 - 2, multiples of 3 -3 though 10
    level_progress += 1
    name = "Add two numbers, up to 18"
    strategy_memorize = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MEMORIZE).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '0, 0', \
                        value_maxs = '9, 9')
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)    
    activity = Activity(category_id = category_addition.id, \
                        strategy_id = strategy_memorize.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    name = "Subtract two numbers, maximum of 18"
    strategy_memorize = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MEMORIZE).first()
    madsActivity = MadsActivity(num_variables = 2, \
                        value_mins = '0, 0', \
                        value_maxs = '18, 9', constraint_type = ConstraintConstants.NON_NEGATIVE, \
                        value_positions_to_apply_contraint_on="2")
    db.session.add(madsActivity)
    db.session.flush()
    url_name = createURL(level, level_progress, name)    
    activity = Activity(category_id = category_subtraction.id, \
                        strategy_id = strategy_memorize.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = madsActivity.id, \
                        activity_action_type = ActivityTypeConstants.MADS, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 25, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    db.session.commit()
    '''
    
    #box activities
    level_progress += 1
    name = "Add two numbers"
    strategy_box_basic = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).first()
    box_method_add = BoxMethod(num_variables = 2);    
    db.session.add(box_method_add)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = LegacyActivity(category_id = category_addition.id, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method_add.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''
    level_progress += 1
    name = "Subtract two numbers"
    strategy_box_basic = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_METHOD).first()
    box_method_subtract = BoxMethod(num_variables = 2);    
    db.session.add(box_method_subtract)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = LegacyActivity(category_id = category_subtraction.id, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method_subtract.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    '''

def setup_activities_level_3(db):
    '''Level 3 table setup '''
    logger.debug(">>setup_activities_level_3")
    
    category_multiplication = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    category_division = db.session.query(Category).filter(Category.name == CategoryConstants.DIVISION).first() 
 
    level = 3
    level_progress = 1
    name = "Multiply two numbers"
    strategy_box_basic = db.session.query(Strategy).filter(Strategy.name == StrategyNames.MULTIPLICATION_BOX_BASIC).first()
    box_method = BoxMethod(num_variables = 2);    
    db.session.add(box_method)
    db.session.flush()
    
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_multiplication.id, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level_progress += 1
    name = "Divide two numbers"
    strategy_box_basic = db.session.query(Strategy).filter(Strategy.name == StrategyNames.DIVISION_BOX_BASIC).first()
    box_method = BoxMethod(num_variables = 2);    
    db.session.add(box_method)
    db.session.flush()
    url_name = createURL(level, level_progress, name)
    activity = Activity(category_id = category_division.id, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        name = name, \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    db.session.commit()
      
def setup_activities_level_4(db):
    '''Level 4 table setup '''
    category_numbers = db.session.query(Category).filter(Category.name == CategoryConstants.NUMBERS).first() 
    category_patterns = db.session.query(Category).filter(Category.name == CategoryConstants.PATTERNS).first() 
    category_addition = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    category_subtraction = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    category_multiplication = db.session.query(Category).filter(Category.name == CategoryConstants.MULTIPLICATION).first() 
    category_division = db.session.query(Category).filter(Category.name == CategoryConstants.DIVISION).first() 
    category_fractions = db.session.query(Category).filter(Category.name == CategoryConstants.FRACTIONS).first() 
    category_decimals = db.session.query(Category).filter(Category.name == CategoryConstants.DECIMALS).first() 
    category_percentage = db.session.query(Category).filter(Category.name == CategoryConstants.PERCENTAGE).first() 
    category_average = db.session.query(Category).filter(Category.name == CategoryConstants.AVERAGE).first() 
    category_ratio = db.session.query(Category).filter(Category.name == CategoryConstants.RATIO).first() 
    category_powers = db.session.query(Category).filter(Category.name == CategoryConstants.POWERS).first() 
    category_roots = db.session.query(Category).filter(Category.name == CategoryConstants.ROOTS).first() 
    category_measurement = db.session.query(Category).filter(Category.name == CategoryConstants.MEASUREMENT).first() 
    category_geometry = db.session.query(Category).filter(Category.name == CategoryConstants.GEOMETRY).first()   
    
    level = 4
    level_progress = 1 
    
#one off db stuff
def create_name_pass_for_user(db, existing_email, user_name, password):
    user = db.session.query(User).filter(User.email == existing_email).first()
    if user:
        user.user_name = user_name
        user.password = password
        user.confirmed = True
        user.time_signedup = datetime.datetime.now()
        user.time_confirmed = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()

#for dev db only
def dummy_create_user(db, email):
    student_role = db.session.query(Role).filter(Role.role_name == RoleTypes.STUDENT).first()
    student_user = User(role_id = student_role.id, email = email, contact_name = 'Parent/Guardian/Teacher')
    db.session.add(student_user)
    db.session.flush()
    student = Student(user_id = student_user.id,
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student)
    db.session.flush()
    
    
def drop_student_by_user_id(db, user_id):
    db.session.query(Student).filter(Student.user_id == user_id).delete()

        
def drop_user_by_username(db, user_name):
    db.session.query(User).filter(User.user_name == user_name).delete()
    
''' 
def setup_box_activities(db):
    logger.debug(">>setup_box_activities()")
    level = 2
    level_progress = 2
    name = StrategyNames.BOX_BASIC+" model: "+CategoryConstants.ADDITION
    url_name = createURL(level, level_progress, name)
    strategy_box_basic = db.session.query(Strategy).filter(Strategy.name == StrategyNames.BOX_BASIC).first()

    box_method = BoxMethod(num_variables = 2);    
    db.session.add(box_method)
    db.session.flush()
    
    activity = Activity(topic = TopicConstants.TOPIC_NUMBER_AND_ALGEBRA, category = CategoryConstants.ADDITION, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        strategy_class = strategy_box_basic.strategy_class, \
                        name = name,  \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    name = StrategyNames.BOX_BASIC+" model: "+CategoryConstants.SUBTRACTION
    activity = Activity(topic = TopicConstants.TOPIC_NUMBER_AND_ALGEBRA, category = CategoryConstants.SUBTRACTION, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        strategy_class = strategy_box_basic.strategy_class, \
                        name = name,  \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    level = 3
    level_progress = 2
    name = StrategyNames.BOX_BASIC+" model: "+CategoryConstants.MULTIPLICATION
    url_name = createURL(level, level_progress, name)
    activity = Activity(topic = TopicConstants.TOPIC_NUMBER_AND_ALGEBRA, category = CategoryConstants.MULTIPLICATION, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        strategy_class = strategy_box_basic.strategy_class, \
                        name = name,  \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    
    name = StrategyNames.BOX_BASIC+" model: "+CategoryConstants.DIVISION
    activity = Activity(topic = TopicConstants.TOPIC_NUMBER_AND_ALGEBRA, category = CategoryConstants.DIVISION, \
                        strategy_id = strategy_box_basic.id, \
                        level = level, level_progress = level_progress, \
                        activity_action_id = box_method.id, \
                        activity_action_type = ActivityTypeConstants.BOX_METHOD, \
                        strategy_class = strategy_box_basic.strategy_class, \
                        name = name,  \
                        url_name = url_name, \
                        time_limit = 600, total_questions = 5, \
                        answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    db.session.commit()
'''
    
'''
def persist_numberbond_addition_activities(db):
    logger.debug(">>persist_numberbond_addition_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    level = 1
    #stage is dependent on operation 
    stage = 1
    topic_progress = 1
    name = "Recognise number bond patterns up to 6"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_counters.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.COUNTERS
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='1', part2='5')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='1', part2='3')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    topic_progress = 2
    name = "Recognise number bond patterns up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_counters.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.COUNTERS
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    topic_progress = 3
    name = "Find the missing whole up to 6"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_part_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.PART_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='1', part2='5')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='1', part2='3')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    topic_progress = 4
    name = "Find the missing whole up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_part_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.PART_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    numberbond_counters = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.COUNTERS).first()
    numberbond_part_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.PART_PART).first()
    numberbond_whole_part = db.session.query(Strategy).filter(Strategy.name == StrategyNames.NUMBER_BONDS).filter(Strategy.qualifier == StrategyNameQualifiers.WHOLE_PART).first()
    topic_progress = 5
    name = "Find the missing part up to 10"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = numberbond_whole_part.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    numberbond_type = NumberBondTypes.WHOLE_PART
    numberBonds1 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='4', part2='3')
    numberBonds2 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='5', part2='3')
    numberBonds3 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='6', part2='4')
    numberBonds4 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='7', part2='3')
    numberBonds5 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='2', part2='8')
    numberBonds6 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='6', part2='3')
    numberBonds7 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='6', part2='2')
    numberBonds8 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='9', part2='1')
    numberBonds9 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='5', part2='5')
    numberBonds10 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='10', part1='8', part2='2')
    numberBonds11 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='1', part2='6')
    numberBonds12 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='4', part2='4')
    numberBonds13 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='2', part2='7')
    numberBonds14 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='5', part2='4')
    numberBonds15 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='1', part2='7')
    numberBonds16 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='9', part1='3', part2='6')
    numberBonds17 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='8', part1='3', part2='5')
    numberBonds18 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='5', part2='2')
    numberBonds19 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='6', part2='1')
    numberBonds20 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='7', part1='3', part2='4')
    numberBonds21 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='2', part2='3')
    numberBonds22 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='3', part2='3')
    numberBonds23 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='3', part2='2')
    numberBonds24 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='2', part2='2')
    numberBonds25 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='4', part1='3', part2='1')
    numberBonds26 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='2', part2='4')
    numberBonds27 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='4', part2='1')
    numberBonds28 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='5', part1='1', part2='4')
    numberBonds29 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='4', part2='2')
    numberBonds30 = NumberBonds(activity_id = activity.id, numberbond_type=numberbond_type, whole='6', part1='5', part2='1')
    db.session.add(numberBonds1)
    db.session.add(numberBonds2)
    db.session.add(numberBonds3)
    db.session.add(numberBonds4)
    db.session.add(numberBonds5)
    db.session.add(numberBonds6)
    db.session.add(numberBonds7)
    db.session.add(numberBonds8)
    db.session.add(numberBonds9)
    db.session.add(numberBonds10)
    db.session.add(numberBonds11)
    db.session.add(numberBonds12)
    db.session.add(numberBonds13)
    db.session.add(numberBonds14)
    db.session.add(numberBonds15)
    db.session.add(numberBonds16)
    db.session.add(numberBonds17)
    db.session.add(numberBonds18)
    db.session.add(numberBonds19)
    db.session.add(numberBonds20)
    db.session.add(numberBonds21)
    db.session.add(numberBonds22)
    db.session.add(numberBonds23)
    db.session.add(numberBonds24)
    db.session.add(numberBonds25)
    db.session.add(numberBonds26)
    db.session.add(numberBonds27)
    db.session.add(numberBonds28)
    db.session.add(numberBonds29)
    db.session.add(numberBonds30)
    db.session.commit()
'''

'''
def persist_friendly_and_fix_addition_activities(db):
    logger.debug(">>persist_friendly_and_fix_addition_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_friendly_and_fix_single_n_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    db.session.flush()
    level = 2
    stage = 1
    topic_progress = 2
    name = "Add two numbers, up to 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_single.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '6 + 7', line_positions = '6, 16, 13', jump_values = '10, -3', stage1_question = '6 + 10 - 3', answer = '13', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '6 + 8', line_positions = '6, 16, 14', jump_values = '10, -2', stage1_question = '6 + 10 - 2', answer = '14', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '6 + 9', line_positions = '6, 16, 15', jump_values = '10, -1', stage1_question = '6 + 10 - 1', answer = '15', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '7 + 7', line_positions = '7, 17, 14', jump_values = '10, -3', stage1_question = '7 + 10 - 3', answer = '14', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '7 + 8', line_positions = '7, 17, 15', jump_values = '10, -2', stage1_question = '7 + 10 - 2', answer = '15', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '7 + 9', line_positions = '7, 17, 16', jump_values = '10, -1', stage1_question = '7 + 10 - 1', answer = '16', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '8 + 7', line_positions = '8, 18, 15', jump_values = '10, -3', stage1_question = '8 + 10 - 3', answer = '15', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '8 + 8', line_positions = '8, 18, 16', jump_values = '10, -2', stage1_question = '8 + 10 - 2', answer = '16', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '8 + 9', line_positions = '8, 18, 17', jump_values = '10, -1', stage1_question = '8 + 10 - 1', answer = '17', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '9 + 7', line_positions = '9, 19, 16', jump_values = '10, -3', stage1_question = '9 + 10 - 3', answer = '16', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '9 + 8', line_positions = '9, 19, 17', jump_values = '10, -2', stage1_question = '9 + 10 - 2', answer = '17', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '9 + 9', line_positions = '9, 19, 18', jump_values = '10, -1', stage1_question = '9 + 10 - 1', answer = '18', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.commit()
        
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_friendly_and_fix_single_n_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    stage = 2
    topic_progress = 7
    name = "Add two numbers, up to 108"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '36 + 7', line_positions = '36, 46, 43', jump_values = '10, -3', stage1_question = '36 + 10 - 3', answer = '43', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '46 + 8', line_positions = '46, 56, 54', jump_values = '10, -2', stage1_question = '46 + 10 - 2', answer = '54', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '56 + 9', line_positions = '56, 66, 65', jump_values = '10, -1', stage1_question = '56 + 10 - 1', answer = '65', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '66 + 7', line_positions = '66, 76, 73', jump_values = '10, -3', stage1_question = '66 + 10 - 3', answer = '73', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '76 + 8', line_positions = '76, 86, 84', jump_values = '10, -2', stage1_question = '76 + 10 - 2', answer = '84', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '86 + 9', line_positions = '86, 96, 95', jump_values = '10, -1', stage1_question = '86 + 10 - 1', answer = '95', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '67 + 7', line_positions = '67, 77, 74', jump_values = '10, -3', stage1_question = '67 + 10 - 3', answer = '74', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '77 + 8', line_positions = '77, 87, 85', jump_values = '10, -2', stage1_question = '77 + 10 - 2', answer = '85', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '87 + 9', line_positions = '87, 97, 96', jump_values = '10, -1', stage1_question = '87 + 10 - 1', answer = '96', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '17 + 7', line_positions = '17, 27, 24', jump_values = '10, -3', stage1_question = '17 + 10 - 3', answer = '24', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '27 + 8', line_positions = '27, 37, 35', jump_values = '10, -2', stage1_question = '27 + 10 - 2', answer = '35', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '37 + 9', line_positions = '37, 47, 46', jump_values = '10, -1', stage1_question = '37 + 10 - 1', answer = '46', flip = False)
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '98 + 7', line_positions = '98, 108, 105', jump_values = '10, -3', stage1_question = '98 + 10 - 3', answer = '105', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '18 + 8', line_positions = '18, 28, 26', jump_values = '10, -2', stage1_question = '18 + 10 - 2', answer = '26', flip = False)
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '28 + 9', line_positions = '28, 38, 37', jump_values = '10, -1', stage1_question = '28 + 10 - 1', answer = '37', flip = False)
    friendlyAndFix16 = FriendlyAndFix(activity_id = activity.id, question = '48 + 7', line_positions = '48, 58, 55', jump_values = '10, -3', stage1_question = '48 + 10 - 3', answer = '55', flip = False)
    friendlyAndFix17 = FriendlyAndFix(activity_id = activity.id, question = '58 + 8', line_positions = '58, 68, 66', jump_values = '10, -2', stage1_question = '58 + 10 - 2', answer = '66', flip = False)
    friendlyAndFix18 = FriendlyAndFix(activity_id = activity.id, question = '68 + 9', line_positions = '68, 78, 77', jump_values = '10, -1', stage1_question = '68 + 10 - 1', answer = '77', flip = False)
    friendlyAndFix19 = FriendlyAndFix(activity_id = activity.id, question = '39 + 7', line_positions = '39, 49, 46', jump_values = '10, -3', stage1_question = '39 + 10 - 3', answer = '46', flip = False)
    friendlyAndFix20 = FriendlyAndFix(activity_id = activity.id, question = '49 + 8', line_positions = '49, 59, 57', jump_values = '10, -2', stage1_question = '49 + 10 - 2', answer = '57', flip = False)
    friendlyAndFix21 = FriendlyAndFix(activity_id = activity.id, question = '59 + 9', line_positions = '59, 69, 68', jump_values = '10, -1', stage1_question = '59 + 10 - 1', answer = '68', flip = False)
    friendlyAndFix22 = FriendlyAndFix(activity_id = activity.id, question = '69 + 7', line_positions = '69, 79, 76', jump_values = '10, -3', stage1_question = '69 + 10 - 3', answer = '76', flip = False)
    friendlyAndFix23 = FriendlyAndFix(activity_id = activity.id, question = '79 + 8', line_positions = '79, 89, 87', jump_values = '10, -2', stage1_question = '79 + 10 - 2', answer = '87', flip = False)
    friendlyAndFix24 = FriendlyAndFix(activity_id = activity.id, question = '89 + 9', line_positions = '89, 99, 98', jump_values = '10, -1', stage1_question = '89 + 10 - 1', answer = '98', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.add(friendlyAndFix16)
    db.session.add(friendlyAndFix17)
    db.session.add(friendlyAndFix18)
    db.session.add(friendlyAndFix19)
    db.session.add(friendlyAndFix20)
    db.session.add(friendlyAndFix21)
    db.session.add(friendlyAndFix22)
    db.session.add(friendlyAndFix23)
    db.session.add(friendlyAndFix24)
    db.session.commit()
'''
   
''' 
def persist_friendly_and_fix_subtraction_activities(db):
    logger.debug(">>persist_friendly_and_fix_subtraction_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    stage = 1
    topic_progress = 4
    name = "Subtract two numbers, maximum of 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '18 - 9', line_positions = '18, 8, 9', jump_values = '-10, 1', stage1_question = '18 - 10 + 1', answer = '9', flip = False)                                                                                                      
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '17 - 9', line_positions = '17, 7, 8', jump_values = '-10, 1', stage1_question = '17 - 10 + 1', answer = '8', flip = False)
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '17 - 8', line_positions = '17, 7, 9', jump_values = '-10, 2', stage1_question = '17 - 10 + 2', answer = '9', flip = False)                                                                                                         
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '16 - 9', line_positions = '16, 6, 7', jump_values = '-10, 1', stage1_question = '16 - 10 + 1', answer = '7', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '16 - 8', line_positions = '16, 6, 8', jump_values = '-10, 2', stage1_question = '16 - 10 + 2', answer = '8', flip = False)
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '16 - 7', line_positions = '16, 6, 9', jump_values = '-10, 3', stage1_question = '16 - 10 + 3', answer = '9', flip = False)                                                                                                       
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '15 - 9', line_positions = '15, 5, 6', jump_values = '-10, 1', stage1_question = '15 - 10 + 1', answer = '6', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '15 - 8', line_positions = '15, 5, 7', jump_values = '-10, 2', stage1_question = '15 - 10 + 2', answer = '7', flip = False)
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '15 - 7', line_positions = '15, 5, 8', jump_values = '-10, 3', stage1_question = '15 - 10 + 3', answer = '8', flip = False)   
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '14 - 9', line_positions = '14, 4, 5', jump_values = '-10, 1', stage1_question = '14 - 10 + 1', answer = '5', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '14 - 8', line_positions = '14, 4, 6', jump_values = '-10, 2', stage1_question = '14 - 10 + 2', answer = '6', flip = False)
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '14 - 7', line_positions = '14, 4, 7', jump_values = '-10, 3', stage1_question = '14 - 10 + 3', answer = '7', flip = False)                                                                                                       
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '13 - 9', line_positions = '13, 3, 4', jump_values = '-10, 1', stage1_question = '13 - 10 + 1', answer = '4', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '13 - 8', line_positions = '13, 3, 5', jump_values = '-10, 2', stage1_question = '13 - 10 + 2', answer = '5', flip = False)
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '13 - 7', line_positions = '13, 3, 6', jump_values = '-10, 3', stage1_question = '13 - 10 + 3', answer = '6', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.commit()
        
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_friendly_and_fix_single_n_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FRIENDLY_AND_FIX).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    stage = 2
    topic_progress = 10
    name = "Subtract two numbers, maximum of 98"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_friendly_and_fix_single_n_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    friendlyAndFix1 = FriendlyAndFix(activity_id = activity.id, question = '28 - 9', line_positions = '28, 18, 19', jump_values = '-10, 1', stage1_question = '28 - 10 + 1', answer = '19', flip = False)
    friendlyAndFix2 = FriendlyAndFix(activity_id = activity.id, question = '68 - 9', line_positions = '68, 58, 59', jump_values = '-10, 1', stage1_question = '68 - 10 + 1', answer = '59', flip = False)                                                                                                  
    friendlyAndFix3 = FriendlyAndFix(activity_id = activity.id, question = '37 - 9', line_positions = '37, 27, 28', jump_values = '-10, 1', stage1_question = '37 - 10 + 1', answer = '28', flip = False)
    friendlyAndFix4 = FriendlyAndFix(activity_id = activity.id, question = '47 - 8', line_positions = '47, 37, 39', jump_values = '-10, 2', stage1_question = '47 - 10 + 2', answer = '39', flip = False)
    friendlyAndFix5 = FriendlyAndFix(activity_id = activity.id, question = '87 - 8', line_positions = '87, 77, 79', jump_values = '-10, 2', stage1_question = '87 - 10 + 2', answer = '79', flip = False)                                                                                                     
    friendlyAndFix6 = FriendlyAndFix(activity_id = activity.id, question = '56 - 9', line_positions = '56, 46, 47', jump_values = '-10, 1', stage1_question = '56 - 10 + 1', answer = '47', flip = False)
    friendlyAndFix7 = FriendlyAndFix(activity_id = activity.id, question = '66 - 8', line_positions = '66, 56, 58', jump_values = '-10, 2', stage1_question = '66 - 10 + 2', answer = '58', flip = False)
    friendlyAndFix8 = FriendlyAndFix(activity_id = activity.id, question = '76 - 7', line_positions = '76, 66, 69', jump_values = '-10, 3', stage1_question = '76 - 10 + 3', answer = '69', flip = False)                                                                                                            
    friendlyAndFix9 = FriendlyAndFix(activity_id = activity.id, question = '85 - 9', line_positions =  '85, 75, 76',  jump_values = '-10, 1', stage1_question = '85 - 10 + 1', answer = '76', flip = False)
    friendlyAndFix10 = FriendlyAndFix(activity_id = activity.id, question = '95 - 8', line_positions = '95, 85, 87', jump_values = '-10, 2', stage1_question = '95 - 10 + 2', answer = '87', flip = False)
    friendlyAndFix11 = FriendlyAndFix(activity_id = activity.id, question = '25 - 7', line_positions = '25, 15, 18', jump_values = '-10, 3', stage1_question = '25 - 10 + 3', answer = '18', flip = False)                                                                                                          
    friendlyAndFix12 = FriendlyAndFix(activity_id = activity.id, question = '34 - 9', line_positions = '34, 24, 25', jump_values = '-10, 1', stage1_question = '34 - 10 + 1', answer = '25', flip = False)
    friendlyAndFix13 = FriendlyAndFix(activity_id = activity.id, question = '44 - 8', line_positions = '44, 34, 36', jump_values = '-10, 2', stage1_question = '44 - 10 + 2', answer = '36', flip = False)
    friendlyAndFix14 = FriendlyAndFix(activity_id = activity.id, question = '54 - 7', line_positions = '54, 44, 47', jump_values = '-10, 3', stage1_question = '54 - 10 + 3', answer = '47', flip = False)                                                                                                    
    friendlyAndFix15 = FriendlyAndFix(activity_id = activity.id, question = '63 - 9', line_positions = '63, 54, 53', jump_values = '-10, 1', stage1_question = '63 - 10 + 1', answer = '54', flip = False)
    friendlyAndFix16 = FriendlyAndFix(activity_id = activity.id, question = '73 - 8', line_positions = '73, 65, 63', jump_values = '-10, 2', stage1_question = '73 - 10 + 2', answer = '65', flip = False)
    friendlyAndFix17 = FriendlyAndFix(activity_id = activity.id, question = '83 - 7', line_positions = '83, 76, 73', jump_values = '-10, 3', stage1_question = '83 - 10 + 3', answer = '76', flip = False)
    db.session.add(friendlyAndFix1)
    db.session.add(friendlyAndFix2)
    db.session.add(friendlyAndFix3)
    db.session.add(friendlyAndFix4)
    db.session.add(friendlyAndFix5)
    db.session.add(friendlyAndFix6)
    db.session.add(friendlyAndFix7)
    db.session.add(friendlyAndFix8)
    db.session.add(friendlyAndFix9)
    db.session.add(friendlyAndFix10)
    db.session.add(friendlyAndFix11)
    db.session.add(friendlyAndFix12)
    db.session.add(friendlyAndFix13)
    db.session.add(friendlyAndFix14)
    db.session.add(friendlyAndFix15)
    db.session.add(friendlyAndFix16)
    db.session.add(friendlyAndFix17)
    db.session.commit()
'''
    
'''
def persist_fun_chunk_addition_activities(db):
    logger.debug(">>persist_fun_chunk_addition_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    stage = 1
    topic_progress = 1
    name = "Add two numbers, up to 18"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_single.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '6 + 5', line_positions = '6, 10, 11', jump_values = '4, 1', stage1_question = '6 + 4 + 1', answer = '11', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '6 + 6', line_positions = '6, 10, 12', jump_values = '4, 2', stage1_question = '6 + 4 + 2', answer = '12', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '6 + 7', line_positions = '7, 10, 13', jump_values = '3, 3', stage1_question = '7 + 3 + 3', answer = '13', flip = True)
    funChunks4 = FunChunks(activity_id = activity.id, question = '6 + 8', line_positions = '8, 10, 14', jump_values = '2, 4', stage1_question = '8 + 2 + 4', answer = '14', flip = True)
    funChunks5 = FunChunks(activity_id = activity.id, question = '6 + 9', line_positions = '9, 10, 15', jump_values = '1, 5', stage1_question = '9 + 1 + 5', answer = '15', flip = True)
    funChunks6 = FunChunks(activity_id = activity.id, question = '7 + 5', line_positions = '7, 10, 12', jump_values = '3, 2', stage1_question = '7 + 3 + 2', answer = '12', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '7 + 6', line_positions = '7, 10, 13', jump_values = '3, 3', stage1_question = '7 + 3 + 3', answer = '13', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '7 + 7', line_positions = '7, 10, 14', jump_values = '3, 4', stage1_question = '7 + 3 + 4', answer = '14', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '7 + 8', line_positions = '8, 10, 15', jump_values = '2, 5', stage1_question = '8 + 2 + 5', answer = '15', flip = True)
    funChunks10 = FunChunks(activity_id = activity.id, question = '7 + 9', line_positions = '9, 10, 16', jump_values = '1, 6', stage1_question = '9 + 1 + 6', answer = '16', flip = True)
    funChunks11 = FunChunks(activity_id = activity.id, question = '8 + 5', line_positions = '8, 10, 13', jump_values = '2, 3', stage1_question = '8 + 2 + 5', answer = '13', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '8 + 6', line_positions = '8, 10, 14', jump_values = '2, 4', stage1_question = '8 + 2 + 4', answer = '14', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '8 + 7', line_positions = '8, 10, 15', jump_values = '2, 5', stage1_question = '8 + 2 + 5', answer = '15', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '8 + 8', line_positions = '8, 10, 16', jump_values = '2, 6', stage1_question = '8 + 2 + 6', answer = '16', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '8 + 9', line_positions = '9, 10, 17', jump_values = '1, 7', stage1_question = '9 + 1 + 7', answer = '17', flip = True)
    funChunks16 = FunChunks(activity_id = activity.id, question = '9 + 5', line_positions = '9, 10, 14', jump_values = '1, 4', stage1_question = '9 + 1 + 4', answer = '14', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '9 + 6', line_positions = '9, 10, 15', jump_values = '1, 5', stage1_question = '9 + 1 + 5', answer = '15', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '9 + 7', line_positions = '9, 10, 16', jump_values = '1, 6', stage1_question = '9 + 1 + 6', answer = '16', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '9 + 8', line_positions = '9, 10, 17', jump_values = '1, 7', stage1_question = '9 + 1 + 7', answer = '17', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '9 + 9', line_positions = '9, 10, 18', jump_values = '1, 8', stage1_question = '9 + 1 + 8', answer = '18', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
        
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()      
    stage = 2
    topic_progress = 5
    name = "Add two numbers, up to 58"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '46 + 5', line_positions = '46, 50, 51', jump_values = '4, 1', stage1_question = '46 + 4 + 1', answer = '51', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '36 + 6', line_positions = '36, 40, 42', jump_values = '4, 2', stage1_question = '36 + 4 + 2', answer = '42', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '26 + 7', line_positions = '26, 30, 33', jump_values = '4, 3', stage1_question = '26 + 4 + 3', answer = '33', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '16 + 8', line_positions = '16, 20, 24', jump_values = '4, 4', stage1_question = '16 + 4 + 4', answer = '24', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '46 + 9', line_positions = '46, 50, 55', jump_values = '4, 5', stage1_question = '46 + 4 + 5', answer = '55', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '47 + 5', line_positions = '47, 50, 52', jump_values = '3, 2', stage1_question = '47 + 3 + 2', answer = '52', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '17 + 6', line_positions = '17, 20, 23', jump_values = '3, 3', stage1_question = '17 + 3 + 3', answer = '23', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '37 + 7', line_positions = '37, 40, 44', jump_values = '3, 4', stage1_question = '37 + 3 + 4', answer = '44', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '27 + 8', line_positions = '27, 30, 35', jump_values = '3, 5', stage1_question = '27 + 3 + 5', answer = '35', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '37 + 9', line_positions = '37, 40, 46', jump_values = '3, 6', stage1_question = '37 + 3 + 6', answer = '46', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '28 + 5', line_positions = '28, 30, 33', jump_values = '2, 3', stage1_question = '28 + 2 + 5', answer = '33', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '48 + 6', line_positions = '48, 50, 54', jump_values = '2, 4', stage1_question = '48 + 2 + 4', answer = '54', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '18 + 7', line_positions = '18, 20, 25', jump_values = '2, 5', stage1_question = '18 + 2 + 5', answer = '25', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '38 + 8', line_positions = '38, 40, 46', jump_values = '2, 6', stage1_question = '38 + 2 + 6', answer = '46', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '28 + 9', line_positions = '28, 30, 37', jump_values = '2, 7', stage1_question = '28 + 2 + 7', answer = '37', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '19 + 5', line_positions = '19, 20, 24', jump_values = '1, 4', stage1_question = '19 + 1 + 4', answer = '24', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '29 + 6', line_positions = '29, 30, 35', jump_values = '1, 5', stage1_question = '29 + 1 + 5', answer = '35', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '49 + 7', line_positions = '49, 50, 56', jump_values = '1, 6', stage1_question = '49 + 1 + 6', answer = '56', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '39 + 8', line_positions = '39, 40, 47', jump_values = '1, 7', stage1_question = '39 + 1 + 7', answer = '47', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '19 + 9', line_positions = '19, 20, 28', jump_values = '1, 8', stage1_question = '19 + 1 + 8', answer = '28', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()

    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()   
    stage = 3
    topic_progress = 8
    name = "Add two numbers, up to 108"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '56 + 5', line_positions = '56, 60, 61', jump_values = '4, 1', stage1_question = '56 + 4 + 1', answer = '61', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '76 + 6', line_positions = '76, 80, 82', jump_values = '4, 2', stage1_question = '76 + 4 + 2', answer = '82', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '86 + 7', line_positions = '86, 90, 93', jump_values = '4, 3', stage1_question = '86 + 4 + 3', answer = '93', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '96 + 8', line_positions = '96, 100, 104', jump_values = '4, 4', stage1_question = '96 + 4 + 4', answer = '104', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '56 + 9', line_positions = '56, 60, 65', jump_values = '4, 5', stage1_question = '56 + 4 + 5', answer = '65', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '67 + 5', line_positions = '67, 70, 72', jump_values = '3, 2', stage1_question = '67 + 3 + 2', answer = '72', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '87 + 6', line_positions = '87, 90, 93', jump_values = '3, 3', stage1_question = '87 + 3 + 3', answer = '93', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '97 + 7', line_positions = '97, 100, 104', jump_values = '3, 4', stage1_question = '97 + 3 + 4', answer = '104', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '57 + 8', line_positions = '57, 60, 65', jump_values = '3, 5', stage1_question = '57 + 3 + 5', answer = '65', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '77 + 9', line_positions = '77, 80, 86', jump_values = '3, 6', stage1_question = '77 + 3 + 6', answer = '86', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '78 + 5', line_positions = '78, 80, 83', jump_values = '2, 3', stage1_question = '78 + 2 + 5', answer = '83', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '88 + 6', line_positions = '88, 90, 94', jump_values = '2, 4', stage1_question = '88 + 2 + 4', answer = '94', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '98 + 7', line_positions = '98, 100, 105', jump_values = '2, 5', stage1_question = '98 + 2 + 5', answer = '105', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '58 + 8', line_positions = '58, 60, 66', jump_values = '2, 6', stage1_question = '58 + 2 + 6', answer = '66', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '68 + 9', line_positions = '68, 70, 77', jump_values = '2, 7', stage1_question = '68 + 2 + 7', answer = '77', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '89 + 5', line_positions = '89, 90, 94', jump_values = '1, 4', stage1_question = '89 + 1 + 4', answer = '94', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '99 + 6', line_positions = '99, 100, 105', jump_values = '1, 5', stage1_question = '99 + 1 + 5', answer = '105', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '79 + 7', line_positions = '79, 80, 86', jump_values = '1, 6', stage1_question = '79 + 1 + 6', answer = '86', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '69 + 8', line_positions = '69, 70, 77', jump_values = '1, 7', stage1_question = '69 + 1 + 7', answer = '77', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '59 + 9', line_positions = '59, 60, 68', jump_values = '1, 8', stage1_question = '59 + 1 + 8', answer = '68', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
    
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.ADDITION).first() 
    strategy_fun_single_single = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_SINGLE).first()
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    stage = 4
    topic_progress = 11
    name = "Add two numbers, up to 208"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '146 + 5', line_positions = '146, 150, 151', jump_values = '4, 1', stage1_question = '146 + 4 + 1', answer = '151', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '136 + 6', line_positions = '136, 140, 142', jump_values = '4, 2', stage1_question = '136 + 4 + 2', answer = '142', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '186 + 7', line_positions = '186, 190, 193', jump_values = '4, 3', stage1_question = '186 + 4 + 3', answer = '193', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '176 + 8', line_positions = '176, 180, 184', jump_values = '2, 4', stage1_question = '176 + 2 + 4', answer = '184', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '156 + 9', line_positions = '156, 160, 165', jump_values = '1, 5', stage1_question = '156 + 1 + 5', answer = '165', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '157 + 5', line_positions = '157, 160, 162', jump_values = '3, 2', stage1_question = '157 + 3 + 2', answer = '162', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '177 + 6', line_positions = '177, 180, 183', jump_values = '3, 3', stage1_question = '177 + 3 + 3', answer = '183', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '167 + 7', line_positions = '167, 170, 174', jump_values = '3, 4', stage1_question = '167 + 3 + 4', answer = '174', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '137 + 8', line_positions = '137, 140, 145', jump_values = '2, 5', stage1_question = '137 + 2 + 5', answer = '145', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '197 + 9', line_positions = '197, 200, 206', jump_values = '1, 6', stage1_question = '197 + 1 + 6', answer = '206', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '158 + 5', line_positions = '158, 160, 163', jump_values = '2, 3', stage1_question = '158 + 2 + 5', answer = '163', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '168 + 6', line_positions = '168, 170, 174', jump_values = '2, 4', stage1_question = '168 + 2 + 4', answer = '174', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '188 + 7', line_positions = '188, 190, 195', jump_values = '2, 5', stage1_question = '188 + 2 + 5', answer = '195', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '148 + 8', line_positions = '148, 150, 156', jump_values = '2, 6', stage1_question = '148 + 2 + 6', answer = '156', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '128 + 9', line_positions = '128, 130, 137', jump_values = '1, 7', stage1_question = '128 + 1 + 7', answer = '137', flip = False)
    funChunks16 = FunChunks(activity_id = activity.id, question = '119 + 5', line_positions = '119, 120, 124', jump_values = '1, 4', stage1_question = '119 + 1 + 4', answer = '124', flip = False)
    funChunks17 = FunChunks(activity_id = activity.id, question = '129 + 6', line_positions = '129, 130, 135', jump_values = '1, 5', stage1_question = '129 + 1 + 5', answer = '135', flip = False)
    funChunks18 = FunChunks(activity_id = activity.id, question = '169 + 7', line_positions = '169, 170, 176', jump_values = '1, 6', stage1_question = '169 + 1 + 6', answer = '176', flip = False)
    funChunks19 = FunChunks(activity_id = activity.id, question = '139 + 8', line_positions = '139, 140, 147', jump_values = '1, 7', stage1_question = '139 + 1 + 7', answer = '147', flip = False)
    funChunks20 = FunChunks(activity_id = activity.id, question = '149 + 9', line_positions = '149, 150, 158', jump_values = '1, 8', stage1_question = '149 + 1 + 8', answer = '158', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.add(funChunks16)
    db.session.add(funChunks17)
    db.session.add(funChunks18)
    db.session.add(funChunks19)
    db.session.add(funChunks20)
    db.session.commit()
'''
    
'''
def persist_fun_chunk_subtraction_activities(db):
    logger.debug(">>persist_fun_chunk_subtraction_activities()")
    topic = db.session.query(Topic).filter(Topic.name == TopicConstants.ADDITION_AND_SUBTRACTION.getName()).first() 
    category = db.session.query(Category).filter(Category.name == CategoryConstants.SUBTRACTION).first() 
    strategy_fun_single_double = db.session.query(Strategy).filter(Strategy.name == StrategyNames.FUN_CHUNKS).filter(Strategy.qualifier == StrategyNameQualifiers.SINGLE_AND_DOUBLE).first()
    level = 2
    #stage is dependent on operation 
    stage = 1
    topic_progress = 3
    name = "Subtract two numbers, maximum of 15"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '11 - 2', line_positions = '11, 10, 9', jump_values = '-1, -1', stage1_question = '11 - 1 - 1', answer = '9', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '11 - 3', line_positions = '11, 10, 8', jump_values = '-1, -2', stage1_question = '11 - 1 - 2', answer = '8', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '11 - 4', line_positions = '11, 10, 7', jump_values = '-1, -3', stage1_question = '11 - 1 - 3', answer = '7', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '11 - 5', line_positions = '11, 10, 6', jump_values = '-1, -4', stage1_question = '11 - 1 -4', answer = '6', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '11 - 6', line_positions = '11, 10, 5', jump_values = '-1, -5', stage1_question = '11 - 1 -5', answer = '5', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '12 - 3', line_positions = '12, 10, 9', jump_values = '-2, -1', stage1_question = '12 - 2 -1', answer = '9', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '12 - 4', line_positions = '12, 10, 8', jump_values = '-2, -2', stage1_question = '12 - 2 -2', answer = '8', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '12 - 5', line_positions = '12, 10, 7', jump_values = '-2, -3', stage1_question = '12 - 2 -3', answer = '7', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '12 - 6', line_positions = '12, 10, 6', jump_values = '-2, -4', stage1_question = '12 - 2 -4', answer = '6', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '13 - 4', line_positions = '13, 10, 9', jump_values = '-3, -1', stage1_question = '13 - 3 -1', answer = '9', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '13 - 5', line_positions = '13, 10, 8', jump_values = '-3, -2', stage1_question = '13 - 3 -2', answer = '8', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '13 - 6', line_positions = '13, 10, 7', jump_values = '-3, -3', stage1_question = '13 - 3 -3', answer = '7', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '14 - 5', line_positions = '14, 10, 9', jump_values = '-4, -1', stage1_question = '14 - 4 -1', answer = '9', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '14 - 6', line_positions = '14, 10, 8', jump_values = '-4, -2', stage1_question = '14 - 4 -2', answer = '8', flip = False)
    funChunks15 = FunChunks(activity_id = activity.id, question = '15 - 6', line_positions = '15, 10, 9', jump_values = '-5, -1', stage1_question = '15 - 5 -1', answer = '9', flip = False) 
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.commit()

    stage = 2
    topic_progress = 6
    name = "Subtract two numbers, maximum of 55"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '41 - 2', line_positions = '41, 40, 39', jump_values = '-1, -1', stage1_question = '41 - 1 - 1', answer = '39', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '31 - 3', line_positions = '31, 30, 28', jump_values = '-1, -2', stage1_question = '31 - 1 - 2', answer = '28', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '31 - 4', line_positions = '31, 30, 27', jump_values = '-1, -3', stage1_question = '31 - 1 - 3', answer = '27', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '51 - 5', line_positions = '51, 50, 46', jump_values = '-1, -4', stage1_question = '51 - 1 -4', answer = '46', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '21 - 6', line_positions = '21, 20, 15', jump_values = '-1, -5', stage1_question = '21 - 1 -5', answer = '15', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '52 - 3', line_positions = '52, 50, 49', jump_values = '-2, -1', stage1_question = '52 - 2 -1', answer = '49', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '22 - 4', line_positions = '22, 20, 18', jump_values = '-2, -2', stage1_question = '22 - 2 -2', answer = '18', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '32 - 5', line_positions = '32, 30, 27', jump_values = '-2, -3', stage1_question = '32 - 2 -3', answer = '27', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '42 - 6', line_positions = '42, 40, 36', jump_values = '-2, -4', stage1_question = '42 - 2 -4', answer = '36', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '23 - 4', line_positions = '23, 20, 19', jump_values = '-3, -1', stage1_question = '23 - 3 -1', answer = '19', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '53 - 5', line_positions = '53, 50, 48', jump_values = '-3, -2', stage1_question = '53 - 3 -2', answer = '48', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '33 - 6', line_positions = '33, 30, 27', jump_values = '-3, -3', stage1_question = '33 - 3 -3', answer = '27', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '24 - 5', line_positions = '24, 20, 19', jump_values = '-4, -1', stage1_question = '24 - 4 -1', answer = '19', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '44 - 6', line_positions = '44, 40, 38', jump_values = '-4, -2', stage1_question = '44 - 4 -2', answer = '38', flip = False)    
    funChunks15 = FunChunks(activity_id = activity.id, question = '55 - 6', line_positions = '55, 50, 49', jump_values = '-5, -1', stage1_question = '55 - 5 -1', answer = '49', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)

    stage = 3
    topic_progress = 9
    name = "Subtract two numbers, maximum of 95"
    url_name = createURL(level, topic_progress, name)
    activity = Activity(topic_id = topic.id, topic_progress = topic_progress, category_id = category.id, \
                        strategy_id = strategy_fun_single_double.id, level = level, \
                        name = name, description = "", stage = stage, url_name = url_name, time_limit = 600, total_questions = 10, \
                        num_variables = 2, answer_format = AnswerFormat.POSITIVE_INT)
    db.session.add(activity)
    db.session.flush()
    funChunks1 = FunChunks(activity_id = activity.id, question = '61 - 2', line_positions = '61, 60, 59', jump_values = '-1, -1', stage1_question = '61 - 1 - 1', answer = '59', flip = False)
    funChunks2 = FunChunks(activity_id = activity.id, question = '71 - 3', line_positions = '71, 70, 68', jump_values = '-1, -2', stage1_question = '71 - 1 - 2', answer = '68', flip = False)
    funChunks3 = FunChunks(activity_id = activity.id, question = '81 - 4', line_positions = '81, 80, 77', jump_values = '-1, -3', stage1_question = '81 - 1 - 3', answer = '77', flip = False)
    funChunks4 = FunChunks(activity_id = activity.id, question = '91 - 5', line_positions = '91, 90, 86', jump_values = '-1, -4', stage1_question = '91 - 1 -4', answer = '86', flip = False)
    funChunks5 = FunChunks(activity_id = activity.id, question = '61 - 6', line_positions = '61, 60, 55', jump_values = '-1, -5', stage1_question = '61 - 1 -5', answer = '55', flip = False)
    funChunks6 = FunChunks(activity_id = activity.id, question = '92 - 3', line_positions = '92, 90, 89', jump_values = '-2, -1', stage1_question = '92 - 2 -1', answer = '89', flip = False)
    funChunks7 = FunChunks(activity_id = activity.id, question = '82 - 4', line_positions = '82, 80, 78', jump_values = '-2, -2', stage1_question = '82 - 2 -2', answer = '78', flip = False)
    funChunks8 = FunChunks(activity_id = activity.id, question = '72 - 5', line_positions = '72, 70, 67', jump_values = '-2, -3', stage1_question = '72 - 2 -3', answer = '67', flip = False)
    funChunks9 = FunChunks(activity_id = activity.id, question = '62 - 6', line_positions = '62, 60, 56', jump_values = '-2, -4', stage1_question = '62 - 2 -4', answer = '56', flip = False)
    funChunks10 = FunChunks(activity_id = activity.id, question = '63 - 4', line_positions = '63, 60, 59', jump_values = '-3, -1', stage1_question = '63 - 3 -1', answer = '59', flip = False)
    funChunks11 = FunChunks(activity_id = activity.id, question = '73 - 5', line_positions = '73, 70, 68', jump_values = '-3, -2', stage1_question = '73 - 3 -2', answer = '68', flip = False)
    funChunks12 = FunChunks(activity_id = activity.id, question = '83 - 6', line_positions = '83, 80, 77', jump_values = '-3, -3', stage1_question = '83 - 3 -3', answer = '77', flip = False)
    funChunks13 = FunChunks(activity_id = activity.id, question = '74 - 5', line_positions = '74, 70, 69', jump_values = '-4, -1', stage1_question = '74 - 4 -1', answer = '69', flip = False)
    funChunks14 = FunChunks(activity_id = activity.id, question = '94 - 6', line_positions = '94, 90, 88', jump_values = '-4, -2', stage1_question = '94 - 4 -2', answer = '88', flip = False)    
    funChunks15 = FunChunks(activity_id = activity.id, question = '85 - 6', line_positions = '85, 80, 79', jump_values = '-5, -1', stage1_question = '85 - 5 -1', answer = '79', flip = False)
    db.session.add(funChunks1)
    db.session.add(funChunks2)
    db.session.add(funChunks3)
    db.session.add(funChunks4)
    db.session.add(funChunks5)
    db.session.add(funChunks6)
    db.session.add(funChunks7)
    db.session.add(funChunks8)
    db.session.add(funChunks9)
    db.session.add(funChunks10)
    db.session.add(funChunks11)
    db.session.add(funChunks12)
    db.session.add(funChunks13)
    db.session.add(funChunks14)
    db.session.add(funChunks15)
    db.session.commit()
'''

'''
#deprecated
def setup_test_users(db):
    student_role = db.session.query(Role).filter(Role.role_name == RoleTypes.STUDENT).first()
    #add steve mcquillan student
    student1_user_name = os.environ.get('MARS_DB_STUDENT1_USER_NAME')
    student1_user_password = os.environ.get('MARS_DB_STUDENT1_PASSWORD')
    student1_first_name = os.environ.get('MARS_DB_STUDENT1_FIRST_NAME')
    student1_last_name = os.environ.get('MARS_DB_STUDENT1_LAST_NAME')
    student1_school = os.environ.get('MARS_DB_STUDENT1_SCHOOL')
    student1_user = User(role_id = student_role.id, first_name=student1_first_name, \
                        last_name=student1_last_name, user_name = student1_user_name, 
                        password=student1_user_password)
    db.session.add(student1_user)
    db.session.flush()
    
    student1 = Student(user_id = student1_user.id, age = 10,
                grade = 5, school = student1_school,
                level = 2,
                country = 'Australia',
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student1)
    db.session.flush()
    db.session.commit()
    
    
    #add ole sundsby student
    student2_user_name = os.environ.get('MARS_DB_STUDENT2_USER_NAME')
    student2_user_password = os.environ.get('MARS_DB_STUDENT2_PASSWORD')
    student2_user_email = os.environ.get('MARS_DB_STUDENT2_EMAIL')
    student2_user = User(role_id = student_role.id, email = student2_user_email, user_name = student2_user_name, 
                        password=student2_user_password)
    db.session.add(student2_user)
    db.session.flush()
    student2 = Student(user_id = student2_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student2)
    db.session.flush()
    db.session.commit()
    
    #add ole sundsby student
    student3_user_name = os.environ.get('MARS_DB_STUDENT3_USER_NAME')
    student3_user_password = os.environ.get('MARS_DB_STUDENT3_PASSWORD')
    student3_user_email = os.environ.get('MARS_DB_STUDENT3_EMAIL')
    student3_user = User(role_id = student_role.id, email = student3_user_email, user_name = student3_user_name, 
                        password=student3_user_password)
    db.session.add(student3_user)
    db.session.flush()
    student3 = Student(user_id = student3_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student3)
    db.session.flush()
    db.session.commit()
    
    #add nick pink student
    student4_user_name = os.environ.get('MARS_DB_STUDENT4_USER_NAME')
    student4_user_password = os.environ.get('MARS_DB_STUDENT4_PASSWORD')
    student4_user_email = os.environ.get('MARS_DB_STUDENT4_EMAIL')
    student4_user = User(role_id = student_role.id, email = student4_user_email, user_name = student4_user_name, 
                        password=student4_user_password)
    db.session.add(student4_user)
    db.session.flush()
    student4 = Student(user_id = student4_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student4)
    db.session.flush()
    db.session.commit()
    
    #add dave wheller student
    student5_user_name = os.environ.get('MARS_DB_STUDENT5_USER_NAME')
    student5_user_password = os.environ.get('MARS_DB_STUDENT5_PASSWORD')
    student5_user_email = os.environ.get('MARS_DB_STUDENT5_EMAIL')
    student5_user = User(role_id = student_role.id, email = student5_user_email, user_name = student5_user_name, 
                        password=student5_user_password)
    db.session.add(student5_user)
    db.session.flush()
    student5 = Student(user_id = student5_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student5)
    db.session.flush()
    db.session.commit()
    
    #add steves mate sjharvey student
    student6_user_name = os.environ.get('MARS_DB_STUDENT6_USER_NAME')
    student6_user_password = os.environ.get('MARS_DB_STUDENT6_PASSWORD')
    student6_user_email = os.environ.get('MARS_DB_STUDENT6_EMAIL')
    student6_user = User(role_id = student_role.id, email = student6_user_email, user_name = student6_user_name, 
                        password=student6_user_password)
    db.session.add(student6_user)
    db.session.flush()
    student6 = Student(user_id = student6_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student6)
    db.session.flush()
    db.session.commit()
    
    #add Louse Eckstein student
    student7_user_name = os.environ.get('MARS_DB_STUDENT7_USER_NAME')
    student7_user_password = os.environ.get('MARS_DB_STUDENT7_PASSWORD')
    student7_user_email = os.environ.get('MARS_DB_STUDENT7_EMAIL')
    student7_user = User(role_id = student_role.id, email = student7_user_email, user_name = student7_user_name, 
                        password=student7_user_password)
    db.session.add(student7_user)
    db.session.flush()
    student7 = Student(user_id = student7_user.id, 
                level = 2,
                goal_session_time = 10,
                goal_session_frequency = 5)
    db.session.add(student7)
    db.session.flush()
    db.session.commit()
'''
    