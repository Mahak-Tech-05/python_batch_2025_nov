#write operation
with open("sample.txt","w") as f:
    f.write("Hello world \n")
    f.write("this is written using my python code file")

#apppending the file data
    
with open("sample.txt","a") as f:
    f.write("\n This is new line inserted using python")

#multiple lines
lines = ["line1 ", "\n line2" , "\n line 3"]
with open("multiline_store.txt","w") as f:
    f.writelines(lines)
