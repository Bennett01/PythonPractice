input = "sent"

def spin_words(sentence):
    results = []
    string = sentence.split()
    for word in string:
        if len(word) > 5:
            flipped = word[::-1]
            results.append(flipped)
        else:
            results.append(word)
    finished = ' '.join(results)
    return finished

print spin_words(input)
