import requests
import random

def get_books():
    url = "https://bible-api.com/data/kjv" 
    response = requests.get(url)
    json = response.json()
    
    return json['books']

def get_random_verse():
    books = get_books()
    book_id = books[random.randrange(0, len(books))]['id']
    
    url = f"https://bible-api.com/data/kjv/{book_id}"
    response = requests.get(url)
    chapter = random.randrange(1, len(response.json()['chapters']))

    url = f"https://bible-api.com/data/kjv/{book_id}/{chapter}"
    response = requests.get(url)
    verses = response.json()['verses']

    verse = verses[random.randrange(1, len(verses))]
    print(f"{verse['book']} {chapter}:{verse['verse']}")
    print(verse['text'])

if __name__ == "__main__":
    get_random_verse()
