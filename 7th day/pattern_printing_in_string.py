#pattern printing in string using string slicing and negative indexing
word = "computer"

for i in range(-1 , -len(word)-1 , -1):
    print(word[i:])
