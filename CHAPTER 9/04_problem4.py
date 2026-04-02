word = "Donkey"  

with open("CHAPTER 9/1file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("1file.txt", "w") as f:
    f.write(contentNew)