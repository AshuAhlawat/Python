#dictionaries as only values change not keys
randomn_input=str(input("your story : "))
randomn_words=randomn_input.split(" ")
randomn_wordcounter={}

for randomn_word in randomn_words:
    randomn_wordcounter[randomn_word]=randomn_wordcounter.get(randomn_word,0) + 1

for word in randomn_wordcounter:
    if randomn_wordcounter[word]==1:
        suffix=""
    else:
        suffix="s"
    print("{} appers {} time{}".format(word,randomn_wordcounter[word],suffix))