def game():
    return 445

score = game()
with open("ch9_prob2_hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr=='':
    with open("ch9_prob2_hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr) < score:
    with open("ch9_prob2_hiscore.txt", "w") as f:
        f.write(str(score))




#----------------------------------------------------------
# with open("ch9_prob2_hiscore.txt") as f:
#     hiscore = int(f.read())

# if hiscore < score:
#     with open("ch9_prob2_hiscore.txt", "w") as f:
#         f.write(str(score))