% load_test_files(test_aufgabe_1).
% run_tests.

:- begin_tests(aufgabe_1).

% Albert will nicht zur Leitung gehören, wenn Emma nicht Vorsitzende wird.
test(leitung, fail) :- leitung(Leitung),
              vorsitzender(Vorsitzender, Leitung), Vorsitzender \= emma,
              zur_leitung_gehoeren(albert, Leitung).
test(leitung, forall) :- leitung(Leitung),
              vorsitzender(emma, Leitung);
              nicht_zur_leitung_gehoeren(albert, Leitung).


:- end_tests(aufgabe_1).