def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i].upper()
        result += chr((ord(char) + s-65) % 26 + 65)
    return result

string = "andare"
offset = 5
print(encrypt(string,offset))
