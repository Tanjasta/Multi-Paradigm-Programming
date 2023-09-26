#https://stackoverflow.com/questions/62544969/creating-a-greeting-program-which-only-accepts-specific-users-and-invalidates-an


names = ("Alice", "Bob")
name = input("Please type your name:")
if name == "Alice":
   print("Hello Alice")
elif name == "Bob":
   print("Hello Bob")
else:
 print("Wrong name")
