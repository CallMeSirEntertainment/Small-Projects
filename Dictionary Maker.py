import csv
from nltk.corpus import wordnet as wn
charcount = int(input("How many letters would you like as the maximum length?\n"))
with open(f'dictionary (letter-per-word-limit {charcount}).csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["word", "def"])
    words = wn.words()
    for word in words:
        if len(word) > charcount:
            continue
        synsets = wn.synsets(word, lang='eng')
        if synsets:
            definitions = []
            for i, synset in enumerate(synsets, start=1):
                definitions.append(f"({i}) {synset.definition()}")
            writer.writerow([word, ' '.join(definitions)])