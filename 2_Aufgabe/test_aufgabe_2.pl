% execute tests with:
% ?- consult('aufgabe_2'), consult('test_aufgabe_2'), run_tests.

:- begin_tests(aufgabe_2).

test(solveSudoku) :-
     sudoku(1, Sudoku), sudoku(2, SudokuSolution),
     solveSudoku(Sudoku),
     Sudoku = SudokuSolution.

test(solveSudoku) :-
     sudoku(2, Sudoku), sudoku(2, SudokuSolution),
     solveSudoku(Sudoku),
     Sudoku = SudokuSolution.

test(solveSudoku) :-
     sudoku(3, Sudoku), sudoku(4, SudokuSolution),
     solveSudoku(Sudoku),
     Sudoku = SudokuSolution.

test(solveSudoku) :-
     sudoku(4, Sudoku), sudoku(4, SudokuSolution),
     solveSudoku(Sudoku),
     Sudoku = SudokuSolution.

:- end_tests(aufgabe_2).
