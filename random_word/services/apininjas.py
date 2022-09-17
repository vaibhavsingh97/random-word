class ApiNinjas(object):
  def __init__(self):
    self.url = 'https://api.api-ninjas.com/v1/randomword'

  
  def get_random_word(self):
    response = request_url(url)
    result = response.json()
    if response.status_code == 200:
      return result["word"]
    else:
      print("could not find the word")
