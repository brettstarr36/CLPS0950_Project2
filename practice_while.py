score = 0
while True:
    name = input('Answer: ')
    if name != "24":
        print("game over")
        print("score")
        print(score)
        break
    else:
        print("correct")
        score +=1