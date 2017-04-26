:- use_module(library(clpfd)).
:- consult('start_allocations').

:- consult('Datei0').
:- consult('Datei1'). % check und print rows mit Sudoku = [Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9]
:- consult('Datei2'). % check domain mit all_distinct(Row1), ... (verworfen!)
:- consult('Datei3'). % vorgänger=Datei1! Hinzufügen von Unterfunktionen
:- consult('Datei4'). % verschiedenste Funktionen auf verschiedenste Weisen geändert
:- consult('Datei5'). % nur rekursionen durch maplist ersetzt (in checkRows und printRows)

solution(Solution) :-
     string_concat("writeln(solution", Solution, A),
     string_concat(A, "), sol", B),
     string_concat(B, Solution, C),
     string_concat(C, "_sudoku(1)", D),
     term_to_atom(E, D),
     E, nl.

run() :- maplist(solution, [0, 1, 2, 3, 4, 5]).
