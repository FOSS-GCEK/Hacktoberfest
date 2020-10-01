import random
import pygame
import tkinter as tk
from tkinter import messagebox
import time
pygame.font.init()



def solve(board): 
    """ function to solve the given sudoku board"""         
    find = find_empty(board) #checks for empty box
    if not find:    #all boxes filled 
        return True     
    else:
        row, col = find #Empty box coordinates put into row and col variables

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board): #recursively solve for subsequent boxes until mistake is found
                return True

            board[row][col] = 0     # if mistake is found makes the box 0 again

    return False


def valid(board, num, pos):
    """ To check if entry into the board is in accordance with all rules"""
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3): 
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board): 
    """to print the solution"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """ returns row and column coordinates of empty box"""
    for i in range(len(board)):    #loop to traverse rows
        for j in range(len(board[0])):     #loop to traverse rows
            if board[i][j] == 0:
                return (i, j)  # (row, col)

    return None

'''print_board(q_board)
solve(q_board)
print("___________________")
print_board(q_board)'''




#from solver import solve, valid



class Grid:     #GRID HOLDS CUBE OBJECTS
    
    boards= [
    [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ],
    [
        [3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]
    ], 
    [ [0,0,4,0,0,0,0,6,7],
    [3,0,0,4,7,0,0,0,5],
    [1,5,0,8,2,0,0,0,3],
    [0,0,6,0,0,0,0,3,1],
    [8,0,2,1,0,5,6,0,4],
    [4,1,0,0,0,0,9,0,0],
    [7,0,0,0,8,0,0,4,6],
    [6,0,0,0,1,2,0,0,0],
    [9,3,0,0,0,0,7,1,0]]

]
    random.shuffle(boards) # to randomly generate board
    q_board=boards[0]       # question board generated


    def __init__(self, rows, cols, width, height): 
        """ initializing variable """
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.q_board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
            #initialising cube         
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        """ initializing cube class"""
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        """Draws individual cubes - selection , text entry and temporary entry"""
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0: #temporary entry
            text = fnt.render(str(self.temp), 1, (128,128,128)) #number value and style set
            win.blit(text, (x+5, y+5))  #number drawn onto pygame window
            #number put on topleft corner 
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 255))  
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))   
            #number put in between the square

        if self.selected: #selected box becomes red
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val #entered number put in value

    def set_temp(self, val):
        self.temp = val #entered number put in temp


def redraw_window(win, board, time, strikes):
    """Updates pygame window after every entry """
    win.fill((255,255,255))
    # timer:
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Strikes:
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    #Draw cubes and thick lines (whole board)
    board.draw(win)


def format_time(secs):
    """for timer"""
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    win = pygame.display.set_mode((540,600)) #window size
    pygame.display.set_caption("Sudoku") #window title
    board = Grid(9, 9, 540, 540) #grid display
    key = None
    run = True
    start = time.time()
    strikes = 0 #wrong moves
    while run:

        play_time = round(time.time() - start) #timer calculation

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #window close
                run = False
            if event.type == pygame.KEYDOWN: #check which key is pressed to enter respective number to board
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE: #clear entry
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN: #correct entry
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success") #log correct
                        else:
                            print("Wrong") #log incorrect
                            strikes += 1 #total wrong moves
                        key = None

                        if board.is_finished():
                            print("Game over!!")
                            message_box('GAME OVER!!! :',play_time )
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


main()
pygame.quit()