import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Window parameters
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game")

# Text font
font = pygame.font.Font(None, 36)

# List of words to guess
words = ["python", "hangman", "programming", "game", "computer"]
word_to_guess = random.choice(words)

# Initialize variables
letters_found = []
letters_wrong = []
remaining_attempts = 7

# Game loop
running = True
while running:
    window.fill(WHITE)

    # Display the word to guess with the found letters
    word_display = ""
    for letter in word_to_guess:
        if letter in letters_found:
            word_display += letter + " "
        else:
            word_display += "_ "
    text_word = font.render(word_display, True, BLACK)
    window.blit(text_word, (50, 50))

    # Display the already guessed letters
    text_letters = "Guessed letters: " + ", ".join(letters_wrong)
    text_letters_render = font.render(text_letters, True, RED)
    window.blit(text_letters_render, (50, 100))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                guessed_letter = event.unicode.lower()
                if guessed_letter in word_to_guess:
                    letters_found.append(guessed_letter)
                else:
                    letters_wrong.append(guessed_letter)
                    remaining_attempts -= 1

    # Check for win
    if all(letter in letters_found for letter in word_to_guess):
        message_win = "Congratulations! You guessed the word: " + word_to_guess.upper()
        text_win = font.render(message_win, True, BLACK)
        window.blit(text_win, (50, 200))

    # Check for loss
    if remaining_attempts == 0:
        message_loss = "Too bad! The word to guess was: " + word_to_guess.upper()
        text_loss = font.render(message_loss, True, BLACK)
        window.blit(text_loss, (50, 200))

    pygame.display.flip()

pygame.quit()
