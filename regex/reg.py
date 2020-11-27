from re import search

regex= "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
password = "Password123"
print(search(regex, password))