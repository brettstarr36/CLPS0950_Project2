print("Welcome to the Color Visual Acuity Game!") # welcoming message
intro_1 = input("enter 1 to continue ") # engagement to trigger directions
if intro_1 == "1" # confirm engagement
    print("Directions: You will be shown an image with a grid where")
    print("all the colors are of the same hue except one square")
    print("You will be shown a matrix of numbers")
    print("corresponding to the squares in the image")
    print("You will be asked to type the number")
    print("corresponding to the square that is a different hue") # displays instructions to participant
    intro_2 = input("enter 1 to continue"); % engagement to confirm understanding of part 1 of directions
else 
    disp('End game')% ends game if they do not want to enter 1 to play
    return % end script if they do not enter '1' to continue
end
if intro_2 == 1 % confirmation of part 1 of directions triggers part two of directions
        disp('The difficulty will increase as you')
        disp('progress futher along the game')
        disp('If you get the number wrong,') 
        disp('the game will end and your score will be displayed')
         intro_3 = input ('enter "1" if you are ready to begin \n'); % engagement to trigger the start of the game
    else 
        disp('End game')
             return % end script if they do not enter '1' to continue to part 2 of directions
end

% Game 
if intro_3 == 1 % confirms engagement to begin game
imshow(level1) %displays the image for level 1
disp(matrix2) %begin game
answer_1 = input('What square is a different color? \n'); % asks for number of correct square
         else 
             disp('End game')
    return % ending script if participant does not press '1' to begin game
end
if answer_1 == 3 % confirming correct answer   
    counter = counter +1; % adds a point to the score
     imshow(level2) % image 2
disp(matrix3) % answer matrix for question 2    
answer_2 = input('What square is a different color? \n'); % asks second question
else
	disp('End game') % ends game if wrong answer
    disp('score') %labels score
    disp(counter) % number of your score
    return % ends script
end
if answer_2 == 6 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level3) % displays image 3
    disp(matrix4') % displays answer matrix for question 3
    answer_3 = input('What square is a different color? \n'); % question 3
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_3 == 2 % confirming correct answer  
    imshow(level4)
    counter = counter +1; % adds a point to the score
disp(matrix5') % answer matrix for question 4    
answer_4 = input('What square is a different color? \n'); % asks 4th question
else
	disp('End game') % ends game if wrong answer
    disp('score') %labels score
    disp(counter) % number of your score
    return % ends script
end
if answer_4 == 10 % confirms correct answer 
    imshow(level5)
    counter = counter + 1; % adds point to score total
    disp(matrix6') % displays answer matrix for question 5
    answer_5 = input('What square is a different color? \n'); % question 5
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_5 == 28 % confirming correct answer   
    counter = counter +1; % adds a point to the score
    imshow(level6)
    disp(matrix6') % answer matrix for question 6    
    answer_6 = input('What square is a different color? \n'); % question 6
else
	disp('End game') % ends game if wrong answer
    disp('score') %labels score
    disp(counter) % number of your score
    return % ends script
end
if answer_6 == 16 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level7)
    disp(matrix6') % displays answer matrix for question 
    answer_7 = input('What square is a different color? \n'); % question 7
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_7 == 23 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level8)
    disp(matrix6') % displays answer matrix for question 
    answer_8 = input('What square is a different color? \n'); % question 8
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_8 == 3 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level9)
    disp(matrix6') % displays answer matrix for question 
    answer_9 = input('What square is a different color? \n'); % question 9
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_9 == 29 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level10)
    disp(matrix6') % displays answer matrix for question 
    answer_10 = input('What square is a different color? \n'); % question 10
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_10 == 33 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level11)
    disp(matrix6') % displays answer matrix for question 
    answer_11 = input('What square is a different color? \n'); % question 11
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_11 == 2 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level12)
    disp(matrix6') % displays answer matrix for question 
    answer_12 = input('What square is a different color? \n'); % question 12
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_12 == 18 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level13)
    disp(matrix6') % displays answer matrix for question 
    answer_13 = input('What square is a different color? \n'); % question 13
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_13 == 23 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level14)
    disp(matrix6') % displays answer matrix for question 
    answer_14 = input('What square is a different color? \n'); % question 14
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_14 == 31 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level15)
    disp(matrix6') % displays answer matrix for question 
    answer_15 = input('What square is a different color? \n'); % question 15
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_15 == 5 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level16)
    disp(matrix6') % displays answer matrix for question 
    answer_16 = input('What square is a different color? \n'); % question 16
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_16 == 28 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level17)
    disp(matrix6') % displays answer matrix for question 
    answer_17 = input('What square is a different color? \n'); % question 17
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_17 == 20 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level18)
    disp(matrix6') % displays answer matrix for question 
    answer_18 = input('What square is a different color? \n'); % question 18
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_18 == 25 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level19)
    disp(matrix6') % displays answer matrix for question 
    answer_19 = input('What square is a different color? \n'); % question 19
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_19 == 10 % confirms correct answer 
    counter = counter + 1; % adds point to score total
    imshow(level20)
    disp(matrix6') % displays answer matrix for question 
    answer_20 = input('What square is a different color? \n'); % question 20
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end
if answer_20 == 3 % confirms correct answer 
    congrats = imread('images/you-win-poster-with-prize-cup-vector-17052074.jpg');
    imshow(congrats)
    counter = counter +1;
    disp('Congrats! You completed all the levels!')
    disp('score') % labels score
    disp(counter) % displays score total
    return
else 
    disp('End game') % ends game if wrong answer   
    disp('score') % labels score
    disp(counter) % displays score total
    return
end