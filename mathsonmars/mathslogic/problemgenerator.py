import operator
import random
from mathsonmars.marslogger import logger
from mathsonmars.constants.modelconstants import CategoryConstants, StrategyNames,\
    ConstraintConstants, BoxConstants, BoxMethodTypeConstants,\
    ActivityTypeConstants, BoxModelFormat
#from mathsonmars.models import Strategy, BoxMethod
import math
from mathsonmars.mathslogic.messenger import Messenger


OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
]

#see https://codereview.stackexchange.com/questions/77299/math-equation-generator-program
class ProblemGenerator():
    
    @classmethod
    def get_questions_for_activity(cls, activity, activity_action, strategy, category):
        '''
        @param activity: db object
        @return result: single csv string of values answers
        '''
        assert activity is not None
        assert activity_action is not None
        assert strategy is not None
        assert category is not None
        m = ""
        if strategy.name == StrategyNames.PATTERNS:
            m = ProblemGenerator.get_questions_for_patterns_activity(activity, activity_action, strategy, category)
        elif strategy.name == StrategyNames.COUNT or strategy.name == StrategyNames.COUNT_ON or strategy.name == StrategyNames.COUNT_BACK:
            m = ProblemGenerator.get_questions_for_count_activity(activity, activity_action, strategy, category)
        elif strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION:
            m = ProblemGenerator.get_questions_for_friendly_and_fix_activity(activity, activity_action, strategy, category)  
        elif strategy.name == StrategyNames.MEMORIZE:
            m = ProblemGenerator.get_questions_for_memorize_activity(activity, activity_action, strategy, category)
        elif strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_DIGIT or strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_SINGLE \
        or strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_DOUBLE or strategy.name == StrategyNames.FUN_CHUNKS_DOUBLE_AND_DOUBLE:
            m = ProblemGenerator.get_questions_for_fun_chunks_activity(activity, activity_action, strategy, category)
        elif strategy.name == StrategyNames.ADDITION_BOX_BASIC or strategy.name == StrategyNames.SUBTRACTION_BOX_BASIC \
        or strategy.name == StrategyNames.MULTIPLICATION_BOX_BASIC or strategy.name == StrategyNames.DIVISION_BOX_BASIC:
            m = ProblemGenerator.get_questions_for_box_activity(activity, activity_action, strategy, category)
        return m

    @classmethod
    def get_questions_for_patterns_activity(cls, activity, activity_action, strategy, category):  
        m = ""
        if strategy.name == StrategyNames.PATTERNS:
            logger.debug("TODO")
        return m
    
    @classmethod
    def get_questions_for_count_activity(cls, activity, activity_action, strategy, category):                    
        m = ""
        if strategy.name == StrategyNames.COUNT:
            logger.debug("TODO")
        elif strategy.name == StrategyNames.COUNT_ON:
            logger.debug("TODO")
        elif strategy.name == StrategyNames.COUNT_BACK:
            logger.debug("TODO")
        return m
    
    @classmethod
    def get_questions_for_friendly_and_fix_activity(cls, activity, activity_action, strategy, category):
        m = ""
        if strategy.name == StrategyNames.FRIENDLY_AND_FIX_ADDITION:
            logger.debug("TODO")
        return m 
    
    @classmethod
    def get_questions_for_memorize_activity(cls, activity, activity_action, strategy, category):
        num_questions = activity.total_questions
        m= ""
        if strategy.name == StrategyNames.MEMORIZE:
            if category.name == CategoryConstants.ADDITION:
                if activity_action.num_variables == 2:
                    operand_range = [int(activity_action.value_mins[0]), int(activity_action.value_maxs[0])] 
                    question_list, answer_list = ProblemGenerator.get_n_two_val_questions(operand_range, num_questions, operator.add)
                    logger.debug("--get_questions_for_activity() MADS qq:{0} ans:{1} ".format(question_list, answer_list))
                    question_result = ','.join(map(str, question_list))
                    answer_result = ','.join(map(str, answer_list))
                    m = Messenger(messenger_type = Messenger.QQ_ANS, question_result=question_result, answer_result=answer_result)
        return m   
    
    @classmethod
    def get_questions_for_fun_chunks_activity(cls, activity, activity_action, strategy, category):
        '''
        @param activity: db object
        @return result: single csv string of values answers
        '''
        logger.debug(">>get_questions_for_activity strategy_name:{0}, activity_action:{1}".format(strategy.name, activity_action))
        assert activity is not None
        assert strategy is not None
        assert activity_action is not None
        assert category is not None
        assert activity.activity_action_type == ActivityTypeConstants.FUN_CHUNKS_OR_FRIENDLY_ACTIVITY
        question_list = []
        question_result = ""
        answer_result = ""
        result = ""
        difference_result = ""
        remaining_result = ""
        m = ""
        num_questions = activity.total_questions
        if strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_DIGIT:
            if category.name == CategoryConstants.ADDITION:
                logger.debug("TODO")
            elif category.name == CategoryConstants.SUBTRACTION:
                logger.debug("TODO")
            
        elif strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_SINGLE:
            if category.name == CategoryConstants.ADDITION:
                if activity_action.num_variables == 2:
                    operand_range =  [int(activity_action.value_mins[0]), int(activity_action.value_maxs[0])] 
                    chunking_position = int(activity_action.value_position_to_split_or_fix)
                    question_list, difference_list, remaining_list, answer_list  = ProblemGenerator.get_n_two_val_chunking_single_single_questions(operand_range, num_questions, chunking_position, operator.add)
                    difference_result = ','.join(map(str, difference_list))
                    remaining_result = ','.join(map(str, remaining_list))
                    question_result = ','.join(map(str, question_list))
                    answer_result = ','.join(map(str, answer_list))
                    m = Messenger(messenger_type=Messenger.QQ_DIFF_REMAIN_ANS_CHUNKPOS, question_result=question_result, difference_result=difference_result, remaining_result=remaining_result, answer_result=answer_result, chunking_position=chunking_position)
            elif category.name == CategoryConstants.SUBTRACTION:
                logger.debug("TODO")
            
        elif strategy.name == StrategyNames.FUN_CHUNKS_SINGLE_AND_DOUBLE:
            if category.name == CategoryConstants.ADDITION:
                logger.debug("TODO")
            elif category.name == CategoryConstants.SUBTRACTION:
                logger.debug("TODO")
        
        elif strategy.name == StrategyNames.FUN_CHUNKS_DOUBLE_AND_DOUBLE:
            if category.name == CategoryConstants.ADDITION:
                logger.debug("TODO")
            elif category.name == CategoryConstants.SUBTRACTION:
                logger.debug("TODO")
        return m
       
    @classmethod
    def get_questions_for_box_activity(cls, activity, activity_action, strategy, category):
        '''
        @param activity: db object
        @return result: single csv string of values answers
        '''
        logger.debug(">>get_questions_for_box_activity strategy_name:{0}, activity_action:{1}".format(strategy.name, activity_action))
        assert activity is not None
        assert strategy is not None
        assert activity_action is not None
        assert category is not None
        question_list = []
        question_result = ""
        answer_result = ""
        result = ""
        difference_result = ""
        remaining_result = ""
        m = ""
        #TODO we only use for box problems 
        variables_result = ""
        num_questions = activity.total_questions
        if strategy.name == StrategyNames.ADDITION_BOX_BASIC or strategy.name == StrategyNames.SUBTRACTION_BOX_BASIC \
        or strategy.name == StrategyNames.MULTIPLICATION_BOX_BASIC or strategy.name == StrategyNames.DIVISION_BOX_BASIC:
            question_list, answer_list, variable_values = ProblemGenerator.generate_box_questions(activity, strategy, activity_action, category)
            if question_list != None and question_list != "" and answer_list != None and answer_list != "":
                logger.debug("--get_questions_for_box_activity() BOX qq:{0} ans:{1} vars:{1}".format(question_list, answer_list, variable_values))
                question_result = ','.join(map(str, question_list))
                answer_result = ','.join(map(str, answer_list))
                variables_result = ','.join(map(str, variable_values))
                m = Messenger(messenger_type=Messenger.QQ_ANS_VARS, question_result=question_result, answer_result=answer_result, variables_result=variables_result)
        return m    
    
    
    @classmethod
    def random_question(cls, binary_operations, operand_range):
        """Generate a pair consisting of a random question (as a string)
        and its answer (as a number)"""
        op_sym, op_func = random.choice(binary_operations)
        n1 = random.randint(min(operand_range), max(operand_range))
        n2 = random.randint(min(operand_range), max(operand_range))
        question = '{} {} {}'.format(n1, op_sym, n2)
        answer = op_func(n1, n2)
        return question, answer
    
    @classmethod
    def two_vals_chunk_question(cls, operand_range, chunking_position, param_op):
        """eg 9 + 5 = 9 + 1 + 4 = 14"""
        assert isinstance(operand_range, list)
        n1 = random.randint(min(operand_range), max(operand_range))
        n2 = random.randint(min(operand_range), max(operand_range))
        #swap them so biggest is always on left - for graphics layout
        if chunking_position == 1:
            if n2 > n1:
                temp = n2
                n2 = n1
                n1 = temp
        else:
            if n1 > n2:
                temp = n1
                n1 = n2
                n2 = temp
        #round first value to nearest ten
        rounded = ProblemGenerator.roundUpByTens(n1)
        difference = rounded - n1
        remaining = n2 - difference
        if difference < 0:
            logger.error("Error: difference < 0")
        elif remaining < 0:
            logger.error("Error: remaining < 0")
        answer = param_op(n1, n2)
        return n1, n2, difference, remaining, answer
    
    @classmethod
    def roundUpByTens(cls, x):
        return int(math.ceil(x/10.0)*10)
        
    @classmethod
    def two_vals_question(cls, operand_range, param_op):
        """values for addition and its answer (as a number)"""
        assert isinstance(operand_range, list)
        n1 = random.randint(min(operand_range), max(operand_range))
        n2 = random.randint(min(operand_range), max(operand_range))
        answer = param_op(n1, n2)       
        return n1, n2, answer
    
    @classmethod
    def get_n_two_val_questions(cls, operand_range, num_questions, operation):
        '''
        NB operand range is not flexible, revise to value_mins, value_maxs 
        @param operand_range: [i, j]
        @param num_questions: int
        @param operation: eg operator.add
        @return question_list: int list
        '''
        question_list = []
        answer_list = []
        for n in range(num_questions):
            n1, n2, answer = ProblemGenerator.two_vals_question(operand_range, operation)
            question_list.extend([n1, n2])
            answer_list.extend([answer])
        return question_list, answer_list
    
    @classmethod
    def get_n_two_val_questions_with_constraint(cls, operand_range, num_questions, operation, constraint, position_of_constraint):
        '''
        NB operand range is not flexible, revise to value_mins, value_maxs 
        @param operand_range: [i, j]
        @param num_questions: int
        @param operation: eg operator.add
        @return question_list: int list
        '''
        question_list = []
        for n in range(num_questions):
            n1, n2, answer = ProblemGenerator.two_vals_question(operand_range, operation)
            if constraint == ConstraintConstants.NON_NEGATIVE:
                answer = ProblemGenerator.apply_non_negative_constraint(operation, n1, n2, operand_range)
            else:
                logger.debug("TODO")
            question_list.extend([n1, n2, answer])
        return question_list   
    
    @classmethod
    def apply_non_negative_constraint(cls, operation, n1, n2, operand_range):
        if operation == operator.sub:
            neg_value = n1 - n2
            pos_value = n1 + (-1)*neg_value
            n1 += pos_value
            #add a randon number
            n3 = random.randint(0, (max(operand_range)-n1))
            n1 += n3
            answer = operation(n1, n2)
        return answer
    
    @classmethod
    def get_n_two_val_chunking_single_single_questions(cls, operand_range, num_questions, chunking_position, operation):
        '''
        NB operand range is not flexible, revise to value_mins, value_maxs 
        @param operand_range: [i, j]
        @param num_questions: int
        @param operation: eg operator.add
        @return question_list: int list
        '''
        question_list = []
        answer_list = []
        difference_list = []
        remaining_list = []
        for n in range(num_questions):
            n1, n2, difference, remaining, answer = ProblemGenerator.two_vals_chunk_question(operand_range, chunking_position, operation)
            question_list.extend([n1, n2])
            difference_list.extend([difference])
            remaining_list.extend([remaining])
            answer_list.extend([answer])
        return question_list, difference_list, remaining_list, answer_list 
    


    
    @classmethod     
    def generate_box_questions(cls, activity, strategy, box_method, category):
        question_list = []
        answer_list = []
        variable_values = []
        if box_method.num_variables == 2:
            if strategy.name == StrategyNames.ADDITION_BOX_BASIC or strategy.name == StrategyNames.SUBTRACTION_BOX_BASIC \
            or strategy.name == StrategyNames.MULTIPLICATION_BOX_BASIC or strategy.name == StrategyNames.DIVISION_BOX_BASIC:
                if category.name == CategoryConstants.ADDITION:
                    
                    if activity.level == 1:
                        #csv of min value for each number
                        value_mins = [1, 1]
                        value_maxs = [10, 10]
                    elif activity.level == 2:
                        #csv of min value for each number
                        value_mins = [2, 2]
                        value_maxs = [20, 20]
                    for _ in range(activity.total_questions):
                        value1 = random.randint(value_mins[0], value_maxs[0])
                        value2 = random.randint(value_mins[1], value_maxs[1])
                        answer = value1 + value2
                        variable_values.append(value1)
                        variable_values.append(value2)
                        model_format = random.choice([BoxModelFormat.OWNER_TEXT_VARIABLE_OBJECT_TWICE_QUESTION, BoxModelFormat.VARIABLE_OBJECT_TWICE_TEXT_QUESTION])
                        #tuple
                        action_item = random.choice(list(BoxConstants.ACTION_ITMES.keys()))
                        #list
                        action_things = BoxConstants.ACTION_ITMES[action_item]
                        thing = random.choice(action_things)
                        if model_format == BoxModelFormat.OWNER_TEXT_VARIABLE_OBJECT_TWICE_QUESTION:
                            gender = random.choice( [BoxConstants.BOY_NAMES, BoxConstants.GIRL_NAMES] )
                            name = random.choice(gender)
                            owner1 = name
                            gender = random.choice( [BoxConstants.BOY_NAMES, BoxConstants.GIRL_NAMES] )
                            name = random.choice(gender)
                            owner2 = name
                            logger.debug("--generate_box_questions() OWNER_TEXT_VARIABLE_OBJECT_TWICE_QUESTION")
                            question = owner1+" "+action_item[0]+" "+str(value1)+" "+thing+". "+owner2+" "+action_item[0]+" "+str(value2)+" "+thing+". "+\
                            "How many "+thing+" did they "+action_item[1]+" in total?"
                        elif model_format == BoxModelFormat.VARIABLE_OBJECT_TWICE_TEXT_QUESTION:
                            logger.debug("--generate_box_questions() VARIABLE_OBJECT_TWICE_TEXT_QUESTION")
                            object_tuple = random.choice(BoxConstants.BASIC_VARIABLE_OBJECT_TWICE_TEXT_QUESTION_OBJECTS)
                            text = random.choice(BoxConstants.BASIC_VARIABLE_OBJECT_TWICE_TEXT_QUESTION_TEXT)
                            question = str(value1)+" "+object_tuple[0]+" and "+str(value2)+" "+object_tuple[1]+" "+text+". How many in total "+text+"?"
                        logger.debug("--generate_box_questions() action_item:{0} action_things:{1} thing:{2} question:{3}".format(action_item, action_things, thing, question))
                        question_list.append(question)
                        answer_list.append(answer)
                    logger.debug("--generate_box_questions() question_list:{0}".format(question_list))
        return question_list, answer_list, variable_values
    
    '''          
    def legacy(self):
        names = []
                variable_values = []
                constant_values = []
                activity_results = []
                for _ in range(activity.total_questions):
                    gender = random.choice( [BoxConstants.BOY_NAMES, BoxConstants.GIRL_NAMES] )
                    name = random.choice(gender)
                    if activity.level == 1:
                        value = random.randint(0, 10)
                        variable_values.append(value)
                        constant = random.randint(0, 10)
                        constant_values.append(constant)
                        total = value + constant
                        activity_results.append(total)
                    action = random.choice(BoxConstants.ACTION_ITMES)
                    item = random.choice(action)
                    item_colour_1 = random.choice(BoxConstants.ITEM_COLOURS)
                    item_colour_2 = random.choice(BoxConstants.ITEM_COLOURS)
                    if (item_colour_2 == item_colour_1):
                        if BoxConstants.ITEM_COLOURS.index(item_colour_2)==len(BoxConstants.ITEM_COLOURS)-1:
                            item_colour_2 == BoxConstants.ITEM_COLOURS.index(item_colour_2)-1
                        else:
                            if len(BoxConstants.ITEM_COLOURS)>=BoxConstants.ITEM_COLOURS.index(item_colour_2)+1:
                                item_colour_2 == BoxConstants.ITEM_COLOURS.index(item_colour_2)+1
                            else:
                                item_colour_2 == BoxConstants.ITEM_COLOURS.index(0)
                                logger.error("Error in BoxConstants index value")
                    qq = name +" "+activity+total+item+". " + constant + " " + item + " were "+item_colour_1 + \
                    " and the other "+ item + " were " + item_colour_2+ ". How many " + item_colour_2 + " " + item + " did " + name + action
    '''        

    def quiz(self, number_of_questions):
        """Ask the specified number of questions, and return the number of correct
        answers."""
        score = 0
        for _ in range(number_of_questions):
            question, answer = self.random_question(OPERATIONS, range(0, 21))
            print('What is {}'.format(question))
            try:
                user_input = float(input("Enter the answer: "))
            except ValueError:
                print("I'm sorry that's invalid")
            else:
                if answer == user_input:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Incorrect!\n")
        return score
    
    def identify_user(self):
        # TODO, as an exercise for you
        return 'Dan', 'Brown', 1
        
    
    def display_score(self, first_name, last_name, class_name):
        # TODO, as an exercise for you
        print(first_name, last_name, class_name)
    
    def menu(self):
        # TODO, as an exercise for you
        return 2
    
    def main(self):
        first_name, last_name, class_name = self.identify_user()
        while True:
            menu_choice = self.menu()
            if menu_choice == 1:        # Display score
                self.display_score(first_name, last_name, class_name)
    
            elif menu_choice == 2:      # Run quiz
                QUESTIONS = 10
                score = self.quiz(QUESTIONS)
                print('{first_name} {last_name}, you scored {score} out of {QUESTIONS}'.format(**locals()))
    
            elif menu_choice == 3:      # Exit
                break
    
            else:
    
                print("Sorry, I don't understand. Please try again...")
                print()

if __name__ == '__main__':
    aSMDQuiz = ProblemGenerator()
    aSMDQuiz.main()