import pygame

# define a bunch of constants/variables
WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
BLUE = (0 , 0 , 255)
RED = (255 , 0 , 0)
WINDOW_X , WINDOW_Y = 500 , 500
WINDOW_SIZE = (WINDOW_X , WINDOW_Y)
FPS = 30
#  1 | 2 | 3
# ---|---|---
#  4 | 5 | 6
# ---|---|---
#  7 | 8 | 9
# insert numbers from 1 to 9 to keep track of taken positions
taken_tiles = []
# insert numbers from 1 to 9 to keep track of tiles that have crosses
tiles_with_crosses = []
# top left corner (not quite) of the tiles
# it is used for drawing a cross/circle in the correct position
POSITION_1 = (WINDOW_X/40 , WINDOW_Y/40)
POSITION_2 = ((WINDOW_X/3)+(WINDOW_X/40) , (WINDOW_Y/40))
POSITION_3 = ((WINDOW_X/3*2)+(WINDOW_X/40) , (WINDOW_Y/40))
POSITION_4 = ((WINDOW_X/40) , (WINDOW_Y/3)+(WINDOW_Y/40))
POSITION_5 = ((WINDOW_X/3)+(WINDOW_X/40) , (WINDOW_Y/3)+(WINDOW_Y/40))
POSITION_6 = ((WINDOW_X/3*2)+(WINDOW_X/40) , (WINDOW_Y/3)+(WINDOW_Y/40))
POSITION_7 = ((WINDOW_X/40) , (WINDOW_Y/3*2)+(WINDOW_Y/40))
POSITION_8 = ((WINDOW_X/3)+(WINDOW_X/40) , (WINDOW_Y/3*2)+(WINDOW_Y/40))
POSITION_9 = ((WINDOW_X/3*2)+(WINDOW_X/40) , (WINDOW_Y/3*2)+(WINDOW_Y/40))

# this thing literally does everything lol
class Game:

    def __init__(self , LINE_WEIGHT):
        # creates the screen object
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        # creates the constant for the width of the drawn lines
        self.LINE_WEIGHT = LINE_WEIGHT
        # keeps track of whose turn it is
        self.player_1 = 1
        #symbolizes that the game is running (it stops when this is set to False)
        self.run = True


    def draw_game_area(self):
        for i in range(1 , 3):
            pygame.draw.line(
                surface = self.window,
                color = BLACK,
                start_pos = (WINDOW_X/3*i , 0),
                end_pos = (WINDOW_X/3*i , WINDOW_Y),
                width = self.LINE_WEIGHT
            )
        for i in range(1 , 3):
            pygame.draw.line(
                surface = self.window,
                color = BLACK,
                start_pos = (0 , WINDOW_Y/3*i),
                end_pos = (WINDOW_X , WINDOW_Y/3*i),
                width = self.LINE_WEIGHT
            )

    # draws two lines perpendicular to one another to form a cross
    def draw_cross(self , position):
        pygame.draw.line(
            surface = self.window,
            color = BLUE,
            start_pos = (
                (position[0]+WINDOW_X/3)-(WINDOW_X/15),
                position[1]
            ),
            end_pos = (
                position[0],
                (position[1]+WINDOW_Y/3)-(WINDOW_Y/15)
            ),
            width = self.LINE_WEIGHT
        )
        pygame.draw.line(
            surface = self.window,
            color = BLUE,
            start_pos = position,
            end_pos = (
                ((position[0]+WINDOW_X/3)-(WINDOW_X/15)),
                (position[1]+(WINDOW_Y/3)-(WINDOW_Y/15))
            ),
          width = self.LINE_WEIGHT
        )

    # draws a circle
    def draw_circle(self , position):
        pygame.draw.ellipse(
            surface = self.window,
            color = RED,
            rect = (
                position[0],
                position[1],
                WINDOW_X/3-WINDOW_X/15,
                WINDOW_Y/3-WINDOW_Y/15
            ),
            width = self.LINE_WEIGHT
        )

    # checks where the user clicked and positions a cross/circle accordingly
    def position_element(self , mouse_position):
        if(
            mouse_position[0] > 0 and
            mouse_position[0] < WINDOW_X/3 and
            mouse_position[1] > 0 and
            mouse_position[1] < WINDOW_Y/3 and
            1 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_1)
                tiles_with_crosses.append(1)
            else:
                self.draw_circle(POSITION_1)
            taken_tiles.append(1)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3 and
            mouse_position[0] < WINDOW_X/3*2 and
            mouse_position[1] > 0 and
            mouse_position[1] < WINDOW_Y/3 and
            2 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_2)
                tiles_with_crosses.append(2)
            else:
                self.draw_circle(POSITION_2)
            taken_tiles.append(2)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3*2 and
            mouse_position[0] < WINDOW_X and
            mouse_position[1] > 0 and
            mouse_position[1] < WINDOW_Y/3 and
            3 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_3)
                tiles_with_crosses.append(3)
            else:
                self.draw_circle(POSITION_3)
            taken_tiles.append(3)
            self.player_1 *= -1
        elif(
            mouse_position[0] > 0 and
            mouse_position[0] < WINDOW_X/3 and
            mouse_position[1] > WINDOW_Y/3 and
            mouse_position[1] < WINDOW_Y/3*2 and
            4 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_4)
                tiles_with_crosses.append(4)
            else:
                self.draw_circle(POSITION_4)
            taken_tiles.append(4)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3 and
            mouse_position[0] < WINDOW_X/3*2 and
            mouse_position[1] > WINDOW_Y/3 and
            mouse_position[1] < WINDOW_Y/3*2 and
            5 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_5)
                tiles_with_crosses.append(5)
            else:
                self.draw_circle(POSITION_5)
            taken_tiles.append(5)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3*2 and
            mouse_position[0] < WINDOW_X and
            mouse_position[1] > WINDOW_Y/3 and
            mouse_position[1] < WINDOW_Y/3*2 and
            6 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_6)
                tiles_with_crosses.append(6)
            else:
                self.draw_circle(POSITION_6)
            taken_tiles.append(6)
            self.player_1 *= -1
        elif(
            mouse_position[0] > 0 and
            mouse_position[0] < WINDOW_X/3 and
            mouse_position[1] > WINDOW_Y/3*2 and
            mouse_position[1] < WINDOW_Y and
            7 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_7)
                tiles_with_crosses.append(7)
            else:
                self.draw_circle(POSITION_7)
            taken_tiles.append(7)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3 and
            mouse_position[0] < WINDOW_X/3*2 and
            mouse_position[1] > WINDOW_Y/3*2 and
            mouse_position[1] < WINDOW_Y and
            8 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_8)
                tiles_with_crosses.append(8)
            else:
                self.draw_circle(POSITION_8)
            taken_tiles.append(8)
            self.player_1 *= -1
        elif(
            mouse_position[0] > WINDOW_X/3*2 and
            mouse_position[0] < WINDOW_X and
            mouse_position[1] > WINDOW_Y/3*2 and
            mouse_position[1] < WINDOW_Y and
            9 not in taken_tiles
        ):
            if self.player_1 == 1:
                self.draw_cross(POSITION_9)
                tiles_with_crosses.append(9)
            else:
                self.draw_circle(POSITION_9)
            taken_tiles.append(9)
            self.player_1 *= -1
        for tile in range(1 , 10 , 3):
            if tile in taken_tiles and tile in tiles_with_crosses:
                if tile+1 in taken_tiles and tile+1 in tiles_with_crosses:
                    if tile+2 in taken_tiles and tile+2 in tiles_with_crosses:
                        print('cross won')
                        self.run = False
            elif tile in taken_tiles and tile not in tiles_with_crosses:
                    if tile+1 in taken_tiles and tile+1 not in tiles_with_crosses:
                        if tile+2 in taken_tiles and tile+2 not in tiles_with_crosses:
                            print('circle won')
                            self.run = False
        for tile in range(1 , 4):
            if tile in taken_tiles and tile in tiles_with_crosses:
                if tile+3 in taken_tiles and tile+3 in tiles_with_crosses:
                    if tile+6 in taken_tiles and tile+6 in tiles_with_crosses:
                        print('cross won')
                        self.run = False
            elif tile in taken_tiles and tile not in tiles_with_crosses:
                if tile+3 in taken_tiles and tile+3 not in tiles_with_crosses:
                    if tile+6 in taken_tiles and tile+6 not in tiles_with_crosses:
                        print('circle won')
                        self.run = False
        if(
            1 in taken_tiles and 1 in tiles_with_crosses and
            5 in taken_tiles and 5 in tiles_with_crosses and
            9 in taken_tiles and 9 in tiles_with_crosses
        ):
            print('cross won')
            self.run = False
        elif(
            3 in taken_tiles and 3 in tiles_with_crosses and
            5 in taken_tiles and 5 in tiles_with_crosses and
            7 in taken_tiles and 7 in tiles_with_crosses
        ):
            print('cross won')
            self.run = False
        elif(
            1 in taken_tiles and 1 not in tiles_with_crosses and
            5 in taken_tiles and 5 not in tiles_with_crosses and
            9 in taken_tiles and 9 not in tiles_with_crosses
        ):
            print('circle won')
            self.run = False
        elif(
            3 in taken_tiles and 3 not in tiles_with_crosses and
            5 in taken_tiles and 5 not in tiles_with_crosses and
            7 in taken_tiles and 7 not in tiles_with_crosses
        ):
            print('circle won')
            self.run = False
        elif len(taken_tiles) == 9:
            print('it\'s a draw')
            self.run = False


# create game object
game = Game(10)

# initialize pygame
pygame.init()


# change the caption of the window
pygame.display.set_caption("tic-tac-toe")

# create the Clock object
clock = pygame.time.Clock()

# main game loop
while game.run:
    # change the background color to white
    game.window.fill(WHITE)

    # calls the function that draws the lines for the game area
    game.draw_game_area()

    # keeps track of events
    for event in pygame.event.get():
        # terminate the application when the 'X' button is hit
        if event.type == pygame.QUIT:
            self.run = False
        # check for a left click and place a cross/circle
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.position_element(
                    pygame.mouse.get_pos(),
                )
    for i in range(1 , 10):
        if i in taken_tiles and i in tiles_with_crosses:
            if i == 1: game.draw_cross(POSITION_1)
            if i == 2: game.draw_cross(POSITION_2)
            if i == 3: game.draw_cross(POSITION_3)
            if i == 4: game.draw_cross(POSITION_4)
            if i == 5: game.draw_cross(POSITION_5)
            if i == 6: game.draw_cross(POSITION_6)
            if i == 7: game.draw_cross(POSITION_7)
            if i == 8: game.draw_cross(POSITION_8)
            if i == 9: game.draw_cross(POSITION_9)
        if i in taken_tiles and i not in tiles_with_crosses:
            if i == 1: game.draw_circle(POSITION_1)
            if i == 2: game.draw_circle(POSITION_2)
            if i == 3: game.draw_circle(POSITION_3)
            if i == 4: game.draw_circle(POSITION_4)
            if i == 5: game.draw_circle(POSITION_5)
            if i == 6: game.draw_circle(POSITION_6)
            if i == 7: game.draw_circle(POSITION_7)
            if i == 8: game.draw_circle(POSITION_8)
            if i == 9: game.draw_circle(POSITION_9)
    # refresh the display to apply changes
    pygame.display.update()
    # caps FPS at 30
    clock.tick(FPS)
