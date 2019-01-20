"use strict";

/* This code is copyright of Maths on Mars Ltd. and may not be copied, or used in any software other than that developed by Maths on Mars.
 Maths on Mars 4th June 2016. */

var equationModerator;
var svgSupported;
var svgEffects = false;
var svgQuestions = false;
var d3jsDrawings = true;
var keyinputEnabled = true;

var sessionId = "";
var startTime = "";
var categoryName = "";
var activityId = 0;
var activityName = "";
var strategyName = "";
var activityLevel = "";
var activityLevelProgress = "";
var timeLimit = "";
var totalQuestions = "";
var answerFormat = "";
var activityNumVariables = "";
var strategyQualifier = "";

var questionIds = "";

var greenBoxColour = "rgba(132, 225, 132, 0.9)";
var redBoxColour = "rgba(255, 132, 132, 0.9)";
var redCrossColour = "rgb(240,0,0)";
var greenTickColour = "rgb(0,215,0)";
var yellowBoxColour = "rgba(225, 225, 0, 0.1)";

var DARK_DARK_GREY = "#181818";
var MEDIUM_DARK_GREY = "#585858";
var MEDIUM_GREY = "#787878";
var LIGHT_GREY = "#B0B0B0";
var MEDIUM_LIGHT_GREY = "#D3D3D3";
var VERY_LIGHT_GREY = "#E9E9E9";

var STRATEGY_COUNT = 'Count';
var STRATEGY_PATTERNS = 'Patterns';
var STRATEGY_NUMBER_BONDS = 'Number bonds';
var STRATEGY_COUNT_ON = 'Count on';
var STRATEGY_COUNT_BACK = 'Count back';
var STRATEGY_FUN_CHUNKS = 'Fun chunks';
var STRATEGY_FRIENDLY_AND_FIX = 'Friendly and fix';
var STRATEGY_MEMORIZE = 'Memory quest';
var STRATEGY_TEN_OR_HUNDRED = 'Ten or hundred';
var STRATEGY_BY_PLACE = 'By place';
var STRATEGY_REPEATED = 'Repeated';
var STRATEGY_GROUPS = 'Groups';
var STRATEGY_FRACTIONS = 'Fractions';
var STRATEGY_BOX_METHOD = 'Box method';
var STRATEGY_WITHOUT_REGROUPING = 'Without regrouping';
var STRATEGY_WITH_REGROUPING = 'With regrouping';
var BOX_METHOD_ADDSUB_VAL_TYPES_CC = 'cc';
var BOX_METHOD_ADDSUB_VAL_TYPES_CU = 'cu';
var BOX_METHOD_ADDSUB_VAL_TYPES_UC = 'uc';
var BOX_METHOD_ADDSUB_VAL_TYPES_GC = 'gc';
var BOX_METHOD_ADDSUB_VAL_TYPES_CCC = 'ccc';
var BOX_METHOD_ADDSUB_VAL_TYPES_CUC = 'cuc';
var BOX_METHOD_ADDSUB_VAL_TYPES_UCC = 'ucc';
var BOX_METHOD_ADDSUB_VAL_TYPES_CCU = 'ccu';
var BOX_METHOD_MAX_N_WIDTH = 12;
var SVG_TEXT_STANDARD_SIZE = 32;

var STRATEGY_QUALIFIER_COUNTER = 'counters';
var STRATEGY_QUALIFIER_WHOLE_PART = 'whole-part find part';
var STRATEGY_QUALIFIER_PART_PART = 'part-part find whole';
var STRATEGY_QUALIFIER_BASIC_ADDITION = 'Basic addition';
var STRATEGY_QUALIFIER_BASIC_SUBTRACTION = 'Basic subtraction';
var STRATEGY_QUALIFIER_BASIC_NAMED_ADDITION = 'Basic named addition';
var STRATEGY_QUALIFIER_BASIC_NAMED_SUBTRACTION = 'Basic named subtraction';
var STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION = 'Basic named multiplication';

var CATEGORY_PATTERNS = 'Patterns';
var CATEGORY_NUMBERS = 'Numbers';
var CATEGORY_ADDITION = 'Addition';
var CATEGORY_SUBTRACTION = 'Subtraction';
var CATEGORY_MULTIPLICATION = 'Multiplication';
var CATEGORY_DIVISION = 'Division';
var CATEGORY_FRACTIONS = 'Fractions';
var CATEGORY_DECIMALS = 'Decimals';
var CATEGORY_POWERS = 'Powers';
var CATEGORY_ROOTS = 'Roots';
var CATEGORY_PERCENTAGE = 'Percentage';
var CATEGORY_RATIO = 'Ration';
var CATEGORY_AVERAGE = 'Average';
var CATEGORY_MEASUREMENT = 'Measurement';
var CATEGORY_GEOMETRY = 'Geometry';

var MULTIPLY_SYMBOL = '&#215;';
var PLUS_SYMBOL = 	'&#43;';
var MINUS_SYMBOL = 	'&#45;';
var EQUALS_SYMBOL = '&#61;';
var MEMORIZE_COUNTERS_SYM_NUMBER = 12;

var SVG_COLOR_ARRAY = ['darkorange','darkturquoise', 'greenyellow','lightblue','darkkhaki', 'coral','limegreen','aquamarine'];
var DEFAULT_TIME_LIMIT = 600;

window.addEventListener("keydown", checkKeyPressed, false);

if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function mathQuiz() {
	console.log(">>mathQuiz()");
	var activity = document.getElementById("activity");
	if(activity) {
        console.log("activity OK)");
        var activityJSON = activity.getAttribute ('data-activityjson');
        var JSONObject = tryParseJSON (activityJSON);
        if (JSONObject !== false) {
            sessionId = JSONObject.session_id;
            startTime = JSONObject.start_time;
            categoryName = JSONObject.category_name;
            activityName = JSONObject.activity_name;
            strategyName = JSONObject.strategy_name;
            activityLevel = JSONObject.activity_level;
            activityLevelProgress = JSONObject.activity_progress;
            timeLimit = JSONObject.time_limit;
            totalQuestions = JSONObject.total_questions;
            answerFormat = JSONObject.answer_format;
            activityNumVariables = JSONObject.activity_variables;
            questionIds = JSONObject.question_ids;
            strategyQualifier = JSONObject.strategy_qualifier;
            activityId = JSONObject.activity_id;
            var rawQuestions = JSONObject.questions;
            var rawAnswers = JSONObject.answers;
            console.log("--mathQuiz() categoryName:"+categoryName+" strategyName:"+strategyName+" sessionId:"+sessionId+
            " startTime:"+startTime+" activityName:"+activityName);
            console.log("--mathQuiz() rawQuestions:"+rawQuestions+" rawAnswers:"+rawAnswers);
            if ((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX)){
                console.log("strategyName === Fun chunks");
                var rawJumpValues = JSONObject.data1;
                var rawStage1Questions = JSONObject.data2;
                var rawLinePositions = JSONObject.data3;
                var rawFlips = JSONObject.data4;
            }
            else if (strategyName === STRATEGY_NUMBER_BONDS){
                var rawWholeValues = JSONObject.data1;
                var rawPart1Values = JSONObject.data2;
                var rawPart2Values = JSONObject.data3;
            }
            else if (strategyName === STRATEGY_MEMORIZE){
                var rawVar1Values = JSONObject.data1;
                var rawVar2Values = JSONObject.data2;
                var rawVar3Values = JSONObject.data3;
                var rawOperator1Values = JSONObject.data4;
                var rawOperator2Values = JSONObject.data5;
                var numVariables = JSONObject.data6;
            }
            else if (strategyName === STRATEGY_BOX_METHOD){
                var rawHints = JSONObject.data1;
                var rawTotals = JSONObject.data2;
                var rawPartTypes = JSONObject.data3;
                var rawPartNames = JSONObject.data4;
                var rawPartValues = JSONObject.data5;
                var partNameAssociations = JSONObject.data6;
                var numVariables = JSONObject.activity_variables;
                var boxMethodThings = JSONObject.data7;
            }
        }
        else {
            console.log("JSONObject is null");
        }
        if  ((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX)) {
            console.log("((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX))");
            if (!!rawQuestions) {
                if (!!rawAnswers) {
                    console.log ("generating equations");
                    equationModerator = generateFunChunkEquations (rawQuestions, rawLinePositions, rawJumpValues, rawStage1Questions, rawAnswers, rawFlips);
                    setUpAnswerElement();
                    //clearAnswerArea();
                    //limitInputToAnswer();
                    var questionText = generateQuestionText();
                    displayQuestion(questionText);
                    displayGraphics();
                    setUpListeners();
                }
                else {
                    console.log("rawAnswers is null");
                }
            }
            else {
                console.log("rawQuestions is null");
            }
        }
        else if (strategyName === STRATEGY_NUMBER_BONDS){
            console.log("strategyName === STRATEGY_NUMBER_BONDS strategyQualifier: "+strategyQualifier);
            if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER){
                console.log("whole: "+rawWholeValues+" part1: "+rawPart1Values+" part2: "+rawPart2Values);
                console.log("STRATEGY_QUALIFIER_COUNTER");
                equationModerator = generateNumberBondEquations(rawWholeValues, rawPart1Values, rawPart2Values, rawQuestions)
                generateQuestionText();
                setUpAnswerElement();
                displayGraphics();
                setUpListeners();
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART){
                console.log("whole: "+rawWholeValues+" part1: "+rawPart1Values+" part2: "+rawPart2Values);
                console.log("STRATEGY_QUALIFIER_WHOLE_PART");
                equationModerator = generateNumberBondEquations(rawWholeValues, rawPart1Values, rawPart2Values, rawQuestions);
                generateQuestionText();
                setUpAnswerElement();
                displayGraphics();
                setUpListeners();
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART){
                console.log("whole: "+rawWholeValues+" part1: "+rawPart1Values+" part2: "+rawPart2Values);
                console.log("STRATEGY_QUALIFIER_PART_PART");
                equationModerator = generateNumberBondEquations(rawWholeValues, rawPart1Values, rawPart2Values, rawQuestions);
                generateQuestionText();
                setUpAnswerElement();
                displayGraphics();
                setUpListeners();
            }
        }
        else if (strategyName === STRATEGY_MEMORIZE){
            if (categoryName === CATEGORY_MULTIPLICATION){
                keyinputEnabled = false;
                disableTextInput();
                equationModerator = generateMemorizeEquations(numVariables, rawVar1Values, rawVar2Values, rawVar3Values, rawOperator1Values, rawOperator2Values, rawAnswers) ;
                var questionText = generateQuestionText();
                displayQuestion(questionText);
                setUpAnswerElement();
                displayGraphics();
                setUpListeners();
            }
        }
        else if (strategyName === STRATEGY_BOX_METHOD){
            if (categoryName === CATEGORY_ADDITION || categoryName === CATEGORY_SUBTRACTION || categoryName === CATEGORY_MULTIPLICATION || categoryName === CATEGORY_DIVISION){
                keyinputEnabled = true;
                equationModerator = generateBoxEquations(numVariables, rawQuestions, rawAnswers, rawHints, rawTotals, rawPartTypes, rawPartNames, rawPartValues, boxMethodThings);
                var questionText = generateQuestionText();
                if (strategyQualifier != STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION) {
                    displayQuestion (questionText);
                }
                setUpAnswerElement();
                displayGraphics();
                setUpListeners();
            }
        }
        else if (strategyName === 'some sort of box question') {
            //svgQuestion();
            //xPosition, yPosition, width, height, numberColoured, fillColour, opacity, strokeWidth
            svgCusineerRod(0, 10, 50, 50, 7, getRodColour(7), 0.5, 2);
            svgCusineerRod(0, 40, 50, 50, 4, getRodColour(4), 0.5, 2);
            svgOverlay();
        }
        else {
            console.log("unrecognised strategy name:"+strategyName);
        }
	}
    else {
		console.log("--mathQuiz activity is null ");
	}
}

function splitOnComma(valueArray){
    console.log(">>splitOnComma() valueArray"+valueArray);
    var splitArray;
    if (valueArray){
        splitArray=valueArray.split(',');
        console.log("--splitOnComma() splitArray"+splitArray);
    }
    return splitArray;
}

function generateNumberBondEquations(rawWholeValues, rawPart1Values, rawPart2Values, rawQuestions) {
    var wholeVals = removeAllWhitespaces(rawWholeValues);
    var wholeValues = splitOnComma(wholeVals);
    var part1Vals = removeAllWhitespaces(rawPart1Values);
    var part1Values = splitOnComma(part1Vals);
    var part2Vals = removeAllWhitespaces(rawPart2Values);
    var part2Values = splitOnComma(part2Vals);
    assert((rawQuestions.length)===1, 'generateNumberBondEquations() len(rawQuestions)===1');
    if ((rawQuestions.length) === 1)
    {
        var questionText = rawQuestions[0];
        console.log("--generateNumberBondEquations() qq text:"+questionText)
    }
    else {
        var questionText = "";
    }
    var startTimes = [];
    var corrects = [];
    var givenAnswers = [];
    var elapsedTimeList = [];
    var sessionFinished = false;
    var hints = [];
    var helps = [];
    var answers = [];
    if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER){
        answers = part2Values;
    }
    else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART){
        answers = part2Values;
    }
    else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART){
        answers = wholeValues;
    }
    var container = pojo('currentIndex', 'wholeValues', 'part1Values',
        'part2Values', 'questionText', 'answers',  'startTimes', 'corrects', 'givenAnswers', 'elapsedTimeList', 'sessionFinished', 'hints', 'helps');
    var equationModerator = container(0, wholeValues, part1Values, part2Values, questionText, answers, startTimes, corrects, givenAnswers, elapsedTimeList, sessionFinished, hints, helps);
    return equationModerator;
}

function generateFunChunkEquations(rawQuestions, rawLinePositions, rawJumpValues, rawStage1Questions, rawAnswers, rawFlips) {
    var qqs = removeAllWhitespaces(rawQuestions);
    var questions = qqs.split(',');
    var rawAnswers = removeAllWhitespaces(rawAnswers);
    var answers = rawAnswers.split(',');
    var rawLinePositions = removeAllWhitespaces(rawLinePositions);
    var linePositions = rawLinePositions.split(',');
    var rawJumpValues = removeAllWhitespaces(rawJumpValues);
    var jumpValues = rawJumpValues.split(',');
    var rawStage1Questions = removeAllWhitespaces(rawStage1Questions);
    var stage1Questions = rawStage1Questions.split(',');
    var rawFlips = removeAllWhitespaces(rawFlips);
    var flips = rawFlips.split(',');
    var startTimes = [];
    var corrects = [];
    var givenAnswers = [];
    var elapsedTimeList = [];
    var sessionFinished = false;
    var hints = [];
    var helps = [];
    assert(type(questions)=='array', 'assert questions is array');

    console.log("--generateFunChunkEquations() jumpValues:"+jumpValues+" stage1Questions:"+stage1Questions+" linePositions:"+linePositions+" flips:"+flips);

    var container = pojo('currentIndex', 'questions', 'answers',
        'linePositions', 'jumpValues', 'stage1Questions', 'flips', 'startTimes', 'corrects', 'givenAnswers', 'elapsedTimeList', 'sessionFinished', 'hints', 'helps');

    var equationModerator = container(0, questions, answers, linePositions, jumpValues, stage1Questions, flips, startTimes, corrects, givenAnswers, elapsedTimeList, sessionFinished, hints, helps);
    return equationModerator;
}

function generateMemorizeEquations(numVariables, rawVar1Values, rawVar2Values, rawVar3Values, rawOperator1Values, rawOperator2Values, rawAnswers) {
    var var1Vals = removeAllWhitespaces(rawVar1Values);
    var var1Values = splitOnComma(var1Vals);
    var var2Vals = removeAllWhitespaces(rawVar2Values);
    var var2Values = splitOnComma(var2Vals);
    var var3Vals = removeAllWhitespaces(rawVar3Values);
    var var3Values = splitOnComma(var3Vals);
    var op1Vals = removeAllWhitespaces(rawOperator1Values);
    var op1Values = splitOnComma(op1Vals);
    var op2Vals = removeAllWhitespaces(rawOperator2Values);
    var op2Values = splitOnComma(op2Vals);
    var answerVals = removeAllWhitespaces(rawAnswers);
    var answers = splitOnComma(answerVals);
    var questionText = "";
    var startTimes = [];
    var corrects = [];
    var givenAnswers = [];
    var elapsedTimeList = [];
    var sessionFinished = false;
    var hints = [];
    var helps = [];
    var questions = [];
    var numVariables = parseInt(numVariables);
    console.log("--generateMemorizeEquations() answers: "+answers+" answerVals: "+answerVals+" rawAnswers: "+rawAnswers)
    if (numVariables===2) {
        for (var i = 0; i < var1Values.length; i++) {
            questions.push(generateMemorizeQuestion2Vars (var1Values[i], var2Values[i], op1Values[i]));
        }
    }
    var container = pojo('currentIndex', 'numVariables', 'var1Values', 'var2Values',
        'var3Values', 'op1Values', 'op2Values', 'questions', 'answers',  'startTimes', 'corrects', 'givenAnswers', 'elapsedTimeList', 'sessionFinished', 'hints', 'helps');
    var equationModerator = container(0, numVariables, var1Values, var2Values, var3Values, op1Values, op2Values, questions, answers, startTimes, corrects, givenAnswers, elapsedTimeList, sessionFinished, hints, helps);
    return equationModerator;
}

function generateMemorizeQuestion2Vars(var1, var2, op1){
    var pt1 = parseInt(var1);
    var pt2 = parseInt(var2);
    var question = '';
    if (op1 === '*'){
        question = pt1.toString()+' '+MULTIPLY_SYMBOL+' '+pt2.toString();
    }
    return question;
}

function generateBoxEquations(numVariables, rawQuestions, rawAnswers, rawHints, rawTotals, rawPartTypes, rawPartNames, rawPartValues, boxMethodItems) {
    var questionText = "";
    var startTimes = [];
    var corrects = [];
    var givenAnswers = [];
    var elapsedTimeList = [];
    var sessionFinished = false;
    var hints = [];
    var helps = [];
    var partNames = [];
    var questions = rawQuestions.split (',');
    var rawAnswers = removeAllWhitespaces (rawAnswers);
    var answers = rawAnswers.split (',');
    var rawHints = removeAllWhitespaces (rawHints);
    var hintTexts = rawHints.split (',');
    var rawTotals = removeAllWhitespaces (rawTotals);
    var totals = rawTotals.split (',');
    var rawPartTypes = removeAllWhitespaces (rawPartTypes);
    var partTypes = rawPartTypes.split (',');
    var numVariables = parseInt (numVariables);
    var rawPartValues = removeAllWhitespaces (rawPartValues);
    var partValues = rawPartValues.split (',');
    var boxMethodThings;
    if (boxMethodItems) {
        var rawBoxThings = removeAllWhitespaces (boxMethodItems);
        boxMethodThings = rawBoxThings.split (',');
    }
    if (rawPartNames){
        var rawPartNames = removeAllWhitespaces (rawPartNames);
        partNames = rawPartNames.split (',');
    }
    var first = true;
    var twoDvalueArray = [];
    var twoDnameArray = [];
    if (numVariables===2) {
        twoDvalueArray = listTo2DX2 (partValues, numVariables);
        twoDnameArray = listTo2DX2 (partNames, numVariables);
    }
    else if(numVariables===3){
        twoDvalueArray = listTo2DX3 (partValues, numVariables);
        twoDnameArray = listTo2DX3 (partNames, numVariables);
    }
    console.log("--generateBoxEquations() questions; "+questions+" numVariables:"+numVariables+" totals:"+totals);
    var container = pojo('currentIndex', 'numVariables', 'questions', 'answers', 'hintTexts', 'totals', 'partTypes', 'partNames', 'partValues',  'startTimes',
        'corrects', 'givenAnswers', 'elapsedTimeList', 'sessionFinished', 'hints', 'helps', 'boxMethodThings');
    var equationModerator = container(0, numVariables, questions, answers, hintTexts, totals, partTypes, twoDnameArray, twoDvalueArray, startTimes,
        corrects, givenAnswers, elapsedTimeList, sessionFinished, hints, helps, boxMethodThings);
    return equationModerator;
}



function tryParseJSON (jsonString){
    try {
        var o = JSON.parse(jsonString);

        // Handle non-exception-throwing cases:
        // Neither JSON.parse(false) or JSON.parse(1234) throw errors, hence the type-checking,
        // but... JSON.parse(null) returns 'null', and typeof null === "object",
        // so we must check for that, too.
        if (o && typeof o === "object" && o !== null) {
            return o;
        }
    }
    catch (e) {
        console.log("--tryParseJSON() string is not JSON")
    }

    return false;
};

function setUpAnswerElement(){
    var maxLen;
    maxLen = getMaxStringLength(equationModerator.answers);
    setAnswerSize(maxLen);
    clearAnswerArea();
}

function setAnswerSize(answerLength){
    assert(type(answerLength)=='number','answerLength is int type: '+type(answerLength));
    var answerWidth = 80+"px";
    if (answerLength <= 2) {
        answerWidth = 40+"px";
    }
    else if (answerLength <= 4) {
        answerWidth = 80+"px";
    }
    else {
        answerWidth = 120+"px";
    }
    var answerElement = document.getElementById ("text_answer");
    answerElement.setAttribute ("style", "width:" + answerWidth);
    answerElement.focus ();
}

function clearAnswerArea(){
    var answerBoxItem = document.getElementById ('text_answer');
    //var answerBoxItem = document.querySelector("#text_answer input");
    console.log("--clearAnswerArea current value:"+answerBoxItem.value+" "+answerBoxItem);
    answerBoxItem.value = "";
    answerBoxItem.setAttribute("style","background-color:"+yellowBoxColour);
}

function disableTextInput(){
    var answerBoxItem = document.getElementById ('text_answer');
    answerBoxItem.value = "";
    answerBoxItem.disabled = true;
    answerBoxItem.setAttribute("style","background-color: "+'gray');
}

/*
function limitInputToAnswer(){
    var field = document.getElementById("text_answer");
    field.onblur = function() {
        field.focus();
    }
}
*/


function displayQuestion(questionText){
    document.getElementById ('text_question').innerHTML = questionText;
}

function clearEverything(){
    var s = Snap("#svg_result");
    s.clear();
    document.getElementById("text_answer").style.visibility = "hidden";
    document.getElementById ('question_title').innerHTML = "";
    document.getElementById ('question_description').innerHTML = "";
    document.getElementById ('text_question').innerHTML = "";
}

function displayGraphics(){
    console.log(">>displayGraphics() strategyName: "+strategyName+" strategyQualifier: "+strategyQualifier);
    if  ((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX)) {
        if (activityNumVariables.toString()==='2')
        {
            //check how many vars in equation
            assert (equationModerator.jumpValues.length.toString () === (2 * totalQuestions).toString (), 'assert jumps length is twice question length');
            var index = equationModerator.currentIndex;
            var linePosArray = equationModerator.linePositions.slice (index * 3, index * 3 + 3);
            var jumpValsArray = equationModerator.jumpValues.slice (index * 2, index * 2 + 2);
            if (categoryName === CATEGORY_ADDITION) {
                funChunkTwoValAdditionDrawing (linePosArray, jumpValsArray);
            }
            else if (categoryName === CATEGORY_SUBTRACTION) {
                funChunkTwoValSubtractionDrawing (linePosArray, jumpValsArray);
            }
        }
    }
    else if (strategyName === STRATEGY_NUMBER_BONDS){
        console.log("--displayGraphics() STRATEGY_NUMBER_BONDS");
        if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER) {
            svgNumberBondsCounters();
        }
        else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART) {
            svgNumberBondsPartPartWhole();
        }
        else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART){
            svgNumberBondsPartPartWhole();
        }
    }
    else if (strategyName === STRATEGY_MEMORIZE){
        if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER) {
            svgNMemorizeCounters();
        }

    }
    else if(strategyName === STRATEGY_BOX_METHOD){
        if (categoryName === CATEGORY_ADDITION || categoryName === CATEGORY_SUBTRACTION || categoryName === CATEGORY_MULTIPLICATION || categoryName === CATEGORY_DIVISION){
            svgBoxMethodASMD();
        }
    }
    updateProgress();
}

function setUpListeners(){
    addButtonListeners();
    //attachKeypressListener();
}

function generateQuestionText() {
    var newQuestion = "";
    if (equationModerator) {
        var runningTotal = 0;
        newQuestion = false;
        console.log("--generateQuestionText() equationModerator.currentIndex "+equationModerator.currentIndex+" totalQuestions: "+totalQuestions);
        if (equationModerator.currentIndex < (totalQuestions)) {
            var totalTime =0;
            for (var i=0; i < equationModerator.elapsedTimeList.length; i++){
                totalTime+= equationModerator.elapsedTimeList[i]
            }
            console.log("--generateQuestionText() totalTime: "+totalTime+" timeLimit: "+timeLimit);
            if (totalTime < timeLimit * 1000) {
                var startTime = Date.now ();
                equationModerator.startTimes[equationModerator.currentIndex] = startTime;
                if (strategyName === STRATEGY_NUMBER_BONDS){
                    replaceNumberBondDescription();
                }
                else if (strategyName === STRATEGY_BOX_METHOD && strategyQualifier === STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION){
                    updateNamedBoxModelDescription();
                    newQuestion = equationModerator.questions[equationModerator.currentIndex];
                }
                else {
                    console.log("--generateQuestionText() newQuestion: "+equationModerator.questions[equationModerator.currentIndex]);
                    newQuestion = equationModerator.questions[equationModerator.currentIndex];
                }

            }
        }
    }
    else{
        console.error("--generateQuestionText input parameter is null");
    }
    console.log("--generateQuestionText() newQuestion "+newQuestion);
	return newQuestion;
}

function appendAnswer(answerText){
    console.log(">>appendAnswer() answerText:"+answerText);
    if (equationModerator.sessionFinished === true){
        return;
    }
    var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
    console.log("--appendAnswer() givenAnswer before:"+givenAnswer);
    if (givenAnswer === undefined){
        givenAnswer = '';
    }
    var newAnswer = givenAnswer+answerText;
    equationModerator.givenAnswers[equationModerator.currentIndex] = newAnswer;
    console.log("--appendAnswer() givenAnswer after:"+equationModerator.givenAnswers[equationModerator.currentIndex]+"currentIndex: "+equationModerator.currentIndex);
    updateAnswerElement(newAnswer);
}

function replaceAnswer(answerText){
    if (equationModerator.sessionFinished === true){
        return;
    }
    equationModerator.givenAnswers[equationModerator.currentIndex] = answerText;
    forceUpdateAnswerElement(answerText);
    allowSubmitOnReplace();
}

function updateAnswerElement(newAnswer) {
    console.log("--updateAnswerElement()");
    var answerBoxItem = document.getElementById("text_answer");
    if (answerBoxItem !== document.activeElement) {
        console.log("--updateAnswerElement() answerBoxItem !== document.activeElement ");
        //only update if not selected
        forceUpdateAnswerElement(newAnswer);
    }
}

function forceUpdateAnswerElement(newAnswer) {
    var answerBoxItem = document.getElementById("text_answer");
    if (answerBoxItem.value !== newAnswer) {
            answerBoxItem.value = newAnswer;
        }
}

function updateNamedBoxModelDescription() {
    var element = document.getElementById ("question_description");
    var nameArray = equationModerator.partNames[equationModerator.currentIndex];
    var thingText = equationModerator.boxMethodThings[equationModerator.currentIndex];
    var partValueArray = equationModerator.partValues[equationModerator.currentIndex];
    if (partValueArray[1]!=1){
        thingText = thingText+'s'
    }
    var newText = nameArray[1] + " has " + partValueArray[1] + " " + thingText+". ";
    newText = newText+nameArray[0] + " has " + partValueArray[0] + " times as many " + thingText +" as "+ nameArray[1]+". ";
    newText = newText+"How many " + thingText + " does " + nameArray[0]  +" have?";
    element.innerHTML = newText;
}


function replaceNumberBondDescription(){
    var element = document.getElementById ("question_description");
    var text = equationModerator.questionText;
    if (equationModerator.currentIndex < totalQuestions) {
        if (strategyName === STRATEGY_NUMBER_BONDS) {
            if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER) {
                var wholeValue = equationModerator.wholeValues[equationModerator.currentIndex];
                var part1Value = equationModerator.part1Values[equationModerator.currentIndex];
                var newText = text.replace ('#w', wholeValue.toString ());
                newText = newText.replace ('#p1', part1Value.toString ());
                if (part1Value.toString () === '1') {
                    newText = newText.replace ('#s', 'circle');
                }
                else {
                    newText = newText.replace ('#s', 'circles');
                }
                element.innerHTML = newText;
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART){
                var part1Value = equationModerator.part1Values[equationModerator.currentIndex];
                var part2Value = equationModerator.part2Values[equationModerator.currentIndex];
                var newText = part1Value.toString()+" "+PLUS_SYMBOL+" "+part2Value.toString()+" "+EQUALS_SYMBOL+" ?";
                element.innerHTML = newText;
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART){
                var wholeValue = equationModerator.wholeValues[equationModerator.currentIndex];
                var part1Value = equationModerator.part1Values[equationModerator.currentIndex];
                var newText = part1Value.toString()+" "+PLUS_SYMBOL+" ? "+EQUALS_SYMBOL+" "+wholeValue.toString();
                element.innerHTML = newText;
            }
        }
    }
    else {
        element.innerHTML = "";
    }
}


function checkAnswer() {
    console.log (">>checkAnswer()");
    if (equationModerator.sessionFinished === true) {
        console.log ("--checkAnswer() equationModerator.sessionFinished");
        return "Finished";
    }
        if (equationModerator.currentIndex >= (equationModerator.givenAnswers.length)) {
            if (equationModerator.currentIndex > 0) {
                console.log ("--checkAnswer() Indexing error");
                wrapUpSession ("Indexing error");
                return "Finished";
            }
        }
        else {
            var actualAnswer = equationModerator.answers[equationModerator.currentIndex];
            var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
            console.log ("--checkAnswer() actualAnswer: "+actualAnswer+" givenAnswer: "+givenAnswer);
            if (givenAnswer.length < actualAnswer.length) {
                console.log ("--checkAnswer() Insufficient length");
                return "Insufficient";
            }
            else if (givenAnswer === actualAnswer) {
                equationModerator.corrects[equationModerator.currentIndex] = true;
                setTimes ();
                showWorking();
                displayStatus (true);
                return "Correct";
            }
            else {
                // answer.length > currentEqn.answer.length or just incorrect
                equationModerator.corrects[equationModerator.currentIndex] = false;
                setTimes ();
                showWorking();
                displayStatus (false);
                return "Incorrect";
            }
        }
}

function showWorking(){
    if  ((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX)) {
        var index = equationModerator.currentIndex;
        if (activityNumVariables.toString()==='2'){
            assert(equationModerator.jumpValues.length.toString()===(2*totalQuestions).toString(), 'assert jumps length is twice question length');
            var linePosArray = equationModerator.linePositions.slice(index*3, index*3+3);
            var jumpValsArray = equationModerator.jumpValues.slice(index*2, index*2+2);
            if (categoryName === CATEGORY_ADDITION){
                {
                    funChunkTwoValAdditionSolution(linePosArray, jumpValsArray);
                }
            }
            else if(categoryName === CATEGORY_SUBTRACTION){
                {
                    funChunkTwoValSubtractionSolution(linePosArray, jumpValsArray);
                }
            }
        }
    }
}

function setTimes(){
    var currentTime = Date.now ();
    equationModerator.elapsedTimeList[equationModerator.currentIndex] = currentTime - equationModerator.startTimes[equationModerator.currentIndex];
}

function wipeQuestion(){
    var questionDescription = document.getElementById ('question_description');
    questionDescription.value = "";
}

function clearQuestionTitle(){
    var questionTitle = document.getElementById ('question_title');
    questionTitle.value = "";
}

function isGivenAnsLenSufficient(){
    if (equationModerator.currentIndex < (totalQuestions-1)) {
        var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
        if (givenAnswer) {
            if (givenAnswer.length >= equationModerator.answers[equationModerator.currentIndex].length) {
                console.log("--isGivenAnsLenSufficient() (givenAnswer.length >= equationModerator.answers[equationModerator.currentIndex].length) givenAnswer.length: "+givenAnswer.length)
                updateSubmitButtonStatus (true);
                return true;
            }
            else {
                updateSubmitButtonStatus (false);
            }
        }
        else {
            updateSubmitButtonStatus (false);
        }
        return false;
    }
    return true;
}

function allowSubmitOnReplace(){
    if (equationModerator.currentIndex < (totalQuestions-1)) {
        var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
        if (givenAnswer) {
            isGivenAnsLenSufficient();
        }
        else {
            updateSubmitButtonStatus (false);
        }
        return false;
    }
    return true;
}

function moveToNextOrFinish() {
    if (equationModerator.currentIndex < (totalQuestions - 1)) {
        if (isGivenAnsLenSufficient () === true) {
            equationModerator.currentIndex += 1;
            var displayText;
            if (equationModerator.totalTime >= timeLimit * 1000) {
                wrapUpSession ();
            }
            else {
                if (equationModerator.currentIndex === (totalQuestions - 1)) {
                    clearAnswerArea();
                    wipeQuestion ();
                    clearSvg ();
                    changeSubmitButtonToFinish ();
                }
                else {
                    clearAnswerArea();
                    wipeQuestion ();
                    clearSvg ();
                    changeSubmitButtonToSubmit ();
                }
                var questionText = generateQuestionText ();
                if (strategyName === STRATEGY_NUMBER_BONDS) {
                    clearAnswerArea();
                    wipeQuestion ();
                    clearSvg ();
                    displayGraphics ();
                }
                else {
                    //if questionText returns false we're done
                    if (questionText !== false) {
                        clearAnswerArea();
                        wipeQuestion ();
                        clearSvg ();
                        if (strategyQualifier != STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION){
                            //for this case we display qq on hint only
                            displayQuestion (questionText);
                        }
                        displayGraphics ();
                    }
                    else {
                        wrapUpSession ();
                    }
                }
            }
        }
    }
    else {
        wrapUpSession ();
    }
}

function equationResultToJSON(){
    var timeLimit, totalTime;
    var results = [];
    var elapsedTimes = [];
    var hints = [];
    var helps = [];
    console.log("--equationResultToJSON() totalQuestions:"+totalQuestions);
    for (var j=0; j<totalQuestions; j++){
        elapsedTimes.push(equationModerator.elapsedTimeList[j]);
        results.push(equationModerator.corrects[j]);
    }
    //Hints and helps could be any length
    for (var j=0; j<equationModerator.hints.length; j++){
        hints.push(equationModerator.hints[j]);
    }
    for (var j=0; j<equationModerator.helps.length; j++){
        helps.push(equationModerator.helps[j]);
    }
    var timeExpired = false;
    if (equationModerator.totalTime >= timeLimit * 1000){
        timeExpired = true;
    }
    var objToStringify = {};

    objToStringify['session_id'] = sessionId;
    objToStringify['start_time'] = startTime;
    objToStringify['results'] = results;
    objToStringify['elapsed_times'] = elapsedTimes;
    objToStringify['hints'] = hints;
    objToStringify['helps'] = helps;
    objToStringify['category_name'] =  categoryName;
    objToStringify['activity_id'] =  activityId;
    objToStringify['activity_name'] =  activityName;
    objToStringify['strategy_name'] =  strategyName;
    objToStringify['activity_level_progress'] =  activityLevelProgress;
    objToStringify['activity_level'] = activityLevel;
    objToStringify['question_ids'] = questionIds;
    objToStringify['time_expired'] = timeExpired;
    var stringifiedObject = JSON.stringify(objToStringify);
    return stringifiedObject;
}

function sendAjax(){
    console.log(">>sendAjax()");
    var csrfToken = document.getElementById("csrf_token").getAttribute("content");
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/activity_completed/');
    xhr.setRequestHeader("X-CSRFToken", csrfToken)
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            var OK = 200;
            if (xhr.status === OK) {
                console.log (xhr.responseText);
                window.location.href = xhr.responseText;
            }
            else {
                console.log ('Error: ' + xhr.status);
                window.location.href = '/level'
            }
        }
    };
    var stringifiedObject = equationResultToJSON();
    console.log("--sendAjax() stringifiedObject:"+stringifiedObject);
    xhr.send(stringifiedObject);
}

function wrapUpSession(){
    console.log(">>wrapUpSession()");
    keyinputEnabled = false;
    equationModerator.sessionFinished = true;
    if (equationModerator.totalTime >= timeLimit * 1000){
        clearEverything();
        svgRocketOnPath();
        var timeLimitMins = DEFAULT_TIME_LIMIT/60;
        if (isInteger(timeLimit)){
            timeLimitMins = timeLimit/60;
        }
        displayQuestion ("Your time limit is set to "+timeLimitMins +" minutes \n"+"Your time is up \n"+ "Sending results to Professor Fuzzplus...");
    }
    else {
        updateProgress();
        clearEverything();
        svgRocketOnPath();
        displayQuestion ("Sending results to Professor Fuzzplus...");
    }
    sendAjax();
}


function dummyAdd(paramA, paramB){
    return paramA + paramB;
}

function dummyRequirement(min, max){
    var randomInt = getRandomInt(min, max)
    return randomInt;
}

/*Snap SVG Renderer*/
var ROD_COLOURS = {
    WHITE: '#ffffff',
    RED: '#c0392b',
    LIGHT_GREEN: '#2ecc71',
    PURPLE: '#8e44ad',
    YELLOW: '#f1c40f',
    DARK_GREEN: '#16a085',
    BLACK: '#34495e',
    BROWN: '#d35400',
    BLUE: '#2980b9',
    ORANGE: '#f39c12',
    CLOUDS: '#ecf0f1',
};

var LINE_Y_0 = 0;
var LINE_Y_1 = 50;
var X_MULTIPLIER = 50;
var Y_MULTIPLIER = 50;
var POINT_DIAMETER = 5;
var X_POINT_START = 2;
var Y_POINT_TEXT_OFFSET = 20;
var FUN_CHUNKS_LINE_LENGTH = 15;

function snapWipeOutQuestion(){
    var s = Snap("#text_question");
    var text = 'Here is some dynamic exciting announcement';
    // inspired from http://codepen.io/GreenSock/pen/AGzci
    var textArray = text.split(" ");
    var len = textArray.length;
    var timing = 750;
    for( var index=0; index < len; index++ ) {
        (function() {
            var svgTextElement = s.text(350,100, textArray[index]).attr({ fontSize: '120px', opacity: 0, "text-anchor": "middle" });
            setTimeout( function() {
                    Snap.animate( 0, 1, function( value ) {
                        //svgTextElement.transform('s' + value   );                              // Animate by transform
                        svgTextElement.attr({ 'font-size': value * 100,  opacity: value });      // Animate by font-size ?
                    }, timing, mina.bounce, function() { svgTextElement.remove() } );
                }
                ,index * timing)
        }());
    };
}

function drawSVG(question){
    console.log("drawSVG "+question);
    var s = new Snap('.rocketsvg');
    s.attr({ viewBox: "0 0 600 600" });
    //lets draw 2 rects at position 100,100 and then reposition them
    var r = s.rect(100,50,300,100,20,20).attr({ stroke: '#123456', 'strokeWidth': 20, fill: 'red', 'opacity': 0.2 });
    var t = s.text(0,100,question);
}

function snapDrawqq(){
    var paper = Snap("#svg_area");
    var t = new Snap.Matrix()
    t.translate(100, 100);
    t.rotate(20, 100, 100);
    var text = paper.text(10, 10, "Hello World");
    text.attr({"font-size":100});
    text.transform(t);
    var circ1 = paper.circle(100, 100, 50);
    circ1.animate({r:100},5000);
}

function svgOverlay(){
    var s = Snap("#snapsvg");
    var block = s.paper.rect(40, 190, 170, 70, 10, 10);
    block.attr({
        fillOpacity: "0",
        stroke: "#1f2c39",
        strokeWidth: 3
    });
    var line = s.paper.line(125, 190, 475, 150);
    line.attr({
        stroke: "#1f2c39",
        strokeWidth: 3
    });
    var triangle = s.paper.polyline("-5,5 0,-5 5,5");
    triangle.transform('t475, 150, r70');
}

function svgRuledLine(xStart, yStart, xEnd, yEnd, strokeColour, strokeWidth) {
    assert(type(xStart)=='number','xStart is number type: '+type(xStart));
    assert(type(yStart)=='number','yStart is number type: '+type(yStart));
    assert(type(xEnd)=='number','xEnd is number type: '+type(xEnd));
    assert(type(yEnd)=='number','yEnd is number type: '+type(yEnd));
    var s = Snap("#snapsvg");
    var ruledLine = s.paper.line(xStart, yStart, xEnd, yEnd);
    ruledLine.attr({
            stroke: strokeColour,
            strokeWidth: strokeWidth
    });
}

function svgRect(x, y, width, height, strokeColor){
    console.log(">>svgRect x:"+x+" y:"+y+" width:"+width+" height:"+height+" strokeColor:"+strokeColor);
    var s = Snap("#snapsvg");
    var r = s.paper.rect(x, y, width, height);
    r.attr({
        stroke: strokeColor,
        strokeWidth: 2,
        fillOpacity: 0
    });
}

function svgArrowHead(xPosition, yPosition, rotation){
    console.log(">>svgArrowHead() xPosition: "+xPosition+" yPosition: "+yPosition+" rotation: "+rotation);
    var s = Snap("#snapsvg");
    var triangle1 = s.paper.polyline("-5,5 0,-5 5,5");
    var tri1TransformString = "t"+xPosition+","+yPosition+",r"+rotation;
    triangle1.transform(tri1TransformString);
}

function svgPoint(xPosition, yPosition, pointColor){
    console.log(">>svgPoint xPosition:"+xPosition+" yPosition:"+yPosition+" pointColor:"+pointColor);
    var s = Snap("#snapsvg");
    var point = s.paper.circle(X_MULTIPLIER*xPosition, yPosition, POINT_DIAMETER);
    point.attr({
        stroke: pointColor,
        strokeWidth: 3,
        fill: pointColor
    });
}

function svgText(xPosition, yPosition, textDraw, fontSize, strokeColour){
    console.log(">>svgText xPosition:"+xPosition+" yPosition:"+yPosition+" textDraw:"+textDraw);
    var s = Snap("#snapsvg");
    var t = s.paper.text(xPosition, yPosition, textDraw);
    if (strokeColour){
        t.attr({
            'fill':strokeColour
        });
    }
    if (fontSize){
        t.attr({
            'font-size':fontSize
        });
    }
    else {
        t.attr ({
            'font-size': 24
        });
    }
}

function svgPath(xStart, yStart, xMid, yMid, xEnd, yEnd){
    var s = Snap("#snapsvg");
    var convertedXStart = (xStart).toString();
    var convertedXMid = (xMid).toString();
    var convertedXEnd = (xEnd).toString();
    var convertedYStart = (yStart).toString();
    var convertedYMid = (yMid).toString();
    var convertedYEnd = (yEnd).toString();
    var pathString = "M"+convertedXStart+","+convertedYStart+" Q"+convertedXMid+","+convertedYMid+" "+convertedXEnd+","+convertedYEnd;
    console.log("--svgPath() pathString: "+pathString);
    var newpath = s.paper.path(pathString);
    newpath.attr({
        stroke: "black",
        strokeWidth: 1,
        fill:"none"
    });
}

function svgNumberBondsPartPartWholeAdvanced(){
    var snapsvg = Snap("#snapsvg");
    snapsvg.clear();
    var part1Text = equationModerator.part1Values[equationModerator.currentIndex];
    var part1Count = parseInt(part1Text);
    var part2Text = equationModerator.part2Values[equationModerator.currentIndex];
    var part2Count = parseInt(part2Text);
    var wholeText = equationModerator.wholeValues[equationModerator.currentIndex];
    var wholeCount = parseInt(wholeText);

    svgRect(4*X_MULTIPLIER, 0, 2*X_MULTIPLIER, 2*Y_MULTIPLIER, MEDIUM_GREY);
    svgRect(2*X_MULTIPLIER, 4*Y_MULTIPLIER, 2*X_MULTIPLIER, 2*Y_MULTIPLIER, MEDIUM_GREY);
    svgRect(6*X_MULTIPLIER, 4*Y_MULTIPLIER, 2*X_MULTIPLIER, 2*Y_MULTIPLIER, MEDIUM_GREY);

    if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART) {
        svgText (4 * X_MULTIPLIER + X_MULTIPLIER, Y_MULTIPLIER, "?", SVG_TEXT_STANDARD_SIZE);
        svgText (2 * X_MULTIPLIER + X_MULTIPLIER, 4 * Y_MULTIPLIER+Y_MULTIPLIER , part1Text, SVG_TEXT_STANDARD_SIZE);
        svgText (6*X_MULTIPLIER + X_MULTIPLIER, 4 * Y_MULTIPLIER+Y_MULTIPLIER , part2Text, SVG_TEXT_STANDARD_SIZE);
    }
    else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART) {
        svgText (4 * X_MULTIPLIER + X_MULTIPLIER, Y_MULTIPLIER/2, wholeText, SVG_TEXT_STANDARD_SIZE);
        svgText (2 * X_MULTIPLIER + X_MULTIPLIER, 6 * Y_MULTIPLIER , part1Text, SVG_TEXT_STANDARD_SIZE);
        svgText ((part1Count*X_MULTIPLIER+2*X_MULTIPLIER)+(part1Count * X_MULTIPLIER + part2Count/2*X_MULTIPLIER), 6 * Y_MULTIPLIER , "?", SVG_TEXT_STANDARD_SIZE);
    }
    svgRuledLine(2*X_MULTIPLIER+X_MULTIPLIER, 4*Y_MULTIPLIER, 4*X_MULTIPLIER+X_MULTIPLIER, 2*Y_MULTIPLIER, MEDIUM_GREY, 2);
    svgRuledLine(6*X_MULTIPLIER+X_MULTIPLIER, 4*Y_MULTIPLIER, 4*X_MULTIPLIER+X_MULTIPLIER, 2*Y_MULTIPLIER, MEDIUM_GREY, 2);
}

function svgNumberBondsPartPartWhole(hint) {
    var snapsvg = Snap ("#snapsvg");
    snapsvg.clear ();
    var part1Text = equationModerator.part1Values[equationModerator.currentIndex];
    var part1Count = parseInt (part1Text);
    var part2Text = equationModerator.part2Values[equationModerator.currentIndex];
    var part2Count = parseInt (part2Text);
    var wholeText = equationModerator.wholeValues[equationModerator.currentIndex];
    var wholeCount = parseInt (wholeText);

    var lMargin;
    if (part1Count<5){
        lMargin = X_MULTIPLIER;
    }
    else if (part1Count<7){
        lMargin = 2*X_MULTIPLIER;
    }
    else if (part1Count<9){
        lMargin = 3*X_MULTIPLIER;
    }
    else {
        lMargin = 4*X_MULTIPLIER;
    }
    var wholeRodXCentre = (4 * X_MULTIPLIER) + X_MULTIPLIER +lMargin;
    var p1RodXCentre = (2 * X_MULTIPLIER) + X_MULTIPLIER - X_MULTIPLIER+lMargin;
    var p2RodXCentre = (6 * X_MULTIPLIER) + X_MULTIPLIER + X_MULTIPLIER+lMargin;
    var lowerRodsYStart = 4*Y_MULTIPLIER;
    var upperRodYEnd = 2 * Y_MULTIPLIER;
    var wholeRodHalfWidth = wholeCount * X_MULTIPLIER / 2;
    var p1RodHalfWidth = part1Count * X_MULTIPLIER / 2;
    var p2RodHalfWidth = part2Count * X_MULTIPLIER / 2;
    var part1Width = part1Count * X_MULTIPLIER;
    if (hint) {
        var wholeRodP1Start = wholeRodXCentre - wholeRodHalfWidth;
        var wholeRodP2Start = wholeRodXCentre - wholeRodHalfWidth + part1Width;
        svgCusineerRod (wholeRodP1Start, Y_MULTIPLIER, 50, 50, part1Count, getRodColour (part1Count), 0.5, 2, MEDIUM_DARK_GREY);
        svgCusineerRod (wholeRodP2Start, Y_MULTIPLIER, 50, 50, part2Count, getRodColour (part2Count), 0.5, 2, MEDIUM_DARK_GREY);
        rectAnimation(wholeRodXCentre-wholeRodHalfWidth-10, Y_MULTIPLIER-10, wholeCount*X_MULTIPLIER+20, Y_MULTIPLIER+20, 'blue', 'blue');
    }
    else {
        svgCusineerRod(wholeRodXCentre-wholeRodHalfWidth, Y_MULTIPLIER, 50, 50, wholeCount, getRodColour(wholeCount), 0.5, 2, MEDIUM_DARK_GREY);
    }
    svgCusineerRod(p1RodXCentre-p1RodHalfWidth, lowerRodsYStart, 50, 50, part1Count, getRodColour(part1Count), 0.5, 2, MEDIUM_DARK_GREY);
    svgCusineerRod(p2RodXCentre-p2RodHalfWidth, lowerRodsYStart, 50, 50, part2Count, getRodColour(part2Count), 0.5, 2, MEDIUM_DARK_GREY);
    svgRuledLine (p1RodXCentre, lowerRodsYStart, wholeRodXCentre, upperRodYEnd, MEDIUM_GREY, 2);
    svgRuledLine (p2RodXCentre, lowerRodsYStart, wholeRodXCentre, upperRodYEnd, MEDIUM_GREY, 2);

    var displayedWhole = wholeText;
    var displayedPart2 = part2Text;
    if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART) {
        displayedWhole = "?";
    }
    else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART) {
        displayedPart2 = "?";
    }
    svgText (wholeRodXCentre, Y_MULTIPLIER/2, displayedWhole, SVG_TEXT_STANDARD_SIZE);
    svgText (p1RodXCentre, 6 * Y_MULTIPLIER , part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (p2RodXCentre, 6 * Y_MULTIPLIER , displayedPart2, SVG_TEXT_STANDARD_SIZE);

}

function svgNMemorizeCounters(){
    console.log(">>svgNMemorizeCounters()");
    var snapsvg = Snap("#snapsvg");
    snapsvg.clear();
    var var1Text = equationModerator.var1Values[equationModerator.currentIndex];
    var var1Count = parseInt(var1Text);
    var var2Text = equationModerator.var2Values[equationModerator.currentIndex];
    var var2Count = parseInt(var2Text);
    var answersText = equationModerator.answers;

    var allAnswersInclDummy = [];
    var var2Numbers = equationModerator.var2Values.map(Number);
    var sortedVar2Array = var2Numbers.sort(function(a, b){return a-b});
    console.log("--svgNMemorizeCounters() answersText: "+answersText+" sortedVar2Array: "+sortedVar2Array+" equationModerator.var2Values: "+equationModerator.var2Values);
    var extras = [];
    var answersCount = answersText.length;
    if (answersCount < MEMORIZE_COUNTERS_SYM_NUMBER){
        if (isNumber(var1Text)){
            var lastItem = sortedVar2Array.slice(-1)[0];
            console.log("--svgNMemorizeCounters() lastItem:"+lastItem);
            var var1Val;
            var lastItemVal;
            var1Val = strToInt(var1Text);
            if (var1Val){
                lastItemVal = strToInt(lastItem);
            }
            else {
                var var1Val = parseFloat(var1Text);
                lastItemVal = parseFloat(lastItem);
            }
            var neededNum = MEMORIZE_COUNTERS_SYM_NUMBER - answersCount;
            var additional = [];
            for(var i=1;i<neededNum+1;i++){
                extras.push((lastItemVal + i)*var1Val);
                console.log("--svgNMemorizeCounters() (lastItemVal + i)*var1Val:"+(lastItemVal + i)*var1Val+" i: "+i);
            }
        }

    }
    if (extras.length>0){
        var stringExtras = extras.toString().split(",");
        allAnswersInclDummy = answersText.concat(stringExtras);
        console.log("--svgNMemorizeCounters() stringExtras: "+stringExtras+" allAnswersInclDummy: "+allAnswersInclDummy+" answersText: "+answersText);
    }
    else {
        allAnswersInclDummy = answersText;
    }
    var yBaseLevel = 50;
    svgMemorizeCountersThreeRows(yBaseLevel, allAnswersInclDummy, snapsvg);
}

function svgNumberBondsCounters(){
    console.log(">>svgNumberBondsCounters()");
    var snapsvg = Snap("#snapsvg");
    snapsvg.clear();
    var part1Text = equationModerator.part1Values[equationModerator.currentIndex];
    var part1Count = parseInt(part1Text);
    var part2Text = equationModerator.part2Values[equationModerator.currentIndex];
    var part2Count = parseInt(part2Text);
    var wholeText = equationModerator.wholeValues[equationModerator.currentIndex];
    var wholeCount = parseInt(wholeText);
    var yBaseLevel = 100;
    if (wholeCount <= 6) {
        svgNumberBondsCountersOneRow(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg);
    }
    else {
        if(wholeCount % 2 == 0)
        { //whole is even
            svgNumberBondsCountersTwoRowsEven(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg);
        }
        else {  //whole is odd
            if(part1Count % 2 == 0)
            { //part1 even
                svgNumberBondsCountersTwoRowsOddP1Even(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg);
            }
            else {
                svgNumberBondsCountersTwoRowsOddP1Odd(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg);
            }
        }
    }
}

function svgNumberBondsCountersOneRow(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg){
    var part1Circles = [];
    var part2Circles = [];
    svgText(X_MULTIPLIER*wholeCount, 20+Y_POINT_TEXT_OFFSET, wholeText);

    for (var i = 0; i < part1Count; i++) {
        var circle = snapsvg.circle ((100 * i) + 50, yBaseLevel, 30);
        circle.attr ({
            fill: 'coral',
            stroke: 'coral',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part1Circles.push (circle);
    }
    for (var i = 0; i < part2Count; i++) {
        var circle = snapsvg.circle ((100 * i) + (100 * part1Count) + 50, yBaseLevel, 30);
        circle.attr ({
            fill: 'lightblue',
            stroke: 'lightblue',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part2Circles.push (circle);
    }
    //svgRect(2, 20, wholeCount*2*X_MULTIPLIER, yBaseLevel+60, LIGHT_GREY);

    svgRect(10, (yBaseLevel/2)+10, part1Count*2*X_MULTIPLIER-10, yBaseLevel-20, MEDIUM_GREY);
    svgRect(part1Count*2*X_MULTIPLIER, (yBaseLevel/2)+10, part2Count*2*X_MULTIPLIER-10, yBaseLevel-20, MEDIUM_GREY);

    svgText(X_MULTIPLIER*part1Count,  yBaseLevel+ yBaseLevel/2+Y_POINT_TEXT_OFFSET, part1Text);
    svgText(X_MULTIPLIER*(part1Count*2 + part2Count), (yBaseLevel+ yBaseLevel/2)+Y_POINT_TEXT_OFFSET, "?");

    svgRuledLine(10, 50, X_MULTIPLIER*wholeCount*2-10, 50, MEDIUM_GREY, 2);
    svgArrowHead(12, 50, 270);
    svgArrowHead(X_MULTIPLIER*wholeCount*2-12, 50, 90);


}

function svgNumberBondsCountersTwoRowsEven(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg) {
    console.log (">>svgNumberBondsCountersTwoRowsEvenP1Even()");
    var part1Circles = [];
    var topLine = true;
    var y;
    var xPos = -1;
    for (var i = 0; i < part1Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel + 80;
            topLine = true;
        }
        var circle = snapsvg.circle ((100 * xPos) + 50, y, 30);
        circle.attr ({
            fill: 'coral',
            stroke: 'coral',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part1Circles.push (circle);
    }
    if(part1Count % 2 == 0)
    { //part1 even
        svgNumberBondsCountersTwoRowsEvenP1Even(yBaseLevel, part1Count, part2Count, snapsvg);
    }
    else {
        svgNumberBondsCountersTwoRowsEvenP1Odd(yBaseLevel, part1Count, part2Count, snapsvg);
    }
    svgText(X_MULTIPLIER*wholeCount/2, 20+Y_POINT_TEXT_OFFSET, wholeText);
    svgRect(2, (yBaseLevel/2), wholeCount*X_MULTIPLIER, yBaseLevel+100, LIGHT_GREY);
    if (part1Count >1) {
        svgText (X_MULTIPLIER*part1Count / 2, (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, part1Text);
    }
    else {
        svgText (X_MULTIPLIER*part1Count / 2, 100-10+Y_POINT_TEXT_OFFSET, part1Text);
    }
    if (part2Count >1) {
        svgText (X_MULTIPLIER*part1Count + part2Count / 2, (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, "?");
    }
    else {
        svgText (X_MULTIPLIER*part1Count + part2Count / 2, 160-10+Y_POINT_TEXT_OFFSET, "?");
    }

}



function svgNumberBondsCountersTwoRowsEvenP1Even(yBaseLevel, part1Count, part2Count, snapsvg){
    console.log(">>svgNumberBondsCountersTwoRowsEvenP1Even()");
    var part2Circles = [];
    var topLine = true;
    var y;
    var xPos;
    var halfPart1 = part1Count/2;
    xPos = halfPart1-1;
    for (var i = 0; i < part2Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel+80;
            topLine = true;
        }
        var circle = snapsvg.circle ((100 * xPos)+50, y, 30);
        circle.attr ({
            fill: 'lightblue',
            stroke: 'lightblue',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part2Circles.push (circle);
    }
    svgRect(10, (yBaseLevel/2)+10, part1Count*X_MULTIPLIER-10, yBaseLevel-20+80, LIGHT_GREY);
    svgRect(part1Count*X_MULTIPLIER, (yBaseLevel/2)+10, (part2Count*X_MULTIPLIER)-10, yBaseLevel-20+80, LIGHT_GREY);
}

function svgNumberBondsCountersTwoRowsEvenP1Odd(yBaseLevel, part1Count, part2Count, snapsvg){
    console.log(">>svgNumberBondsCountersTwoRowsEvenP1Odd()");
    var part1Circles = [];
    var part2Circles = [];
    var topLine;
    var oddShift = 100;
    var y;
    var xPos;
    var downHalfPart1 = (part1Count-1)/2;
    xPos = downHalfPart1-1;
    for (var i = 0; i < part2Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel+80;
            topLine = true;
        }
        var circle = snapsvg.circle (oddShift+(100 * xPos)+50, y, 30);
        circle.attr ({
            fill: 'lightblue',
            stroke: 'lightblue',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part2Circles.push (circle);
    }

    svgRuledLine(10, 60, X_MULTIPLIER*(part1Count+part2Count)-10, 60, MEDIUM_GREY, 2);
    if ((part1Count>2)&&(part2Count>2)) {
        svgRuledLine (X_MULTIPLIER * (part1Count - 1), 140, X_MULTIPLIER * (part1Count - 1) + X_MULTIPLIER * 2, 140, MEDIUM_GREY, 2);
    }
    else {
        if (part1Count<=2){
            svgRuledLine(X_MULTIPLIER*(part1Count-1)+10, 140, X_MULTIPLIER*(part1Count-1)+ X_MULTIPLIER*2, 140, MEDIUM_GREY, 2);
        }
        else if (part2Count<=2){
            svgRuledLine(X_MULTIPLIER*(part1Count-1), 140, X_MULTIPLIER*(part1Count-1)+ X_MULTIPLIER*2-10, 140, MEDIUM_GREY, 2);
        }

    }

    svgRuledLine(10, yBaseLevel+120, X_MULTIPLIER*(part1Count+part2Count)-10,  yBaseLevel+120, MEDIUM_GREY, 2);

    svgRuledLine(X_MULTIPLIER*part1Count+50, 140, X_MULTIPLIER*part1Count+50, 60, MEDIUM_GREY, 2);
    svgRuledLine((X_MULTIPLIER*(part1Count-1)), yBaseLevel+120, (X_MULTIPLIER*(part1Count-1)), 140, MEDIUM_GREY, 2);

    svgRuledLine(10, yBaseLevel+120, 10, 60, MEDIUM_GREY, 2);
    svgRuledLine(X_MULTIPLIER*(part1Count+part2Count)-10, yBaseLevel+120, X_MULTIPLIER*(part1Count+part2Count)-10, 60, MEDIUM_GREY, 2);

}
//xStart, yStart, xEnd, yEnd, strokeColour, strokeWidth

function svgNumberBondsCountersTwoRowsOddP1Even(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg){
    console.log (">>svgNumberBondsCountersTwoRowsEvenP1Even()");
    var part1Circles = [];
    var part2Circles = [];
    var topLine = true;
    var y;
    var xPos = -1;
    for (var i = 0; i < part1Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel + 80;
            topLine = true;
        }
        var circle = snapsvg.circle ((100 * xPos) + 50, y, 30);
        circle.attr ({
            fill: 'coral',
            stroke: 'coral',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part1Circles.push (circle);
    }
    //part2 circles
    for (var i = 0; i < part2Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel+80;
            topLine = true;
        }
        var circle = snapsvg.circle ((100 * xPos)+50, y, 30);
        circle.attr ({
            fill: 'lightblue',
            stroke: 'lightblue',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part2Circles.push (circle);
    }

    svgText(wholeCount/2, 20, wholeText);
    if (part1Count >1) {
        svgText (X_MULTIPLIER*part1Count / 2, (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, part1Text);
    }
    else {
        svgText (X_MULTIPLIER*part1Count / 2, 100-10+Y_POINT_TEXT_OFFSET, part1Text);
    }
    if (part2Count >1) {
        svgText (X_MULTIPLIER*(part1Count + part2Count / 2), (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, "?");
    }
    else {
        svgText (X_MULTIPLIER*(part1Count + part2Count / 2), 160-10+Y_POINT_TEXT_OFFSET, "?");
    }
    //Top
    svgRuledLine(10, 60, (2*X_MULTIPLIER*((part1Count+part2Count-1)/2))+2*X_MULTIPLIER-10, 60, MEDIUM_GREY, 2);
    //Middle
    if ((part1Count>2)&&(part2Count>2)) {
        svgRuledLine (X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count), 140, X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count)+2*X_MULTIPLIER-10, 140, MEDIUM_GREY, 2);
    }
    else {
        if (part1Count<=2){
            svgRuledLine(X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count), 140, X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count)+2*X_MULTIPLIER-10, 140, MEDIUM_GREY, 2);
        }
        else if (part2Count<=2){
            svgRuledLine(X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count), 140, X_MULTIPLIER * (part2Count-1) + X_MULTIPLIER * (part1Count)+2*X_MULTIPLIER-10, 140, MEDIUM_GREY, 2);
        }
    }
    //Base
    svgRuledLine(10, yBaseLevel+120, X_MULTIPLIER*(part1Count+(part2Count -1)),  yBaseLevel+120, MEDIUM_GREY, 2);
    //vertical right
    svgRuledLine(X_MULTIPLIER*part1Count+(X_MULTIPLIER*part2Count-1)+X_MULTIPLIER-10, 140, X_MULTIPLIER*part1Count+(X_MULTIPLIER*part2Count-1)+X_MULTIPLIER-10, 60, MEDIUM_GREY, 2);
    //vertical mid
    svgRuledLine(X_MULTIPLIER*part1Count+(X_MULTIPLIER*part2Count-1)-X_MULTIPLIER, yBaseLevel+120, X_MULTIPLIER*part1Count+(X_MULTIPLIER*part2Count-1)-X_MULTIPLIER, 140, MEDIUM_GREY, 2);
    //vertical divider
    svgRuledLine(X_MULTIPLIER*part1Count, yBaseLevel+120, X_MULTIPLIER*part1Count, 60, MEDIUM_GREY, 2);
    //left
    svgRuledLine(10, yBaseLevel+120, 10, 60, MEDIUM_GREY, 2);

    svgRect(2, (yBaseLevel/2), (part1Count+part2Count+1)*X_MULTIPLIER, yBaseLevel+100, LIGHT_GREY);

}

function svgNumberBondsCountersTwoRowsOddP1Odd(wholeCount, wholeText, yBaseLevel, part1Count, part1Text, part2Count, snapsvg) {
    console.log ("--svgNumberBondsCountersTwoRowsOddP1Odd() whole odd,>6, P1 odd, whole: " + wholeCount + " part1: " + part1Count);
    var part1Circles = [];
    var part2Circles = [];
    var part1Circles = [];
    var part2Circles = [];
    var part1Circles = [];
    var part2Circles = [];
    var topLine = true;
    var y;
    var xPos = -1;
    for (var i = 0; i < part1Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel + 80;
            topLine = true;
        }
        var circle = snapsvg.circle ((100 * xPos) + 50, y, 30);
        circle.attr ({
            fill: 'coral',
            stroke: 'coral',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part1Circles.push (circle);
    }

    var oddShift = 100;
    var y;
    var xPos;
    var downHalfPart1 = (part1Count - 1) / 2;
    var extend = 0;
    xPos = downHalfPart1 - 1;
    for (var i = 0; i < part2Count; i++) {
        if (topLine) {
            y = yBaseLevel;
            topLine = false;
            xPos++;
        }
        else {
            y = yBaseLevel + 80;
            topLine = true;
        }
        var circle = snapsvg.circle (oddShift + (100 * xPos) + 50, y, 30);
        circle.attr ({
            fill: 'lightblue',
            stroke: 'lightblue',
            strokeOpacity: .3,
            strokeWidth: 10
        });
        part2Circles.push (circle);
    }
    if (part2Count <= 2) {
        extend = 10;
    }
    else {
        extend = 0;
    }
    svgText (wholeCount / 2, 20, wholeText);
    if (part1Count > 1) {
        svgText (X_MULTIPLIER*part1Count / 2, (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, part1Text);
    }
    else {
        svgText (X_MULTIPLIER*part1Count / 2, 100 - 10+Y_POINT_TEXT_OFFSET, part1Text);
    }
    if (part2Count > 1) {
        svgText (X_MULTIPLIER*(part1Count + part2Count / 2), (yBaseLevel + 75 + yBaseLevel / 2)+Y_POINT_TEXT_OFFSET, "?");
    }
    else {
        svgText (X_MULTIPLIER*(part1Count + part2Count / 2), 160 - 10+Y_POINT_TEXT_OFFSET, "?");
    }
    //top
    svgRuledLine (10, 60, X_MULTIPLIER * (part1Count + part2Count) + X_MULTIPLIER - 10, 60, MEDIUM_GREY, 2);
    //pt1 mid
    if (part1Count === 1) {
        svgRuledLine (X_MULTIPLIER * (part1Count - 1)+10, 140, X_MULTIPLIER * (part1Count - 1) + X_MULTIPLIER * 2 - extend, 140, MEDIUM_GREY, 2);
    }
    else {
        svgRuledLine (X_MULTIPLIER * (part1Count - 1), 140, X_MULTIPLIER * (part1Count - 1) + X_MULTIPLIER * 2 - extend, 140, MEDIUM_GREY, 2);
    }
    //base
    svgRuledLine(10, yBaseLevel+120, X_MULTIPLIER*(part1Count+part2Count-1)+extend-10,  yBaseLevel+120, MEDIUM_GREY, 2);
    //pt1 right vert
    svgRuledLine(X_MULTIPLIER*part1Count+X_MULTIPLIER-extend, 140, X_MULTIPLIER*part1Count+X_MULTIPLIER-extend, 60, MEDIUM_GREY, 2);
    //pt1 mid vert
    svgRuledLine((X_MULTIPLIER*(part1Count-1)), yBaseLevel+120, (X_MULTIPLIER*(part1Count-1)), 140, MEDIUM_GREY, 2);
    //left vertical
    svgRuledLine(10, yBaseLevel+120, 10, 60, MEDIUM_GREY, 2);
    //pt2 right vert
    if (part2Count <= 2) {
        svgRuledLine (X_MULTIPLIER * (part1Count + part2Count + 1) - extend , 140, X_MULTIPLIER * (part1Count + part2Count + 1) - extend, 60, MEDIUM_GREY, 2);
        //pt2 mid
        svgRuledLine (X_MULTIPLIER*(part1Count+part2Count-1), 140, X_MULTIPLIER*(part1Count+part2Count+1)-10, 140, MEDIUM_GREY, 2);
    }
    else {
        svgRuledLine (X_MULTIPLIER * (part1Count + part2Count + 1) - extend - 10, 140, X_MULTIPLIER * (part1Count + part2Count + 1) - extend - 10, 60, MEDIUM_GREY, 2);
        //pt2 mid
        svgRuledLine (X_MULTIPLIER*(part1Count+part2Count-1)-extend-10, 140, X_MULTIPLIER*(part1Count+part2Count+1)-10, 140, MEDIUM_GREY, 2);
    }
    //pt2 mid vert
    svgRuledLine((X_MULTIPLIER*(part1Count+part2Count-1))+extend-10, yBaseLevel+120, (X_MULTIPLIER*(part1Count+part2Count-1))+extend-10, 140, MEDIUM_GREY, 2);
    svgRect(2, (yBaseLevel/2), (part1Count+part2Count+1)*X_MULTIPLIER, yBaseLevel+100, LIGHT_GREY);
    console.log("<<svgNumberBondsCountersTwoRowsOddP1Odd() extend:"+extend);
}

function svgNumberBondsCounterHint(){
    var s = Snap("#snapsvg");
    var part1Circles = [];
    var part2Circles = [];
    var part1Text = equationModerator.part1Values[equationModerator.currentIndex];
    var part1Count = parseInt(part1Text);
    var part2Text = equationModerator.part2Values[equationModerator.currentIndex];
    var part2Count = parseInt(part2Text);
    var wholeText = equationModerator.wholeValues[equationModerator.currentIndex];
    var wholeCount = parseInt(wholeText);
    var yBaseLevel = 100;
    if (wholeCount <= 6) {
        s.clear();
        svgText(X_MULTIPLIER*wholeCount, 0+Y_POINT_TEXT_OFFSET, wholeText);
        svgRuledLine(0, 50, X_MULTIPLIER*wholeCount*2, 50, MEDIUM_GREY, 3);
        svgPoint(POINT_DIAMETER/X_MULTIPLIER, 50, MEDIUM_GREY);
        svgPoint(wholeCount*2, 50, MEDIUM_GREY);
        for (var i = 0; i < part1Count; i++) {
            var circle = s.circle ((100 * i) + 50, yBaseLevel, 30);
            circle.attr ({
                fill: 'coral',
                stroke: 'coral',
                strokeOpacity: .3,
                strokeWidth: 10
            });
            part1Circles.push (circle);
        }
        for (var i = 0; i < part2Count; i++) {
            var x = (100 * i) + (100 * part1Count) + 50;
            var circle = s.circle (x, yBaseLevel, 30);
            circle.attr ({
                fill: 'blue',
                stroke: 'blue',
                strokeOpacity: .3,
                strokeWidth: 10
            });
            part2Circles.push (circle);
            circleAnimation(circle, 25, 30, 'blue', 'lightblue');
        }

        svgRect(0, (yBaseLevel/2)+10, part1Count*2*X_MULTIPLIER, yBaseLevel-20, LIGHT_GREY);
        svgRect(part1Count*2*X_MULTIPLIER, (yBaseLevel/2)+10, part2Count*2*X_MULTIPLIER, yBaseLevel-20, LIGHT_GREY);
        svgText(X_MULTIPLIER*part1Count,  (yBaseLevel+ yBaseLevel/2)+Y_POINT_TEXT_OFFSET, part1Text);
        svgText(X_MULTIPLIER*(part1Count*2 + part2Count), (yBaseLevel+ yBaseLevel/2)+Y_POINT_TEXT_OFFSET, "?");
    }
    else {
        console.log("--svgNumberBondsCounterHint() TODO wholeCount:"+wholeCount);
        /*
        if(wholeCount % 2 == 0)
        {
            s.clear();
            //Even total number
            var halfCount = wholeCount/2;
            var topLine = true;
            var y = yBaseLevel;
            for (var i = 0; i < part1Count; i++) {
                if (topLine) {
                    y = yBaseLevel;
                    topLine = false;
                }
                else {
                    y = yBaseLevel+50;
                    topLine = true;
                }
                var circle = s.circle ((100 * i-1) + 50, y, 30);
                circle.attr ({
                    fill: 'coral',
                    stroke: 'coral',
                    strokeOpacity: .3,
                    strokeWidth: 10
                });
                part1Circles.push (circle);
            }
            if(part1Count % 2 == 0)
            { //even
                var topLine = true;
                var halfPart1 = part1Count/2;
                for (var i = 0; i < part2Count; i++) {
                    if (topLine) {
                        y = yBaseLevel;
                        topLine = false;
                    }
                    else {
                        y = yBaseLevel+50;
                        topLine = true;
                    }
                    var circle = s.circle ((100 * halfPart1) + (100 * i) + (100 * part1Count) + 50, y, 30);
                    circle.attr ({
                        fill: 'lightblue',
                        stroke: 'lightblue',
                        strokeOpacity: .3,
                        strokeWidth: 10
                    });
                    part2Circles.push (circle);
                }
            }
            else {
                var topLine = false;
                var halfPart1 = part1Count-1/2;
                var oddShift =0;
                for (var i = 0; i < part2Count; i++) {
                    if (topLine) {
                        y = yBaseLevel;
                        topLine = false;
                        oddShift = 100;
                    }
                    else {
                        y = yBaseLevel+50;
                        topLine = true;
                        oddShift = 0;
                    }
                    var circle = s.circle (oddShift+(100 * halfPart1) + (100 * i) + (100 * part1Count) + 50, y, 30);
                    circle.attr ({
                        fill: 'lightblue',
                        stroke: 'lightblue',
                        strokeOpacity: .3,
                        strokeWidth: 10
                    });
                    part2Circles.push (circle);
                }
            }
        }
        */
    }
}

function svgMemorizeCountersThreeRows(yBaseLevel, answersText, snapsvg) {
    console.log (">>svgMemorizeCountersThreeRows() answersText.length: "+answersText.length);
    var answerCircles = [];
    var topLine = true;
    var y;
    var xPos = -1;
    console.log("--svgMemorizeCountersThreeRows() answersText:"+answersText);
    var answersShuffled = shuffleArray(answersText);
    console.log("--svgMemorizeCountersThreeRows() answersShuffled:"+answersShuffled);
    assert(answersText.length === MEMORIZE_COUNTERS_SYM_NUMBER, 'Is correct memorize array length');
    var k =0;
    var printedAnswer="";
    var textXShift = 0;
    for (var i = 0; i < 3; i++) {
        xPos = -1;
        for (var j = 0; j < MEMORIZE_COUNTERS_SYM_NUMBER/3; j++) {
            y = yBaseLevel+i*100;
            xPos++;
            if (k<answersShuffled.length){
                printedAnswer = answersShuffled[k]
            }
            else {
                console.log("--svgMemorizeCountersThreeRows() Error k!<answersShuffled.length");
                printedAnswer = 0;
            }
            var svgCircleColor = randomItemFromArray(SVG_COLOR_ARRAY);
            var circle = snapsvg.circle ((120 * xPos) + 50, y, 40);
            circle.attr ({
                fill: svgCircleColor,
                stroke: svgCircleColor,
                fillOpacity: .5,
                strokeOpacity: .3,
                strokeWidth: 10
            });
            textXShift = calcCounterTextXShift(printedAnswer);
            var textxPosition = (120 * xPos) + textXShift;
            var textyPosition = y+10, printedAnswer;
            var t = snapsvg.paper.text(textxPosition, textyPosition, printedAnswer);
            t.attr ({
                'font-size': SVG_TEXT_STANDARD_SIZE,
                cursor: 'default',
                pointer_events: 'none'
            });
            var g = snapsvg.group(circle,t);
            g.data('value',printedAnswer);
            g.click( clickFunc );
            k += 1;
        }

    }
}

function svgBoxMethodASMD() {
    console.log(">>svgBoxMethodASMD()");
    var snapsvg = Snap ("#snapsvg");
    snapsvg.clear();
    var partTypes = equationModerator.partTypes[equationModerator.currentIndex];
    var numVariables = equationModerator.numVariables;
    var nameArray = equationModerator.partNames[equationModerator.currentIndex];
    var valueArray = equationModerator.partValues[equationModerator.currentIndex];
    var total = equationModerator.totals[equationModerator.currentIndex];
    var answer = equationModerator.answers[equationModerator.currentIndex];
    console.log("--svgBoxMethodASMD() valueArray:"+valueArray+" total:"+total+" numVariables:"+numVariables+" partTypes:"+partTypes+" nameArray:"+nameArray)
    var maxTotal = 0;
    var p1RodXLeft=0;
    var part1_val = 0;
    var part2_val = 0;
    var part3_val = 0;
    var total_val = 0;
    var rodY = 2 * Y_MULTIPLIER;
    var rodTextLevel = (rodY)+(Y_MULTIPLIER/2)+10;
    var rodTotalLevel = (rodY)-(Y_MULTIPLIER/2);
    var totalText="";
    var part1Text = "";
    var part2Text = "";
    var part3Text = "";
    var lMargin = X_MULTIPLIER;
    var runningValue = 0;
    for (var i = 0; i < equationModerator.totals.length; i++) {
        runningValue = getIntOrFloatFromInput(equationModerator.totals[i]);
        if (i === 0) {
            maxTotal = runningValue;
            console.log("--svgBoxMethodASMD() i === 0 maxTotal:"+maxTotal+" equationModerator.totals.length: "+equationModerator.totals.length);
        }
        if (runningValue > maxTotal) {
            maxTotal = runningValue;
            console.log("--svgBoxMethodASMD() runningValue > maxTotal maxTotal:"+maxTotal);
        }
    }
    console.log("--svgBoxMethodASMD() maxTotal:"+maxTotal);

    if (numVariables.toString () === '2') {
        if (categoryName === CATEGORY_ADDITION) {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    totalText = "?";
                    part1Text = part1_val.toString ();
                    part2Text = part2_val.toString ();
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_UC){
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    part1_val = getIntOrFloatFromInput (answer);
                    totalText = total.toString ();
                    part1Text = "?";
                    part2Text = part2_val.toString ();
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CU){
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (answer);
                    totalText = total.toString ();
                    part1Text = part1_val.toString ();
                    part2Text = "?";
            }
        }
        else if (categoryName === CATEGORY_SUBTRACTION) {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC) {
                totalText = getIntOrFloatFromInput (valueArray[0]);
                part1_val = getIntOrFloatFromInput (valueArray[1]);
                part2_val = getIntOrFloatFromInput (answer);
                part1Text = part1_val.toString ();
                part2Text = "?";
            }
        }
        else if (categoryName === CATEGORY_MULTIPLICATION) {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC || partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_GC) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                totalText = "?";
                part1Text = part1_val.toString ();
                part2Text = part2_val.toString ();
            }

        }
        else if (categoryName === CATEGORY_DIVISION) {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC ) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                totalText = getIntOrFloatFromInput (valueArray[0]);
                part1Text = part1_val.toString ();
                part2Text = part2_val.toString ();
            }

        }
        /*
        if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC) {
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                totalText = "?";
                part1Text = part1_val.toString ();
                part2Text = part2_val.toString ();
            }
            else if (categoryName === CATEGORY_SUBTRACTION) {
                totalText = getIntOrFloatFromInput (valueArray[0]);
                part1_val = getIntOrFloatFromInput (valueArray[1]);
                part2_val = getIntOrFloatFromInput (answer);
                part1Text = part1_val.toString ();
                part2Text = "?";
            }
        }
        else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_UC){
            if (categoryName === CATEGORY_ADDITION) {
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                part1_val = getIntOrFloatFromInput (answer);
                totalText = total.toString ();
                part1Text = "?";
                part2Text = part2_val.toString ();
            }
        }
        else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CU){
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (answer);
                totalText = total.toString ();
                part1Text = part1_val.toString ();
                part2Text = "?";
            }
        }
        */
        if (categoryName === CATEGORY_MULTIPLICATION){
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC ) {
                if (strategyName === STRATEGY_BOX_METHOD && strategyQualifier === STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION){
                    var name1 = nameArray[0];
                    var name2 = nameArray[1];
                    //X_MULTIPLIER pushes it too far to the R
                    lMargin = 5;
                    drawNamedBoxMethodMulti2Vars(name1, name2, total, rodTotalLevel, lMargin, part1_val, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY)
                }
                else {
                    boxMethodMultiBoxUnlimitedRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal)
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_GC){
                console.log("TODO");
                //boxMethod2BoxGroupRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal, partTypes)
            }
        }
        else if (categoryName === CATEGORY_DIVISION){
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC ) {
                boxMethodMultiBoxDivisionUnlimitedRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal)
            }
        }
        else if (maxTotal<=BOX_METHOD_MAX_N_WIDTH) {
            if (strategyQualifier === STRATEGY_QUALIFIER_BASIC_ADDITION || strategyQualifier === STRATEGY_QUALIFIER_BASIC_SUBTRACTION) {
                boxMethod2BoxRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY);
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_BASIC_NAMED_ADDITION || strategyQualifier === STRATEGY_QUALIFIER_BASIC_NAMED_SUBTRACTION) {
                var name1 = nameArray[0];
                var name2 = nameArray[1];
                boxMethod2BoxNamedRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, name1, name2);
            }
        }
        else {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC ) {
                boxMethodMultiBoxUnlimitedRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal)
            }
        }
    }
    else if (numVariables.toString () === '3'){
        console.log("partTypes:"+partTypes+" categoryName:"+categoryName)
        if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CCC) {
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                part3_val = getIntOrFloatFromInput (valueArray[2]);
                totalText = "?";
                part1Text = part1_val.toString ();
                part2Text = part2_val.toString ();
                part3Text = part3_val.toString ();
            }
            else if (categoryName === CATEGORY_SUBTRACTION) {
                totalText = getIntOrFloatFromInput (valueArray[0]);
                part1_val = getIntOrFloatFromInput (valueArray[1]);
                part2_val = getIntOrFloatFromInput (valueArray[2]);
                part3_val = getIntOrFloatFromInput (answer);
                part1Text = part1_val.toString ();
                part2Text = part2_val.toString ();
                part3Text = "?";
            }
        }

        /* TODO
        else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_UCC){
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (answer);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                part3_val = getIntOrFloatFromInput (valueArray[2]);
                totalText = total.toString ();
                part1Text = "?";
                part2Text = part2_val.toString ();
            }
        }
        else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CUC){
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (answer);
                part3_val = getIntOrFloatFromInput (valueArray[2]);
                totalText = total.toString ();
                part1Text = part1_val.toString ();
                part2Text = "?";
            }
        }
        else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CCU){
            if (categoryName === CATEGORY_ADDITION) {
                part1_val = getIntOrFloatFromInput (valueArray[0]);
                part2_val = getIntOrFloatFromInput (valueArray[1]);
                part3_val = getIntOrFloatFromInput (answer);
                totalText = total.toString ();
                part1Text = part1_val.toString ();
                part2Text = "?";
            }
        }
        */
        boxMethod3BoxUnlimitedRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, part3_val, part3Text, maxTotal);
    }

}

function boxMethod2BoxRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY){
    var p2RodXLeft = lMargin+(X_MULTIPLIER*part1_val);
    svgText (lMargin+(total*X_MULTIPLIER/2), rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER/2), rodTextLevel , part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER)+(part2_val*X_MULTIPLIER/2), rodTextLevel , part2Text, SVG_TEXT_STANDARD_SIZE);

    svgCusineerRod(lMargin, rodY, X_MULTIPLIER, Y_MULTIPLIER, part1_val, getRodColour(part1_val), 0.2, 2, LIGHT_GREY);
    svgCusineerRod(p2RodXLeft, rodY, X_MULTIPLIER, Y_MULTIPLIER, part2_val, getRodColour(part2_val), 0.2, 2, LIGHT_GREY);
    svgRect(lMargin, rodY, part1_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRect(p2RodXLeft, rodY, part2_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRuledLine(lMargin, rodTotalLevel+10, lMargin+(total*X_MULTIPLIER)-10, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(lMargin+2, rodTotalLevel+10, 270);
    svgArrowHead( lMargin+(total*X_MULTIPLIER)-12, rodTotalLevel+10, 90);
}

/*
TODO
function boxMethod2BoxGroupRender (lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal, partTypes){
    if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_GC){
        //swap part1 and 2 positions
    }
    var p2RodXLeft = lMargin+(X_MULTIPLIER*part1_val);
    svgText (lMargin+(total*X_MULTIPLIER/2), rodTotalLevel, totalText, 32);
    svgText (lMargin+(part1_val*X_MULTIPLIER/2), rodTextLevel , part1Text, 32);
    svgText (lMargin+(part1_val*X_MULTIPLIER)+(part2_val*X_MULTIPLIER/2), rodTextLevel , part2Text, 32);

    svgCusineerRod(lMargin, rodY, X_MULTIPLIER, Y_MULTIPLIER, part1_val, getRodColour(part1_val), 0.2, 2, LIGHT_GREY);
    svgCusineerRod(p2RodXLeft, rodY, X_MULTIPLIER, Y_MULTIPLIER, part2_val, getRodColour(part2_val), 0.2, 2, LIGHT_GREY);
    svgRect(lMargin, rodY, part1_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRect(p2RodXLeft, rodY, part2_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRuledLine(lMargin, rodTotalLevel+10, lMargin+(total*X_MULTIPLIER)-10, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(lMargin+2, rodTotalLevel+10, 270);
    svgArrowHead( lMargin+(total*X_MULTIPLIER)-12, rodTotalLevel+10, 90);
}
*/

function boxMethod2BoxNamedRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, name1, name2){
    var maxNameLength = name1.length;
    if (name2.length>maxNameLength){
        maxNameLength=name2.length;
    }
    var boxLMargin = maxNameLength*20+lMargin;
    var p2RodXLeft = boxLMargin+(X_MULTIPLIER*part1_val);
    var greaterLength = part1_val;
    if (part2_val>part1_val){
        greaterLength=part2_val;
    }
    svgText (boxLMargin+(greaterLength*X_MULTIPLIER)+40, rodY+Y_MULTIPLIER, totalText, SVG_TEXT_STANDARD_SIZE);
    svgText (boxLMargin+(part1_val*X_MULTIPLIER/2), rodTextLevel , part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (boxLMargin+(part2_val*X_MULTIPLIER/2), rodTextLevel+Y_MULTIPLIER , part2Text, SVG_TEXT_STANDARD_SIZE);

    svgText (lMargin, rodTextLevel , name1, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin, rodTextLevel+Y_MULTIPLIER , name2, SVG_TEXT_STANDARD_SIZE);

    svgCusineerRod(boxLMargin, rodY, X_MULTIPLIER, Y_MULTIPLIER, part1_val, getRodColour(part1_val), 0.2, 2, LIGHT_GREY);
    svgCusineerRod(boxLMargin, rodY+Y_MULTIPLIER, X_MULTIPLIER, Y_MULTIPLIER, part2_val, getRodColour(part2_val), 0.2, 2, LIGHT_GREY);
    var bracketX = boxLMargin+(X_MULTIPLIER*greaterLength)+10;
    var bracketYstart = rodY;
    var bracketYend = rodY+Y_MULTIPLIER+Y_MULTIPLIER;
    var bracketXmid = boxLMargin+(X_MULTIPLIER*greaterLength)+60;
    var bracketYmid = rodY +Y_MULTIPLIER;
    svgPath(bracketX, bracketYstart, bracketXmid, bracketYmid, bracketX, bracketYend);
    svgArrowHead(boxLMargin+(X_MULTIPLIER*greaterLength)+10, rodY, 300);
    svgArrowHead(boxLMargin+(X_MULTIPLIER*greaterLength)+10, rodY+Y_MULTIPLIER+Y_MULTIPLIER, 240);

}

function boxMethod3BoxUnlimitedRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, part3_val,  part3Text, maxTotal) {
    var p2RodXLeft = lMargin + (X_MULTIPLIER * part1_val);
    var p3RodXLeft = lMargin + (X_MULTIPLIER * part1_val) + (X_MULTIPLIER * part2_val);
    var totalTextX = lMargin + (total * X_MULTIPLIER / 2);
    var part1TextX = lMargin + (part1_val * X_MULTIPLIER / 2);
    var part2TextX = lMargin + (part1_val * X_MULTIPLIER) + (part2_val * X_MULTIPLIER / 2);
    var part3TextX = lMargin + (part1_val * X_MULTIPLIER) + (part2_val * X_MULTIPLIER) + (part3_val * X_MULTIPLIER / 2);
    var part1RectLeftX = lMargin;
    var part1RectXWidth = part1_val * X_MULTIPLIER;
    var part2RectWidth = part2_val * X_MULTIPLIER;
    var part3RectWidth = part3_val * X_MULTIPLIER;
    var totalRuledLineLeftX = lMargin;
    var totalRuledLineWidth = lMargin + (total * X_MULTIPLIER) - 10;
    var totalRuledLineLArrowHeadX = lMargin + 2;
    var totalRuledLineRArrowHeadX = lMargin + (total * X_MULTIPLIER) - 12;
    if (maxTotal > BOX_METHOD_MAX_N_WIDTH) {
        var proportionalMultiplier = BOX_METHOD_MAX_N_WIDTH / maxTotal;
        p2RodXLeft = p2RodXLeft * proportionalMultiplier;
        p3RodXLeft = p3RodXLeft * proportionalMultiplier;
        totalTextX = totalTextX * proportionalMultiplier;
        part1TextX = part1TextX * proportionalMultiplier;
        part2TextX = part2TextX * proportionalMultiplier;
        part3TextX = part3TextX * proportionalMultiplier;
        part1RectLeftX = part1RectLeftX * proportionalMultiplier;
        part1RectXWidth = part1RectXWidth * proportionalMultiplier;
        part2RectWidth = part2RectWidth * proportionalMultiplier;
        part3RectWidth = part3RectWidth * proportionalMultiplier;
        totalRuledLineLeftX = totalRuledLineLeftX * proportionalMultiplier;
        totalRuledLineWidth = totalRuledLineWidth * proportionalMultiplier;
        totalRuledLineRArrowHeadX = totalRuledLineRArrowHeadX * proportionalMultiplier;
        totalRuledLineLArrowHeadX = totalRuledLineLArrowHeadX * proportionalMultiplier;
    }
    else {
        svgCusineerRod (lMargin, rodY, X_MULTIPLIER, Y_MULTIPLIER, part1_val, getRodColour (part1_val), 0.2, 2, LIGHT_GREY);
        svgCusineerRod (p2RodXLeft, rodY, X_MULTIPLIER, Y_MULTIPLIER, part2_val, getRodColour (part2_val), 0.2, 2, LIGHT_GREY);
        svgCusineerRod (p3RodXLeft, rodY, X_MULTIPLIER, Y_MULTIPLIER, part3_val, getRodColour (part3_val), 0.2, 2, LIGHT_GREY);
    }
    svgText (totalTextX, rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    svgText (part1TextX, rodTextLevel, part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (part2TextX, rodTextLevel, part2Text, SVG_TEXT_STANDARD_SIZE);
    svgText (part3TextX, rodTextLevel, part3Text, SVG_TEXT_STANDARD_SIZE);

    //(xPosition, yPosition, width, height, fillColour, opacity, strokeWidth, strokeColour)
    var boxOpacity = 0.2;
    var strokeWidth = 2;
    var part1FillColour = ROD_COLOURS.WHITE;
    var part2FillColour = ROD_COLOURS.WHITE;
    var part3FillColour = ROD_COLOURS.WHITE;
    if (part1_val<=10) {
        part1FillColour = getRodColour(part1_val);
    }
    svgFilledRect (part1RectLeftX, rodY, part1RectXWidth, Y_MULTIPLIER, part1FillColour, boxOpacity, strokeWidth, DARK_DARK_GREY)
    if (part2_val<=10) {
        part2FillColour = getRodColour(part2_val);
    }
    svgFilledRect (p2RodXLeft, rodY, part2RectWidth, Y_MULTIPLIER, part2FillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
    if (part3_val<=10) {
        part3FillColour = getRodColour(part3_val);
    }
    svgFilledRect(p3RodXLeft, rodY, part3RectWidth, Y_MULTIPLIER, part3FillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
    svgRuledLine(totalRuledLineLeftX, rodTotalLevel+10, totalRuledLineWidth, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(totalRuledLineLArrowHeadX, rodTotalLevel+10, 270);
    svgArrowHead(totalRuledLineRArrowHeadX, rodTotalLevel+10, 90);
}

function boxMethodMultiBoxUnlimitedRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal) {
    console.log(">>boxMethodMultiBoxUnlimitedRender()");
    var nVarValues = [];
    var nVarLefts = [];
    var nVarTextLefts = [];
    var nVarRectLefts = [];
    var proportionalMultiplier = BOX_METHOD_MAX_N_WIDTH / total;
    var nVarRectWidth = part2_val * X_MULTIPLIER*proportionalMultiplier;
    var totalTextX = lMargin+(total * X_MULTIPLIER / 2)*proportionalMultiplier;
    var totalRuledLineLeftX = lMargin;
    var totalRuledLineXend = lMargin+((total * X_MULTIPLIER)*proportionalMultiplier);
    var totalRuledLineLArrowHeadX = (lMargin + 2);
    var totalRuledLineRArrowHeadX = lMargin + ((total * X_MULTIPLIER)-4)*proportionalMultiplier;
    var currentRectLeft = lMargin;
    console.log("--boxMethodMultiBoxUnlimitedRender() currentRectLeft:"+currentRectLeft);
    for(var j=0; j<part1_val; j++){
        nVarValues.push(part2_val);
        if (j===0){
            nVarRectLefts.push(currentRectLeft);
            nVarTextLefts.push(currentRectLeft+nVarRectWidth/2 - 4);
        }
        else {
            nVarRectLefts.push (currentRectLeft + nVarRectWidth);
            nVarTextLefts.push(currentRectLeft + nVarRectWidth+nVarRectWidth/2- 4)
        }
        currentRectLeft = nVarRectLefts[j];
        console.log("--boxMethodMultiBoxUnlimitedRender() end loop currentRectLeft:"+currentRectLeft+" j:"+j);
    }
    svgText (totalTextX, rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    var boxOpacity = 0.2;
    var strokeWidth = 2;
    var nVarFillColour = ROD_COLOURS.WHITE;
    if (part2_val<=10) {
        nVarFillColour = getRodColour(part2_val);
    }
    for (var k=0; k<nVarValues.length; k++){
        console.log("--boxMethodMultiBoxUnlimitedRender() k:"+k);
        svgFilledRect (nVarRectLefts[k], rodY, nVarRectWidth, Y_MULTIPLIER, nVarFillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
        svgText (nVarTextLefts[k], rodTextLevel, part2Text, SVG_TEXT_STANDARD_SIZE);
    }
    svgRuledLine(totalRuledLineLeftX, rodTotalLevel+10, totalRuledLineXend, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(totalRuledLineLArrowHeadX, rodTotalLevel+10, 270);
    svgArrowHead(totalRuledLineRArrowHeadX, rodTotalLevel+10, 90);
}

function drawNamedBoxMethodMulti2Vars(name1, name2, total, rodTotalLevel, lMargin, part1_val, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY){
    var nVarValues = [];
    var nVarLefts = [];
    var nVarTextLefts = [];
    var nVarRectLefts = [];
    var maxNameLength = name1.length;
    if (name2.length>maxNameLength){
        maxNameLength=name2.length;
    }
    var boxLMargin = maxNameLength*20+lMargin;
    var proportionalMultiplier = BOX_METHOD_MAX_N_WIDTH / total;
    var nVarRectWidth = part2_val * X_MULTIPLIER*proportionalMultiplier;
    var totalTextX = boxLMargin+(total * X_MULTIPLIER / 2)*proportionalMultiplier;
    var totalRuledLineLeftX = boxLMargin;
    var totalRuledLineXend = boxLMargin+((total * X_MULTIPLIER)*proportionalMultiplier);
    var totalRuledLineLArrowHeadX = (boxLMargin + 2);
    var totalRuledLineRArrowHeadX = boxLMargin + ((total * X_MULTIPLIER)-4)*proportionalMultiplier;

    var p2RodXLeft = boxLMargin+(X_MULTIPLIER*part1_val);
    var greaterLength = part1_val;
    if (part2_val>part1_val){
        greaterLength=part2_val;
    }
    var currentRectLeft = boxLMargin;

    svgText (lMargin, rodTextLevel , name1, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin, rodTextLevel+Y_MULTIPLIER , name2, SVG_TEXT_STANDARD_SIZE);

    for(var j=0; j<part1_val; j++){
        nVarValues.push(part2_val);
        if (j===0){
            nVarRectLefts.push(currentRectLeft);
            nVarTextLefts.push(currentRectLeft+nVarRectWidth/2 - 4);
        }
        else {
            nVarRectLefts.push (currentRectLeft + nVarRectWidth);
            nVarTextLefts.push(currentRectLeft + nVarRectWidth+nVarRectWidth/2- 4)
        }
        currentRectLeft = nVarRectLefts[j];
        console.log("--boxMethodMultiBoxUnlimitedRender() end loop currentRectLeft:"+currentRectLeft+" j:"+j);
    }
    svgText (totalTextX, rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    var boxOpacity = 0.2;
    var strokeWidth = 2;
    var nVarFillColour = ROD_COLOURS.WHITE;
    if (part2_val<=10) {
        nVarFillColour = getRodColour(part2_val);
    }
    for (var k=0; k<nVarValues.length; k++){
        console.log("--boxMethodMultiBoxUnlimitedRender() k:"+k);
        svgFilledRect (nVarRectLefts[k], rodY, nVarRectWidth, Y_MULTIPLIER, nVarFillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
        svgText (nVarTextLefts[k], rodTextLevel, part2Text, SVG_TEXT_STANDARD_SIZE);
    }
    svgFilledRect (nVarRectLefts[0], rodY+Y_MULTIPLIER, nVarRectWidth, Y_MULTIPLIER, nVarFillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
    svgText (nVarTextLefts[0], rodTextLevel+Y_MULTIPLIER, part2Text, SVG_TEXT_STANDARD_SIZE);

    svgRuledLine(totalRuledLineLeftX, rodTotalLevel+10, totalRuledLineXend, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(totalRuledLineLArrowHeadX, rodTotalLevel+10, 270);
    svgArrowHead(totalRuledLineRArrowHeadX, rodTotalLevel+10, 90);



}

function boxMethodMultiBoxDivisionUnlimitedRender(lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, part1Text, part2_val, part2Text, rodY, maxTotal) {
    console.log(">>boxMethodMultiBoxDivisionUnlimitedRender()");
    var nVarLefts = [];
    var nVarTextLefts = [];
    var nVarRectLefts = [];
    var proportionalMultiplier = BOX_METHOD_MAX_N_WIDTH / total;
    var answer =  part1_val/part2_val;
    var nVarRectWidth = answer * X_MULTIPLIER*proportionalMultiplier;
    var totalTextX = lMargin+(total * X_MULTIPLIER / 2)*proportionalMultiplier;
    var totalRuledLineLeftX = lMargin;
    var totalRuledLineXend = lMargin+((total * X_MULTIPLIER)*proportionalMultiplier);
    var totalRuledLineLArrowHeadX = (lMargin + 2);
    var totalRuledLineRArrowHeadX = lMargin + ((total * X_MULTIPLIER)-4)*proportionalMultiplier;
    var currentRectLeft = lMargin;
    console.log("--boxMethodMultiBoxDivisionUnlimitedRender() currentRectLeft:"+currentRectLeft);
    for(var j=0; j<part2_val; j++){
        if (j===0){
            nVarRectLefts.push(currentRectLeft);
            nVarTextLefts.push(currentRectLeft+nVarRectWidth/2 - 4);
        }
        else {
            nVarRectLefts.push (currentRectLeft + nVarRectWidth);
            nVarTextLefts.push(currentRectLeft + nVarRectWidth+nVarRectWidth/2- 4)
        }
        currentRectLeft = nVarRectLefts[j];
        console.log("--boxMethodMultiBoxDivisionUnlimitedRender() end loop currentRectLeft:"+currentRectLeft+" j:"+j);
    }

    svgText (totalTextX, rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);

    var boxOpacity = 0.2;
    var strokeWidth = 2;
    var nVarFillColour = ROD_COLOURS.WHITE;
    if (answer<=10) {
        nVarFillColour = getRodColour(answer);
    }
    for (var k=0; k<part2_val; k++){
        console.log("--boxMethodMultiBoxDivisionUnlimitedRender() k:"+k);
        svgFilledRect (nVarRectLefts[k], rodY, nVarRectWidth, Y_MULTIPLIER, nVarFillColour, boxOpacity, strokeWidth, DARK_DARK_GREY);
        svgText (nVarTextLefts[k], rodTextLevel, "?", SVG_TEXT_STANDARD_SIZE);
    }

    svgRuledLine(totalRuledLineLeftX, rodTotalLevel+10, totalRuledLineXend, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(totalRuledLineLArrowHeadX, rodTotalLevel+10, 270);
    svgArrowHead(totalRuledLineRArrowHeadX, rodTotalLevel+10, 90);
}

function svgBoxMethodNamedAdditionSubtraction() {
    console.log(">>svgBoxMethodNamedAdditionSubtraction()");
    var snapsvg = Snap ("#snapsvg");
    snapsvg.clear();
    var partTypes = equationModerator.partTypes[equationModerator.currentIndex];
    var numVariables = equationModerator.numVariables;
    var nameArray = equationModerator.partNames[equationModerator.currentIndex];
    var valueArray = equationModerator.partValues[equationModerator.currentIndex];
    var total = equationModerator.totals[equationModerator.currentIndex];
    var answer = equationModerator.answers[equationModerator.currentIndex];
    console.log("--svgBoxMethodNamedAdditionSubtraction() valueArray:"+valueArray+" total:"+total+" numVariables:"+numVariables+" partTypes:"+partTypes+" nameArray:"+nameArray)
    var maxTotal = 0;
    var p2RodXLeft=0;
    var p1RodXLeft=0;
    var p3RodXLeft=0;
    var part1_val = 0;
    var part2_val = 0;
    var part3_val = 0;
    var total_val = 0;
    var rodY = 2 * Y_MULTIPLIER;
    var rodTextLevel = (rodY)+(Y_MULTIPLIER/2)+10;
    var rodTotalLevel = (rodY)-(Y_MULTIPLIER/2);
    var totalText="";
    var part1Text = "";
    var part2Text = "";
    var part3Text = "";
    var lMargin = X_MULTIPLIER;
    for (var i = 0; i < equationModerator.totals.length; i++) {
        if (i === 0) {
            maxTotal = equationModerator.totals[i];
        }
        if (equationModerator.totals[i] > maxTotal) {
            maxTotal = equationModerator.totals[i];
        }
    }
    if (maxTotal<=10) {
        if (numVariables.toString () === '2') {
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CC) {
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    totalText = "?";
                    part1Text = part1_val.toString ();
                    part2Text = part2_val.toString ();
                }
                else if (categoryName === CATEGORY_SUBTRACTION) {
                    totalText = getIntOrFloatFromInput (valueArray[0]);
                    part1_val = getIntOrFloatFromInput (valueArray[1]);
                    part2_val = getIntOrFloatFromInput (answer);
                    part1Text = part1_val.toString ();
                    part2Text = "?";
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_UC){
                if (categoryName === CATEGORY_ADDITION) {
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    part1_val = getIntOrFloatFromInput (answer);
                    totalText = total.toString ();
                    part1Text = "?";
                    part2Text = part2_val.toString ();
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CU){
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (answer);
                    totalText = total.toString ();
                    part1Text = part1_val.toString ();
                    part2Text = "?";
                }
            }
            drawNamesBoxMethod2Vars(p2RodXLeft, lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, rodY, part2_val );
        }
        else if (numVariables.toString () === '3'){
            console.log("partTypes:"+partTypes+" categoryName:"+categoryName)
            if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CCC) {
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    part3_val = getIntOrFloatFromInput (valueArray[2]);
                    totalText = "?";
                    part1Text = part1_val.toString ();
                    part2Text = part2_val.toString ();
                    part3Text = part3_val.toString ();
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_UCC){
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (answer);
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    part3_val = getIntOrFloatFromInput (valueArray[2]);
                    totalText = total.toString ();
                    part1Text = "?";
                    part2Text = part2_val.toString ();
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CUC){
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (answer);
                    part3_val = getIntOrFloatFromInput (valueArray[2]);
                    totalText = total.toString ();
                    part1Text = part1_val.toString ();
                    part2Text = "?";
                }
            }
            else if (partTypes === BOX_METHOD_ADDSUB_VAL_TYPES_CCU){
                if (categoryName === CATEGORY_ADDITION) {
                    part1_val = getIntOrFloatFromInput (valueArray[0]);
                    part2_val = getIntOrFloatFromInput (valueArray[1]);
                    part3_val = getIntOrFloatFromInput (answer);
                    totalText = total.toString ();
                    part1Text = part1_val.toString ();
                    part2Text = "?";
                }
            }
            drawNamesBoxMethod3Vars (part1_val, part2_val, rodTotalLevel, totalText, rodTextLevel, part1Text, part3_val, part3Text);

        }
    }
    else {
        if (numVariables.toString () === '2') {
            console.log("2");
        }
        else if (numVariables.toString () === '3'){
            console.log("3");
        }
    }
}

function drawNamesBoxMethod2Vars(p2RodXLeft, lMargin, part1_val, total, rodTotalLevel, totalText, rodTextLevel, rodY, part2_val ){
    var p2RodXLeft = lMargin+(X_MULTIPLIER*part1_val);
    svgText (lMargin+(total*X_MULTIPLIER/2), rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER/2), rodTextLevel , part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER)+(part2_val*X_MULTIPLIER/2), rodTextLevel , part2Text, SVG_TEXT_STANDARD_SIZE);

    svgCusineerRod(lMargin, rodY, X_MULTIPLIER, Y_MULTIPLIER, part1_val, getRodColour(part1_val), 0.2, 2, LIGHT_GREY);
    svgCusineerRod(p2RodXLeft, rodY, X_MULTIPLIER, Y_MULTIPLIER, part2_val, getRodColour(part2_val), 0.2, 2, LIGHT_GREY);
    svgRect(lMargin, rodY, part1_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRect(p2RodXLeft, rodY, part2_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRuledLine(lMargin, rodTotalLevel+10, lMargin+(total*X_MULTIPLIER)-10, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(lMargin+2, rodTotalLevel+10, 270);
    svgArrowHead( lMargin+(total*X_MULTIPLIER)-12, rodTotalLevel+10, 90);

}

function drawNamesBoxMethod3Vars(part1_val, part2_val, rodTotalLevel, totalText, rodTextLevel, part1Text, part3_val, part3Text){
    var p2RodXLeft = lMargin+(X_MULTIPLIER*part1_val);
    var p3RodXLeft = lMargin+(X_MULTIPLIER*part1_val)+(X_MULTIPLIER*part2_val);
    svgText (lMargin+(total*X_MULTIPLIER/2), rodTotalLevel, totalText, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER/2), rodTextLevel , part1Text, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER)+(part2_val*X_MULTIPLIER/2), rodTextLevel , part2Text, SVG_TEXT_STANDARD_SIZE);
    svgText (lMargin+(part1_val*X_MULTIPLIER)+(part2_val*X_MULTIPLIER)+(part3_val*X_MULTIPLIER/2), rodTextLevel , part3Text, SVG_TEXT_STANDARD_SIZE);
    svgRect(lMargin, rodY, part1_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRect(p2RodXLeft, rodY, part2_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRect(p3RodXLeft, rodY, part3_val*X_MULTIPLIER, Y_MULTIPLIER, DARK_DARK_GREY);
    svgRuledLine(lMargin, rodTotalLevel+10, lMargin+(total*X_MULTIPLIER)-10, rodTotalLevel+10, MEDIUM_GREY, 2);
    svgArrowHead(lMargin+2, rodTotalLevel+10, 270);
    svgArrowHead( lMargin+(total*X_MULTIPLIER)-12, rodTotalLevel+10, 90);
}



function svgRocketOnPath(){

// ---------
//  SVG C
// ---------

    var snapC = Snap("#snapsvg");
    snapC.clear();

    // SVG C - "Squiggly" Path
    var myPathC = snapC.path("M62.9 14.9c-25-7.74-56.6 4.8-60.4 24.3-3.73 19.6 21.6 35 39.6 37.6 42.8 6.2 72.9-53.4 116-58.9 65-18.2 191 101 215 28.8 5-16.7-7-49.1-34-44-34 11.5-31 46.5-14 69.3 9.38 12.6 24.2 20.6 39.8 22.9 91.4 9.05 102-98.9 176-86.7 18.8 3.81 33 17.3 36.7 34.6 2.01 10.2.124 21.1-5.18 30.1").attr({
        id: "squiggle",
        fill: "none",
        strokeWidth: "4",
        stroke: "#ddff00",
        strokeMiterLimit: "10",
        strokeDasharray: "9 9",
        strokeDashOffset: "988.01"
    });

    // SVG C - Draw Path
    var lenC = myPathC.getTotalLength();

    // SVG C - Animate Path
    myPathC.attr({
        stroke: '#eef',
        strokeWidth: 4,
        fill: 'none',
        // Draw Path
        "stroke-dasharray": "12 6",
        "stroke-dashoffset": "180"
    }).animate({"stroke-dashoffset": 10}, 4500,mina.easeinout);

    var rocketPath = snapC.path("M42.7,48.1c3.7-5.6,7.6-10.3,11.3-13.7L65,41.7c-1.7,4.7-4.5,10.2-8.2,15.7"+
    "c-2.4,3.6-4.9,6.8-7.3,9.6l0.2,13.2l-9.1,13.7l0-19c-0.4,0.3-0.9,0.5-1.3,0.7l-6.7-4.5c0-0.6,0.1-1.2,"+
        "0.3-1.9L15,77l9.1-13.7l12.8-5.2C38.4,54.9,40.4,51.5,42.7,48.1z M65,41.7l8.2-24.7L53.9,34.4l0,0").attr({
        id: "rocket",
        fill: "#34495e"
    });

    var rocketGroup = snapC.g( rocketPath ); // Group polyline

    var movePoint;
    setTimeout( function() {
        Snap.animate(0, lenC, function( value ) {
            movePoint = myPathC.getPointAtLength( value );
            rocketGroup.transform( 't' + parseInt(movePoint.x - 15) + ',' + parseInt( movePoint.y - 15) + 'r' + (movePoint.alpha - 90));
        }, 4500,mina.easeinout);
    });
}



var clickFunc = function (){
    var value = this.data('value');
    console.log("clicked: "+value);
    replaceAnswer(value);
}

function circleAnimation(svgCircle, radiusStart, radiusStop, colorStart, colorStop){
    svgCircle.animate({r: radiusStart}, 1000);
    svgCircle.stop().animate(
        {fill: colorStart, r: radiusStart}, 1000,
        function(){
            svgCircle.attr({fill: colorStop, r: radiusStop}, 1000); //reset
        }
    );

}

function rectAnimation(x, y, width, height, strokeColorStart, strokeColorStop){
    var snapsvg = Snap ("#snapsvg");
    var rect = snapsvg.rect(x, y, width, height);
    rect.attr({fillOpacity: 0});
    rect.animate({stroke: strokeColorStart, strokeOpacity: 0}, 1000,
        function(){
            rect.attr({stroke: strokeColorStop, strokeOpacity: 1}, 1000);
        }
    );

}

/*
// SVG C - Triangle (As Polyline)
var Triangle = snapC.polyline("0, 30, 15, 0, 30, 30");
Triangle.attr({
    id: "plane",
    fill: "#fff"
});

initTriangle();

// Initialize Triangle on Path
function initTriangle(){
    var triangleGroup = snapC.g( Triangle ); // Group polyline
    movePoint = myPathC.getPointAtLength(length);
    triangleGroup.transform( 't' + parseInt(movePoint.x - 15) + ',' + parseInt( movePoint.y - 15) + 'r' + (movePoint.alpha - 90));
}

// SVG C - Draw Path
var lenC = myPathC.getTotalLength();

// SVG C - Animate Path
function animateSVG() {
    myPathC.attr({
        stroke: '#fff',
        strokeWidth: 4,
        fill: 'none',
        // Draw Path
        "stroke-dasharray": "12 6",
        "stroke-dashoffset": "180"
    }).animate({"stroke-dashoffset": 10}, 4500,mina.easeinout);

    var triangleGroup = snapC.g( Triangle ); // Group polyline

    setTimeout( function() {
        Snap.animate(0, lenC, function( value ) {
            movePoint = myPathC.getPointAtLength( value );
            triangleGroup.transform( 't' + parseInt(movePoint.x - 15) + ',' + parseInt( movePoint.y - 15) + 'r' + (movePoint.alpha - 90));

        }, 4500,mina.easeinout, function(){
            alertEnd();
        });
    });
}

*/


function funChunkTwoValAdditionDrawing(linePositions, jumpValues){
    if (linePositions.length > 0 )
    {
        clearSvg ();


        var jump0, jump1;
        jump0 = getIntOrFloatFromInput(jumpValues[0]);
        jump1 = getIntOrFloatFromInput(jumpValues[1]);
        var longestJump = jump0 + jump1;
        if (jump0>longestJump){
            longestJump=jump0;
        }
        else if (jump1>longestJump){
            longestJump=jump1;
        }

        var firstPos = linePositions[0].toString ();
        var firstPosValue = getIntOrFloatFromInput(firstPos);
        svgPoint (X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
        svgText (X_MULTIPLIER*X_POINT_START, (LINE_Y_1+10)+Y_POINT_TEXT_OFFSET, firstPos);
        for (var i=1; i<=longestJump; i++){
            svgPoint((i+X_POINT_START), LINE_Y_1, LIGHT_GREY);
        }
        svgRuledLine (X_MULTIPLIER, LINE_Y_1, X_MULTIPLIER*FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, DARK_DARK_GREY, 3);
        svgArrowHead (X_MULTIPLIER, LINE_Y_1, 270);
        svgArrowHead (X_MULTIPLIER * FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, 90);
        console.log ("<<funChunkAdditionDrawing()");
    }
}

function funChunkTwoValAdditionHint1(jumpValues){
    var jump0, jump1;
    jump0 = getIntOrFloatFromInput(jumpValues[0]);
    jump1 = getIntOrFloatFromInput(jumpValues[1]);
    var jump0Operator = "";
    var jump1Operator = "";
    if (jump0 > 0){
        jump0Operator = "+";
    }
    if (jump1 > 0){
        jump1Operator = "+";
    }
    svgPath(X_MULTIPLIER*X_POINT_START, LINE_Y_1, X_MULTIPLIER*(X_POINT_START+jump0/2), LINE_Y_0, X_MULTIPLIER*(jump0+X_POINT_START), LINE_Y_1);
    svgPath(X_MULTIPLIER*(jump0+X_POINT_START), LINE_Y_1, X_MULTIPLIER*(jump0+X_POINT_START+(jump1/2)), LINE_Y_0, X_MULTIPLIER*(jump0+X_POINT_START+jump1), LINE_Y_1);
    svgPoint(jump0+X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    svgPoint(jump0+jump1+X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    var operatorStr = "+";
    if (strategyName === STRATEGY_FRIENDLY_AND_FIX) {
        operatorStr = "";
    }
    svgText(X_MULTIPLIER*(X_POINT_START+jump0/2), LINE_Y_0+Y_POINT_TEXT_OFFSET, jump0Operator+jump0);
    svgText(X_MULTIPLIER*(jump0+X_POINT_START+(jump1/2)), LINE_Y_0+Y_POINT_TEXT_OFFSET, jump1Operator+jump1);
}

function funChunkTwoValSubtractionDrawing(linePositions, jumpValues){
    console.log(">>funChunkTwoValSubtractionDrawing() linePositions:"+linePositions+" jumpValues:"+jumpValues);
    clearSvg();
    var jump0, jump1;
    jump0 = getIntOrFloatFromInput(jumpValues[0]);
    jump1 = getIntOrFloatFromInput(jumpValues[1]);
    var longestJump = jump0 + jump1;
    if (jump0<longestJump){
        longestJump=jump0;
    }
    else if (jump1<longestJump){
        longestJump=jump1;
    }
    var jumpSteps = Math.abs(longestJump);
    for (var i=1; i<=jumpSteps; i++){
        svgPoint((FUN_CHUNKS_LINE_LENGTH-X_POINT_START-i), LINE_Y_1, LIGHT_GREY);
    }
    svgRuledLine(X_MULTIPLIER, LINE_Y_1, X_MULTIPLIER*FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, DARK_DARK_GREY, 3);
    var firstPos = linePositions[0].toString();
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    svgText(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START), LINE_Y_1+Y_POINT_TEXT_OFFSET, firstPos);
    svgArrowHead(X_MULTIPLIER, LINE_Y_1, 270);
    svgArrowHead(X_MULTIPLIER*FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, 90);
}

function funChunkTwoValSubtractionHint1(jumpValues){
    console.log(">>funChunkTwoValSubtractionHint1() jumpValues:"+jumpValues);
    var jump0, jump1;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    svgPath(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START), LINE_Y_1, X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0/2), LINE_Y_0, X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0), LINE_Y_1);
    svgPath(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0), LINE_Y_1, X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+(jump1/2)), LINE_Y_0, X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1), LINE_Y_1);
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0, LINE_Y_1, DARK_DARK_GREY);
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1, LINE_Y_1, DARK_DARK_GREY);
    svgText(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0/2), LINE_Y_0+Y_POINT_TEXT_OFFSET, jump0);
    svgText(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+(jump1/2)), LINE_Y_0+Y_POINT_TEXT_OFFSET, jump1);
}

function funChunkTwoValAdditionSolution(linePositions, jumpValues){
    console.log(">>funChunkTwoValAdditionSolution() linePositions:"+linePositions+" jumpValues:"+jumpValues);
    clearSvg();
    funChunkTwoValAdditionDrawing(linePositions, jumpValues);
    funChunkTwoValAdditionHint1(jumpValues);
    var jump0, jump1;
    var secondPos, lastPos;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    if (linePositions.length === 3){
        secondPos = linePositions[1].toString();
        lastPos = linePositions[2].toString();
    }
    else {
        console.log("Error in linePositions array length");
    }
    svgText(X_MULTIPLIER*(jump0+X_POINT_START), LINE_Y_1+10+Y_POINT_TEXT_OFFSET, secondPos);
    svgText(X_MULTIPLIER*(jump0+jump1+X_POINT_START), LINE_Y_1+10+Y_POINT_TEXT_OFFSET, lastPos);
}

function funChunkTwoValSubtractionSolution(linePositions, jumpValues){
    clearSvg();
    funChunkTwoValSubtractionDrawing(linePositions, jumpValues);
    funChunkTwoValSubtractionHint1(jumpValues);
    var jump0, jump1;
    var secondPos, lastPos;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    if (linePositions.length === 3){
        secondPos = linePositions[1].toString();
        lastPos = linePositions[2].toString();
    }
    else {
        console.log("Error in linePositions array length");
    }
    svgText(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0), LINE_Y_1+Y_POINT_TEXT_OFFSET, secondPos);
    svgText(X_MULTIPLIER*(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1), LINE_Y_1+Y_POINT_TEXT_OFFSET, lastPos);
}

function getRodColour(numberColoured){
    var fillColour;
    switch(numberColoured) {
        case 0:
            fillColour = ROD_COLOURS.WHITE;
            break;
        case 1:
            fillColour = ROD_COLOURS.WHITE;
            break;
        case 2:
            fillColour = ROD_COLOURS.RED;
            break;
        case 3:
            fillColour = ROD_COLOURS.LIGHT_GREEN;
            break;
        case 4:
            fillColour = ROD_COLOURS.PURPLE;
            break;
        case 5:
            fillColour = ROD_COLOURS.YELLOW;
            break;
        case 6:
            fillColour = ROD_COLOURS.DARK_GREEN;
            break;
        case 7:
            fillColour = ROD_COLOURS.BLACK;
            break;
        case 8:
            fillColour = ROD_COLOURS.BROWN;
            break;
        case 9:
            fillColour = ROD_COLOURS.BLUE;
            break;
        case 10:
            fillColour = ROD_COLOURS.ORANGE;
            break;
    }
    return fillColour;
}

function svgCusineerRod(xPosition, yPosition, width, height, numberColoured, fillColour, rodOpacity, strokeWidth, strokeColour){
    console.log(">>svgCusineerRod xPosition:"+xPosition+" yPosition:"+yPosition+" width:"+ width+" height:"+height+" numberColoured:"+ numberColoured+" fillColour:"+ fillColour+" rodOpacity:"+ rodOpacity+" strokeWidth:"+ strokeWidth+" strokeColour:"+ strokeColour);
    var s = Snap("#snapsvg")
    var colouredBlocks = [];
    for (var i=0; i<numberColoured; i++){
        svgFilledRect(xPosition+(width*i), yPosition, width, height, fillColour, rodOpacity, strokeWidth, strokeColour);
        colouredBlocks.push(svgFilledRect);
    }
}

function svgFilledRect(xPosition, yPosition, width, height, fillColour, rectOpacity, strokeWidth, strokeColour){
    var s = Snap("#snapsvg");
    var block = s.paper.rect(xPosition, yPosition, width, height);
    block.attr({
        fill: fillColour,
        stroke: strokeColour,
        strokeWidth: strokeWidth,
        fillOpacity: rectOpacity
    });
}

function clearSvg(){
    var s = Snap("#snapsvg");
    s.clear();
    var sresult = Snap("#svg_result");
    sresult.clear();
}

function displayStatus(statusFlag){
    console.log(">>displayStatus() statusFlag:"+statusFlag);
    var s = Snap("#svg_result");
    var resultText;
    var colour;
    if (statusFlag === true){
        //tick
        resultText = String.fromCharCode( 10004 );
        colour = 'green';
    }
    else {
        //cross
        resultText =String.fromCharCode( 10006 );
        colour = 'red';
    }
    var svgTextElement = s.text(20,32, resultText).attr({ fontSize: '48px', "text-anchor": "middle" , fill: colour});

}




function updateProgress(){
    var index = equationModerator.currentIndex;
    if (totalQuestions !== 0)
    {
        console.log("--updateProgress() index: "+index+" totalQuestions: "+totalQuestions)
        if (equationModerator.sessionFinished === true) {
            var progressValue = 1;
        }
        else {
            var progressValue = index / totalQuestions;
        }
        var progressIntValue = Math.round( progressValue * 100 );
        var progressPercent = (progressIntValue ).toString()+"%";
        var d = document.getElementById("qq-progress");
        if (progressIntValue <= 50) {
            d.className = "progress-bar progress-bar-info";
        }
        else if (progressIntValue <= 80) {
            d.className = "progress-bar progress-bar-success";
        }
        else if (progressIntValue <= 90) {
            d.className = "progress-bar progress-bar-warning";
        }
        else {
            d.className = "progress-bar progress-bar-danger";
        }
        d.style.width= progressPercent;
        var progressText = document.getElementById("qq-progress-text");
        progressText.innerHTML = progressPercent + " done";
    }
}


/*Events*/
function ignoreKeyIfTooLong(){
    var ignore = false;
    var givenAnswersLength = equationModerator.givenAnswers.length;
    console.log("--ignoreKeyIfTooLong() givenAnswersLength "+givenAnswersLength+" equationModerator.currentIndex"+equationModerator.currentIndex)
    if (givenAnswersLength > equationModerator.currentIndex) {
        if (equationModerator.givenAnswers[equationModerator.currentIndex].length >= equationModerator.answers[equationModerator.currentIndex].length) {
            ignore = true;
        }
        else {
            ignore = false;
        }
    }
    return ignore;
}


function checkKeyPressed(ev) {
    if (keyinputEnabled) {
        var keyCode = ev.keyCode;
        console.log ("--checkKeyPressed() key: " + keyCode);
        var charStr = String.fromCharCode (keyCode);
        if (isNaN (charStr) || charStr == " ") {
            console.log ("--checkKeyPressed() isNaN (charStr) || charStr == ");

            if (answerFormat == "negative_positive_int" || answerFormat == "negative_positive_float") {
                //subtract
                if (charStr == '-' || keyCode == 173) {
                    if (equationModerator.givenAnswers.length > equationModerator.currentIndex) {
                        var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
                        if (givenAnswer.length == 0) {
                            processKey (charStr);

                        }
                    }
                }
            }
            //backspace or delete
            if (keyCode == 8 || keyCode == 46) {
                console.log ("--checkKeyPressed back/del givenanslen: " + equationModerator.givenAnswers.length + " index:" + equationModerator.currentIndex)
                if (equationModerator.givenAnswers.length > equationModerator.currentIndex) {
                    var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
                    console.log ("--checkKeyPressed givenAnswer: " + givenAnswer + " currentIndex: " + equationModerator.currentIndex);
                    if (givenAnswer.length > 0) {
                        equationModerator.givenAnswers[equationModerator.currentIndex] = givenAnswer.substr (0, givenAnswer.length - 1);
                        forceUpdateAnswerElement (equationModerator.givenAnswers[equationModerator.currentIndex]);
                        ev.preventDefault ();
                    }
                }
                else {
                    console.log (" answers length:" + equationModerator.givenAnswers.length + " index: " + equationModerator.currentIndex);
                }
            }
            //space
            else if (charStr == ' ') {
                ev.preventDefault ();
            }

            //numpad
            else if (keyCode >= 96 && keyCode <= 105) {
                console.log ("numpad " + keyCode)
                if (ignoreKeyIfTooLong () === true) {
                    ev.preventDefault ();
                    return;
                }
                else {
                    processKey (String.fromCharCode ((96 <= keyCode && keyCode <= 105) ? keyCode - 48 : keyCode));
                }

            }
            else {
                // prevent default behaviour
                ev.preventDefault ();
                return false;
            }
        }
        //tab, enter
        else if (keyCode == 9 || keyCode == 13) {
            if (isGivenAnsLenSufficient () === true) {
                submitAnswer ();
            }
            ev.preventDefault ();
        }
        else {
            //is a number
            if (ignoreKeyIfTooLong () === true) {
                console.log ("--checkKeyPressed() ignoreKeyIfTooLong () === true ");
                ev.preventDefault ();
                return;
            }
            else {
                processKey (charStr);
            }
        }
        if (equationModerator.currentIndex >= totalQuestions) {
            wrapUpSession ();
        }
        else {
            isGivenAnsLenSufficient ();
        }
    }
}

function processKey(keyString) {
    console.log(">>processKey() key:"+keyString);
    appendAnswer(keyString);
}



/*
 function addHelpListener() {
 var helpSVG = document.getElementById ("svg_help");
 if (helpSVG.addEventListener) {
 helpSVG.addEventListener ("click", showHelpDialog, false);
 }
 else if (helpSVG.attachEvent) {
 helpSVG.attachEvent ('onclick', showHelpDialog);
 }
 else {
 helpSVG.onclick = showHelpialog;
 helpSVG.click = showHelpDialog;
 }
 }
 */

function submitAnswer(){
    console.log(">>submitAnswer()");
    var submitButton = document.getElementById("submit_button");
    if (submitButton.text.toUpperCase().trim() === 'Submit'.toUpperCase().trim())
    {
        if ((checkAnswer() === 'Correct')||(checkAnswer() === 'Incorrect')) {
            console.log("--submitAnswer() Correct: "+submitButton.text.toUpperCase());
            changeSubmitButtonToNext();
        }
    }
    else if (submitButton.text.toUpperCase().trim() === 'Finish'.toUpperCase().trim()){
        console.log("--submitAnswer() Finish: "+submitButton.text.toUpperCase());
        checkAnswer();
        moveToNextOrFinish();
    }
    else {
        console.log("--submitAnswer() Next: "+submitButton.text.toUpperCase());
        moveToNextOrFinish ();
    }
}

function addSubmitButtonListener(){
    console.log(">>addSubmitButtonListener");
    var submitButton = document.getElementById("submit_button");
    if (submitButton.addEventListener) {
        submitButton.addEventListener ("click", submitAnswer, false);
    }
    else if (submitButton.attachEvent) {
        submitButton.attachEvent ('onclick', submitAnswer);
    }
    else {
        submitButton.onclick = submitAnswer;
        submitButton.click = submitAnswer;
    }
}



function addHintButtonListener(){
    console.log(">>addHintButtonListener");
    var hintButton = document.getElementById("hint_button");
    if (hintButton.addEventListener) {

        hintButton.addEventListener ("click", showHint, false);
    }
    else if (hintButton.attachEvent) {
        hintButton.attachEvent ('onclick', showHint);
    }
    else {
        hintButton.onclick = showHint;
        hintButton.click = showHint;
    }
}

function changeSubmitButtonToSubmit(){
    var d = document.getElementById("submit_button");
    d.innerHTML = "Submit";
    d.className = "btn btn-default";
}

function changeSubmitButtonToNext(){
    var d = document.getElementById("submit_button");
    d.className = "btn btn-info";
    d.innerHTML = 'Next'+'&nbsp;'+'&nbsp;'+'&nbsp;';
}


function updateSubmitButtonStatus(validLength){
    console.log(">>updateSubmitButtonStatus() validLength:"+validLength);
    var d = document.getElementById("submit_button");
    if (validLength) {
        console.log(">>updateSubmitButtonStatus() validLength:"+validLength);
        d.className = "btn btn-success";
    }
    else {
        d.className = "btn btn-default";
    }
}

function changeSubmitButtonToFinish(){
    console.log(">>changeSubmitButtonToFinish()");
    var d = document.getElementById("submit_button");
    d.innerHTML = 'Finish'+'&nbsp;'+'&nbsp;';
}

function showHint(){
    var index = equationModerator.currentIndex;
    console.log("--showHint index: "+index+" hints: "+equationModerator.hints);
    if (!isInArray(index, equationModerator.hints)){
        //only add if not alredy pressed hint for this qq
        console.log("pushing "+index);
        equationModerator.hints.push(index);
    }
    if  ((strategyName === STRATEGY_FUN_CHUNKS) || (strategyName === STRATEGY_FRIENDLY_AND_FIX)) {
        if (activityNumVariables.toString()==='2')
        {
            assert(equationModerator.jumpValues.length.toString()===(2*totalQuestions).toString(), 'assert jumps length is twice question length');
            var linePosArray = equationModerator.linePositions.slice(index*3, index*3+3);
            var jumpValsArray = equationModerator.jumpValues.slice(index*2, index*2+2);
            if (categoryName === CATEGORY_ADDITION){
                funChunkTwoValAdditionHint1(jumpValsArray);
            }
            else if (categoryName === CATEGORY_SUBTRACTION){
                funChunkTwoValSubtractionHint1(jumpValsArray);
            }
        }
    }
    else if (strategyName === STRATEGY_NUMBER_BONDS){
        if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER){
            if (strategyQualifier === STRATEGY_QUALIFIER_COUNTER){
                svgNumberBondsCounterHint();
            }
        }
        else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART) {
            svgNumberBondsPartPartWhole(true);
        }
    }

    else if (strategyName === STRATEGY_BOX_METHOD && strategyQualifier === STRATEGY_QUALIFIER_BASIC_NAMED_MULTIPLICATION){
        var questionText = equationModerator.questions[equationModerator.currentIndex];
        displayQuestion(questionText);
    }
}

function showHelp(){
    equationModerator.helps.push(currentIndex);
    console.log("TODO showHelp")
}

function addButtonListeners(){
    console.log(">>addButtonListeners");

    addSubmitButtonListener();
    addHintButtonListener();
    //addHelpListener();
}

/*Event Utils*/
//WROX Professional JavaScript for Web Developers utility source code
var eventUtil = {

    addHandler: function(element, type, handler){
        if (element.addEventListener){
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent){
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;
        }
    },

    getButton: function(event){
        if (document.implementation.hasFeature("MouseEvents", "2.0")){
            return event.button;
        } else {
            switch(event.button){
                case 0:
                case 1:
                case 3:
                case 5:
                case 7:
                    return 0;
                case 2:
                case 6:
                    return 2;
                case 4: return 1;
            }
        }
    },

    getCharCode: function(event){
        if (typeof event.charCode == "number"){
            return event.charCode;
        } else {
            return event.keyCode;
        }
    },

    getClipboardText: function(event){
        var clipboardData =  (event.clipboardData || window.clipboardData);
        return clipboardData.getData("text");
    },

    getEvent: function(event){
        return event ? event : window.event;
    },

    getRelatedTarget: function(event){
        if (event.relatedTarget){
            return event.relatedTarget;
        } else if (event.toElement){
            return event.toElement;
        } else if (event.fromElement){
            return event.fromElement;
        } else {
            return null;
        }

    },

    getTarget: function(event){
        return event.target || event.srcElement;
    },

    getWheelDelta: function(event){
        if (event.wheelDelta){
            return (client.engine.opera && client.engine.opera < 9.5 ? -event.wheelDelta : event.wheelDelta);
        } else {
            return -event.detail * 40;
        }
    },

    preventDefault: function(event){
        if (event.preventDefault){
            event.preventDefault();
        } else {
            event.returnValue = false;
        }
    },

    removeHandler: function(element, type, handler){
        if (element.removeEventListener){
            element.removeEventListener(type, handler, false);
        } else if (element.detachEvent){
            element.detachEvent("on" + type, handler);
        } else {
            element["on" + type] = null;
        }
    },

    setClipboardText: function(event, value){
        if (event.clipboardData){
            event.clipboardData.setData("text/plain", value);
        } else if (window.clipboardData){
            window.clipboardData.setData("text", value);
        }
    },

    stopPropagation: function(event){
        if (event.stopPropagation){
            event.stopPropagation();
        } else {
            event.cancelBubble = true;
        }
    }

};

/*Utils*/

function isInArray(value, array) {
    return array.indexOf(value) > -1;
}

function getIntOrFloatFromInput(inItem){
    var outValue = null;
    if (isInteger(inItem)){
        outValue = parseInt(inItem);
    }
    else if (isFloat(inItem)){
        outValue = parseFloat(inItem);
    }
    return outValue;
}


function calcCounterTextXShift(printedAnswer){
    var textXShift = 40;
    if (printedAnswer.length === 2){
        textXShift = 34;
    }
    else if (printedAnswer.length === 3){
        textXShift = 24;
    }
    else if (printedAnswer.length === 4){
        textXShift = 18;
    }
    else if (printedAnswer.length > 4){
        textXShift = 12;
    }
    return textXShift;
}

var pojo = function () {
    var members = arguments;

    return function () {
        var obj = {}, i = 0, j = members.length;
        for (; i < j; ++i) {
            obj[members[i]] = arguments[i];
        }

        return obj;
    };
};

//Gets the browser window size
//Returns object with height and width properties
//see nvd3 utils.js
var windowSize = function() {
    // Sane defaults
    var size = {width: 640, height: 480};

    // Most recent browsers use
    if (window.innerWidth && window.innerHeight) {
        size.width = window.innerWidth;
        size.height = window.innerHeight;
        return (size);
    }

    // IE can use depending on mode it is in
    if (document.compatMode=='CSS1Compat' &&
        document.documentElement &&
        document.documentElement.offsetWidth ) {

        size.width = document.documentElement.offsetWidth;
        size.height = document.documentElement.offsetHeight;
        return (size);
    }

    // Earlier IE uses Doc.body
    if (document.body && document.body.offsetWidth) {
        size.width = document.body.offsetWidth;
        size.height = document.body.offsetHeight;
        return (size);
    }

    return (size);
};

//works OK,  better version of JS typeof operator
function type(val){
    return Object.prototype.toString.call(val).replace(/^\[object (.+)\]$/,"$1").toLowerCase();
}

function assert(outcome, description) {
    //see bookmarks js/testing
    var li = outcome ? 'pass' : 'fail';
    if (li == 'fail') {
        console.log('FAIL: '+description);
    }
    else {
        console.log('PASS: '+description);
    }
}

function removeAllWhitespaces(paramStr){
    console.log(">>removeAllWhitespaces() paramStr:"+paramStr);
    var outStr;
    if (paramStr) {
        outStr = paramStr.replace (/\s/g, '');
    }
    console.log(">>removeAllWhitespaces() outStr:"+outStr);
    return outStr;
}

function removeNonAlphanumericCharacters(paramStr){
    var outStr;
    if (paramStr) {
        outStr = paramStr.replace(/\W/g, '')
    }
    return outStr;
}

function fadeOut(elementId, speed) {
    var s = document.getElementById(elementId).style;
    s.opacity = 1;
    (function fade() {(s.opacity-=.1)<.1?s.display="none":setTimeout(fade,speed)})();
    //clearAnswer();
}

function strToInt(strVariable){
    console.log(">>strToInt type:"+type(strVariable));
    var converted;
    try {
        //tell JS is base 10
        converted = parseInt(strVariable, 10);
    }
    catch(err){
        console.log("--strToInt() "+err);
    }

    return converted;
}

function maxInArray(numberArray){
    return Math.max.apply(Math,numberArray);
}

//deprecated use lodash/underscore
function strListToIntList(strList){
    console.log(">>strListToIntList strList.length:"+strList.length);
    var converted = [];
    for (var i=0; i<strList.length; i++) {
        console.log(">>strListToIntList strList[i]:"+strList[i]);
        converted[i] = strToInt(strList[i]);
    }
    console.log(">>strToInt converted:"+converted);
    return converted;
}

function add(a, b) {
    return a + b;
}

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}



//Returns a random integer between min and max
//Using Math.round() will give you a non-uniform distribution!
function getRandomInt (min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomItemFromArray(items){
    var item = items[Math.floor(Math.random()*items.length)];
    return item;
}

function consolelogPropertyValues(paramObject){
    console.log(">>logPropertyValues")
    var keys = Object.keys(paramObject);
    for (var i = 0; i < keys.length; i++) {
        var val = paramObject[keys[i]];
        console.log("Key: "+keys[i]+" Value: "+val)
    }
}

function isFloat(value){
    if (value)
    {
        if (parseFloat (value).toString () === value.toString ()) {
            return true;
        }
    }
    return false;
}

function isFloat2(value){
    return (this % 1 != 0);
}

function isFloat3(n) {
    return n === +n && n !== (n|0);
}

function isInteger(n) {
    return n === +n && n === (n|0);
}

function concatArrays(arrToConvert){
    var newArr = [];
    for(var i = 0; i < arrToConvert.length; i++)
    {
        newArr = newArr.concat(arrToConvert[i]);
    }
    return newArr;
}

function getMaxStringLength(dataArray){
    var currentLen = 0;
    var maxLen = 0;
    for(var i=0;i<dataArray.length;i++){
        currentLen = dataArray[i].length;
        if (currentLen > maxLen){
            maxLen = currentLen;
        }
    }
    return maxLen
}

function isEven(n) {
    return n % 2 == 0;
}

function isMultipleOf(n, divisor) {
    return n % divisor == 0;
}

function isOdd(n) {
    return Math.abs(n % 2) == 1;
}

function listTo2DX3(inList){
    var twoDarray = [];
    if (inList && inList.length >0) {
        assert (isEven (inList.length), "listTo2D is even");
        assert (isMultipleOf (inList.length, 3), "is multiple of 3");
        twoDarray = create2DArray (inList.length / 3);
        var dimensions = [twoDarray.length, twoDarray[0].length];
        var first = true;
        for (var i = 0; i < inList.length; i++) {
            if (isMultipleOf (i, 3)) {
                twoDarray[i / 3].push (inList[i]);
                twoDarray[i / 3].push (inList[i + 1]);
                twoDarray[i / 3].push (inList[i + 2]);
            }
        }
        console.log (">>listTo2DX3() twoDarray:" + twoDarray);
    }
    return twoDarray;
}

function listTo2DX2(inList){
    var twoDarray = [];
    if (inList && inList.length >0) {
        assert(isEven(inList.length),"listTo2D is even");
        twoDarray = create2DArray (inList.length / 2);
        var dimensions = [twoDarray.length, twoDarray[0].length];
        var first = true;
        for (var i = 0; i < inList.length; i++) {
            if (isEven (i)) {
                twoDarray[i / 2].push (inList[i]);
                twoDarray[i / 2].push (inList[i + 1]);
            }
        }
        console.log (">>listTo2DX2() twoDarray:" + twoDarray);
    }
    return twoDarray;
}


function create2DArray(rows) {
    console.log(">>create2DArray() rows:"+rows);
    var arr = [];
    for (var i=0;i<rows;i++) {
        arr[i] = [];
    }
    console.log("--create2DArray() arr.length:"+arr.length);
    return arr;
}
/**
 * Randomize array element order in-place.
 * Using Durstenfeld shuffle algorithm.
 */
function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}


/*Mocha*/
if (typeof exports !== 'undefined') {
    module.exports.generateEquations = generateEquations;
    module.exports.generateTwoVariableEquations = generateTwoVariableEquations;
    module.exports.generateQuestionText = generateQuestionText;
    module.exports.dummyAdd = dummyAdd;
    module.exports.dummyRequirement = dummyRequirement;
    module.exports.assert = assert;
    module.exports.type = type;
    module.exports.strToInt = strToInt;
    module.exports.strListToIntList = strListToIntList;
    module.exports.removeAllWhitespaces = removeAllWhitespaces;
    module.exports.fadeOut = fadeOut;
}