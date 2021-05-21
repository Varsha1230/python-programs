with open("ch9_prob4_donkey.txt")as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("ch9_prob4_donkey.txt", 'w') as f:
    f.write(content)