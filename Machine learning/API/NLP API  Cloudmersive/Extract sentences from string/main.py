from __future__ import print_function
from cloudmersive_nlp_api_client.rest import ApiException
import cloudmersive_nlp_api_client
from pprint import pprint
import time

# Configuring the API key for authorization
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = ''

# Creating an instance of the SegmentationApi class for text segmentation
api_instance = cloudmersive_nlp_api_client.SegmentationApi(
                cloudmersive_nlp_api_client.ApiClient(configuration))

# Creating a segmentation request object
input = cloudmersive_nlp_api_client.SentenceSegmentationRequest(
            'Cloudmersive is a platform containing numerous APIs. NLP API is a part of it.')

try:
    # Making a request to the API to extract sentences from the input string
    api_response = api_instance.segmentation_get_sentences(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationApi %s\n" % e)
