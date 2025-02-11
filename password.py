import random
import string
import requests

def random_charatcer():
    choices = string.ascii_letters + string.digits + sting.punctuation
    return random.choice(choices)

    passswordLength = 12

    def generate_strong_password():
        password=""
        for i in range(passwordLength):
            password = password + random_charcter()
        print(password)
    generate_strong_password()

    def fetch_word():
        url = "https://random-word-api.herokuapp.com/word?length=6"

        response = requests.get(url)
        word = respond.json()[0]
        return word

    def generate_weaker_password():
        word1 = fetch_word()
        word2 = fetch()
        password = word1 + word2
        return password
        
    print(ferch_word())