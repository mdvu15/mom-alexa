import json
from blockcypher import create_wallet_from_address
from blockcypher import generate_new_address
from blockcypher import get_address_details
from blockcypher import simple_spend
from blockcypher import get_total_balance
from blockcypher import create_unsigned_tx
from blockcypher import send_faucet_coins


def lambda_handler(event, context):
    #if (event["session"]["application"]["applicationId"] !=
    #        "amzn1.echo-sdk-ams.app.bd304b90-xxxx-xxxx-xxxx-xxxxd4772bab"):
    #    raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session_started_request, session):
    print "Starting new session."

def on_launch(launch_request, session):
    return get_welcome_response()

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "Hungry":
        return get_hungry_status()
    elif intent_name == "HiMom":
        return get_hi_status()
    elif intent_name == "Money":
        return get_money()
    elif intent_name == "Hug":
	return get_hug_status()
    elif intent_name == "MeanKids":
	return get_kids_status()
    elif intent_name == "Thanks":
	return get_thanks_status()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...

def handle_session_end_request():
    card_title = "Okay, I'll be downstairs if you need anything"
    speech_output = "Okay, I'll be downstairs if you need anything"
    should_end_session = True

    return build_response({}, build_speechlet_response_text(card_title, speech_output, None, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "PARENT MODE"
    speech_output = "Becoming your mom"
    reprompt_text = "Honey, are you there?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))

def get_hungry_status():
    session_attributes = {}
    card_title = ""
    reprompt_text = ""
    should_end_session = False

    speech_output = "I made you cookies, sunshine"

    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))

def get_hi_status():
    session_attributes = {}
    card_title = ""
    reprompt_text = "Do you want anything to eat?"
    should_end_session = False

    speech_output = "Hi, honey"

    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))

def get_money():
    try:
        #print(get_total_balance('C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2'))
        simple_spend(from_privkey='356ce8496d761f51aa5939da9f7bbfb94886234f1f8eb5507bea9f3676e6c8e8', to_address='C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', to_satoshis=500, coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')
        session_attributes = {}
        card_title = ""#"I transferred money to your account. Your balance is now " + str(get_total_balance('C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')) + " satoshis."
        reprompt_text = ""
        should_end_session = False
        speech_output = "I transferred money to your account. Your balance is now " + str(get_total_balance('C22cpHQAzQ2rt7Jj1fQjevQeTdZhKbUysW', coin_symbol='bcy', api_key='4bcc9dcc6bc449fc85cd525802b30fa2')) + " satoshis."
        print speech_output
        return build_response(session_attributes, build_speechlet_response_text(card_title, speech_output, reprompt_text, should_end_session))

    except:
        session_attributes = {}
        carde_title = ""
        should_end_session = False
        speech_output = "I have nothing left to give"
        return build_response(session_attributes, build_speechlet_response_text(card_title, speech_output, reprompt_text, should_end_session))


def get_hug_status():
    session_attributes = {}
    card_title = ""
    reprompt_text = ""
    should_end_session = False

    speech_output = "Awwwwww, do you want a hug?"

    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))

def get_kids_status():
    session_attributes = {}
    card_title = ""
    reprompt_text = ""
    should_end_session = False

    speech_output = "I'm sorry, I think you are great, honey. The other kids will learn better"

    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))

def get_thanks_status():
    session_attributes = {}
    card_title = ""
    reprompt_text = ""
    should_end_session = False

    speech_output = "Don't thank me, sweety, I am not a regular mom. I like to think of myself as a cool mom"

    return build_response(session_attributes, build_speechlet_response_text(
        card_title, speech_output, reprompt_text, should_end_session))



'''def get_train_times(intent):
    session_attributes = {}
    card_title = "BART Departures"
    speech_output = "I'm not sure which station you wanted train times for. " \
                    "Please try again."
    reprompt_text = "I'm not sure which station you wanted train times for. " \
                    "Try asking about Fremont or Powell Street for example."
    should_end_session = False

    if "Station" in intent["slots"]:
        station_name = intent["slots"]["Station"]["value"]
        station_code = get_station_code(station_name.lower())

        if (station_code != "unkn"):
            card_title = "BART Departures from " + station_name.title()

            response = urllib2.urlopen(API_BASE + "/departures/" + station_code)
            station_departures = json.load(response)

            speech_output = "Train departures from " + station_name + " are as follows: "
            for destination in station_departures["etd"]:
                speech_output += "Towards " + destination["destination"] + " on platform " + destination["estimate"][0]["platform"] + ". ";
                for estimate in destination["estimate"]:
                    if estimate["minutes"] == "Leaving":
                        speech_output += "Leaving now: "
                    elif estimate["minutes"] == "1":
                        speech_output += "In one minute: "
                    else:
                        speech_output += "In " + estimate["minutes"] + " minutes: "

                    speech_output += estimate["length"] + " car train. "

            reprompt_text = ""

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))'''


def build_speechlet_response_text(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_speechlet_response_ssml(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "SSML",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "SSML",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
