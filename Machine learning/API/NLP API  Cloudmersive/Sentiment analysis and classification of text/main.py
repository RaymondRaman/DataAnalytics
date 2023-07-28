from __future__ import print_function
from cloudmersive_nlp_api_client.rest import ApiException
import cloudmersive_nlp_api_client
from pprint import pprint
import time

# Configuring the API key for authorization
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = ""

# Creating an instance of the AnalyticsApi class for sentiment analysis
api_instance = cloudmersive_nlp_api_client.AnalyticsApi(
                        cloudmersive_nlp_api_client.ApiClient(configuration))

# Creating a sentiment analysis request object
input = cloudmersive_nlp_api_client.SentimentAnalysisRequest(
                        'Educative is a platform where courses for developers are created')

try:
    # Making a request to the API to perform sentiment analysis on the input
    api_response = api_instance.analytics_sentiment(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_sentiment: %s\n" % e)
