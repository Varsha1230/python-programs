words = ["donkey", "kaddu", "mote"]
with open("ch9_prob5_sample.txt") as f:
     content=f.read()

for word in words:
    content= content.replace(word, "$%^@$^#")
    with open("ch9_prob5_sample.txt", "w") as f:
        f.write(content)