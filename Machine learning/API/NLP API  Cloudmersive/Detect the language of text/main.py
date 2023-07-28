from __future__ import print_function
from cloudmersive_nlp_api_client.rest import ApiException
import cloudmersive_nlp_api_client
from pprint import pprint
import time

# Configuring the API key for authorization
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = ""

# Creating an instance of the LanguageDetectionApi class for language detection
api_instance = cloudmersive_nlp_api_client.LanguageDetectionApi(
                cloudmersive_nlp_api_client.ApiClient(configuration))


# Creating a language detection request object
input = cloudmersive_nlp_api_client.LanguageDetectionRequest('Bonjour')

try:
    # Making a request to the API to detect the language of the input text
    api_response = api_instance.language_detection_get_language(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageDetectionApi %s\n" % e)
