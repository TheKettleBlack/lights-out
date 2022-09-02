import pygame, random, time
pygame.init()

# Static variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GRAY = (69,69,69)
WHITE = (255,255,255)
TILE_SIZE = 100
FPS = 60

# Pygame config
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lights Out")
programIcon = pygame.image.load("img/icon.png").convert_alpha()
pygame.display.set_icon(programIcon)
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100,-16,2,512)

# Game variables
font = pygame.font.Font("font/CreatoDisplay-Regular.otf", 32)
font_small = pygame.font.Font("font/CreatoDisplay-Regular.otf", 9)
run = True
tile_list = []
map_array = []
clicks = 0
win_text = ""
win_state = False

# Game images
green_square = pygame.image.load("img/green.png").convert_alpha()
gray_square = pygame.image.load("img/gray.png").convert_alpha()
selector = pygame.image.load("img/selector.png").convert_alpha()
new_img = pygame.image.load('img/new.png').convert_alpha()

# Game sounds
new_sound = pygame.mixer.Sound('sound/new_game.ogg')
win_sound = pygame.mixer.Sound('sound/win.ogg')

# Functions
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

def draw_bg():
    screen.fill(GRAY)

def random_game():
    pygame.mixer.Sound.play(new_sound)
    global map_array, clicks, win_text
    win_text = ""
    map_array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for y in range(0,5):
        for x in range(0,5):
            click_or_not = random.choice(["yes", "no"])
            if click_or_not == "yes":
                click(y,x)
    clicks = 0
    draw_it(map_array)

def draw_it(map_array):
    global win_text, win_state
    for y,row in enumerate(map_array):
        for x,tile in enumerate(row):
            if tile == 1:
                img = green_square
            else:
                img = gray_square
            img_rect = img.get_rect()
            img_rect.x = x*TILE_SIZE
            img_rect.y = y*TILE_SIZE
            tile_data = (img,img_rect)
            tile_list.append(tile_data)
    blank_rows = 0
    for x in range(0,5):
        if 1 not in map_array[x]:
            blank_rows += 1
    if blank_rows == 5:
        pygame.mixer.Sound.play(win_sound)
        win_text = "Victory!"
        win_state = True
        game_info()
        which_flourish = random.choice([0,1,2])
        flourish(which_flourish)

def flourish_square(flourish_list):
    temp_tile_list = []
    for y,row in enumerate(flourish_list):
        for x,tile in enumerate(row):
            if tile == 1:
                img = green_square
            else:
                img = gray_square
            img_rect = img.get_rect()
            img_rect.x = x*TILE_SIZE
            img_rect.y = y*TILE_SIZE
            temp_tile_data = (img,img_rect)
            temp_tile_list.append(temp_tile_data)
    for tile in temp_tile_list:
        screen.blit(tile[0],tile[1])
    pygame.display.update()
    time.sleep(0.1)

def flourish_row(flourish_list):
    for x in range(0,len(flourish_list)):
        img = green_square
        off_img = gray_square
        img_rect = img.get_rect()
        img_rect.x = flourish_list[x][0]*TILE_SIZE
        img_rect.y = flourish_list[x][1]*TILE_SIZE
        tile_data = (img,img_rect)
        screen.blit(img,img_rect)
        pygame.display.update()
        time.sleep(0.05)
        screen.blit(off_img,img_rect)
        pygame.display.update()

def flourish(which_flourish):
    if which_flourish == 0:
        flourish_list1 = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        flourish_list2 = [[0,0,0,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
        flourish_list3 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        flourish_list4 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        flourish_square(flourish_list1)
        flourish_square(flourish_list2)
        flourish_square(flourish_list3)
        flourish_square(flourish_list4)
        flourish_square(flourish_list3)
        flourish_square(flourish_list2)
        flourish_square(flourish_list1)
        flourish_square(flourish_list2)
        flourish_square(flourish_list3)
        flourish_square(flourish_list4)
    if which_flourish == 1:
        empty_list = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        flourish_square(empty_list)
        flourish_list = [[0,0],[0,1],[0,2],[0,3],[0,4],
                         [1,4],[2,4],[3,4],[4,4],[4,3],
                         [4,2],[4,1],[4,0],[3,0],[2,0],
                         [1,0],[1,1],[1,2],[1,3],[2,3],
                         [3,3],[3,2],[3,1],[2,1],[2,2]]
        flourish_row(flourish_list)
    if which_flourish == 2:
        empty_list = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        flourish_square(empty_list)
        flourish_list = [[0,4],[0,3],[0,2],[0,1],[0,0],
                         [1,0],[1,1],[1,2],[1,3],[1,4],
                         [2,4],[2,3],[2,2],[2,1],[2,0],
                         [3,0],[3,1],[3,2],[3,3],[3,4],
                         [4,4],[4,3],[4,2],[4,1],[4,0]]
        flourish_row(flourish_list)

def game_info():
    draw_text("Moves:",font,WHITE,510,90)
    draw_text(str(clicks),font,WHITE,620,90)
    draw_text(str(win_text),font,WHITE,510,130)
    draw_text("©2022 Spin Co.",font_small,WHITE,632,490)

def click(col,row):
    global map_array, clicks
    clicks += 1
    # Handle the clicked tile
    if map_array[row][col] == 1:
        map_array[row][col] = 0
    else:
        map_array[row][col] = 1
    # Handle the tile above
    if row > 0:
        if map_array[row-1][col] == 1:
            map_array[row-1][col] = 0
        else:
            map_array[row-1][col] = 1
    # Handle the tile below
    if row < 4:
        if map_array[row+1][col] == 1:
            map_array[row+1][col] = 0
        else:
            map_array[row+1][col] = 1
    # Handle the tile left
    if col > 0:
        if map_array[row][col-1] == 1:
            map_array[row][col-1] = 0
        else:
            map_array[row][col-1] = 1
    # Handle the tile right
    if col < 4:
        if map_array[row][col+1] == 1:
            map_array[row][col+1] = 0
        else:
            map_array[row][col+1] = 1
    # Update the board state
    draw_it(map_array)

# Start a fresh game on load
random_game()

# Main game loop
while run:
    draw_bg()
    for tile in tile_list:
        screen.blit(tile[0],tile[1])
    mouse_pos = pygame.mouse.get_pos()
    row =  mouse_pos[1] // 100
    col =  mouse_pos[0] // 100
    new_button = screen.blit(new_img,(505,15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if win_state == False:
                    if col < 5:
                        click(col,row)
                if new_button.collidepoint(mouse_pos):
                    win_state = False
                    random_game()
    if col < 5:
        selector_rect = pygame.Rect((col * TILE_SIZE,row * TILE_SIZE),(TILE_SIZE,TILE_SIZE))
        screen.blit(selector,selector_rect)
    game_info()
    clock.tick(FPS)
    pygame.display.update()
