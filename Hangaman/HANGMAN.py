import random
import hangman_art
import hangman_words

print (hangman_art.logo)

print("\n\n\n\t\t\t\t\tWELCOME TO HANGMAN \n\n\nYOU HAVE GOT 7 LIVES IF THE 7 LIVES ARE GONE THE GAME WILL END ")

print("\nYOU CAN GET HINT FOR 2 LETTERS")

hints, lives = 2 , 7

correct_guess , wrong_guess = [] ,[]

random_word = random.choice(hangman_words.word_list)

list_store = ['_' for i in range (len(random_word))]

while lives > 0 :
   
    if "_" in list_store :
    
        guessed_letter = input("\nGUESS THE LETTER : ").lower()
    
        if len(guessed_letter) >= 2 : 
            print("\nENTER A SINGLE ALPHABET")
    
        else :
            j = 0
    
            for i in random_word :
    
                if i == guessed_letter:
                    list_store[j] = i
    
                j+=1

        if guessed_letter not in random_word :
            lives -= 1
            print("\nOOPS YOU HAVE ENTERED A WRONG LETTER\n\nTOTAL LIVES - ", lives)
            print(hangman_art.stages[lives])
            wrong_guess.append(guessed_letter)

        else :
            correct_guess.append(guessed_letter)

        print(list_store)

        print("\nCORRECT GUESSES  : ", correct_guess) 

        print("\nWRONG GUESSES : ", wrong_guess) 

        if lives > 0 and hints >0 :
            hint = input("\nDO YOU WANT HINT 'Y' OR 'N : ").lower()

        if hint == "y" :
            position = int(input("\nENTER THE POSITION: "))
            print(random_word[position - 1])
            hints-=1
            
    else :
        break

if lives > 0 :
    print("\nYAY YOU WON THE GAME\n :)")

else :
    print("\nSORRY YOU LOST\t\t:(\n\nCORRECT ANSWER IS - ", random_word.upper())
    