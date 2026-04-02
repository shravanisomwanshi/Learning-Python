words = ["donkey", "bad", "ganda"]

with open("CHAPTER 9/1file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word)) 

with open("1file.txt", "w") as f:   
    f.write(content)    