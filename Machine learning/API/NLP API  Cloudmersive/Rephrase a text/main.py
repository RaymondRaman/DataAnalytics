from __future__ import print_function
from cloudmersive_nlp_api_client.rest import ApiException
import cloudmersive_nlp_api_client
from pprint import pprint
import time

# Configuring the API key for authorization
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = "24cefa8c-e6fb-4266-a9cf-1e3d6874ade4"

# Creating an instance of the RephraseApi class for sentence rephrasing
api_instance = cloudmersive_nlp_api_client.RephraseApi(
                cloudmersive_nlp_api_client.ApiClient(configuration))

# Creating a rephrase request object
input = cloudmersive_nlp_api_client.RephraseRequest('Content creation takes a lot of effort', '2')

try:
    # Making a request to the API to rephrase the input text
    api_response = api_instance.rephrase_english_rephrase_sentence_by_sentence(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RephraseApi %s\n" % e)
