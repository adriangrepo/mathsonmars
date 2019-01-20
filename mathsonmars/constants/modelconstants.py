from mathsonmars.utils.fileutils import FileUtils
from mathsonmars.utils.listutils import ListUtils


class ActivityTypeConstants():
    MADS = "mads"
    FUN_CHUNKS_OR_FRIENDLY_ACTIVITY = "fun_chunks_or_friendly_activity"
    BOX_METHOD = "box_method"

class BoxMethodTypeConstants():
    SUM_OF_A_B_EQ_TOTAL = "Sum of two variables equals total"
    SUM_OF_A_B_C_EQ_TOTAL = "Sum of three variables equals total"
    
class BoxMethodVariableContraintConstants():
    A_EQ_B_PLS_C = "A equals B plus C" 
    A_EQ_B_MIN_C = "A equals B minus C"  

class ConstraintConstants():
    #used where have values on own that could add to a number greater than want
    #eg if want to add to max total of 9 but want to use digits from 0 to 9
    ADD_TO_MAX_OF = "Add to maximum of"
    #eg disallow 1-3
    NON_NEGATIVE = "Non negative"
    #used where want to multiply to max eg up to 99 but want to use 1-12
    MULTIPLY_TO_MAX_OF = "Multiply to maximum of"
    ONES_COLUMN_GREATER_THAN_N = "Ones column greater than n"
    ONES_COLUMN_LESS_THAN_N = "Ones column less than n"
    #eg 13 - 5 ones column = -2
    ONES_COLUMN_VALUE1_MINUS_VALUE0_NEGATIVE = "Ones column value1 minus value0 negative"


class TopicConstants():
    name = str()
    uid = str()
    typesArrayList = []
    
    def __init__(self, name, uid):
        """ generated source for method __init__ """
        self.name = name
        self.uid = uid
        self.typesArrayList.append(self)

    def __str__(self):
        """ generated source for method toString """
        return self.name

    def getName(self):
        """ return ZAxis.name """
        return self.name

    def getUid(self):
        return self.uid
    
    @classmethod
    def getTopicConstantsFromName(cls, name):
        """ generated source for method getTopicConstantsFromName """
        j = 0
        while j < len(cls.typesArrayList):
            zaxis = cls.typesArrayList[j]
            if zaxis.getName() == name:
                return zaxis
            j += 1
        return cls.NONE
    
    @classmethod
    def getTopicConstantsFromUid(cls, uid):
        j = 0
        while j < len(cls.typesArrayList):
            zaxis = cls.typesArrayList[j]
            if zaxis.getUid() == uid:
                return zaxis
            j += 1
        return cls.NONE
    
TopicConstants.NUMBERS_AND_PATTERNS = TopicConstants("Numbers and Patterns", "NP")
TopicConstants.ADDITION_AND_SUBTRACTION = TopicConstants("Addition and Subtraction", "AS")
TopicConstants.MULTIPLICATION_AND_DIVISION = TopicConstants("Multiplication and Division", "MD")
TopicConstants.FRACIONS_AND_DECIMALS = TopicConstants("Fractions and Decimals", "FD")
TopicConstants.MEASUREMENT_AND_GEOMETRY = TopicConstants("Measurement and Geometry", "MG")
TopicConstants.POWERS_AND_ROOTS = TopicConstants("Powers and Roots", "PR")
TopicConstants.PERCENTAGES_AND_PROPORTIONS = TopicConstants("Percentages and Proportions", "PP")
TopicConstants.STATISTICS = TopicConstants("Statistics", "S")
    
class CategoryConstants():
    """A maths category eg Addition."""
    #levels 1 & 2 dot patterns
    PATTERNS = "Patterns"
    #levels 2, 3, 4 number pace value
    NUMBERS = "Numbers"
    #levels 1-5
    ADDITION = "Addition"
    #levels 1-5
    SUBTRACTION = "Subtraction"
    #levels 2-5
    MULTIPLICATION = "Multiplication"
    #levels 3-5
    DIVISION = "Division"
    #levels 3-5
    FRACTIONS = "Fractions"
    #levels 4-5
    DECIMALS = "Decimals"
    #???
    #COMPARISON = "comparison"
    #levels 5
    PERCENTAGE = "Percentage"
    #levels 5
    AVERAGE = "Average"
    #levels 5
    RATIO = "Ratio"
    #levels 5
    POWERS = "Powers"
    #levels 5
    ROOTS = "Roots"
    #???
    MEASUREMENT = "Measurement"
    #???
    GEOMETRY = "Geometry"

'''
class StrategyClasses():
    MEMORY = 'Memory'
    FUN_CHUNKS = 'Fun chunks'
    FRIENDLY_AND_FIX = 'Friendly and fix'
    BY_PLACE = 'By place'
    FRIENDLY_PAIRS = 'Friendly pairs'
    GROUPING = 'Grouping'
    COLUMNS = 'Columns'
    COLUMNS_WITH_REGROUPING = 'Columns with regrouping'
    #fractions
    MAKE_COMMON = 'Make common'
    DO_SAME = 'Do same'
    FLIP = 'Flip'
    BOX = 'Box'
'''
    
    
class StrategyNames():
    """Mental/Written strategy constants."""
    COUNT = 'Count'
    PATTERNS = 'Patterns'
    NUMBER_BONDS = 'Number bonds'
    #process names
    COUNT_ON = 'Count on'
    COUNT_BACK = 'Count back'
    CROSS_OUT = 'Cross out'
    MEMORIZE = 'Memory quest'
    #splitting, use when ending in 1, 2, 3
    FUN_CHUNKS = 'Fun chunks'
    #Delta up to nearest ten, delta down to nearest ten
    CHUNK_DIFFERENCES = 'Chunk differences'
    #round up and cut down- use when ending with 7, 8, 9
    FRIENDLY_AND_FIX = 'Friendly and fix'
    
    TEN_OR_HUNDRED = 'Ten or one hundred'
    #when 3 or more numbers, find pair that adds to 10
    FRIENDLY_PAIRS = 'Friendly pairs'
    BY_PLACE = 'By place'
    #multiplication basics eg 2+2+2+2
    REPEATED = 'Repeated'
    #eg for 14, divide into 7 groups of 2
    GROUPS = 'Groups'
    #make denomonators common (down below), numerator = no air up here
    FRACTIONS = 'Fractions'
    #multiply top, multiply bottom, simplify
    #turn second fraction upside down and multiply
    
    #Items without written examples:
    #written column addition/subtraction
    WITHOUT_REGROUPING = 'Without regrouping'
    WITH_REGROUPING = 'With regrouping'
    
    BOX_METHOD = 'Box method'
    
class StrategyNameQualifiers():
    SINGLE_DIGIT = 'single digit'
    COUNTERS = 'counters'
    WHOLE_PART = 'whole-part find part'
    PART_PART = 'part-part find whole'
    SINGLE_AND_SINGLE = 'single and single digits'
    SINGLE_AND_DOUBLE = 'single and double digits'
    DOUBLE_AND_DOUBLE = 'double and double digits'
    ADDITION = 'addition'
    SUBTRACTION = 'subtraction'
    #Block concepts
    BASIC_ADDITION = "Basic addition"
    BASIC_NAMED_ADDITION = "Basic named addition"
    BASIC_SUBTRACTION = "Basic subtraction"
    BASIC_NAMED_SUBTRACTION = "Basic named subtraction"
    BASIC_MULTIPLICATION = "Basic multiplication"
    BASIC_NAMED_MULTIPLICATION = "Basic named multiplication"
    BASIC_DIVISION= "Basic division"
    BASIC_NAMED_DIVISION = "Basic named division"
    PART_WHOLE = "Part-whole"
    COMPARISON = "Comparison"
    CHANGE = "Change"
    PART_WHOLE_COMPARISON = "Part-whole comparison"
    COMPARISON_CHANGE = "Comparison change"
    PART_WHOLE_COMPARISON_CHANGE = "Part-whole comparison change"
    #Block sub-concepts
    PLACE_HOLDER= "Place holder"
    REMAINDER = "Remainder"
    EQUAL = "Equal"
    CONSTANT_DIFFERENCE = "Constant difference"
    REPEATED_VARIABLE = "Repeated variable"
    CONSTANT_TOTAL = "Constant total"
    EXCESS_VALUE = "Excess Value"
    CONSTANT_QUANTITY = "Constant quantity"

    
def getTableNameForStrategy(strategy_name):
    return {
        StrategyNames.COUNT: 1,
        StrategyNames.PATTERNS: 2,
        StrategyNames.NUMBER_BONDS: 'numberbonds',
        StrategyNames.COUNT_ON: 1,
        StrategyNames.COUNT_BACK: 2,
        StrategyNames.CROSS_OUT: 1,
        StrategyNames.MEMORIZE: 2,
        StrategyNames.FUN_CHUNKS: 'funchunks',
        StrategyNames.FRIENDLY_AND_FIX: 'friendlyandfix',
        StrategyNames.TEN_OR_HUNDRED: 1,
        StrategyNames.FRIENDLY_PAIRS: 2,
        StrategyNames.BY_PLACE: 1,
        StrategyNames.REPEATED: 2,
        StrategyNames.GROUPS: 1,
        StrategyNames.FRACTIONS: 2,
        StrategyNames.WITHOUT_REGROUPING: 1,
        StrategyNames.WITH_REGROUPING: 2,
        StrategyNames.BOX_METHOD: 'boxmethod',
    }.get(strategy_name, 9)  
  
class StrategyDescriptions():
    """Mental/Written strategy descriptions."""
    COUNT = 'counting basics'
    PATTERNS = 'recognizing patterns'
    NUMBER_BONDS_COUNTERS = 'There are #w circles.<br>#p1 #s are orange.<br>How many blue circles are there?'
    NUMBER_BONDS_WHOLE_PART = 'How much is the missing part?'
    NUMBER_BONDS_PART_PART = 'How much is the whole?'
    #process names
    COUNT_ON = 'Count by ones using a number line.'
    COUNT_BACK = 'Count backwards by ones using a number line.'
    CROSS_OUT = 'Take away items by crossing them out.'
    MEMORIZE = 'Try to remember the answers'
    #splitting, use when ending in 1, 2, 3
    FUN_CHUNKS_SINGLE_DIGIT = 'Split the number into chunks that add up to the original number'
    FUN_CHUNKS_ADDITION = 'Chunk to nearest ten then add the rest'
    FUN_CHUNKS_SUBTRACTION = 'Chunk down to nearest ten then subtract the rest'
    #round up and cut down- use when ending with 7, 8, 9
    FRIENDLY_AND_FIX_ADDITION = 'Make one number friendly, add to the other number then fix'
    ADD_TEN_OR_HUNDRED = 'Add ten or one hundred by changing the number in the tens or hundreds place'
    #when 3 or more numbers, find pair that adds to 10
    FRIENDLY_PAIRS = 'Find pairs that add up to a friendly number'
    
    SUBTRACT_TEN_OR_HUNDRED = 'Subtract ten or one hundred by changing the number in the tens or hundreds place'
    FRIENDLY_AND_FIX_SUBTRACTION = 'Make one number friendly, subtract from the other number then fix'
    ADDITION_BY_PLACE = 'Add each place working from left to right'
    #multiplication basics eg 2+2+2+2
    REPEATED_ADDITION = 'Keep adding the same number'
    #eg for 14, divide into 7 groups of 2
    DIVIDED_GROUPS = 'Divide into groups of a smaller number'
    #written column addition/subtraction
    ADDING_WITHOUT_REGROUPING = 'Add the numbers in each column working from right to left'
    ADDING_WITH_REGROUPING = 'If the number does not fit in the column carry part of it to the next column'
    SUBTRACTING_WITHOUT_REGROUPING = 'Subtract the number on the bottom from the number on the top working from right to left'
    SUBTRACTING_WITH_REGROUPING = 'Borrow from the next column'
    #make denomonators common (down below), numerator = no air up here
    ADDING_FRACTIONS = 'Make the denominators (numbers down below) common then add the numerators (numbers on top)'
    SUBTRACTING_FRACTIONS = 'Make the denominators (numbers down below) common then subtract the numerators (numbers on top)'
    #multiply top, multiply bottom, simplify
    MULTIPLYING_FRACTIONS = 'Multiplying the numerators (numbers on top), multiply denominators (number down below), then simplify'
    #turn second fraction upside down and multiply
    DIVIDING_FRACTIONS = 'Turn the second fraction upside-down then multiply'
    #Block method
    BOX_BASIC = "basic"
    BOX_PART_WHOLE = "part-whole"
    BOX_COMPARISON = "comparison"
    BOX_CHANGE = "change"
    BOX_PART_WHOLE_COMPARISON = "part-whole_comparison"
    BOX_COMPARISON_CHANGE = "comparison_change"
    BOX_PART_WHOLE_COMPARISON_CHANGE = "part-whole_comparison_change"
    BOX_PLACE_HOLDER= "Place_holder"
    BOX_REMAINDER = "Remainder"
    BOX_EQUAL = "Equal"
    BOX_CONSTANT_DIFFERENCE = "Constant_difference"
    BOX_REPEATED_VARIABLE = "Repeated_variable"
    BOX_CONSTANT_TOTAL = "Constant_total"
    BOX_EXCESS_VALUE = "Excess_Value"
    BOX_CONSTANT_QUANTITY = "Constant_quantity"
    
class BoxModelFormat():
    OWNER_TEXT_VARIABLE_OBJECT_TWICE_QUESTION = "OWNER_TEXT_VARIABLE_OBJECT_TWICE_QUESTION"
    VARIABLE_OBJECT_TWICE_TEXT_QUESTION = "VARIABLE_OBJECT_TWICE_TEXT_QUESTION"
    
class StrategyExamples():
    """Mental/Written strategy examples."""

    #process names
    COUNT_ON = ['2 + 1 + 1 = 4', '5 + 1 + 1 + 1 = 8', '7 + 1 + 1 + 1 = 10'] 

    COUNT_BACK = ['5 - 1 - 1 = 3', '7 - 1 - 1 - 1 = 4', '8 - 1 - 1 - 1 = 5']
    #splitting, use when ending in 1, 2, 3
    FUN_CHUNKS_SINGLE_DIGIT = ['5 = 2 + 3', '7 = 3 + 4', '9 = 4 + 5']
    FUN_CHUNKS_SINGLE_AND_SINGLE = ['9 + 7 = 9 + 1 + 6 = 10 + 6 = 16', \
                                           '5 + 8 = 3 + 2 + 8 = 3 + 10 = 13', \
                                           '4 + 7 = 1 + 3 + 7 = 1 + 10 = 11']
    FUN_CHUNKS_SINGLE_AND_DOUBLE = ['17 + 6 = 17 + 3 + 3 = 20 + 3 = 23', \
                                           '38 + 5 = 38 + 2 + 3 = 40 + 3 = 43',\
                                           '97 + 8 = 97 + 3 + 5 = 100 + 5 = 105']
    FUN_CHUNKS_DOUBLE_AND_DOUBLE = ['23 + 31 = 3 + 20 + 31. First 20 + 31 = 51, Second 51 + 3 = 54', \
                                           '54 + 12 = 54 + 10 + 2. First 54 + 10 = 64, Second 64 + 2 = 66',\
                                           '65 + 33 = 65 + 30 + 3. First 65 + 30 = 95, Second 95 + 3 = 98']
    FUN_CHUNKS_SUBTRACTION_SINGLE_AND_DOUBLE = ['33 - 4 = 33 - 3 - 1 = 30 - 1 = 29' \
                                              '44 - 6 = 43 - 3 - 3 = 40 - 3 = 37' \
                                              '85 - 8 = 85 - 5 - 3 = 80 - 3 = 77']
    #round up and cut down- use when ending with 7, 8, 9
    FRIENDLY_AND_FIX_ADDITION = ['45 + 9 = 45 + 10 - 1 = 55 - 1 = 54', \
                                '67 + 18 = 67 + 20 - 2 = 87 - 2 = 85', \
                                '86 + 27 = 86 + 30 - 3 = 86 + 20 + 10 - 3 = 106 + 10 - 3 = 113']
    
    ADD_TEN_OR_HUNDRED = ['44 + 10 = 54', \
               '125 + 10 = 135', \
               '367 + 100 = 467']
    
    #when 3 or more numbers, find pairs that adds to 10
    FRIENDLY_PAIRS = ['8 + 7 + 3 = 8 + 10 = 18', \
                      '9 + 12 + 1 = (9 + 1) + 12 = 10 + 12 = 22', \
                      '7 + 9 + 3 + 1 = (7 + 3) + (9 + 1) = 10 + 10']
    
    SUBTRACT_TEN_OR_HUNDRED = ['44 - 10 = 34', \
               '125 - 10 = 115', \
               '367 - 100 = 267']
    
    FRIENDLY_AND_FIX_SUBTRACTION = ['35 - 9 = 35 - 10 - 1 = 25 - 1 = 24', \
                                    '58 - 19 = 58 - 20 - 1 = 38 - 1 = 37', \
                                    '85 - 27 = 85 - 30 - 3 = 55 - 3 = 52']
    
    #iMaths 4 Place Value
    ADDITION_BY_PLACE = ['132 + 62 = 100 + (30 + 60) + (2 + 2) = 194', \
                              '76 + 61 = (70 + 60) + (6 + 1) = 137' \
                              '245 + 312 = (200 + 300) + (40 + 10) + (5 + 2) = 557']
    
    #multiplication basics eg 2+2+2+2
    REPEATED_ADDITION = ['2 x 3 = 2 + 2 + 2 = 6', \
                         '3 x 3 = 3 + 3 + 3 = 9', \
                         '4 x 5 = 4 + 4 + 4 + 4 + 4 = 20 ']
    
    #eg for 14, divide into 7 groups of 2
    DIVIDED_GROUPS = ['14 divided by 7 = 7 groups of 2']

    #make denomonators common (down below), numerator = no air up here
    ADDING_FRACTIONS = ['1/2 + 1/3 = 1/2 x 3/3 + 1/3 x 2/2 = 3/6 + 2/6 = 5/6', \
                        '2/3 + 1/4 = 2/3 x 4/4 + 1/4 x 3/3 = 8/12 + 3/12 = 11/12', \
                        '1/2 + 1/5 = 1/2 x 5/5 + 1/5 x 2/2 = 5/10 + 2/10 = 7/10',]
    SUBTRACTING_FRACTIONS = ['1/2 - 1/3 = 1/2 x 3/3 - 1/3 x 2/2 = 3/6 - 2/6 = 1/6', \
                             '2/3 - 1/4 = 2/3 x 4/4 - 1/4 x 3/3 = 8/12 - 3/12 = 5/12', \
                        '1/2 - 1/5 = 1/2 x 5/5 - 1/5 x 2/2 = 5/10 - 2/10 = 3/10',]
    #multiply top, multiply bottom, simplify
    MULTIPLYING_FRACTIONS = ['1/2 x 1/4 = (1 x 1)/(2 x 4) = 1/8', \
                             '2/3 x 3/4 = (2 x 3)/(3 x 4) = 6/12 = 1/2', \
                             '4/5 x 7/8 = (4 x 7)/(5 x 8) = 28/40 = 14/20']
    #turn second fraction upside down and multiply
    DIVIDING_FRACTIONS = ['1/2 divided by 1/4 = 1/2 x 4/1 = (1 x 4)/(2 x 1) = 4/2 = 2/1 = 2', \
                             '2/3 divided by 3/4 = 2/3 x 4/3 = (2 x 4)/(3 x 3) = 8/9', \
                             '4/5 divided by 7/8 = 4/5 x 8/7 = (4 x 8)/(5 x 7) = 32/35']
    
class BoxConstants():
    BOY_NAMES = ['Bob', 'Bruce', 'Brian', 'Ernie', 'Ernesto', 'Daniel', 'David', 'Daniella', 'Fred', 'Harry', \
             'Ignatio', 'Jack' , 'Peter' , 'Richard', 'Tom']
    GIRL_NAMES = ['Alice', 'Belinda', 'Esther', 'Elizabeth', 'Ming', 'Rebecca', 'Rachel', 'Sue']
    ACTION_ITMES = {('ate', 'eat'): ['potatoes', 'peas', 'fish', 'carrots', 'apples', 'bananas', 'oranges'], \
                     ('caught','catch'): ['fish', 'spiders', 'tadpoles', 'crickets'], \
                     ('bought','buy'): ['books', 'bikes', 'presents'], \
                     ('found','find'):['coins','gems','insects','seeds'], \
                     ('lost', 'loose'):['coins','dollars','pens', 'pencils']}
    ITEM_COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'white', 'black', 'purple']
    BASIC_VARIABLE_OBJECT_TWICE_TEXT_QUESTION_OBJECTS = [('boys', 'girls'),('frogs', 'snakes'),('bears', 'lions'),('sheep', 'cows')]
    BASIC_VARIABLE_OBJECT_TWICE_TEXT_QUESTION_TEXT = ['went to school', \
                                                      'caught a cold', \
                                                      'ate ice-cream', \
                                                      'went fishing']
    
class BoxSentences():
    FISH = ["caught", "fish.", "were",]   
    
class AnswerFormat():
    '''Format for answers'''
    STRING = 'string'
    POSITIVE_INT = 'positive_int'
    NEGATIVE_POSITIVE_INT = 'negative_positive_int'
    POSITIVE_FLOAT = 'positive_float'
    NEGATIVE_POSITIVE_FLOAT = 'negative_positive_float'
    FRACTION = 'fraction'
    
class RoleTypes():
    ADMIN = 'admin'
    CONTACT = 'contact'
    STUDENT = 'student'
    PARENT = 'parent'
    TEACHER = 'teacher'
    GUARDIAN = 'guardian'
    
    
class DefaultUserName():
    PARENT_GUARDIAN_TEACHER = "Parent/Guardian/Teacher"
    STUDENT = "Student"
    
class ValueConstants():
    MAX_STUDENTS_TO_REGISTER = 10
    MIN_EMAIL_LENGTH = 6
    MAX_EMAIL_LENGTH = 254
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 255
    MIN_PASSWORD_LENGTH = 6
    #see http://security.stackexchange.com/questions/39849/does-bcrypt-have-a-maximum-password-length
    MAX_PASSWORD_LENGTH = 50
    
class EmailTypes():
    EMAIL_INTERNAL_SIGNUP = "New Signup."
    EMAIL_INTERNAL_CONATCT_REQUEST_PREFIX = "Contact Request."
    EMAIL_GENERAL_PREFIX = "Hello from Maths on Mars."
    EMAIL_RESET_PASSWORD = "Maths on Mars Password Reset."
    
class LoginConstants():
    #max number of unsuccessful logins from unknown ip since previous success
    MAX_LOGIN_ATTEMPTS = 10
    LOGIN_RATE_LIMIT_HR_PERIOD = 24
    LOGIN_RATE_LIMIT_SECS = 1
    
class SignUpConstants():
    CONTACT = 'contact'
    STANDARD = 'standard'
    LIMITED_OFFER = 'limited_offer'
    FREE = 'free'
    
class NumberBondTypes():
    COUNTERS = 'counters'
    WHOLE_PART = 'whole_part'
    PART_PART = 'part_part'
    
class ResultClassification():
    #0%
    KEEP_TRYING = 'Keep trying'
    #10%
    YOU_ARE_LEARNING = 'You are learning'
    #30%
    GOOD_TRY = 'Good try'
    #50%
    WELL_DONE = 'Well done'
    #70%
    GREAT_WORK = 'Great work'
    #80%
    GREAT_WORK = 'Really good'
    #90%
    EXCELLENT = 'Excellent'
    #100%
    PERFECT = 'Perfect'
    TIME_EXPIRED = 'Your time ran out'
    
class OperatorTypes():
    MULTIPLY = '*'
    DIVIDE = '/'
    ADD = '+'
    SUBTRACT = '-'