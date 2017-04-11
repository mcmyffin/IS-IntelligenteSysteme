% execute tests with:
% ?- consult('aufgabe_1'), consult('test_aufgabe_1'), run_tests.

:- begin_tests(aufgabe_1).



% a) Albert will nicht zur Leitung gehören, wenn Emma nicht Vorsitzende wird.
test(leitung, fail) :- leitung(Leitung),
                       not(vorsitzender(emma, Leitung)),
                       zur_leitung_gehoeren(albert, Leitung).
test(leitung) :- leitung(Leitung),
                 (     vorsitzender(emma, Leitung);
                       not(zur_leitung_gehoeren(albert, Leitung))     ).



% b) ...
test(leitung) :- true.



:- end_tests(aufgabe_1).