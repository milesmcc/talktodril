import markovify
import random

def generate_sentence(model, start=None):
    if start == None or len(start.strip()) == 0:
        return model.make_sentence(max_words=30)
    else:
        start = start.split(" ")
    try:
        return " ".join(start[:-2]) + " " + model.make_sentence_with_start(" ".join(start[-2:]), strict=False, max_words=30)
    except:
        return " ".join(start) + " " + model.make_sentence_with_start(random.choice(["for", "and", "but", ".", "!"]), strict=False, max_words=30)

if __name__ == "__main__":
    with open("model.json", "r") as infile:
        model = markovify.NewlineText.from_json(infile.read())
        for i in range(50):
            print(generate_sentence(model, "we can"))