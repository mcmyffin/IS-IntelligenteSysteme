% execute tests with:
% ?- consult('aufgabe_1'), consult('test_aufgabe_1'), run_tests.

:- begin_tests(aufgabe_1).

% Allgemeine Tests
test(leitung) :- leitung(Leitung),
     % Die Leitung muss aus drei Personen bestehen
     Leitung = [Vorsitzender, Stellvertreter, Sekretaer],
     % Die Personen muessen sich unterscheiden
     Vorsitzender \= Stellvertreter,
     Stellvertreter \= Sekretaer,
     Vorsitzender \= Sekretaer.



% a) Albert will nicht zur Leitung gehören, wenn Emma nicht Vorsitzende wird.
test(leitung, nondet) :- leitung(Leitung),
     (vorsitzender(emma, Leitung);
     not(zur_leitung_gehoeren(albert, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     not(vorsitzender(emma, Leitung)),
     zur_leitung_gehoeren(albert, Leitung).

% b) Berta will nicht zur Leitung gehören, wenn sie über Chris stehen soll.
test(leitung, nondet) :- leitung(Leitung),
     (not(ist_ueber(berta, chris, Leitung));
     not(zur_leitung_gehoeren(berta, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     ist_ueber(berta, chris, Leitung),
     zur_leitung_gehoeren(berta, Leitung).

% c) Berta will unter gar keinen Umständen zusammen mit Felix arbeiten.
test(leitung, nondet) :- leitung(Leitung),
     (not(zur_leitung_gehoeren(berta, Leitung));
     not(zur_leitung_gehoeren(felix, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     zur_leitung_gehoeren(berta, Leitung),
     zur_leitung_gehoeren(felix, Leitung).

% d) Chris will nicht mitarbeiten, wenn der Leitung Emma und Felix zusammen angehören.
test(leitung, nondet) :- leitung(Leitung),
     (not(zur_leitung_gehoeren(emma, Leitung));
     not(zur_leitung_gehoeren(felix, Leitung));
     not(zur_leitung_gehoeren(chris, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     zur_leitung_gehoeren(emma, Leitung),
     zur_leitung_gehoeren(felix, Leitung),
     zur_leitung_gehoeren(chris, Leitung).

% e) Chris wird nicht mitarbeiten, wenn Felix Vorsitzender oder Berta Sekretär ist.
test(leitung, nondet) :- leitung(Leitung),
     (not(vorsitzender(felix, Leitung));
     not(sekretaer(berta, Leitung));
     not(zur_leitung_gehoeren(chris, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     vorsitzender(felix, Leitung),
     sekretaer(berta, Leitung),
     zur_leitung_gehoeren(chris, Leitung).

% f) Detlef wird nicht mit Chris oder Emma arbeiten, wenn er dem einen oder anderen unterstellt ist.
test(leitung, nondet) :- leitung(Leitung),
     (not(ist_ueber(chris, detlef, Leitung)); not(zur_leitung_gehoeren(detlef, Leitung))),
     (not(ist_ueber(emma, detlef, Leitung)); not(zur_leitung_gehoeren(detlef, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     (ist_ueber(chris, detlef, Leitung); ist_ueber(emma, detlef, Leitung)),
     zur_leitung_gehoeren(detlef, Leitung).

% g) Emma will nicht Stellvertreter sein.
test(leitung, nondet) :- leitung(Leitung),
     not(stellvertreter(emma, Leitung)).
test(leitung, fail) :- leitung(Leitung),
     stellvertreter(emma, Leitung).

% h) Emma will nicht Sekretär sein, wenn Detlef Mitglied der Leitung ist.
test(leitung, nondet) :- leitung(Leitung),
     (not(zur_leitung_gehoeren(detlef, Leitung));
     not(sekretaer(emma, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     zur_leitung_gehoeren(detlef, Leitung),
     sekretaer(emma, Leitung).

% i) Emma will nicht zusammen mit Albert arbeiten, wenn Felix nicht der Leitung angehört.
test(leitung, nondet) :- leitung(Leitung),
     (zur_leitung_gehoeren(felix, Leitung);
     not(zur_leitung_gehoeren(emma, Leitung));
     not(zur_leitung_gehoeren(albert, Leitung))).
test(leitung, fail) :- leitung(Leitung),
     not(zur_leitung_gehoeren(felix, Leitung)),
     zur_leitung_gehoeren(emma, Leitung),
     zur_leitung_gehoeren(albert, Leitung).

% j) Felix will nur mitarbeiten, wenn er oder Chris Vorsitzender wird.
test(leitung, nondet) :- leitung(Leitung),
     (not(zur_leitung_gehoeren(felix, Leitung));
     vorsitzender(felix, Leitung);
     vorsitzender(chris, Leitung)).
test(leitung, fail) :- leitung(Leitung),
     zur_leitung_gehoeren(felix, Leitung),
     not(vorsitzender(felix, Leitung)),
     not(vorsitzender(chris, Leitung)).

:- end_tests(aufgabe_1).