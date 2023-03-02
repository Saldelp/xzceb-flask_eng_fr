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
    #write the code here
    try:
    # Invoke a method
        return frenchText
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def frenchToEnglish(frenchText):
    #write the code here
    try:
    # Invoke a method
        return englishText
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        