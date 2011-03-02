#!/usr/bin/env python
print ">>> Connect 4! <<<"

global EMPTY, BLACK, WHITE, a, b, c, d, e, f, g
EMPTY = " "
BLACK = "X"
WHITE = "O"
a = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
b = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
c = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
d = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
e = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
f = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
g = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]

# >>> Combo Database Update Routine
COMBOS = lambda: [
        (a[0],a[1],a[2],a[3]),
        (a[1],a[2],a[3],a[4]),
        (a[2],a[3],a[4],a[5]),
        (b[0],b[1],b[2],b[3]),
        (b[1],b[2],b[3],b[4]),
        (b[2],b[3],b[4],b[5]),
        (c[0],c[1],c[2],c[3]),
        (c[1],c[2],c[3],c[4]),
        (c[2],c[3],c[4],c[5]),
        (d[0],d[1],d[2],d[3]),
        (d[1],d[2],d[3],d[4]),
        (d[2],d[3],d[4],d[5]),
        (e[0],e[1],e[2],e[3]),
        (e[1],e[2],e[3],e[4]),
        (e[2],e[3],e[4],e[5]),
        (f[0],f[1],f[2],f[3]),
        (f[1],f[2],f[3],f[4]),
        (f[2],f[3],f[4],f[5]),
        (g[0],g[1],g[2],g[3]),
        (g[1],g[2],g[3],g[4]),
        (g[2],g[3],g[4],g[5]),
        (a[1],b[1],c[1],d[1]),
        (b[1],c[1],d[1],e[1]),
        (c[1],d[1],e[1],f[1]),
        (a[2],b[2],c[2],d[2]),
        (b[2],c[2],d[2],e[2]),
        (c[2],d[2],e[2],f[2]),
        (a[3],b[3],c[3],d[3]),
        (b[3],c[3],d[3],e[3]),
        (c[3],d[3],e[3],f[3]),
        (a[4],b[4],c[4],d[4]),
        (b[4],c[4],d[4],e[4]),
        (c[4],d[4],e[4],f[4]),
        (a[5],b[5],c[5],d[5]),
        (b[5],c[5],d[5],e[5]),
        (c[5],d[5],e[5],f[5]),
        (a[0],b[1],c[2],d[3]),
        (b[0],c[1],d[2],e[3]),
        (c[0],d[1],e[2],f[3]),
        (d[0],e[1],f[2],g[3]),
        (a[1],b[2],c[3],d[4]),
        (b[1],c[2],d[3],e[4]),
        (c[1],d[2],e[3],f[4]),
        (d[1],e[2],f[3],g[4]),
        (a[2],b[3],c[4],d[5]),
        (b[2],c[3],d[4],e[5]),
        (c[2],d[3],e[4],f[5]),
        (d[2],e[3],f[4],g[5]),
        (g[0],f[1],e[2],d[3]),
        (f[0],e[1],d[2],c[3]),
        (e[0],d[1],c[2],b[3]),
        (d[0],c[1],b[2],a[3]),
        (g[1],f[2],e[3],d[4]),
        (f[1],e[2],d[3],c[4]),
        (e[1],d[2],c[3],b[4]),
        (d[1],c[2],b[3],a[4]),
        (g[2],f[3],e[4],d[5]),
        (f[2],e[3],d[4],c[5]),
        (e[2],d[3],c[4],b[5]),
        (d[2],c[3],b[4],a[5]),
    ]


# >>> Definitions
def main():
    global COMP,HUMN 
    response = raw_input("\nWould you like to go first [y/N]?: ").lower()
    print "At any time, just type 'exit' or 'quit' to leave the game...\n"
    if response[0] != "y":
        COMP = WHITE
        HUMN = BLACK
        comp_move()
    else:
        COMP = BLACK
        HUMN = WHITE
        draw_board()
        human_move()
    # Instead of putting things in a loop, I've set it so that the AI/HUMN functions run their course, and then call each other.
    # The AI function calls the main algorithm which is expected to not only interpret possible AI moves, but to be aware of the 
    # game STATE, as I like to call it. (In a way, it is a loop, but there is more control over it...)

def draw_board():
    # This relies completely on globals. There is an easier way to code this, but for right now,
    # it helps to be able to visualize the board when coding.
    print "6 | %s | %s | %s | %s | %s | %s | %s |" % (a[5],b[5],c[5],d[5],e[5],f[5],g[5])
    print "5 | %s | %s | %s | %s | %s | %s | %s |" % (a[4],b[4],c[4],d[4],e[4],f[4],g[4])
    print "4 | %s | %s | %s | %s | %s | %s | %s |" % (a[3],b[3],c[3],d[3],e[3],f[3],g[3])
    print "3 | %s | %s | %s | %s | %s | %s | %s |" % (a[2],b[2],c[2],d[2],e[2],f[2],g[2])
    print "2 | %s | %s | %s | %s | %s | %s | %s |" % (a[1],b[1],c[1],d[1],e[1],f[1],g[1])
    print "1 | %s | %s | %s | %s | %s | %s | %s |" % (a[0],b[0],c[0],d[0],e[0],f[0],g[0])
    print "--| a | b | c | d | e | f | g |"


def quit(message, draw=True):
    if draw == True:
        draw_board()
    print message
    exit()
    
def check_state():
    # I recently realized that even though the COMBOS array was global, it would not provide absolute references to the a,b,c,d,e,f,g arrays.
    # But lambda solves this problem very elegantly.
    combos = COMBOS()
    # Check if game is over.
    for win in combos:
        if win[0]+win[1]+win[2]+win[3] == COMP*4:
            quit("The computer has won.")
        if win[0]+win[1]+win[2]+win[3] == HUMN*4:
            quit("Human has won.")
        # Insert super-awesome algorithm here. If a move has not been determined, then continue. Else, make it.

        # Base : Find a win in combos that is within gravitational restraints and brute force into making that win.
            # If Case 1 occurs OR if a necessary location in Base is taken by human, reload Base and try again.
                # It may occur that Base will be reloaded to the SAME Base. This is OK.
        # Case 1. If there is a possible human victory in the next move, block it. If computer is first, skip to #2.
        # Case 2. If there is a possible computer victory in the next move, make it. If there is a gravity error;
            # a) find another winning move
            # b) find a different Base
        # Regardless of Base or STATE status, once a move is determined, run the according set of evaled column, row assignments.
            # If there is a computer win and a human win in the next move, make the computer win.
            

def help_text(flargh):
    print "Your error involves",flargh
    print "An example of a correct input (locator) would be: a,1"
    human_move()

def human_move():
    coords = raw_input("\nConnect4 [Option] <column>,<row>: ").lower()
    quitting = ['exit','quit']
    if coords in quitting:
        quit("Game Over...", False)
    # Petty error handling.
    yAlpha = ['a','b','c','d','e','f','g']
    if len(coords) != 3 or coords[1] != ',':
        help_text("a misformed locator.")
    if coords[0] not in yAlpha:
        help_text(coords[0]+" being out of the acceptable range [a-g].")
    if eval(coords[2]) not in range(1,6):
        help_text(coords[2]+" being out of the acceptable range [1-6].")
    # Works brilliantly. Much easier to implement than I thought as well!
    if eval(coords[0])[eval(coords[2])-1] == EMPTY:
        if eval(coords[2])-2 < 0:
            pass
        else:
            if eval(coords[0])[eval(coords[2])-2] == EMPTY:
                print "Illegal Move: Gravity Error."
                human_move()
        eval(coords[0])[eval(coords[2])-1] = HUMN
        print "HUMAN:"
        draw_board()
        comp_move()
    else:
        print "Illegal Move: That spot has been taken."
        human_move()

def comp_move():
    check_state()
    print "COMPUTER:"
    # This is done so that if additional difficulties are added, the general display routine would not be interrupted.
    # (I don't want draw_board() or such to be in check_state().)
    draw_board()
    human_move()

# Ta-daaaa!!!
main()
