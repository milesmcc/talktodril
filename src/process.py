from bs4 import BeautifulSoup
import requests
import json
import markovify

# Get tweets
print("Collecting tweets...")
page = requests.get("https://cooltweets.herokuapp.com/dril/old")
soup = BeautifulSoup(page.content, "html.parser")
texts = soup.find_all("div", "text")
tweets = []
for text in texts:
    tweets.extend(text.text + "\n")

# Markovify tweets
print("Building model...")
text_model = markovify.NewlineText("".join(tweets))
with open("model.json", "w") as outfile:
    outfile.write(text_model.to_json())

print("...done!")