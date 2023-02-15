def hangman(word, temp):
    attempts = 8
    word = word.lower()
    word_list = list(word)
    guessed = ['-'] * len(word_list)
    used_letters = []
    guess = ""
    win = 0
    lost = 0

    while attempts > 0:
        print("".join(guessed))
        letter = input("Input a letter: ")
        if (len(letter) != 1):
            print("Please, input a single letter")

        if (not(letter.islower()) or not(letter.isascii())):
            print("Please, enter a lowercase letter from the English alphabet")

        if ((letter.islower()) and (len(letter) == 1)):

            if letter in used_letters:
                print("You've already guessed this letter.")

            elif letter in word_list:
                for i in range(len(word_list)):
                    if word_list[i] == letter:
                        guessed[i] = letter
                used_letters.append(letter)



            elif not (letter in word_list):
                print("That letter doesn't appear in the word.")
                used_letters.append(letter)
                attempts -= 1
            if "-" not in guessed:
                for i in range (len(guessed)):
                    guess +=guessed[i]
                print("You guessed the word " + guess+"!")
                print("You survived!")
                win += 1
                return 1

    print("You lost!")
    lost += 1
    return 0




import  random
print ("H A N G M A N\nThe game will be available soon.")
words = ('python', 'java', 'swift', 'javascript')
rand_word=random.choice(words)
word = random.choice(words)
lost = 0
win = 0

while True:
    temp = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if temp == "play":

        if (hangman(word,temp)):
            win += 1
        else:
            lost += 1
    elif temp == "results":
        print("You won:",win, "times.")
        print("You lost: ",lost," times.")

    elif temp == "exit":
        break

