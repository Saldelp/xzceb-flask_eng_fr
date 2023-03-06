"""
This module provides APIs for english to/from french translation
by using IBM Watson Language Translation Service
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """
    API to perform english to french translation
    """
    if english_text is None or english_text == "":
        return ""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation.get("translations")[0].get("translation")
        return french_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        error_message = "en-2-fr failed with status code " + str(ex.code) + ": " + ex.message
        return error_message

def french_to_english(french_text):
    """
    API to perform french to english translation
    """
    if french_text is None or french_text == "":
        return ""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation.get("translations")[0].get("translation")
        return english_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        error_message = "fr-2-en failed with status code " + str(ex.code) + ": " + ex.message
        return error_message
