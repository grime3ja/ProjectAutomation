import requests

def get_affirmations():
  url = "https://www.affirmations.dev/"
  response = requests.get(url)
  json = response.json()
  affirmation = json['affirmation']
  print(affirmation)


if __name__ == "__main__":
  get_affirmations()
