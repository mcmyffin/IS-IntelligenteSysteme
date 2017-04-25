% execute tests with:
% ?- consult('aufgabe_2'), consult('test_aufgabe_2'), run_tests.

:- begin_tests(aufgabe_2).

checkEqual(SudokuName, SolutionName) :-
     sudoku(SudokuName, Sudoku), sudoku(SolutionName, Solution),
     solveSudoku(Sudoku),
     Sudoku = Solution.

test(solveSudoku) :- checkEqual(sudoku_1, solution_1).
test(solveSudoku) :- checkEqual(solution_1, solution_1).
test(solveSudoku) :- checkEqual(sudoku_2, solution_2).
test(solveSudoku) :- checkEqual(solution_2, solution_2).

test(solveSudoku, fail) :- sudoku(sudoku_fail_length_1, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_length_2, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_length_3, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_length_4, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_domain_1, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_domain_2, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_row_1, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_col_1, Sudoku), solveSudoku(Sudoku).
test(solveSudoku, fail) :- sudoku(sudoku_fail_block_1, Sudoku), solveSudoku(Sudoku).

:- end_tests(aufgabe_2).
