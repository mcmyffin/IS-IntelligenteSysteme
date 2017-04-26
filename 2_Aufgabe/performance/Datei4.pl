sol4_sudoku(Number) :-
     sudoku(Number, Sudoku),
     sol4_solveSudoku(Sudoku),
     time(sol4_printSudoku(Sudoku)).

sol4_solveSudoku(Sudoku) :-
     time(sol4_checkLength(Sudoku)),
     time(sol4_checkDomain(Sudoku)),
     time(sol4_checkRows(Sudoku)),
     time(sol4_checkCols(Sudoku)),
     time(sol4_checkBlocks(Sudoku)).

sol4_checkLength(Sudoku) :- length(Sudoku, 9), sol4_checkLengthInner(Sudoku).
sol4_checkLengthInner([]).
sol4_checkLengthInner([Row|Rest]) :- length(Row, 9), sol4_checkLengthInner(Rest).

sol4_checkDomain(Sudoku) :-
     append(Sudoku, SudokuFlatted),
     SudokuFlatted ins 1..9.

sol4_checkRows([]).
sol4_checkRows([Row|Rest]) :- all_distinct(Row), sol4_checkRows(Rest).

sol4_checkCols(Sudoku) :-
     transpose(Sudoku, SudokuTransposed),
     sol4_checkRows(SudokuTransposed).

sol4_checkBlocks(Sudoku) :-
     Sudoku = [Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9],
     sol4_checkBlocks(Row1, Row2, Row3),
     sol4_checkBlocks(Row4, Row5, Row6),
     sol4_checkBlocks(Row7, Row8, Row9).

sol4_checkBlocks([], [], []).
sol4_checkBlocks(Row1, Row2, Row3) :-
     Row1 = [R1C1, R1C2, R1C3 | R1Rest],
     Row2 = [R2C1, R2C2, R2C3 | R2Rest],
     Row3 = [R3C1, R3C2, R3C3 | R3Rest],
     all_distinct([R1C1, R1C2, R1C3, R2C1, R2C2, R2C3, R3C1, R3C2, R3C3]),
     sol4_checkBlocks(R1Rest, R2Rest, R3Rest).

sol4_printSudoku([]).
sol4_printSudoku([Row|Rest]) :- writeln(Row), sol4_printSudoku(Rest).
