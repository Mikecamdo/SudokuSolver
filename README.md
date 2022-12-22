# SudokuSolver

## Programming Language: Python

Description: A standard sudoku game with easy, medium, and hard modes that also allows the user to enter 
custom sudoku boards for the program to solve. The program solves sudoku boards through iterative backtracking,
which iterates through each blank tile and selects a valid option for that tile before continuing to the next.
If the program runs out of valid options for a tile, it backtracks to the previously solved tile and finds a
new valid option for that tile (and then moves forward again). This repeats until the board is solved 
(assuming the board is solvable). The pygame library was used extensively for GUI and gameplay implementation.

How to use the project: Run the program (either using an IDE or the terminal, I used PyCharm). The main menu will pop up, allowing the user
to select whether they want to play the easy, medium, or hard sudoku boards. Alternatively, they can select the custom option
which allows the user to enter a custom board. The user makes their selection by clicking on the respective buttons. For the 
easy, medium, and hard sudoku boards, simply click on an empty square with the mouse and click a number between 1 and 9 to 
enter your guess for that square. If the guess is correct, then the number will be entered onto the screen. If the guess is 
incorrect, then a red X will appear at the bottom of the screen. The game ends after you receive 3 red X's.

If the custom option is selected on the main menu, then an empty board will appear. The user then clicks on each square
with the mouse and selects a number between 1 and 9 to enter the number for that square. After the user is done entering the
board, they hit the enter/return button on the keyboard. They then can enter their guesses to solve the board just like the 
easy, medium and hard boards (however, the program does not error check, meaning no red X's will appear if the user enters 
a wrong guess).

For any of the boards (easy/medium/hard/custom), simply hit the 's' button on the keyboard to get the program to solve
the board (if the board is custom, it is assumed that the board has a solution).
After any of the boards have been solved, the user enters 3 incorrect guesses for an easy/medium/hard board,
or the user successfully completes one of the easy/medium/hard boards, then a main menu button will appear
at the bottom of the screen that will take the user back to the main menu (to then choose another option).

To quit the game, the user can simply hit the exit button in the top right of the GUI.

Known oddities:
- If the user solves one of the easy/medium/hard boards, returns to the main menu, and selects the board they just solved,
then the board will automatically be solved and they will be unable to play that board until they restart the program.
- If the user enters a custom, unsolvable board, then the program will infinitiely try to solve it.

Future features (if I ever work on this again):
If I was to add more features in the future, I would add functionality that allows error checking on custom boards entered
by the user (so that the custom boards could actually be played).
I would also add randomized board creation (the program randomly generating valid Sudoku boards for the user to solve).
