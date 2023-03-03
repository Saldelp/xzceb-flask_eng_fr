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

def englishToFrench(englishText):
    """ 
        API to perform english to french translation 
    """
    if englishText is None:
        return ""
    try:
        # Check that input text is english
        # if englishText is None:
        #     return "Source text is not in english"
        # Invoke tranlsator method
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        frenchText = translation["translations"][0]["translation"]            
        return frenchText
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return "en-fr translation method failed with status code " + str(ex.code) + ": " + ex.message

def frenchToEnglish(frenchText):
    """ 
        API to perform french to english translation 
    """
    if frenchText is None:
        return ""
    try:
        # Check that input text is french
        # if frenchText is None:
        #     return "Source text is not in french"
        # Invoke tranlsator method
        translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        englishText = translation["translations"][0]["translation"] 
        return englishText
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return "fr-en translation method failed with status code " + str(ex.code) + ": " + ex.message
