
score = 0
while True:
    answer = input("Answer: ")
    if answer == "24":
        print("correct")
        score += 1
    else:
        print("game over")
        print("score")
        print(score)
        break