def translate(phrase):                          #DECLARE FUNCTION THAT TAKES IN A PHRASE ARGUMENT
    translation = ""                            #FINAL OUTPUT
    for letter in phrase:                       #LOOP THROUGH PHRASE INPUT
        if letter.lower() in "aeiou":           #CHECK IF LETTER IS A VOWEL
            if letter.isupper():                #ACCOUNTS FOR UPPERCASE PHRASE INPUT
                translation = translation + "G" #CHANGE PHRASE INPUT INDEX TO 'G'
            else:
                translation = translation + "g" #CHANGE PHRASE INPUT INDEX TO 'g'
        else:
            translation = translation + letter  #IF NOT A VOWEL, INCREMENT PHRASE INDEX AND MOVE ON
    return translation                          #RETURN FINAL OUTPUT


print(translate(input("Enter a phrase: ")))    #MAIN TEST CASE