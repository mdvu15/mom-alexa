/**
    Copyright 2014-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

        http://aws.amazon.com/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/

/**
 * This simple sample has no external dependencies or session management, and shows the most basic
 * example of how to create a Lambda function for handling Alexa Skill requests.
 *
 * Examples:
 * One-shot model:
 *  User: "Alexa, tell Hello World to say hello"
 *  Alexa: "Hello World!"
 */

/**
 * App ID for the skill
 */
var APP_ID = undefined; //replace with "amzn1.echo-sdk-ams.app.[your-unique-value-here]";

/**
 * The AlexaSkill prototype and helper functions
 */
var AlexaSkill = require('./AlexaSkill');

/**
 * HelloWorld is a child of AlexaSkill.
 * To read more about inheritance in JavaScript, see the link below.
 *
 * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript#Inheritance
 */
var LoverMode = function () {
    AlexaSkill.call(this, APP_ID);
};

// Extend AlexaSkill
LoverMode.prototype = Object.create(AlexaSkill.prototype);
LoverMode.prototype.constructor = LoverMode;

LoverMode.prototype.eventHandlers.onSessionStarted = function (sessionStartedRequest, session) {
    console.log("LoverMode onSessionStarted requestId: " + sessionStartedRequest.requestId
        + ", sessionId: " + session.sessionId);
    // any initialization logic goes here
};

LoverMode.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    console.log("LoverMode onLaunch requestId: " + launchRequest.requestId + ", sessionId: " + session.sessionId);
    var speechOutput = "Entering desperate lover mode";
    var repromptText = "Hi baby, are you there?";
    response.ask(speechOutput, repromptText);
};

LoverMode.prototype.eventHandlers.onSessionEnded = function (sessionEndedRequest, session) {
    console.log("LoverMode onSessionEnded requestId: " + sessionEndedRequest.requestId
        + ", sessionId: " + session.sessionId);
    // any cleanup logic goes here
};

LoverMode.prototype.intentHandlers = {
    "GetTraffic": function (intent, session, response) {
      response.ask("Where do you think you're going? You are supposed to stay and love me forever","Hey, don't ignore me");
    },
    "GetWeather": function(intent, session, response) {
      handleWeatherIntent(session, response);
    },
    "Default" : function(intent, session, response) {
      response.tell("Are you ignoring me?");
    },
    "AMAZON.StopIntent": function (intent, session, response) {
        var speechOutput = "Goodbye";
        response.tellWithCard(speechOutput, speechOutput, speechOutput);
    },
    "AMAZON.CancelIntent": function (intent, session, response) {
        var speechOutput = "Goodbye";
        response.tellWithCard(speechOutput, speechOutput, speechOutput);
    }
};

var handleWeatherIntent = function(session, response) {
  var speechOutput = {
    speech: "<speak>Can't you feel it? It's hoooot <break time=\"0.2s\"/> being with me.</speak>",
    type: AlexaSkill.speechOutputType.SSML
  };
  var repromptOutput = {
    speech: "<speak>Honey, <break time=\"0.2s\"/> are you there?</speak>",
    type: AlexaSkill.speechOutputType.SSML
  };
  response.ask(speechOutput, repromptOutput);
};

/** var handleDefault = function(session, response) {
  var speechOutput = {
    speech: "<speak>OH <break strength=medium/> MY <break strength=medium/> GOD. Stop ignoring me. </speak>",
    type: AlexaSkill.speechOutputType.SSML
  };
  var repromptOutput = "I'm off!";
  response.tell(repromptOutput);
}; */

exports.handler = function (event, context) {
    // Create an instance of the HelloWorld skill.
    var loverMode = new LoverMode();
    loverMode.execute(event, context);
};
