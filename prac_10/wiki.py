import wikipedia

word = input("Type a page TITLE to be summarised: ")

while word != "":
    try:
        print(wikipedia.summary(word))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    word = input("Type a page TITLE to be summarised: ")
