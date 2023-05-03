{\rtf1\ansi\ansicpg1251\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pygame\
\
# \uc0\u1048 \u1085 \u1080 \u1094 \u1080 \u1072 \u1083 \u1080 \u1079 \u1072 \u1094 \u1080 \u1103  Pygame\
pygame.init()\
\
# \uc0\u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1080 \u1077  \u1088 \u1072 \u1079 \u1084 \u1077 \u1088 \u1072  \u1101 \u1082 \u1088 \u1072 \u1085 \u1072 \
screen_width = 800\
screen_height = 800\
screen = pygame.display.set_mode((screen_width, screen_height))\
\
# \uc0\u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1080 \u1077  \u1094 \u1074 \u1077 \u1090 \u1086 \u1074 \
white = (255, 255, 255)\
black = (0, 0, 0)\
red = (255, 0, 0)\
blue = (0, 0, 255)\
\
# \uc0\u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1080 \u1077  \u1087 \u1072 \u1088 \u1072 \u1084 \u1077 \u1090 \u1088 \u1086 \u1074  \u1076 \u1086 \u1089 \u1082 \u1080  \u1080  \u1096 \u1072 \u1096 \u1077 \u1082 \
board_size = 8\
cell_size = 80\
piece_radius = 30\
\
# \uc0\u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1080 \u1077  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1081 \
def draw_board():\
    for i in range(board_size):\
        for j in range(board_size):\
            x = i * cell_size + cell_size / 2\
            y = j * cell_size + cell_size / 2\
            pygame.draw.circle(screen, white, (x, y), cell_size / 2 - 5)\
            pygame.draw.circle(screen, black, (x, y), cell_size / 2, 5)\
\
def draw_piece(x, y, color):\
    pygame.draw.circle(screen, color, (x, y), piece_radius)\
\
# \uc0\u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085 \u1080 \u1077  \u1080 \u1075 \u1088 \u1086 \u1074 \u1086 \u1081  \u1083 \u1086 \u1075 \u1080 \u1082 \u1080 \
board = [[None for i in range(board_size)] for j in range(board_size)]\
board[0][0] = "white"\
board[1][1] = "white"\
board[2][2] = "white"\
board[3][3] = "white"\
board[4][4] = "black"\
board[5][5] = "black"\
board[6][6] = "black"\
board[7][7] = "black"\
\
def get_cell(x, y):\
    i = int(x / cell_size)\
    j = int(y / cell_size)\
    return (i, j)\
\
def get_piece_color(cell):\
    return board[cell[0]][cell[1]]\
\
def move_piece(cell1, cell2):\
    color1 = get_piece_color(cell1)\
    color2 = get_piece_color(cell2)\
    if color1 == None:\
        return False\
    if color2 != None:\
        return False\
    dx = cell2[0] - cell1[0]\
    dy = cell2[1] - cell1[1]\
    if abs(dx) != abs(dy):\
        return False\
    if abs(dx) > 2:\
        return False\
    if abs(dx) == 2:\
        cell3 = ((cell1[0] + cell2[0]) // 2, (cell1[1] + cell2[1]) // 2)\
        color3 = get_piece_color(cell3)\
        if color3 == None:\
            return False\
        if color3 == color1:\
            return False\
        board[cell3[0]][cell3[1]] = None\
    board[cell2[0]][cell2[1]] = color1\
    board[cell1[0]][cell1[1]] = None\
    return True\
\
# \uc0\u1054 \u1089 \u1085 \u1086 \u1074 \u1085 \u1086 \u1081  \u1094 \u1080 \u1082 \u1083  \u1080 \u1075 \u1088 \u1099 \
running = True\
selected_cell = None\
while running:\
    for event in pygame.event.get():\
        if event.type == pygame.\
}