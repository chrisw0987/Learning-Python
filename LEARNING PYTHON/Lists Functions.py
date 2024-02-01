lucky_numbers = [1, 2, 3, 4, 5, 6]
friends = ["Bob", "John", "Michael", "Jim"]
print(friends)

print(friends[2])

print(friends[1:])             #PRINTS NAMES FROM INDEX 1 TO END
print(friends[1:3])            #PRINTS NAMES FROM INDEX 1 TO 2(3-1)(BECAUSE LIST STARTS AT INDEX 0)

friends.extend(lucky_numbers)

friends.append("Jacky")        #THIS FUNCTION ADDS NAME AT END OF LIST
friends.insert(0,"George")     #THIS FUNCTION ADDS NAME AT SPECIFIC INDEX

friends.remove("Bob")          #THIS FUNCTION REMOVES A SPECIFIC NAME IN THE LIST
friends.clear()                #CLEARS ENTIRE LIST

friends2 = friends.copy()        #COPIES SPECIFIED LIST INTO NEW LIST
print(friends2)