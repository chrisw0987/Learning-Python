def word_counter(sentence):
    counter = 1
    for i in sentence:
        if i == " ":
            counter += 1
    print(counter)

word_counter("The Goofy Goober Is Goofy")