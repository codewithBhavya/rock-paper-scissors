import random
import pygame
import time   
pygame.mixer.init()
win_sound_path = "win_sound.wav"
lose_sound_path = "lose_sound.wav"
win_sound = pygame.mixer.Sound(win_sound_path)
lose_sound = pygame.mixer.Sound(lose_sound_path)
moves = ["rock", "paper", "scissors"]
score_limit = int(input("How many rounds would you like to play: "))
user_score = 0
computer_score = 0
while user_score < score_limit and computer_score < score_limit:
    user_move_input = input("Type your move: ").lower()
    if user_move_input not in moves:
        print("Please enter a valid move (rock, paper, scissors).")
        continue
    computer_move = random.choice(moves)
    print("Your move: " + user_move_input)
    print("Opponent Move: " + computer_move)
    if user_move_input == computer_move:
        print("It's a tie")
    elif (user_move_input == "rock" and computer_move == "scissors") or \
         (user_move_input == "paper" and computer_move == "rock") or \
         (user_move_input == "scissors" and computer_move == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
        

    print("Your score:", user_score)
    print("Computer's score:", computer_score)


if user_score >= score_limit:
    print("Congratulations! You reached the score limit. You win!")
    win_sound.play()
    
elif computer_score >= score_limit:
    print("Computer reached the score limit. Computer wins!")
    lose_sound.play()
time.sleep(2)
pygame.mixer.stop()
pygame.mixer.quit()