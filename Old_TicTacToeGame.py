#Lang Kenney
#HMWK9.py
#11/03/2005

from graphics import *
from random import *
from button import *

class BoardModel:
    """A BoardModel is a model or representation of the tic-tac-toe board.
    It is typically represented using a list [...] of markers indicating
    the contents of specific location. Exteranlly, the board presents an
    interface of (x,y) locations to simplify developing players and to
    encapsulate the internal data structure"""
    
    def __init__(self, n):
        """Constructor for board"""
        self.n = n
        board = {}
        for i in range(n):
            for j in range(n):
                board[(i,j)] = " "
            
        self.board = board
        
        
    def clone(self):
        """Make a copy of the current board. This should return a new
        BoardModel that with a replaced internal list"""
        copy = BoardModel(self.n)
        for i in range(self.n):
            for j in range(self.n):
                copy.board[(i,j)] = self.board[(i,j)]
        
        return copy
        
        
    def get(self, x, y):
        """Get the contents of the board at location (x,y)"""
        return self.board[(x,y)]

    def set(self,x,y,value):
        """Set the contents of the board at location (x,y) to value """
        self.board[(x,y)] = value
        
    def getn(self):
        return self.n

    def checkrow(self,row,col,who):
        """You will make this routine be a tail-recursive subroutine
        that checks that each location in a specific row is equal
        to "who". The statement "pass" below means "do nothing". """
        
        if self.get(col,row) != who:
            return False
            
        elif col == self.n-1:
            return True
        else:
            return self.checkrow(row,col+1,who)
             
    
    def checkcol(self,row,col,who):
        """You will make this routine be a tail-recursive subroutine
        that checks that each location in a specific column is equal
        to "who". """
        if self.get(col,row) != who:
            return False
        elif row == self.n-1:
            return True
        else:
            return self.checkcol(row+1,col,who)
             
    
    def checklr(self,rowcol,who):
        """You will make this routine be a tail-recursive subroutine
        that checks that each location in the left-to-right diagonal
        is equal to "who". """
        
        if self.board[(rowcol,rowcol)] != who:
            return False
        elif rowcol == self.n-1:
            return True
        else:
            return self.checklr(rowcol+1,who)
        
    
    def checkrl(self,rowcol,who):
        """You will make this routine be a tail-recursive subroutine
        that checks that each location in the right-to-left diagonal
        is equal to "who". """
        if self.board[(rowcol-1,self.n-rowcol)] != who:
            return False
        elif rowcol == 1:
            return True
        else:
            return self.checkrl(rowcol-1,who)
        

    def checkwin(self, who):
        """Check to see if the board represents a "win" for player "who".
        This should return True/False if there is a win/no-win"""
        ##
        ## Check horizontal
        ##
        
        for i in range(self.n):
            if self.checkrow(i,0,who)== True:
                return True
    
        ##
        ## Check vertical
        ##
        
        for i in range(self.n):
            if self.checkcol(0,i,who) == True:
                return True
       
        ##
        ## Left diagonal
        ##
        if self.checklr(0,who) == True:
            return True
        
        ##
        ## Right diagonal
        ##
        if self.checkrl(self.n,who) == True:
            return True
       
        ##
        ## None of the winning patterns worked
        ##
        return False

class BoardView:
    def __init__(self,n):
        self.n = n
        self.count = 0
        self.board = BoardModel(n)
        self.win = GraphWin("Tic Tac Toe", max(n * 50, 400), max(n * 50 + 100,400))
        self.win.setCoords(0.0, -1.0, float(n), float(n))
        self.msgtxt = Text(Point(self.n/2.0, -0.5), "")
        self.msgtxt.setSize(30)
        self.msgtxt.setStyle("bold")
        for x in range(n-1):
            x = x + 1
            v = Line(Point(x,0), Point(x,n))
            v.setWidth(5)
            v.draw(self.win)
            h = Line(Point(0,x), Point(n,x))
            h.setWidth(5)
            h.draw(self.win)

    def getboard(self):
        return self.board.clone()

    def getn(self):
        return self.n

    def _drawimg(self, location, image, fallback):
        """ Draw the X or O -- we put in a "counter" that helps show the sequence of play """
        self.count += 1
        try:
            img = Image(location, image)
            img.draw(self.win)
        except:
            print "Unable to open graphics image", image
            f = "%s-%d" % (fallback, self.count)
            letter = Text(location, f)
            letter.setSize(30)
            letter.draw(self.win)
    
    def makemove(self, x, y, player):
        """Put a marker at location (x,y) for player "player".
        The player must be either "X" or "Y". We raise an error
        if you try to play on an existing location, just to help
        debugging."""
        if not self.checkmove(x,y):
            print "ERRROR: trying to play marker on occupied spot"
            raise NameError()
        self.board.set(x,y,player)
        location = Point(x + 0.5, y + 0.5)
        if player == "X":
            self._drawimg(location, "x.gif", player)
        else:
            self._drawimg(location, "o.gif", player)

    def playerwins(self, player):
        """Check to see if player "player" wins the game.
        Returns True/False"""
        return self.board.checkwin(player)

    def checkmove(self, x, y):
        """ Check to see if we can make a move (place a marker
        at the (x,y) location. """
        return self.board.get(x,y) == " "

    def singlemove(self):
        while True:
            p = self.win.getMouse()
            x = p.getX()
            y = p.getY()
            if (x >= 0 and x < self.n and y >= 0 and y < self.n) and self.checkmove(int(x),int(y)):
                return int(x), int(y)

    def msg(self, text, size=20, color = "green", needclick = False):
        """Place a message 'text' in the message window in the specified
        textsize and color. If needclick is true, wait for a mouse click
        from the user before continuing, otherwise exit immediately"""
        self.msgtxt.setText(text)
        self.msgtxt.setTextColor(color)
        self.msgtxt.setSize(size)
        self.msgtxt.draw(self.win)
        if needclick:
            self.win.getMouse()

    def msgclear(self):
        self.msgtxt.undraw()

    def close(self):
        self.win.close()

class Player:
    """A Player represents the logic of a player in the
    tic-tac-toe game. This class is never really used;
    it simply defines the interface common to all players """

    def getplayer(self):
        """This method will cause your program to stop and give an error
        if a subclass (HumanPlayer or BadAIPlayer) does not redefine
        it."""
        raise NotImplementedError()
    
    def play(self):
        """This method will cause your program to stop and give an error
        if a subclass (HumanPlayer or BadAIPlayer) does not redefine
        it."""
        raise NotImplementedError()

class HumanPlayer(Player):
    """A HumanPlayer represents human player. """
    
    def __init__(self, board, marker):
        self.board = board
        self.marker = marker

    def getplayer(self):
        """ Notice that this is a reimplementation of getplayer in the
        Player parent class."""
        return self.marker

    def play(self):
        self.board.msg("Click spot for player %s" % self.marker)
        x,y = self.board.singlemove()
        self.board.msgclear()
        self.board.makemove(x,y, self.marker)

class BadAIPlayer(Player):
    """This is the BadAIplayer you're supposed to implement. """
    
    def __init__(self, board, marker, debug=False):
        """Create the player with the indicated marker and
        provide it the board it will use for play"""
        self.board = board
        self.marker = marker
        if marker == "X":
            self.Human = "O"
        else:
            self.Human = "X"
            
    def getplayer(self):
        """Needs a definition"""
        return self.marker
        

    def play(self):
        """ Play the move for your marker """
        board2 = self.board.getboard()
        for i in range(self.board.getn()):
                for j in range(self.board.getn()):
                    if self.board.checkmove(i,j):
                        board2.set(i,j, self.marker)
                        win = board2.checkwin(self.marker)
                        if win == True:
                            self.board.makemove(i,j, self.marker)
                            return
                        else:
                            board2.set(i,j," ")
                            
         
        for i in range(self.board.getn()):
                 for j in range(self.board.getn()):
                    if self.board.checkmove(i,j):
                        board2.set(i,j,self.Human)
                        loose = board2.checkwin(self.Human)
                        if loose == True:
                            self.board.makemove(i,j, self.marker)
                            return
                        else:
                            board2.set(i,j," ")
                            

        while True:
            i = randint(0,self.board.getn()-1)
            j = randint(0,self.board.getn()-1)
            if self.board.checkmove(i,j):
                self.board.makemove(i,j, self.marker)
                return

    
def choosePlayer(board, marker):
    """ This routine pops up a window that asks the user what kind of player
    should be created for the specified marker """
    buttonwin = GraphWin("Select %s Player" % marker)
    Text(Point(100,50),"Select the player for %s" % marker).draw(buttonwin)
    Text(Point(100,150), "Click window to continue").draw(buttonwin)
    ai = Button(buttonwin, Point(100,75), 100, 25, "AI Player")
    human = Button(buttonwin, Point(100,125), 100, 25, "Human Player")
    ai.activate()
    human.activate()
    m = buttonwin.getMouse()
    buttonwin.close()
    if ai.clicked(m):
        return BadAIPlayer(board, marker)
    else:
        return HumanPlayer(board, marker)

def main():
    firstwin = GraphWin("Select Board Size")
    Text(Point(100,50),"Select the board size").draw(firstwin)
    Text(Point(100,150), "Click window to continue").draw(firstwin)
    e = Entry(Point(100,100), 4)
    e.setText("3")
    e.draw(firstwin)
    p = firstwin.getMouse()
    n = eval(e.getText())
    firstwin.close()
    #
    # Now, play game
    #
    board = BoardView(n)

    ##
    ## Create the players
    ##
    xplayer = choosePlayer(board, "X")
    oplayer = choosePlayer(board, "O")

    for player in [ xplayer, oplayer ] * ((n*n)/2) + [xplayer]*(n%2):
        player.play()
        if board.playerwins(player.getplayer()):
            board.msg("%s Wins!" % player.getplayer(), size = 30, color="red", needclick=True)
            board.close()
            return
    board.msg("It's A Draw", size = 30, color="red", needclick=True)
    board.close()

main()
