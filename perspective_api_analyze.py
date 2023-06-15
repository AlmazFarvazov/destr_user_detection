import requests
import json

def analyze_text_perspective_api(text, api_key):
    url = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' 
    data_dict = {
        'comment': {'text': text},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    response = requests.post(url=url, data=json.dumps(data_dict), params={'key': api_key})
    response_dict = json.loads(response.content)
    return response_dict

