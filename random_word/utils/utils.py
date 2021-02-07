import sys

import requests


def request_url(url):
    try:
        response = requests.get(url)
    except Exception as e:
        e = sys.exc_info()[0]
        raise e
    return response


def check_payload_items(payload, allParams):
    if payload:
        for (key, val) in payload.items():
            if key not in allParams:
                raise TypeError(
                    "Got an unexpected keyword argument '%s' to method get_random_word"
                    % key
                )
