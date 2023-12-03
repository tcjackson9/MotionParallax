###
### Author: Tanner Jackson
### Class: Csc 110
### Description: This code first builds a static image with a sky, sun,
### mountains, and a foreground. Then the program uses gui.mouse to make
### the picture move towards the mouse. The objects further away in the
### image move less than the objects closer, this is done through the
### use of division after gui.mouse.
###
from graphics import graphics
import random
def main():
    '''
    This function is my main function that creates the canvas for the image.
    In addition, this function also creates the random colors for the
    mountains. Lastly, this function calls the other functions in the
    program that create the static image and motion parallax.
    There are no parameters for this function.
    '''
    global gui
    gui = graphics(700, 700, 'Motion Parallax')
    # Creates all the random colors for the mountains.
    random_color1 = random.randint(1, 255)
    random_color2 = random.randint(1, 255)
    random_color3 = random.randint(1, 255)
    random_color4 = random.randint(1, 255)
    random_color5 = random.randint(1, 255)
    random_color6 = random.randint(1, 255)
    random_color7 = random.randint(1, 255)
    random_color8 = random.randint(1, 255)
    random_color9 = random.randint(1, 255)
    while True:
        # Puts everything on the canvas with a update frame of 60.
        gui.clear()
        backdrop()
        sun()
        mountain1(random_color1, random_color2, random_color3)
        mountain2(random_color4, random_color5, random_color6)
        mountain3(random_color7, random_color8, random_color9)
        ground()
        tree()
        birds()
        gui.update_frame(60)

def backdrop():
    '''
    This function creates the background for the image. It takes a shade
    of blue from the color chart that I picked. This background does not
    move and is just a static image.
    There are no parameters in this function.
    '''
    color_string = gui.get_color_string(17, 232, 210)
    gui.rectangle(0, 0, 700, 700, color_string)

def sun():
    '''
    This function creates the sun in the static image of the canvas. It
    also makes the sun move with the mouse cursor but not by that much as
    it is divided by 25. This gives the effect that the sun is far away.
    There are no parameters in this function.
    '''
    color_string = gui.get_color_string(233, 202, 26)
    gui.ellipse(550 + gui.mouse_x / 25, 100 + gui.mouse_y / 25,
                100, 100, color_string)

def mountain1(random_color1, random_color2, random_color3):
    '''
    This function creates the first mountain which is the one in the middle back.
    This mountain is given a random color and can move based on where the mouse
    cursor is. It moves more than the sun, however, less than everything else
    in the program.
    random_color1: Can be integer 1-255.
    random_color2: Can be integer 1-255.
    random_color3: Can be integer 1-255.
    '''
    color_string = gui.get_color_string(random_color1, random_color2, random_color3)
    gui.triangle(125.5 + gui.mouse_x / 15, 550 + gui.mouse_y / 15,
                 350 + gui.mouse_x / 15, 175.5 + gui.mouse_y / 15,
                 600 + gui.mouse_x / 15, 550 + gui.mouse_y / 15, color_string)

def mountain2(random_color4, random_color5, random_color6):
    '''
    This function creates the second mountain which is the one on the left side of
    the canvas. It overlaps the first mountain that was created and is given a
    random color. It moves based on where the mouse cursor is more than the first
    mountain, however, less than the foreground.
    random_color4: Can be integer 1-255.
    random_color5: Can be integer 1-255.
    random_color6: Can be integer 1-255.
    '''
    color_string = gui.get_color_string(random_color4, random_color5, random_color6)
    gui.triangle(-250 + gui.mouse_x / 10, 700 + gui.mouse_y / 10,
                 150 + gui.mouse_x / 10, 175.5 + gui.mouse_y / 10,
                 550 + gui.mouse_x / 10, 700 + gui.mouse_y / 10, color_string)

def mountain3(random_color7, random_color8, random_color9):
    '''
    This function creates the third mountain on the canvas that is in front of
    both of the other two mountains. This mountain is given a random color and moves
    based off of where the mouse cursor is. It moves the same as the second
    mountain and less than the foreground.
    random_color7: Can be integer 1-255.
    random_color8: Can be integer 1-255.
    random_color9: Can be integer 1-255.
    '''
    color_string = gui.get_color_string(random_color7, random_color8, random_color9)
    gui.triangle(200 + gui.mouse_x / 10, 700 + gui.mouse_y / 10,
                 550 + gui.mouse_x / 10, 175.5 + gui.mouse_y / 10,
                 1000 + gui.mouse_x / 10, 700 + gui.mouse_y / 10, color_string)

def ground():
    '''
    This function creates the ground in the foreground and the grass coming
    off of the ground. The grass is created with a while loop, and both
    move based off the mouse cursor. They move more than the mountains
    and sun and tie with the tree in the foreground.
    There are no parameters in this function.
    '''
    color_string = gui.get_color_string(131, 243, 56)
    color_string_2 = gui.get_color_string(89, 218, 42)
    i = -20
    while i < 70:
        offset = i * 10
        gui.line(offset + gui.mouse_x / 5, 475 + gui.mouse_y / 5,
                 offset + gui.mouse_x / 5, 515 + gui.mouse_y / 5,
                 color_string_2)
        i += 1
    gui.rectangle(-200 + gui.mouse_x / 5, 500 + gui.mouse_y / 5,
                  1500, 800, color_string)

def tree():
    '''
    This function creates the tree in the foreground by making a rectangle
    and an ellipse. This tree moves the same as the ground by the mouse
    cursor at the same amount of strength.
    There are no parameters in this function.
    '''
    color_string = gui.get_color_string(122, 68, 27)
    gui.rectangle(500 + gui.mouse_x / 5, 500 + gui.mouse_y / 5,
                  25, 65, color_string)
    gui.ellipse(512.5 + gui.mouse_x / 5, 480 + gui.mouse_y / 5,
                75, 100, 'green')

def birds():
    '''
    This function creates the birds that are in the sky of the
    canvas. The birds are created with a while loop that makes
    them the same distance apart from one another. The birds
    do not move or are effected by the mouse cursor.
    There are no parameters in this function.
    '''
    i = 1
    while i < 6:
        offset_x = i * 75
        offset_y = i * 30
        gui.line(offset_x, offset_y,
                offset_x + 22, offset_y + 10, 'black')
        gui.line(offset_x + 22, offset_y + 10,
                offset_x + 44, offset_y, 'black')
        i += 1

main()