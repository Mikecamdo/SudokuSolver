import pygame
# Easy, Medium, and Hard boards were found on sudokuessentials.com
easy_grid = [
    [8, 0, 0, 9, 3, 0, 0, 0, 2],
    [0, 0, 9, 0, 0, 0, 0, 4, 0],
    [7, 0, 2, 1, 0, 0, 9, 6, 0],
    [2, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 7, 0, 0, 0, 6, 0, 0, 5],
    [0, 2, 7, 0, 0, 8, 4, 0, 6],
    [0, 3, 0, 0, 0, 0, 5, 0, 0],
    [5, 0, 0, 0, 6, 2, 0, 0, 8]
]

medium_grid = [
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [4, 2, 7, 0, 6, 0, 0, 9, 8],
    [0, 0, 0, 2, 9, 0, 3, 7, 0],
    [0, 0, 5, 0, 0, 0, 0, 3, 0],
    [0, 0, 3, 5, 1, 9, 6, 0, 0],
    [0, 4, 0, 0, 0, 0, 2, 0, 0],
    [0, 3, 2, 0, 7, 6, 0, 0, 0],
    [8, 5, 0, 0, 3, 0, 7, 2, 4],
    [0, 0, 0, 0, 0, 0, 9, 0, 0]
]

hard_grid = [
    [0, 0, 0, 5, 0, 0, 0, 7, 0],
    [0, 2, 0, 0, 3, 4, 0, 0, 8],
    [0, 0, 1, 0, 2, 0, 4, 0, 5],
    [0, 7, 0, 0, 0, 3, 0, 0, 0],
    [6, 0, 9, 0, 0, 0, 3, 0, 1],
    [0, 0, 0, 8, 0, 0, 0, 2, 0],
    [9, 0, 4, 0, 5, 0, 8, 0, 0],
    [8, 0, 0, 6, 9, 0, 0, 5, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0]
]

easy_grid_solved = [
    [8, 4, 6, 9, 3, 7, 1, 5, 2],
    [3, 1, 9, 6, 2, 5, 8, 4, 7],
    [7, 5, 2, 1, 8, 4, 9, 6, 3],
    [2, 8, 5, 7, 1, 3, 6, 9, 4],
    [4, 6, 3, 8, 5, 9, 2, 7, 1],
    [9, 7, 1, 2, 4, 6, 3, 8, 5],
    [1, 2, 7, 5, 9, 8, 4, 3, 6],
    [6, 3, 8, 4, 7, 1, 5, 2, 9],
    [5, 9, 4, 3, 6, 2, 7, 1, 8]
]

medium_grid_solved = [
    [3, 6, 9, 7, 5, 8, 4, 1, 2],
    [4, 2, 7, 1, 6, 3, 5, 9, 8],
    [5, 1, 8, 2, 9, 4, 3, 7, 6],
    [7, 9, 5, 6, 4, 2, 8, 3, 1],
    [2, 8, 3, 5, 1, 9, 6, 4, 7],
    [6, 4, 1, 3, 8, 7, 2, 5, 9],
    [9, 3, 2, 4, 7, 6, 1, 8, 5],
    [8, 5, 6, 9, 3, 1, 7, 2, 4],
    [1, 7, 4, 8, 2, 5, 9, 6, 3]
]

hard_grid_solved = [
    [4, 9, 3, 5, 1, 8, 6, 7, 2],
    [5, 2, 6, 7, 3, 4, 1, 9, 8],
    [7, 8, 1, 9, 2, 6, 4, 3, 5],
    [2, 7, 8, 1, 6, 3, 5, 4, 9],
    [6, 4, 9, 2, 7, 5, 3, 8, 1],
    [3, 1, 5, 8, 4, 9, 7, 2, 6],
    [9, 6, 4, 3, 5, 2, 8, 1, 7],
    [8, 3, 7, 6, 9, 1, 2, 5, 4],
    [1, 5, 2, 4, 8, 7, 9, 6, 3]
]


def main():  # Main method
    pygame.init()  # Initializes pygame
    window = pygame.display.set_mode((550, 550))  # The GUI window
    pygame.display.set_caption("SudokuSolver")  # Sets the caption to SudokuSolver
    window.fill((255, 255, 255))  # Makes the board white
    font = pygame.font.SysFont('Bahnschrift', 35)  # Font for the game

    pygame.display.update()
    while True:  # Loop that doesn't end until the user picks a menu choice (or quits the game)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                if 175 <= position[0] <= 375 and 25 <= position[1] <= 75:  # If the user clicks the easy button
                    play_game("Easy", window)
                    return
                elif 175 <= position[0] <= 375 and 175 <= position[1] <= 225:  # If the user clicks the medium button
                    play_game("Medium", window)
                    return
                elif 175 <= position[0] <= 375 and 325 <= position[1] <= 375:  # If the user clicks the hard button
                    play_game("Hard", window)
                    return
                elif 175 <= position[0] <= 375 and 475 <= position[1] <= 525:  # If the user clicks the custom button
                    play_game("Custom", window)
                    return
            elif event.type == pygame.QUIT:  # If the user quits the game
                pygame.quit()
                return

        # The following lines create the buttons for the main menu
        mouse = pygame.mouse.get_pos()
        if 175 <= mouse[0] <= 375 and 25 <= mouse[1] <= 75:  # If the user hovers over the easy button
            pygame.draw.rect(window, (0, 0, 0), (175, 25, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 175, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 325, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 475, 200, 50))
        elif 175 <= mouse[0] <= 375 and 175 <= mouse[1] <= 225:  # If the user hovers over the medium button
            pygame.draw.rect(window, (128, 128, 128), (175, 25, 200, 50))
            pygame.draw.rect(window, (0, 0, 0), (175, 175, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 325, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 475, 200, 50))
        elif 175 <= mouse[0] <= 375 and 325 <= mouse[1] <= 375:  # If the user hovers over the hard button
            pygame.draw.rect(window, (128, 128, 128), (175, 25, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 175, 200, 50))
            pygame.draw.rect(window, (0, 0, 0), (175, 325, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 475, 200, 50))
        elif 175 <= mouse[0] <= 375 and 475 <= mouse[1] <= 525:  # If the user hovers over the custom button
            pygame.draw.rect(window, (128, 128, 128), (175, 25, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 175, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 325, 200, 50))
            pygame.draw.rect(window, (0, 0, 0), (175, 475, 200, 50))
        else:  # If the user is not hovering over a button
            pygame.draw.rect(window, (128, 128, 128), (175, 25, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 175, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 325, 200, 50))
            pygame.draw.rect(window, (128, 128, 128), (175, 475, 200, 50))

        text1 = font.render("Easy", True, (255, 0, 0))
        window.blit(text1, (235, 27))  # Displays "Easy" on the first button

        text2 = font.render("Medium", True, (255, 0, 0))
        window.blit(text2, (215, 177))  # Displays "Medium" on the second button

        text3 = font.render("Hard", True, (255, 0, 0))
        window.blit(text3, (235, 327))  # Displays "Hard" on the third button

        text4 = font.render("Custom", True, (255, 0, 0))
        window.blit(text4, (215, 477))  # Displays "Custom" on the fourth button

        pygame.display.update()  # Displays any updates


def draw_board(board, window):  # Draws the given board to the window
    window.fill((255, 255, 255))  # Resets what's on the screen

    for i in range(0, 10):  # Draws the thinner lines within each subgrid
        pygame.draw.line(window, (128, 128, 128), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(window, (128, 128, 128), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    for i in range(0, 4):  # Draws the thicker lines around each subgrid
        pygame.draw.line(window, (0, 0, 0), (50 + 150 * i, 50), (50 + 150 * i, 500), 2)
        pygame.draw.line(window, (0, 0, 0), (50, 50 + 150 * i), (500, 50 + 150 * i), 2)

    font = pygame.font.SysFont('Bahnschrift', 35)  # Font for the game

    for i in range(0, 9):  # Loops through the given board and prints any given values to the screen
        for j in range(0, 9):
            if 0 < board[i][j] < 10:
                value = font.render(str(board[i][j]), True, (52, 31, 151))
                window.blit(value, ((j + 1) * 50 + 17, (i + 1) * 50 + 3))

    pygame.display.update()  # Displays the update


def insert_guess(window, position, original_grid, original_grid_solved, wrong_guesses, empty_spots_left, mode):  # Enters the user's correct guess, or prints an X to the screen
    x = position[1] // 50
    y = position[0] // 50
    font = pygame.font.SysFont('Bahnschrift', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if position[0] < 50 or position[1] < 50 or position[0] > 500 or position[1] > 500:  # Prevents numbers from being added outside of the board
                    return wrong_guesses, empty_spots_left
                elif original_grid[x - 1][y - 1] != 0:  # if the user clicks on a given number
                    return wrong_guesses, empty_spots_left
                elif 0 < event.key - 48 < 10:
                    if mode == "Custom":  # For custom boards (no error checking)
                        pygame.draw.rect(window, (255, 255, 255), (y * 50 + 2, x * 50 + 2, 48, 45))
                        guess = font.render(str(event.key - 48), True, (0, 0, 0))
                        window.blit(guess, (y * 50 + 17, x * 50 + 3))
                        pygame.display.update()
                        return wrong_guesses, empty_spots_left
                    else:  # For given boards (with error checking)
                        if original_grid_solved[x - 1][y - 1] == event.key - 48:  # If the user guessed correctly
                            pygame.draw.rect(window, (255, 255, 255), (y * 50 + 2, x * 50 + 2, 48, 45))
                            guess = font.render(str(event.key - 48), True, (0, 0, 0))
                            window.blit(guess, (y * 50 + 17, x * 50 + 3))  # Adds the user's correct guess to the screen
                            pygame.display.update()
                            empty_spots_left -= 1  # Decreases the number of empty spots by 1
                            return wrong_guesses, empty_spots_left
                        else:  # If the user guessed incorrectly
                            wrong = font.render("X", True, (255, 0, 0))
                            window.blit(wrong, (50 * (wrong_guesses + 1) + 15, 500))  # Add a red X to the screen
                            pygame.display.update()
                            wrong_guesses += 1  # Add 1 to the number of wrong_guesses
                            return wrong_guesses, empty_spots_left


def insert_board(window, position, custom_grid):  # Used to create a user's custom grid
    x = position[1] // 50
    y = position[0] // 50
    font = pygame.font.SysFont('Bahnschrift', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if position[0] < 50 or position[1] < 50 or position[0] > 500 or position[1] > 500:  # Prevents numbers from being added outside of the board
                    return custom_grid
                elif 0 < event.key - 48 < 10:  # If the user entered a valid choice (1-9)
                    pygame.draw.rect(window, (255, 255, 255), (y * 50 + 2, x * 50 + 2, 48, 45))
                    guess = font.render(str(event.key - 48), True, (52, 31, 151))
                    window.blit(guess, (y * 50 + 17, x * 50 + 3))  # Print the number to the screen
                    pygame.display.update()
                    custom_grid[x - 1][y - 1] = event.key - 48  # Update the custom grid
                    return custom_grid


def is_valid_number(x, y, guess, board):  # Used to solve boards. Checks to see if the guess is a valid number for the spot provided.
    for i in range(9):
        if board[x][i] == guess and i != y:  # Checks the column
            return False
        elif board[i][y] == guess and i != x:  # Checks the row
            return False

    # Checks the mini_grid
    if x % 3 == 0:  # If x is in the first column of a mini grid
        if y % 3 == 0:  # If y is in the first row of the mini grid
            if board[x + 1][y + 1] == guess or board[x + 2][y + 1] == guess or board[x + 1][y + 2] == guess or board[x + 2][y + 2] == guess:
                return False
        elif y % 3 == 1:  # If y is in the second row of the mini grid
            if board[x + 1][y + 1] == guess or board[x + 2][y + 1] == guess or board[x + 1][y - 1] == guess or board[x + 2][y - 1] == guess:
                return False
        else:  # If y is in the third row of the mini grid
            if board[x + 1][y - 1] == guess or board[x + 2][y - 1] == guess or board[x + 1][y - 2] == guess or board[x + 2][y - 2] == guess:
                return False
    elif x % 3 == 1:  # If x is in the second column of a mini grid
        if y % 3 == 0:  # If y is in the first row of the mini grid
            if board[x + 1][y + 1] == guess or board[x - 1][y + 1] == guess or board[x + 1][y + 2] == guess or board[x - 1][y + 2] == guess:
                return False
        elif y % 3 == 1:  # If y is in the second row of the mini grid
            if board[x + 1][y + 1] == guess or board[x - 1][y + 1] == guess or board[x + 1][y - 1] == guess or board[x - 1][y - 1] == guess:
                return False
        else:  # If y is in the third row of the mini grid
            if board[x + 1][y - 1] == guess or board[x - 1][y - 1] == guess or board[x + 1][y - 2] == guess or board[x - 1][y - 2] == guess:
                return False
    else:  # If x is in the third column of a mini grid
        if y % 3 == 0:  # If y is in the first row of the mini grid
            if board[x - 1][y + 1] == guess or board[x - 2][y + 1] == guess or board[x - 1][y + 2] == guess or board[x - 2][y + 2] == guess:
                return False
        elif y % 3 == 1:  # If y is in the second row of the mini grid
            if board[x - 1][y + 1] == guess or board[x - 2][y + 1] == guess or board[x - 1][y - 1] == guess or board[x - 2][y - 1] == guess:
                return False
        else:  # If y is in the third row of the mini grid
            if board[x - 1][y - 1] == guess or board[x - 2][y - 1] == guess or board[x - 1][y - 2] == guess or board[x - 2][y - 2] == guess:
                return False

    return True


def solve(board, window):  # Solves the board passed to it.
    x_stack = []  # Holds the x positions of the previously solved tiles
    y_stack = []  # Holds the y positions of the previously solved tiles
    guess_stack = []  # Holds the values of the previously solve tiles
    font = pygame.font.SysFont('Bahnschrift', 35)
    i = 0  # Used to iterate through every x position
    while i < 9:
        j = 0  # Used to iterate through every y position
        k = 1  # Used to iterate through every possible value a sudoku tile could have (1-9)
        while j < 9:
            if board[i][j] == 0:  # If an empty spot is found
                while k < 10:
                    if is_valid_number(i, j, k, board):  # If k is a valid number for the spot
                        board[i][j] = k  # Set the board spot to k
                        x_stack.append(i)  # Add the x position to the stack
                        y_stack.append(j)  # Add the y position to the stack
                        guess_stack.append(k)  # Add the value of the tile to the stack

                        pygame.draw.rect(window, (255, 255, 255), ((j + 1) * 50 + 10, (i + 1) * 50 + 10, 40, 40))
                        guess = font.render(str(k), True, (0, 0, 0))
                        window.blit(guess, ((j + 1) * 50 + 17, (i + 1) * 50 + 3))  # Print the updated value to the screen
                        pygame.display.update()

                        k = 1
                        break
                    k += 1
                if k == 10:  # If no value is found
                    i = x_stack.pop()  # Reset i
                    j = y_stack.pop()  # Reset j
                    board[i][j] = 0  # Reset the previous position to 0
                    k = guess_stack.pop() + 1  # Reset k
                    continue
            j += 1
        i += 1


def play_game(mode, window):  # Starts the game off based on the given mode.
    original_grid = []
    original_grid_solved = []
    custom_grid = [  # Used for the user's custom grid if they select custom mode
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    if mode == "Easy":
        draw_board(easy_grid, window)  # Draws the board
        original_grid = easy_grid  # Sets the original grid equal to the easy grid
        original_grid_solved = easy_grid_solved  # Sets the original grid solution equal to the easy grid solution
    elif mode == "Medium":
        draw_board(medium_grid, window)  # Draws the board
        original_grid = medium_grid  # Sets the original grid equal to the medium grid
        original_grid_solved = medium_grid_solved  # Sets the original grid solution equal to the medium grid solution
    elif mode == "Hard":
        draw_board(hard_grid, window)  # Draws the board
        original_grid = hard_grid  # Sets the original grid equal to the hard grid
        original_grid_solved = hard_grid_solved  # Sets the original grid solution equal to the hard grid solution
    elif mode == "Custom":
        draw_board(custom_grid, window)  # Draws the board (which at this point is empty)
        i = 0
        while i < 10:  # Loop that doesn't end until the user presses the enter/return key
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # If the user clicks on a tile
                    position = pygame.mouse.get_pos()
                    custom_grid = insert_board(window, position, custom_grid)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # If the user presses the enter/return key
                        i = 10
                elif event.type == pygame.QUIT:  # If the user quits the game
                    pygame.quit()
                    return
        original_grid = custom_grid

    wrong_guesses = 0  # The number of wrong guesses the user makes
    empty_spots_left = 0  # The number of empty tiles left in the board
    for i in range(9):  # Loops through every tile in the board to count the number of empty tiles
        for j in range(9):
            if original_grid[i][j] == 0:
                empty_spots_left += 1

    while True:
        for event in pygame.event.get():
            if wrong_guesses == 3:  # If the user gets 3 guesses wrong
                font = pygame.font.SysFont('Bahnschrift', 35)  # Font for the game
                game_over = font.render("Game Over", True, (255, 0, 0))
                window.blit(game_over, (185, 5))  # Prints game over message
                pygame.display.update()
                while True:
                    # The following lines are for the main menu button
                    mouse = pygame.mouse.get_pos()
                    if 300 <= mouse[0] <= 500 and 506 <= mouse[1] <= 556:
                        pygame.draw.rect(window, (0, 0, 0), (300, 506, 200, 50))
                    else:
                        pygame.draw.rect(window, (128, 128, 128), (300, 506, 200, 50))

                    main_menu = font.render("Main Menu", True, (255, 0, 0))
                    window.blit(main_menu, (315, 506))

                    pygame.display.update()
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:  # If the user quits the game
                            pygame.quit()
                            return
                        elif event2.type == pygame.MOUSEBUTTONUP and event2.button == 1:  # If the user clicks the main menu button
                            if 300 <= mouse[0] <= 500 and 506 <= mouse[1] <= 556:
                                main()
                                return
            elif empty_spots_left == 0:  # If the user solves the easy/medium/hard board
                font = pygame.font.SysFont('Bahnschrift', 35)  # Font for the game
                game_over = font.render("You Win!", True, (0, 128, 0))
                window.blit(game_over, (205, 5))  # Prints the winning message
                pygame.display.update()
                while True:
                    # The following lines are for the main menu button
                    mouse = pygame.mouse.get_pos()
                    if 300 <= mouse[0] <= 500 and 506 <= mouse[1] <= 556:
                        pygame.draw.rect(window, (0, 0, 0), (300, 506, 200, 50))
                    else:
                        pygame.draw.rect(window, (128, 128, 128), (300, 506, 200, 50))

                    main_menu = font.render("Main Menu", True, (255, 0, 0))
                    window.blit(main_menu, (315, 506))

                    pygame.display.update()
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:  # If the user quits the game
                            pygame.quit()
                            return
                        elif event2.type == pygame.MOUSEBUTTONUP and event2.button == 1:  # If the user clicks the main menu button
                            if 300 <= mouse[0] <= 500 and 506 <= mouse[1] <= 556:
                                main()
                                return
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # If the user clicks a tile
                position = pygame.mouse.get_pos()
                wrong_guesses, empty_spots_left = insert_guess(window, position, original_grid, original_grid_solved, wrong_guesses, empty_spots_left, mode)  # User enters guess
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # If the user presses the 's' key on the keyboard
                    if mode == "Easy":
                        solve(easy_grid, window)
                        wrong_guesses = 3  # This is so it enters the "Game Over" loop after solving
                    elif mode == "Medium":
                        solve(medium_grid, window)
                        wrong_guesses = 3  # This is so it enters the "Game Over" loop after solving
                    elif mode == "Hard":
                        solve(hard_grid, window)
                        wrong_guesses = 3  # This is so it enters the "Game Over" loop after solving
                    elif mode == "Custom":
                        solve(custom_grid, window)
                        wrong_guesses = 3  # This is so it enters the "Game Over" loop after solving
            elif event.type == pygame.QUIT:  # If the user quits the game
                pygame.quit()
                return


main()  # starts the program
