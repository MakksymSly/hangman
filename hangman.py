import math

words_hard = ["abbreviate",
"abdication",
"abdominous",
"backsplash",
"backstroke",
"bacteritic",
"campestral",
"cancelling",
"Candelario",
"eyeglasses",]
words_medium = ["abyss",
"acene",
"achoo",
"blitz",
"bloom",
"Boldt",
"cache",
"cabin",
"delta",
"disco",]
words_easy = ["ask",
"ash",
"dog",
"fog",
"eye",
"can",
"bus",
"sus",
"web",
"arm",
]

def hangman(word):
    wrong = 0
    stages = ["",
            "__________      ",
            "|               ",
            "|               ",
            "|        |      ",
            "|        O      ",
            "|       /|\     ",
            "|       / \     ",
            "|               ",
             ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to the game")
    while wrong<len(stages)-1 :
        print("\n")
        msg = "Enter a char"
        print(rletters)
        char = input(msg)
        
       
       
       
        if char in rletters:
            guess = rletters.index(char)
            board[guess] = char
            rletters[guess] = "$"
        
        
        
        else:
            wrong += 1




        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        
        
        if "_" not in board:
            print("you won. the word is:")
            print("".join(board))
            win = True
            break
    
    
    
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose. The word is {}".format(word))

def start():

    levelmode = "Type difficult (hard)||(medium)||(easy) or (exit)"
    ask = input(levelmode)
    if ask == "hard" :
        hangman(words_hard[math.ceil(9)])
    elif ask == "medium" :
        hangman(words_medium[math.ceil(9)])
    elif ask == "easy":
        hangman(words_easy[math.ceil(9)])
    elif ask == "exit":
        exit()
    else:
        print("!!!!Type difficult mode!!!!!")
        start()
        

    




start()
