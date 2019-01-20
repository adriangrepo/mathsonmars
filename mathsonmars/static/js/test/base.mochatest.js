/**
 * Created by a on 16/01/16.
 */

//'use strict';
//var expect = require('chai').expect;
//var base = require('../mads/build/bundle.js');
//var logger = require('../logger/winston_logger.js');

const winston = require('winston');
var logger = new (winston.Logger)({ transports: [
    new (winston.transports.Console)({ colorize: true })
] });
module.exports = logger;

describe("dummyAdd", function() {
    it("contains spec with an expectation", function() {
        console.log("dummyAdd test");
        var result = base.dummyAdd(1, 2);
        expect(result).to.equal(3);
    });
});

/*
describe("Add numbers test", function() {
    it("checks valid result", function() {
        var a = 2;
        var b = 1;
        var result = addNumbers(a, b);
        expect(result).to.equal(3);
    });
});
*/

/*
describe("generateTwoVariableEquations add", function() {
    it("contains spec with an expectation", function() {
        console.log("generateTwoVariableEquations add");
        var category, rawArray, paramRawAnswers;
        category = "Addition";
        rawArray = "1,2,4,4";
        paramRawAnswers = "3,8";
        var splitArray = rawArray.split(',');
        var splitAnswers = paramRawAnswers.split(',');
        var equationArray = base.generateTwoVariableEquations(category, splitArray, splitAnswers);
        expect(equationArray.length).to.equal(1);
        expect(equationArray[0].numVariables).to.equal(2);
        expect(equationArray[0].variables[0]).to.equal('1');
        expect(equationArray[0].variables[1]).to.equal('2');
        expect(equationArray[0].operators[0]).to.equal("+");
        expect(equationArray[0].question).to.equal("1 + 2 = ");
        expect(equationArray[0].answer).to.equal("3");
        expect(equationArray[0].correct).to.equal(false);
        expect(equationArray[0].elapsedTime).to.equal(0);
    });
});


describe("generateEquations x2", function() {
    it("contains spec with an expectation", function() {
        console.log("generateEquations");
        var operation, rawNumValues, rawQuestions, timeLimit;
        operation = "Add";
        rawNumValues = "2";
        rawQuestions = "1,2,3, 7, 12, 19";
        timeLimit = 600;
        var equationModerator = base.generateEquations(operation, rawNumValues, rawQuestions);
        var currentIndex = equationModerator.currentIndex;
        var equationArray = equationModerator.equationArray;
        var timeLimit = timeLimit;
        expect(currentIndex).to.equal(0);
        expect(equationArray.length).to.equal(2);
        var equation1 = equationArray[0];
        var equation2 = equationArray[1];
        expect(equation1.numVariables).to.equal(2);
        expect(equation1.variables[0]).to.equal('1');
        expect(equation1.variables[1]).to.equal('2');
        expect(equation1.operators[0]).to.equal("+");
        expect(equation1.question).to.equal("1 + 2 = ");
        expect(equation1.answer).to.equal("3");
        expect(equation1.correct).to.equal(false);
        expect(equation1.elapsedTime).to.equal(0);
        expect(equation2.numVariables).to.equal(2);
        expect(equation2.variables[0]).to.equal('7');
        expect(equation2.variables[1]).to.equal('12');
        expect(equation2.operators[0]).to.equal("+");
        expect(equation2.question).to.equal("7 + 12 = ");
        expect(equation2.answer).to.equal("19");
        expect(equation2.correct).to.equal(false);
        expect(equation2.elapsedTime).to.equal(0);
    });
});


describe("generateQuestionText", function() {
    it("contains spec with an expectation", function() {
        console.log("unit test generateQuestionText");
        var operation, rawNumValues, rawQuestions, timeLimit;
        operation = "Add";
        rawNumValues = "2";
        rawQuestions = "1,2,3, 7, 12, 19";
        timeLimit = 600;
        var equationModerator = base.generateEquations(operation, rawNumValues, rawQuestions, timeLimit);
        var equationArray = equationModerator.equationArray;
        var equation1 = equationArray[0];
        expect(equationModerator.currentIndex).to.equal(0);
        expect(equationArray.length).to.equal(2);
        expect(equationModerator.timeLimit).to.equal(600);
        expect(equation1.question).to.equal("1 + 2 = ");
        var newQuestion = base.askQuestion(equationModerator);
        expect(newQuestion).to.equal(equation1.question);
        console.log("generateQuestionText newQuestion:"+newQuestion);
    });
});
*/

/*
 describe("generateQuestions", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateQuestions");
 var operation, rawNumValues, rawQuestions;
 operation = "Add";
 rawNumValues = "2";
 rawQuestions = "1,2,3";
 var qaArray = base.generateQuestions(operation, rawNumValues, rawQuestions);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("1 + 2 = ");
 expect(a1).to.equal("3");
 });
 });




 describe("generateQuestions x2", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateQuestions");
 var operation, rawNumValues, rawQuestions;
 operation = "Add";
 rawNumValues = "2";
 rawQuestions = "1,2,3, 7, 12, 19";
 var qaArray = base.generateQuestions(operation, rawNumValues, rawQuestions);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("1 + 2 = ");
 expect(a1).to.equal("3");
 var q2 = q1Array[1];
 var a2 = a1Array[1];
 expect(q2).to.equal("7 + 12 = ");
 expect(a2).to.equal("19");
 });
 });

 describe("generateTwoVariableQuestions add", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateTwoVariableQuestions add");
 var operation, questions, rawArray;
 operation = "Add";
 questions = "1,2,3";
 var rawArray = questions.split(',');
 var qaArray = base.generateTwoVariableQuestions(operation, rawArray);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("1 + 2 = ");
 expect(a1).to.equal("3");
 });
 });

 describe("generateTwoVariableQuestions sub", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateTwoVariableQuestions sub");
 var operation, questions, rawArray;
 operation = "Sub";
 questions = "1,2,-1";
 var rawArray = questions.split(',');
 var qaArray = base.generateTwoVariableQuestions(operation, rawArray);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("1 - 2 = ");
 expect(a1).to.equal("-1");
 });
 });



 describe("generateTwoVariableQuestions mul", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateTwoVariableQuestions mul");
 var operation, questions, rawArray;
 operation = "Mul";
 questions = "3,2,6";
 var rawArray = questions.split(',');
 var qaArray = base.generateTwoVariableQuestions(operation, rawArray);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("3 "+String.fromCharCode(215)+" 2 = ");
 expect(a1).to.equal("6");
 });
 });

 describe("generateTwoVariableQuestions div", function() {
 it("contains spec with an expectation", function() {
 logger.debug("generateTwoVariableQuestions div");
 var operation, questions, rawArray;
 operation = "Div";
 questions = "10,5,2";
 var rawArray = questions.split(',');
 var qaArray = base.generateTwoVariableQuestions(operation, rawArray);
 var q1Array = qaArray[0];
 var a1Array = qaArray[1];
 var q1 = q1Array[0];
 var a1 = a1Array[0];
 expect(q1).to.equal("10 "+String.fromCharCode(247)+" 5 = ");
 expect(a1).to.equal("2");
 });
 });
 */

