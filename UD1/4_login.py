
correct_user="admin"
correct_passwd="1234"

user= input("User: ")
passwd= input("Password: ")

if user == correct_user and passwd == correct_passwd:
   print("Allow acces ")
else:
  print("Denied acces")

