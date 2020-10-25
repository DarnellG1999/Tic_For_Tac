import pygame
pygame.init()

win_width = 750
win_height = 750


board_size = 0
nums_in_win = 0
maximum_board_size = 10
maximum_board_size -= 2
current_turn = "X"
playing = True
winner = False

win = pygame.display.set_mode((win_width, win_height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


def win_conditions(symbol_list, nums_in_win):
    global winner
    global current_turn
    for u in range(1, board_size+1):
        vertical_win = []
        horizontal_win = []
        for i in range(0, len(symbol_list), 2):
            for w in range(1, board_size+1):
                if symbol_list[i][0] == u and symbol_list[i][1] == w:
                    vertical_win.append(symbol_list[i + 1])
                    if "O" in vertical_win and "X" in vertical_win:
                        vertical_win = [symbol_list[i + 1]]
                    elif len(vertical_win) == nums_in_win:
                        if current_turn == "X":
                            current_turn = "O"
                        else:
                            current_turn = "X"
                        winner = True
                        return winner
                    elif [u, w+1] not in symbol_list and w != board_size:
                        vertical_win = [symbol_list[i + 1]]
                if symbol_list[i][0] == w and symbol_list[i][1] == u:
                    horizontal_win.append(symbol_list[i + 1])
                    if "O" in horizontal_win and "X" in horizontal_win:
                        horizontal_win = [symbol_list[i + 1]]
                    elif len(horizontal_win) == nums_in_win:
                        if current_turn == "X":
                            current_turn = "O"
                        else:
                            current_turn = "X"
                        winner = True
                        return winner
                    elif [w+1, u] not in symbol_list and w != board_size:
                        horizontal_win = [symbol_list[i + 1]]


    for i in range(1, board_size-1):
        diagonal_win1 = []
        diagonal_win2 = []
        for j in range(0, len(symbol_list), 2):
            for e in range(1, board_size+1):
                for t in range(1, board_size+1):
                    if symbol_list[j][0] == e and symbol_list[j][1] == t:
                        diagonal_win1.append(symbol_list[j + 1])
                        diagonal_win2.append(symbol_list[j + 1])
                        if e != i + (t - 1):
                            diagonal_win1.pop()
                        if t != i + e:
                            diagonal_win2.pop()
                        if "X" in diagonal_win1 and "O" in diagonal_win1:
                            diagonal_win1 = [symbol_list[j + 1]]
                        if "X" in diagonal_win2 and "O" in diagonal_win2:
                            diagonal_win2 = [symbol_list[j + 1]]
                        if len(diagonal_win1) == nums_in_win:
                            if current_turn == "X":
                                current_turn = "O"
                            else:
                                current_turn = "X"
                            winner = True
                            return  winner
                        if len(diagonal_win2) == nums_in_win:
                            if current_turn == "X":
                                current_turn = "O"
                            else:
                                current_turn = "X"
                            winner = True
                            return winner


    for i in range(1, board_size-1):
        diagonal_win1 = []
        diagonal_win2 = []
        for j in range(0, len(symbol_list), 2):
            for e in range(1, board_size+1):
                for t in range(1, board_size+1):
                    if symbol_list[j][0] == e and symbol_list[j][1] == t:
                        diagonal_win1.append(symbol_list[j + 1])
                        diagonal_win2.append(symbol_list[j + 1])
                        if e != i + (board_size - t):
                            diagonal_win1.pop()
                        if t != -i + (board_size - e):
                            diagonal_win2.pop()
                        if "X" in diagonal_win1 and "O" in diagonal_win1:
                            diagonal_win1 = [symbol_list[j + 1]]
                        if "X" in diagonal_win2 and "O" in diagonal_win2:
                            diagonal_win2 = [symbol_list[j + 1]]
                        if len(diagonal_win1) == nums_in_win:
                            if current_turn == "X":
                                current_turn = "O"
                            else:
                                current_turn = "X"
                            winner = True
                            return winner
                        if len(diagonal_win2) == nums_in_win:
                            if current_turn == "X":
                                current_turn = "O"
                            else:
                                current_turn = "X"
                            winner = True
                            return winner


def print_symbol(symbol_list):
    for i in range(0, len(symbol_list), 2):
        if symbol_list[i+1] == "X":
            pygame.draw.line(win, black, ((symbol_list[i][0] - 1) * (win_width // board_size), (symbol_list[i][1] - 1) * (win_height // board_size)), (symbol_list[i][0] * (win_width // board_size), symbol_list[i][1] * (win_height // board_size)), 5)
            pygame.draw.line(win, black, ((symbol_list[i][0] - 1) * (win_width // board_size), (symbol_list[i][1]) * (win_height // board_size)), (symbol_list[i][0] * (win_width // board_size), (symbol_list[i][1] - 1) * (win_height // board_size)), 5)
        else:
            pygame.draw.circle(win, black, ((win_width // board_size) * symbol_list[i][0] - (win_width // (board_size * 2)), (win_height // board_size) * symbol_list[i][1] - (win_height // (board_size * 2))), 30)
    pygame.display.update()
    return


def symbol_placer(board_size, symbol_list):
    global current_turn
    if current_turn == "O":
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for size in range(board_size):
                    for ezis in range(board_size):
                        if size * (win_width * (1 / board_size)) < pygame.mouse.get_pos()[0] < (size + 1) * (win_width * (1 / board_size)) \
                            and ezis * (win_height * (1 / board_size)) < pygame.mouse.get_pos()[1] < (ezis + 1) * (win_height * (1 / board_size)):
                                if [size+1, ezis+1] not in symbol_list:
                                    symbol_list.append([size+1, ezis+1])
                                    symbol_list.append("O")
                                    current_turn = "X"
                                continue

    if current_turn == "X":
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for size in range(board_size):
                    for ezis in range(board_size):
                        if size * (win_width * (1 / board_size)) < pygame.mouse.get_pos()[0] < (size + 1) * (
                                win_width * (1 / board_size)) \
                                and ezis * (win_height * (1 / board_size)) < pygame.mouse.get_pos()[1] < (ezis + 1) * (
                                win_height * (1 / board_size)):
                            if [size + 1, ezis + 1] not in symbol_list:
                                symbol_list.append([size + 1, ezis + 1])
                                symbol_list.append("X")
                                current_turn = "O"

    return symbol_list


def print_board(board_size, symbol_list):
    win.fill(white)
    for size in range(1, board_size):
        pygame.draw.rect(win, black, [size * (win_width * (1 / board_size)), 0, win_width // 75, win_height])
        pygame.draw.rect(win, black, [0, size * (win_height * (1 / board_size)), win_width, win_height // 75])
    print_symbol(symbol_list)
    pygame.display.update()

def message_to_user(msg, color):
    font = pygame.font.SysFont("JetBrains Mono", 25)
    text = font.render(msg, True, color)
    middle_screen_width = text.get_width()
    middle_screen_height = text.get_height()
    win.blit(text, (win_width//2 - middle_screen_width//2, win_height//2 - middle_screen_height//2))


def num_in_row(max_board_size):
    global nums_in_win
    pygame.display.update()
    win.fill(white)
    message_to_user("Pick the amount in a row that will be needed to win", black)
    for size in range(max_board_size):
        font = pygame.font.SysFont("JetBrains Mono", 30)
        text = font.render(f"{size + 3}", True, black)
        pygame.draw.rect(win, blue, [size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2), (1/3) * win_height, win_width // (max_board_size + 4), win_height // (max_board_size + 4)])
        win.blit(text, [size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2), (1/3) * win_height])
    while True:
        try:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for size in range(max_board_size):
                        if size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2) < pygame.mouse.get_pos()[0] < size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2) + win_width // (max_board_size + 4) \
                            and (1/3) * win_height <= pygame.mouse.get_pos()[1] < (1/3) * win_height + win_height // (max_board_size +4):
                            nums_in_win = size + 3
                            if nums_in_win > board_size:
                                raise ValueError
                            return nums_in_win
        except ValueError:
            font = pygame.font.SysFont("JetBrains Mono", 25)
            text = font.render("You cannot Choose a number bigger than the board side", True, red)
            middle_screen_width = text.get_width()
            middle_screen_height = text.get_height()
            win.blit(text, (win_width // 2 - middle_screen_width // 2, win_height // 4 - middle_screen_height // 2))


def pick_size(max_board_size):
    global win_height
    global win_width
    global board_size
    for size in range(max_board_size):
        font = pygame.font.SysFont("JetBrains Mono", 30)
        text = font.render(f"{size+3}", True, black)
        pygame.draw.rect(win, blue, [size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2), (1/3) * win_height, win_width // (max_board_size + 4), win_height // (max_board_size + 4)])
        win.blit(text, [size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2), (1 / 3) * win_height])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for size in range(max_board_size):
                if size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2) < pygame.mouse.get_pos()[0] < size * (win_width // (max_board_size + 2)) + win_width // (max_board_size + 2) + win_width // (max_board_size + 4) \
                    and (1/3) * win_height <= pygame.mouse.get_pos()[1] < (1/3) * win_height + win_height // (max_board_size +4):
                    board_size = size + 3
                    return board_size
    pygame.display.update()
    return



def main(max_board_size):
    global winner
    global current_turn
    global win_width
    global win_height
    global board_size
    global playing
    global nums_in_win
    symbol_list = []
    while playing:
        if board_size == 0:
            win.fill(white)
            message_to_user("Choose the size of the board", black)
            pick_size(max_board_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
        elif nums_in_win == 0:
            win.fill(white)
            message_to_user("Pick the amount in a row that will be needed to win", black)
            num_in_row(max_board_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
        else:
            win.fill(white)
            print_board(board_size, symbol_list)
            symbol_placer(board_size, symbol_list)
            print_symbol(symbol_list)
            if len(symbol_list) > 0:
                win_conditions(symbol_list, nums_in_win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            while winner:
                win.fill(white)
                message_to_user(f"{current_turn} wins! Do you want to play again?", black)
                pygame.draw.rect(win, red, [win_width//5, win_height//5, win_width//4, win_height//4])
                pygame.draw.rect(win, red, [3*win_width // 5 - win_width // 25, win_height // 5, win_width // 4, win_height // 4])
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if win_width // 5 < pygame.mouse.get_pos()[0] < win_width // 5 + win_width // 4 and win_height // 5 < pygame.mouse.get_pos()[1] < win_height // 5 + win_height // 4:
                            board_size = 0
                            nums_in_win = 0
                            symbol_list = []
                            winner = False
                        elif 3*win_width // 5 - win_width // 25 < pygame.mouse.get_pos()[0] < 3*win_width // 5 - win_width // 25 + win_width // 4 and win_height // 5 < pygame.mouse.get_pos()[1] < win_height // 5 + win_height // 4:
                            quit()
                font = pygame.font.SysFont("JetBrains Mono", 60)
                text = font.render("Yes", True, black)
                middle_screen_width_yes = text.get_width()
                txet = font.render("No", True, black)
                middle_screen_width_no = txet.get_height()
                win.blit(text, [win_width//5 + win_width // 8 - middle_screen_width_yes // 2, win_height//5 + win_height // 8])
                win.blit(txet, [3*win_width // 5 - win_width // 25 + win_width // 9 - middle_screen_width_no // 2, win_height//5 + win_height // 8])
                pygame.display.update()


main(maximum_board_size)
