with open("ch9_prob8_this.txt") as f:
    content=f.read()

    with open("ch9_prob8_copy.txt", "w") as f:
        f.write(content)