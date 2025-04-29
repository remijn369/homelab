# #### conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#       #                           print or assign one of two values based on a condition
#       #                          x if condition else y
#
#
#  #example
#
#
# num = 5
# age =17.5
#
# user_role = "guest"
#
# today_weather  = 34
# today_weather= "hot" if today_weather >30 else "cold"
# result = "Adult" if age > 18 else "teenager"
# #result = "even" if   x  % 2 == 0 else "ODD"
#
# #result = "high" if num > 24 else "LOW"
#
# user_role = "full access granted"if user_role == "admin" else "limited access is granted"
#
# print(today_weather)


### few useful string usage that might be handy

#name = input("Enter your phone # ?:")
#result =len(name)
#result = name.find("b")
#result = name.rfind("e")
#name = name.upper()
#name = name.lower()
#name  = name.capitalize()
#result = name.isdigit()

# result= name.phone_number =234-3444-2332
# print(result)




# while loop = execute some code WHILE other condition remains true

name =input("what is your name")

while name == "":
    print(f"you need to input your user name")
