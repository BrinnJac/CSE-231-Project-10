'''Project 10
CSE 231
In this project, the user interacts with the program to play a
game of Solitarie'''

# Solitaire: Scorpion


#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

MENU = '''     
Input options:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau (column,row) to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''
#Function moves a card within the tableau
def move(T,col,row,d_col):
	co = validate_move(T,col ,row,d_col)
	if co:
		T[ d_col ].extend(T[ col ][ row: ]); T[ col ] = T[ col ][ :row ]
		if (row > 1 and not T[col  ][ row-1 ].is_face_up()):
			T[ col ][ row-1 ].flip_card()
	return co
#Function initialize the deck and separates the cards
def initialize():
	S = cards.Deck()
	S.shuffle()
	T = [[]for i in range(7)]; F = [[]for i in range(4)]
	for i in range(7):
		for j in range(7):
			T[j].append(S.deal())
	for i in range(3):
	    for j in range(3):
	        T[i][j].flip_card()
	return(S,T,F)
#Function displays the option menu and allows the user to enter input
def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau column,row to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
    '''
    option = input( "\nInput an option (DMRHQ): " )
    option_list = option.strip().split()
    
    opt_char = option_list[0].upper()
    
    if opt_char in 'DRHQ' and len(option_list) == 1:
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 4 and option_list[1].isdigit() and option_list[2].isdigit() and option_list[3].isdigit():
        return ['M',int(option_list[1]),int(option_list[2]),int(option_list[3])]

    print("Error in option:", option)
    return None
# Function checks if the user has won the game
def check_for_win(F):
    for i in F:
        if len(i) == F:
            return False
        else:
            return True
#Function displays the cards for the user
def display(S, T, F):
    print("\n{:<8s}{:s}".format( "stock", "foundation"))
    if S.is_empty():
        print("{}{}".format( " ", " "),end='')
    else:
        print("{}{}".format( " X", "X"),end='')
    for f in F:
        if f:
            print(f[0],end=' ')
        else:
            print("{}{}".format( " ", " "),end='') 
            
    print()
    print("\ntableau")
    print("   ",end=' ')
    for i in range(1,8):
        print("{:>2d} ".format(i),end=' ')
    print()
    # determine the number of rows in the longest column        
    max_col = max([len(i) for i in T])
    for row in range(max_col):
        print("{:>2d}".format(row+1),end=' ')
        for col in range(7):
            # check that a card exists before trying to print it
            if row < len(T[col]):
                print(T[col][row],end=' ')
            else:
                print("   ",end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole T   
#Function Restarts the game after shuffling
def restart():
	pass
#Deals cards to the Tableau
def deal_from_stock(S,T):
	for i in range(3):
		T[i].append(S.deal())    
#Function determines if a requested move by the user is valid
def validate_move(T,col,row,d_col):
	if not (d_col != col ):
		return False
	if (row < len(T[ col ]) and col>= 0 and col<7 and row>=0 and d_col>= 0 and d_col<7):
		if T[ col ][ row ].is_face_up():
			if (len(T[ d_col ]) == 0):
				if (T[ col ][ row ].rank() == 13): 
					return True
			elif (T[ col ][ row ].suit() == T[ d_col ][-1].suit()): 
				if(T[ col ][ row ].rank() == T[ d_col ][-1].rank()-1):
					return True
	return False

#Function Checks if a column in the tableau is a complete sequence from king down to ace of the same suit
def check_sequence(column_lst):
    pass
#Function checks if any column sequences are complete and calls check_sequence
def move_to_foundation(T,F):
    pass
#User interacts with this function as the main brain
def main():
    print("\nWelcome to Scorpion Solitaire.\n")
    S, T, F = initialize(); option = get_option()
    display(S, T, F)
    print(MENU)
    while option and option[0] != 'Q':
        if option == None:
            pass
        #Displays menu options
        elif option[0] == 'H':
            print(MENU)
        #Restarts the game
        elif option[0] == 'R':
            restart()
            #Deals to the Tableau
        elif option[0] == 'D':
            deal_from_stock(S,T)
            #Moves card in Tableau
        elif option[0] == 'M':
            co = move(T,option[1],option[2],option[3])
            if co == False: 
                print("Error in move:",option[0],",",option[1],",",option[2],",",option[3])
                #statement breaks the program
        elif option[0] == 'Q':
            break
        display(S,T,F)
        option = get_option()
    print("Thank you for playing.")

if __name__ == '__main__':
    main()