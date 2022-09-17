from json import load

from random_word.utils.utils import request_url


class ApiNinjas(object):
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = "https://api.api-ninjas.com/v1/randomword"

    def get_random_word(self):
        if self.api_key != None:
            response = request_url(self.url, headers={"X-Api-Key": self.api_key})
            if response.status_code == 200:
                result = response.json()
                return result["word"]
            else:
                print("Error:", response.status_code, response.text)
        else:
            response = request_url(self.url)
            result = response.json()
            if response.status_code == 200:
                return result["word"]
            else:
                print("could not find the word")
