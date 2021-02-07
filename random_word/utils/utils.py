import sys
import yaml
import secrets
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


def get_api_keys(filepath):
    yaml_config = ""
    with open(filepath, "r") as stream:
        try:
            yaml_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Error in configuration file:", exc)
    return yaml_config


def get_random_api_key(api_key_arr):
    return secrets.choice(api_key_arr)
