from Chef import Chef                                  #MAKES CHEF OBJECT ACCESSIBLE TO THIS FILE                      

class ChineseChef(Chef):                               #CHINESE CHEF INHERITS INFO FROM GENERAL CHEF OBJECT
    def make_special_dish(self):                       #CAN OVERWRITE THE SPECIAL DISH FUNCTION FROM GENERAL CHEF OBJECT
        print("The chef makes orange chicken!")
    def make_fried_rice(self):                         #HAS UNIQUE FUNCTION ONLY CHINESE CHEF CAN DO
        print("The chef makes fried rice!")
