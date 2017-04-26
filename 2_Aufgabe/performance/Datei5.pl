sol5_sudoku(Number) :-
     sudoku(Number, Sudoku),
     sol5_solveSudoku(Sudoku),
     time(sol5_printSudoku(Sudoku)).

sol5_solveSudoku(Sudoku) :-
     time(sol5_checkLength(Sudoku)),
     time(sol5_checkDomain(Sudoku)),
     time(sol5_checkRows(Sudoku)),
     time(sol5_checkCols(Sudoku)),
     time(sol5_checkBlocks(Sudoku)).

sol5_checkLength(Sudoku) :- length(Sudoku, 9), maplist(sol5_checkLengthInner, Sudoku).
sol5_checkLengthInner(Row) :- length(Row, 9).

sol5_checkDomain(Sudoku) :-
     append(Sudoku, SudokuFlatted),
     SudokuFlatted ins 1..9.

sol5_checkRows(Sudoku) :- maplist(all_distinct, Sudoku).

sol5_checkCols(Sudoku) :-
     transpose(Sudoku, SudokuTransposed),
     sol5_checkRows(SudokuTransposed).

sol5_checkBlocks(Sudoku) :-
     Sudoku = [Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9],
     sol5_checkBlocks(Row1, Row2, Row3),
     sol5_checkBlocks(Row4, Row5, Row6),
     sol5_checkBlocks(Row7, Row8, Row9).

sol5_checkBlocks([], [], []).
sol5_checkBlocks(Row1, Row2, Row3) :-
     Row1 = [R1C1, R1C2, R1C3 | R1Rest],
     Row2 = [R2C1, R2C2, R2C3 | R2Rest],
     Row3 = [R3C1, R3C2, R3C3 | R3Rest],
     all_distinct([R1C1, R1C2, R1C3, R2C1, R2C2, R2C3, R3C1, R3C2, R3C3]),
     sol5_checkBlocks(R1Rest, R2Rest, R3Rest).

sol5_printSudoku(Sudoku) :- maplist(writeln, Sudoku).
