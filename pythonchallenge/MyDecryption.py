
print("#Notice: this will only work with if the alphabets are encrypted. And Not the Signs like +/- signs")
raw = input("Enter your Text here: ")
key = int(input("Enter the key: "))
result = ""
for c in raw:
    if 'a' <= c <= 'z':
        result += chr(((ord(c) + key) - ord('a')) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        result += chr(((ord(c) + key) - ord('a')) % 26 + ord('A'))
    else:
        result += c

print("Decrypted code: " +result)