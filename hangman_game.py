import random
HANGMAN_PICS =['''
    +----+
         |
         |
         |
        ===''','''

   +----+
    o   |
        |
        |
       === ''','''
     +----+
     o    |
     |    |
          |
         === ''','''
     +----+
     o    |
    /|    |
          |
         === ''','''
     +----+
     o    |
    /|\   |
          |
         === ''','''
    +----+
     o    |
    /|\   |
    /     |
         === ''','''
   
     +----+
     o    |
    /|\   |
    / \   |
         ===''']


words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
#used split() to get list of words , list[] can be used -.-

def getRandomword(wordList):
     wordIndex=random.randint(0,len(wordList)-1)

     return wordList[wordIndex]


def displayBoard(missedletter,correctletter,secretletter):
    print(HANGMAN_PICS[len(missedletter)])
    print()

    print('Missed letters:',end=' ')
    for letters in missedletter:
        print(letters,end='')

    print()
    print('Length of Secret Word :',end=' ')
    blank='_'*len(secretletter)
    for i in range(len(secretletter)):
        if secretletter[i] in correctletter:
            blank=blank[:i]+secretletter[i]+blank[i+1:]

    for letter in blank:
        print(letter,end=' ')

    print()

def getguess(alreadyGuessed):
     
     print('Hint : It is a name of an animal')
     while True:
          
        print('Enter a guess: ')
        guess=input()
        guess=guess.lower()

        if len(guess)!=1:
            print('Enter a single letter :')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. ')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter a LETTER .')
        else:
            return guess


def playagain():
    print('Do you want to play again? y/yes:')
    return input().lower().startswith('y')

print('\nWELCOME TO HANGMAN GAME\n ')
missedletter=''
correctletter=''
secretletter=getRandomword(words)
gamedone=False

while True:
    displayBoard(missedletter,correctletter,secretletter)

    guess=getguess(missedletter+correctletter)

    if guess in secretletter:
        correctletter=correctletter+guess

        foundallletter=True

        for i in range(len(secretletter)):
            if secretletter[i] not in correctletter:
                foundallletter=False
                break

        if foundallletter:
            print('Yes the secret word is '+ ' '+secretletter+' ')
            gamedone=True

    else:
        missedletter=missedletter+guess

        if len(missedletter)==len(HANGMAN_PICS)-1:
             displayBoard(missedLetters, correctLetters, secretWord)
             print('You have run out of guesses!\nAfter ' )
             gamedone=True


    if gamedone:
        if playagain():
            missedletter=''
            correctletter=''
            gamedone=False
            secretletter=getRandomword(words)
        else:
             
             print('You have logged out from the game')
             break
        
            
     
     
 
