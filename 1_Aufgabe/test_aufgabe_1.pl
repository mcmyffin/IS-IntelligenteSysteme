% load_test_files(test_aufgabe_1).
% run_tests.

:- begin_tests(aufgabe_1).

% Albert will nicht zur Leitung geh�ren, wenn Emma nicht Vorsitzende wird.
test(leitung, fail) :- leitung(Leitung),
              zur_leitung_gehoeren(albert, Leitung),
              vorsitzender(Vorsitzender, Leitung), Vorsitzender \= emma.
test(leitung, forall) :- leitung(Leitung),
              nicht_zur_leitung_gehoeren(albert, Leitung);
              vorsitzender(emma, Leitung).


:- end_tests(aufgabe_1).