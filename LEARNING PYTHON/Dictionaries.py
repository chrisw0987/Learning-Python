monthConversions = {
    0: "January",                                      #SET KEY AND A ASSOCIATED VALUE
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",
}
print(monthConversions.get(0))
print(monthConversions.get("Luv", "Not a valid Key"))  #IF INPUT NOT IN DICTIONARY, THE SECOND ARGUMENT IS PRINTED BY DEFAULT