"use strict";

//global holder of current index and equationArray
var equationModerator;
//global flag
var svgSupported;
var svgEffects = false;
var svgQuestions = false;
var d3jsDrawings = true;
var progressBarChart;

var sessionId = "";
var startTime = "";
var categoryName = "";
var activityName = "";
var strategyName = "";
var activityLevel = "";
var activityLevelProgress = "";
var timeLimit = "";
var totalQuestions = "";
var answerFormat = "";
var activityNumVariables = "";
var questionIds = "";
var strategyQualifier = "";

var greenBoxColour = "rgba(132, 225, 132, 0.9)";
var redBoxColour = "rgba(255, 132, 132, 0.9)";
var redCrossColour = "rgb(240,0,0)";
var greenTickColour = "rgb(0,215,0)";
var yellowBoxColour = "rgba(225, 225, 102, 0.9)";

var DARK_DARK_GREY = "#181818";
var MEDIUM_DARK_GREY = "#585858";
var MEDIUM_GREY = "#787878";
var LIGHT_GREY = "#B0B0B0";

var STRATEGY_COUNT = 'Count';
var STRATEGY_PATTERNS = 'Patterns';
var STRATEGY_NUMBER_BONDS = 'Number bonds';
var STRATEGY_COUNT_ON = 'Count on';
var STRATEGY_COUNT_BACK = 'Count back';
var STRATEGY_FUN_CHUNKS = 'Fun chunks';
var STRATEGY_FRIENDLY_AND_FIX = 'Friendly and fix';
var STRATEGY_MEMORIZE = 'Memorize';
var STRATEGY_TEN_OR_HUNDRED = 'Ten or hundred';
var STRATEGY_BY_PLACE = 'By place';
var STRATEGY_REPEATED = 'Repeated';
var STRATEGY_GROUPS = 'Groups';
var STRATEGY_FRACTIONS = 'Fractions';
var STRATEGY_BOX_METHOD = 'BOX_METHOD';
var STRATEGY_WITHOUT_REGROUPING = 'Without regrouping';
var STRATEGY_WITH_REGROUPING = 'With regrouping';

var STRATEGY_QUALIFIER_COUNTER = 'counters';
var STRATEGY_QUALIFIER_WHOLE_PART = 'whole-part find part';
var STRATEGY_QUALIFIER_PART_PART = 'part-part find whole';

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

window.addEventListener("keydown", checkKeyPressed, false);

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
            var rawQuestions = JSONObject.questions;
            var rawAnswers = JSONObject.answers;
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
                    updateProgress();
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
                replaceNumberBondDescription();
                setUpAnswerElement();
                svgNumberBondsCounters(rawWholeValues, rawPart1Values, rawPart2Values, strategyName);
                setUpListeners();
                updateProgress();
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_WHOLE_PART){
                console.log("whole: "+rawWholeValues+" part1: "+rawPart1Values+" part2: "+rawPart2Values);
                console.log("STRATEGY_QUALIFIER_WHOLE_PART");
            }
            else if (strategyQualifier === STRATEGY_QUALIFIER_PART_PART){
                console.log("whole: "+rawWholeValues+" part1: "+rawPart1Values+" part2: "+rawPart2Values);
                console.log("STRATEGY_QUALIFIER_PART_PART");
            }
        }
        else if (strategyName === 'some sort of box question') {
            //svgQuestion();
            svgRectangle(0, 10, 7);
            svgRectangle(1, 10, 4);
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

function generateNumberBondEquations(rawWholeValues, rawPart1Values, rawPart2Values, rawQuestions) {
    var wholeVals = removeAllWhitespaces(rawWholeValues);
    var wholeValues = wholeVals.split(',');
    var part1Vals = removeAllWhitespaces(rawPart1Values);
    var part1Values = part1Vals.split(',');
    var part2Vals = removeAllWhitespaces(rawPart2Values);
    var part2Values = part2Vals.split(',');
    assert((rawQuestions.length)===1, 'generateNumberBondEquations() len(rawQuestions)===1');
    if ((rawQuestions.length) === 1)
    {
        var questionText = rawQuestions[0];
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
    var answerWidth = (answerLength+1).toString() +"em";
    var answerElement = document.getElementById("text_answer");
    answerElement.setAttribute("style","width:"+answerWidth);
    answerElement.focus();
}

function clearAnswerArea(){
    //document.getElementById ('text_answer').value = "";
    var answerBoxItem = document.querySelector("#text_answer input");
    console.log("--clearAnswerArea current value:"+answerBoxItem.value+" "+answerBoxItem);
    answerBoxItem.value = "";
    answerBoxItem.setAttribute("style","foreground-color:"+yellowBoxColour);
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

function displayGraphics(){
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
    updateProgress();
}

function setUpListeners(){
    addButtonListeners();
    //attachKeypressListener();
}

function generateQuestionText() {
    var newQuestion;
    if (equationModerator) {
        var runningTotal = 0;
        newQuestion = false;
        if (equationModerator.currentIndex < (totalQuestions)) {
            var totalTime =0;
            for (var i=0; i < equationModerator.elapsedTimeList.length; i++){
                totalTime+= equationModerator.elapsedTimeList[i]
            }
            if (totalTime < timeLimit * 1000) {
                var startTime = Date.now ();
                equationModerator.startTimes[equationModerator.currentIndex] = startTime;
                newQuestion = equationModerator.questions[equationModerator.currentIndex];
            }
        }
    }
    else{
        console.error("--generateQuestionText input parameter is null");
    }
	return newQuestion;
}

function appendAnswer(answerText){
    if (equationModerator.sessionFinished === true){
        return;
    }
    var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
    if (givenAnswer === undefined){
        givenAnswer = '';
    }
    var newAnswer = givenAnswer+answerText;
    equationModerator.givenAnswers[equationModerator.currentIndex] = newAnswer;
    updateAnswerElement(newAnswer);
}

function updateAnswerElement(newAnswer) {
    console.log("--updateAnswerElement()");
    var answerBoxItem = document.querySelector ("#text_answer input");
    if (answerBoxItem !== document.activeElement) {
        console.log("--updateAnswerElement() answerBoxItem !== document.activeElement ");
        //only update if not selected
        foreceUpdateAnswerElement(newAnswer);
    }
}

function foreceUpdateAnswerElement(newAnswer) {
    var answerBoxItem = document.querySelector ("#text_answer input");
    if (answerBoxItem.value !== newAnswer) {
            answerBoxItem.value = newAnswer;
        }
}

function replaceNumberBondDescription(){
    var element = document.getElementById("question_description");
    var text = equationModerator.questionText;
    if (strategyName === STRATEGY_NUMBER_BONDS) {
        var wholeValue = equationModerator.wholeValues[equationModerator.currentIndex];
        var part1Value = equationModerator.part1Values[equationModerator.currentIndex];
        var newText = text.replace ('#w', wholeValue.toString());
        newText = newText.replace ('#p1', part1Value.toString());
        element.innerHTML = newText;
    }
}


function checkAnswer() {
    console.log (">>checkAnswer()");
    if (equationModerator.sessionFinished === true) {
        return "Finished";
    }
        if (equationModerator.currentIndex >= (equationModerator.givenAnswers.length)) {
            if (equationModerator.currentIndex > 0) {
                //shouldn't happen
                wrapUpSession ("Indexing error");
                return "Finished";
            }
        }
        else {
            var actualAnswer = equationModerator.answers[equationModerator.currentIndex];
            var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
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
    console.log("wipeQuestion")
    if (svgQuestions === true){
        renderWipeOutQuestion();
    }
    else {
        clearAnswerArea();
    }
}

function isGivenAnsLenSufficient(){
    console.log("--isGivenAnsLenSufficient()")
    if (totalQuestions>equationModerator.currentIndex) {
        var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
        console.log("--isGivenAnsLenSufficient() givenAnswer: "+givenAnswer);
        if (!!givenAnswer) {
            if (givenAnswer.length >= equationModerator.answers[equationModerator.currentIndex].length) {
                console.log("--isGivenAnsLenSufficient() updateSubmitButtonStatus(true) ");
                updateSubmitButtonStatus(true);
                return true;
            }
            else {
                console.log("--isGivenAnsLenSufficient() updateSubmitButtonStatus(false) ");
                updateSubmitButtonStatus(false);
            }
        }
        updateSubmitButtonStatus(false);
        return false;
    }
    return true;
}

function generateSummaryText(){
    var corrects = [];
    var correct;
    var total = totalQuestions;
    for (var i = 0; i<equationModerator.corrects.length; i++){
        correct = equationModerator.corrects[i];
        if (correct === true)
        {
            corrects.push(correct);
        }
    }
    console.log(" correct:"+corrects.length);
    var ratio = correct/total;
    var prefix;
    if (ratio < 0.3){
        prefix = 'Good effort'
    }
    else if (ratio < 0.6){
        prefix = 'Well done'
    }
    else if (ratio < 1){
        prefix = 'Great work'
    }
    else {
        prefix = 'Perfect'
    }
    var displayText = prefix+". You got "+corrects.length+" out of "+total+" correct."
    return displayText
}

function moveToNextOrFinish(){
    if (isGivenAnsLenSufficient() === true) {
        console.log ("--moveToNextOrFinish() (isGivenAnsLenSufficient() === true)");
        wipeQuestion ();
        clearSvg ();
        equationModerator.currentIndex += 1;
        var displayText;
        //if questionText returns false we're done
        if (equationModerator.currentIndex >= totalQuestions+1){
            displayText = generateSummaryText ();
            wrapUpSession (displayText);
        }
        else if (equationModerator.totalTime >= timeLimit * 1000) {
            displayText = generateSummaryText ();
            var preDisplayText = "Time's up. "
            wrapUpSession (preDisplayText + displayText);
        }
        else {
            console.log ("--moveToNextOrFinish() 528");
            if (equationModerator.currentIndex === (totalQuestions - 1)) {
                changeSubmitButtonToFinish ();
            }
            else {
                changeSubmitButtonToSubmit ();
            }
            if (strategyName === STRATEGY_NUMBER_BONDS)
            {
                console.log ("--moveToNextOrFinish() 537");
                replaceNumberBondDescription();
            }
            else {
                console.log ("--moveToNextOrFinish() 541 strategyName: "+strategyName);
                var questionText = generateQuestionText (equationModerator);
                displayQuestion (questionText);
                displayGraphics ();
            }
        }
    }
}

function equationResultToJSON(paramEqModerator){
    console.log(">>equationResultToJSON() paramEqModerator:"+paramEqModerator);
    var timeLimit, totalTime;
    var results = [];
    var elapsedTimes = [];
    var hints = [];
    var helps = [];


    for (var j=0; j<paramEqModerator.questions.length; j++){
        elapsedTimes.push(paramEqModerator.elapsedTimeList[j]);
        results.push(equationModerator.corrects[j]);
    }
    //Hints and helps could be any length
    for (var j=0; j<paramEqModerator.hints.length; j++){
        hints.push(paramEqModerator.hints[j]);
    }
    for (var j=0; j<paramEqModerator.helps.length; j++){
        helps.push(paramEqModerator.helps[j]);
    }
    var objToStringify = {};

    objToStringify['session_id'] = sessionId;
    objToStringify['start_time'] = startTime;
    objToStringify['results'] = results;
    objToStringify['elapsedTimes'] = elapsedTimes;
    objToStringify['hints'] = hints;
    objToStringify['helps'] = helps;
    objToStringify['categoryName'] =  categoryName;
    objToStringify['activityName'] =  activityName;
    objToStringify['strategyName'] =  strategyName;
    objToStringify['activityLevelProgress'] =  activityLevelProgress;
    objToStringify['activityLevel'] = activityLevel;
    objToStringify['question_ids'] = questionIds;
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

    var stringifiedObject = equationResultToJSON(equationModerator);
    console.log("--sendAjax() stringifiedObject:"+stringifiedObject);
    xhr.send(stringifiedObject);

}

function wrapUpSession(displayText){
    console.log(">>wrapUpSession");
    equationModerator.sessionFinished = true;
    displayWrapUpStatement(displayText);
    sendAjax();
}


function displayWrapUpStatement(displayText){
    console.log(">>displayWrapUpStatement text"+displayText);
    var answerBoxItem = document.querySelector("#text_answer input");
    answerBoxItem.style.display = 'none';
    var questionDesc = document.getElementById("question_description");
    questionDesc.innerHTML = displayText;
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

function svgRuledLine(xOffset, yPosition, length, strokeColour, strokeWidth) {
    var s = Snap("#snapsvg");
    var ruledLine = s.paper.line(xOffset, yPosition, X_MULTIPLIER*length, yPosition);
    ruledLine.attr({
            stroke: strokeColour,
            strokeWidth: strokeWidth
    });
}

function svgRect(x, y, width, height, strokeColor){
    var s = Snap("#snapsvg");
    var r = s.paper.rect(x, y, width, height);
    r.attr({
        stroke: strokeColor,
        strokeWidth: 2,
        fillOpacity: 0
    });
}

function svgArrowHead(xPosition, yPosition, rotation){
    var s = Snap("#snapsvg");
    var triangle1 = s.paper.polyline("-5,5 0,-5 5,5");
    var tri1TransformString = "t"+xPosition+","+yPosition+",r"+rotation;
    triangle1.transform(tri1TransformString);
}

function svgPoint(xPosition, yPosition, pointColor){
    console.log(">>svgPoint xPosition:"+xPosition+" yPosition:"+yPosition);
    var s = Snap("#snapsvg");
    var point = s.paper.circle(X_MULTIPLIER*xPosition, yPosition, POINT_DIAMETER);
    point.attr({
        stroke: pointColor,
        strokeWidth: 3,
        fill: pointColor
    });
}

function svgText(xPosition, yPosition, textDraw){
    console.log(">>svgText xPosition:"+xPosition+" yPosition:"+yPosition+" textDraw:"+textDraw);
    var s = Snap("#snapsvg");
    var t = s.paper.text(X_MULTIPLIER*xPosition, yPosition+Y_POINT_TEXT_OFFSET, textDraw);
    t.attr({
        'font-size':24
    });
}

function svgPath(start, mid, end){
    var s = Snap("#snapsvg");
    var convertedXStart = (X_MULTIPLIER*start).toString();
    var convertedXMid = (X_MULTIPLIER*mid).toString();
    var convertedXEnd = (X_MULTIPLIER*end).toString();
    var pathString = "M"+convertedXStart+","+LINE_Y_1+" Q"+convertedXMid+","+LINE_Y_0+" "+convertedXEnd+","+LINE_Y_1;
    var newpath = s.paper.path(pathString);
    newpath.attr({
        stroke: "black",
        strokeWidth: 1,
        fill:"none"
    });
}

function svgNumberBondsCounters(whole, part1, part2, strategyName){
    console.log(">>svgNumberBondsCounters() strategyName: "+strategyName+" type(part1):"+type(part1)+" whole: "+whole+" part1: "+part1+" part2: "+part2);
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
        svgText(wholeCount, 0, wholeText);
        svgRuledLine(0, 50, wholeCount*2, MEDIUM_GREY, 3);
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
            var circle = s.circle ((100 * i) + (100 * part1Count) + 50, yBaseLevel, 30);
            circle.attr ({
                fill: 'lightblue',
                stroke: 'lightblue',
                strokeOpacity: .3,
                strokeWidth: 10
            });
            part2Circles.push (circle);
        }
        svgRect(0, (yBaseLevel/2)+10, part1Count*2*X_MULTIPLIER, yBaseLevel-20, LIGHT_GREY);
        svgRect(part1Count*2*X_MULTIPLIER, (yBaseLevel/2)+10, part2Count*2*X_MULTIPLIER, yBaseLevel-20, LIGHT_GREY);
        svgText(part1Count,  yBaseLevel+ yBaseLevel/2, part1Text);
        svgText(part1Count*2 + part2Count, yBaseLevel+ yBaseLevel/2, "?");
    }
    else {
        if(wholeCount % 2 == 0)
        {
            //Even total number
            var halfCount = wholeCount/2;
            var topLine = True;
            var y = yBaseLevel;
            for (var i = 0; i < part1Count; i++) {
                if (topLine) {
                    y = yBaseLevel;
                    topLine = False;
                }
                else {
                    y = yBaseLevel+50;
                    topLine = True;
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
                var topLine = True;
                var halfPart1 = part1Count/2;
                for (var i = 0; i < part2Count; i++) {
                    if (topLine) {
                        y = yBaseLevel;
                        topLine = False;
                    }
                    else {
                        y = yBaseLevel+50;
                        topLine = True;
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
                var topLine = False;
                var halfPart1 = part1Count-1/2;
                var oddShift =0;
                for (var i = 0; i < part2Count; i++) {
                    if (topLine) {
                        y = yBaseLevel;
                        topLine = False;
                        oddShift = 100;
                    }
                    else {
                        y = yBaseLevel+50;
                        topLine = True;
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
    }
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
    console.log(">>funChunkAdditionDrawing() linePositions:"+linePositions+" jumpValues:"+jumpValues);
    clearSvg();
    svgRuledLine(X_MULTIPLIER, LINE_Y_1, FUN_CHUNKS_LINE_LENGTH, DARK_DARK_GREY, 3);
    var jump0, jump1;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }

    var firstPos = linePositions[0].toString();
    svgPoint(X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    svgText(X_POINT_START, LINE_Y_1, firstPos);
    svgArrowHead(X_MULTIPLIER, LINE_Y_1, 270);
    svgArrowHead(X_MULTIPLIER*FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, 90);
}

function funChunkTwoValSubtractionDrawing(linePositions, jumpValues){
    console.log(">>funChunkTwoValSubtractionDrawing() linePositions:"+linePositions+" jumpValues:"+jumpValues);
    clearSvg();
    svgRuledLine(X_MULTIPLIER, LINE_Y_1, FUN_CHUNKS_LINE_LENGTH, DARK_DARK_GREY, 3);
    var jump0, jump1;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    var firstPos = linePositions[0].toString();
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    svgText(FUN_CHUNKS_LINE_LENGTH-X_POINT_START, LINE_Y_1, firstPos);
    svgArrowHead(X_MULTIPLIER, LINE_Y_1, 270);
    svgArrowHead(X_MULTIPLIER*FUN_CHUNKS_LINE_LENGTH, LINE_Y_1, 90);
}

function funChunkTwoValAdditionHint1(jumpValues){
    var jump0, jump1;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    svgPath(X_POINT_START, X_POINT_START+jump0/2, jump0+X_POINT_START);
    svgPath(jump0+X_POINT_START, jump0+X_POINT_START+(jump1/2), jump0+X_POINT_START+jump1);
    svgPoint(jump0+X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    svgPoint(jump0+jump1+X_POINT_START, LINE_Y_1, DARK_DARK_GREY);
    var operatorStr = "+";
    if (strategyName === STRATEGY_FRIENDLY_AND_FIX) {
        operatorStr = "";
    }
    svgText(X_POINT_START+jump0/2, LINE_Y_0, operatorStr+jump0);
    svgText(jump0+X_POINT_START+(jump1/2), LINE_Y_0, operatorStr+jump1);
}

function funChunkTwoValSubtractionHint1(jumpValues){
    var jump0, jump1;
    try {
        jump0 = parseInt(jumpValues[0]);
        jump1 = parseInt(jumpValues[1]);
    }
    catch(err) {
        console.log("Error converting "+type(jumpValues[0])+" to int");
    }
    svgPath(FUN_CHUNKS_LINE_LENGTH-X_POINT_START, FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0/2, FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0);
    svgPath(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0, FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+(jump1/2), FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1);
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0, LINE_Y_1, DARK_DARK_GREY);
    svgPoint(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1, LINE_Y_1, DARK_DARK_GREY);
    svgText(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0/2, LINE_Y_0, +jump0);
    svgText(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+(jump1/2), LINE_Y_0, +jump1);
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
    svgText(jump0+X_POINT_START, LINE_Y_1, secondPos);
    svgText(jump0+jump1+X_POINT_START, LINE_Y_1, lastPos);
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
    svgText(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0, LINE_Y_1, secondPos);
    svgText(FUN_CHUNKS_LINE_LENGTH-X_POINT_START+jump0+jump1, LINE_Y_1, lastPos);
}

function add(a, b) {
    return a + b;
}

function svgRectangle(yPosition, length, numberColoured){
    //var block = s.rect(100, 100, 60*length);
    console.log(">>svgRectangle")
    var s = Snap("#snapsvg")
    var colouredBlocks = [];
    var fillColour = "";
    switch(numberColoured) {
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
    for (var i=1; i<=length; i++){
        var block = s.paper.rect(50*i, 100*yPosition, 50, 50);
        if (i <=numberColoured){
            block.attr({
                fill: fillColour,
                stroke: "#1f2c39",
                strokeWidth: 3
            });
        }
        else {
            block.attr({
                fill: ROD_COLOURS.CLOUDS,
                stroke: "#95a5a6",
                strokeWidth: 3
            });
        }

        colouredBlocks.push(block)
    }

}

function clearSvg(){
    var s = Snap("#snapsvg");
    s.clear();
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
    //var svgTextElement = s.text(0,0, resultText).attr({ fontSize: '48px', opacity: 50, "text-anchor": "middle" , fill: colour});
    //s.attr('fill', 'red');     //This is the elements area to fill
    /*
    var timing = 500;
    for( var index=0; index < 1; index++ ) {
        (function() {
            var svgTextElement = s.text(10,10, resultText).attr({ fontSize: '48px', opacity: 0, "text-anchor": "middle" , fill: colour});
            setTimeout( function() {
                    Snap.animate( 0, 1, function( value ) {
                        //svgTextElement.transform('s' + value   );                              // Animate by transform
                        svgTextElement.attr({ 'font-size': value * 100,  opacity: value });      // Animate by font-size ?
                    }, timing, mina.bounce, function() { svgTextElement.remove() } );
                }
                ,index * timing)
        }());
    };
    */

}

function updateSubmitButtonStatus(validLength){
    var d = document.getElementById("submit_button");
    if (validLength) {
        d.className = "btn btn-success";
    }
    else {
        d.className = "btn btn-default";
    }
}


function updateProgress(){
    var index = equationModerator.currentIndex;
    if (totalQuestions !== 0)
    {
        var progressValue = index / totalQuestions;
        var progressIntValue = Math.round( progressValue );
        var progressPercent = (progressIntValue * 100).toString()+"%";
        var d = document.getElementById("qq-progress");
        if (progressValue <= 0.2) {
            d.className = "progress-bar progress-bar-success";
        }
        else if (progressValue <= 0.2) {
            d.className = "progress-bar progress-bar-info";
        }
        else if (progressValue <= 0.2) {
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
    var keyCode = ev.keyCode;
    console.log("--checkKeyPressed() key: "+keyCode)
    var charStr = String.fromCharCode(keyCode);
    if (isNaN(charStr) || charStr == " "){
        if (answerFormat == "negative_positive_int" || answerFormat == "negative_positive_float"){
            //subtract
            if(charStr == '-' || keyCode == 173){
                if (equationModerator.givenAnswers.length > equationModerator.currentIndex ) {
                    var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
                    if (givenAnswer.length == 0) {
                        processKey (charStr);

                    }
                }
            }
        }
        //backspace or delete
        if (keyCode == 8 || keyCode == 46) {
            console.log("--checkKeyPressed back/del givenanslen: "+equationModerator.givenAnswers.length+" index:"+equationModerator.currentIndex)
            if (equationModerator.givenAnswers.length > equationModerator.currentIndex ){
                var givenAnswer = equationModerator.givenAnswers[equationModerator.currentIndex];
                console.log("--checkKeyPressed givenAnswer: "+givenAnswer+" currentIndex: "+equationModerator.currentIndex);
                if (givenAnswer.length > 0) {
                    equationModerator.givenAnswers[equationModerator.currentIndex] = givenAnswer.substr (0, givenAnswer.length - 1);
                    foreceUpdateAnswerElement(equationModerator.givenAnswers[equationModerator.currentIndex]);
                    console.log("--checkKeyPressed ev.preventDefault  givenAnswer: "+givenAnswer+" currentIndex: "+equationModerator.currentIndex);
                    ev.preventDefault ();
                }
            }
            else {
                console.log(" answers length:"+equationModerator.givenAnswers.length+" index: "+ equationModerator.currentIndex);
            }
        }
        //space
        else if (charStr == ' ') {
            ev.preventDefault();
        }
        else {
            // prevent default behaviour
            ev.preventDefault();
            return false;
        }
    }
    //tab, enter
    else if(keyCode == 9 || keyCode == 13){
        if (isGivenAnsLenSufficient() === true) {
            submitAnswer();
        }
        ev.preventDefault();
    }
    else {
        //is a number
        if (ignoreKeyIfTooLong() === true) {
            ev.preventDefault();
            return;
        }
        processKey(charStr);
    }
    if (equationModerator.currentIndex >= equationModerator.givenAnswers.length) {
        console.log(" index: "+ equationModerator.currentIndex+">="+" answers length:"+equationModerator.givenAnswers.length);
    }
    isGivenAnsLenSufficient();
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
    var submitButton = document.getElementById("submit_button");
    if (submitButton.text === 'Submit')
    {
        if ((checkAnswer() === 'Correct')||(checkAnswer() === 'Incorrect')) {
            changeSubmitButtonToNext();
        }
    }
    else {
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
    d.innerHTML = 'Next'+'&nbsp;'+'&nbsp;'+'&nbsp;';
    d.className = "btn btn-primary";
}

function updateSubmitButtonStatus(validLength){
    var d = document.getElementById("submit_button");
    if (validLength) {
        d.className = "btn btn-success";
    }
    else {
        d.className = "btn btn-default";
    }
}

function changeSubmitButtonToFinish(){
    document.getElementById("submit_button").textContent = "Finish";
}

function showHint(){
    var index = equationModerator.currentIndex;
    equationModerator.hints.push(index);
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

function strToInt(strVariable){
    console.log(">>strToInt type:"+type(strVariable));
    var converted = 0;
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

function removeAllWhitespaces(paramStr){
    var outStr = paramStr.replace(/\s/g,'');
    return outStr;
}

function fadeOut(elementId, speed) {
    var s = document.getElementById(elementId).style;
    s.opacity = 1;
    (function fade() {(s.opacity-=.1)<.1?s.display="none":setTimeout(fade,speed)})();
    //clearAnswer();
}

//Returns a random integer between min and max
//Using Math.round() will give you a non-uniform distribution!
function getRandomInt (min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
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
    if (parseFloat(value).toString() === value.toString()) {
        return true;
    }
    return false;
}

function isFloat2(value){
    return (this % 1 != 0);
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