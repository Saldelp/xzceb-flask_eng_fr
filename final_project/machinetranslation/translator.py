"""
    This module provides APIs for english to/from french translation 
    by using IBM Watson Language Translation Service
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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

def english_to_french(english_text):
    """ 
        API to perform english to french translation 
    """
    if english_text is None:
        return ""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation.get("translations")[0].get("translation")            
        return french_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return "en-fr translation method failed with status code " + str(ex.code) + ": " + ex.message

def french_to_english(french_text):
    """ 
        API to perform french to english translation 
    """
    if french_text is None:
        return ""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation.get("translations")[0].get("translation")
        return english_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return "fr-en translation method failed with status code " + str(ex.code) + ": " + ex.message
