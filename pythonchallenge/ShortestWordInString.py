long_string = "Find the shortest word in the string using Python"

tokens_string = long_string.split(" ")

print(tokens_string)

length_tokens = []

for token in tokens_string:

     length_tokens.append(len(token))

length_tokens.sort()

print(length_tokens[0])