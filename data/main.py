import pygame
import sys
import PyQt5
import os


pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 50
        self.top = 50
        self.cell_size = 30
        self.colour = [[0] * width for _ in range(height)]
        self.color_for_lox_anton = [[0] * 60 for _ in range(60)]

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        button = pygame.Rect(50, 10, 30, 30)
        pos1 = button
        pos1_1 = (51, 11, 30, 30)
        pygame.draw.rect(screen, (0, 255, 0), pos1, 1)
        screen.blit(load_image("block.png"), pos1_1)
        button2 = pygame.Rect(90, 10, 30, 30)
        pos2 = button2
        pos2_1 = (91, 11, 30, 30)
        pygame.draw.rect(screen, (0, 255, 0), pos2, 1)
        screen.blit(load_image("dfg.png"), pos2_1)
        button3 = pygame.Rect(130, 10, 30, 30)
        pos3 = button3
        pos3_1 = (131, 11, 30, 30)
        pygame.draw.rect(screen, (0, 255, 0), pos3, 1)
        screen.blit(load_image("block_block.png"), pos3_1)
        button4 = pygame.Rect(170, 10, 30, 30)
        pos4 = button4
        pos4_1 = (171, 11, 30, 30)
        pygame.draw.rect(screen, (0, 255, 0), pos4, 1)
        screen.blit(load_image("bl.png"), pos4_1)
        return button, button2, button3, button4

    def render_1(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (0, 255, 0),
                                 (self.top + self.cell_size * i, self.left + self.cell_size * j,
                                  self.cell_size, self.cell_size), 1)
        for i in range(self.width):
            for j in range(self.height):
                pos = (self.top + self.cell_size * i + 1, self.left + self.cell_size * j + 1,
                       self.cell_size - 2, self.cell_size - 2)
                if self.colour[j][i] == 1:
                    screen.blit(load_image("dfg.png"), pos)
                if self.colour[j][i] == 2:
                    screen.blit(load_image("block.png"), pos)
                if self.colour[j][i] == 3:
                    screen.blit(load_image("block_block.png"), pos)
                if self.colour[j][i] == 4:
                    screen.blit(load_image("bl.png"), pos)



    def fffffdfffdffddd(self):
        for i in range(5):
            print([-1 for _ in range(70)])
        for i in self.color_for_lox_anton:
            print([-1 for _ in range(5)] + i + [-1 for _ in range(5)])
        for i in range(5):
            print([-1 for _ in range(70)])

    def get_cell(self, mouse_pos):
        x = (((self.width * self.cell_size) - (mouse_pos[0] - self.left)) // self.cell_size) - (self.width - 1)
        y = (((self.height * self.cell_size) - (mouse_pos[1] - self.top)) // self.cell_size) - (self.height - 1)
        if (-1 * self.width) < x < 1 and (-1 * self.height) < y < 1:
            return abs(x), abs(y)
        else:
            return None

    def on_click(self, cell_cords, name):
        if cell_cords:
            if name == "dfg.png":
                if self.colour[cell_cords[1]][cell_cords[0]] == 0:
                    self.colour[cell_cords[1]][cell_cords[0]] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] += 1
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] += 1
                else:
                    self.colour[cell_cords[1]][cell_cords[0]] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] = 0
            elif name == "block.png":
                if self.colour[cell_cords[1]][cell_cords[0]] == 0:
                    self.colour[cell_cords[1]][cell_cords[0]] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] += 2
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] += 2
                else:
                    self.colour[cell_cords[1]][cell_cords[0]] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] = 0
            elif name == "block_block.png":
                if self.colour[cell_cords[1]][cell_cords[0]] == 0:
                    self.colour[cell_cords[1]][cell_cords[0]] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] += 3
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] += 3
                else:
                    self.colour[cell_cords[1]][cell_cords[0]] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] = 0
            elif name == "bl.png":
                if self.colour[cell_cords[1]][cell_cords[0]] == 0:
                    self.colour[cell_cords[1]][cell_cords[0]] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] += 4
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] += 4
                else:
                    self.colour[cell_cords[1]][cell_cords[0]] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 2] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 2][cell_cords[0] * 3 + 1] = 0
                    self.color_for_lox_anton[cell_cords[1] * 3 + 1][cell_cords[0] * 3 + 2] = 0

    def get_click(self, mouse_pos, name):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, name)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Main_window:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 150)

    def addRect(self):
        button = pygame.Rect(10, 10, 520, 120)
        button1 = pygame.Rect(170, 160, 520, 120)
        button2 = pygame.Rect(10, 300, 520, 120)
        button3 = pygame.Rect(170, 440, 520, 120)
        self.rect = pygame.draw.rect(screen, (0, 100, 0), button, 2)
        self.rect1 = pygame.draw.rect(screen, (0, 100, 0), button1, 2)
        self.rect2 = pygame.draw.rect(screen, (0, 100, 0), button2, 2)
        self.rect3 = pygame.draw.rect(screen, (0, 100, 0), button3, 2)
        return button, button1, button2, button3

    def addText(self):
        screen.blit(self.font.render('Редактор', True, "pink"), (18, 20))
        screen.blit(self.font.render('Уровни', True, "pink"), (184, 170))
        screen.blit(self.font.render('2 х 2', True, "pink"), (170, 310))
        screen.blit(self.font.render('PVP', True, "pink"), (330, 450))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('q1')
    # size = width, height = 180, 250
    size = width, height = 700, 570
    screen = pygame.display.set_mode(size)
    running_for_main_window = True
    running_for_editor_window = False
    b = Main_window()
    while running_for_main_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b.addRect()[0].collidepoint(event.pos):
                    running_for_main_window = False
                    running1 = True
                if b.addRect()[1].collidepoint(event.pos):
                    running_for_main_window = False
                if b.addRect()[2].collidepoint(event.pos):
                    running_for_main_window = False
                if b.addRect()[3].collidepoint(event.pos):
                    running_for_main_window = False
        screen.fill((200, 255, 200))
        b.addRect()
        b.addText()
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        pygame.display.flip()
    flag1 = True
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    board = Board(20, 20)
    pos = 50, 50
    while running_for_editor_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                board.fffffdfffdffddd()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.render(screen)[0].collidepoint(event.pos):
                    flag1 = False
                    print(1)
                    name = "block.png"
                if board.render(screen)[1].collidepoint(event.pos):
                    print(2)
                    name = "dfg.png"
                    flag1 = False
                if board.render(screen)[2].collidepoint(event.pos):
                    print(3)
                    name = "block_block.png"
                    flag1 = False
                if board.render(screen)[3].collidepoint(event.pos):
                    print(4)
                    name = "bl.png"
                    flag1 = False
                if flag1:
                    board.get_click(event.pos, name="block.png")
                else:
                    board.get_click(event.pos, name)
        screen.fill(pygame.Color('purple'))
        board.render(screen)
        board.render_1(screen)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        pygame.display.flip()
pygame.quit()


