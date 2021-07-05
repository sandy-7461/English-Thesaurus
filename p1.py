import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def transalation(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn=input("Did you mean %s instead? If yes Enter Y or N:" % get_close_matches(word,data.keys())[0])
        if(yn=="Y"):
            return data[get_close_matches(word,data.keys())[0]]
        elif(yn=="N"):
            return "The word doesnt exist please double check it"
        else:
            return "We Didn't understand your query."
    else:
        return "The word doesnt exist please double check it"

s=input("Enter the word to search in the available data: ")
r=transalation(s)
if(type(r)==list):
    for item in r:
        print(item)
else:
    print(r)

