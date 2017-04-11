% Personen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
personen([albert, berta, chris, detlef, emma, felix]).



% Positionen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
vorsitzender(X, Leitung)   :- nth1(1, Leitung, X).
stellvertreter(X, Leitung) :- nth1(2, Leitung, X).
sekretaer(X, Leitung)      :- nth1(3, Leitung, X).

% X ueber Y in der Leitung %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ist_ueber(X, Y, Leitung) :- zur_leitung_gehoeren(X, Leitung),
                            nicht_zur_leitung_gehoeren(Y, Leitung).
ist_ueber(X, Y, Leitung) :- zur_leitung_gehoeren(X, Leitung),
                            zur_leitung_gehoeren(Y, Leitung),
                            nth1(IndexX, Leitung, X),
                            nth1(IndexY, Leitung, Y),
                            IndexX < IndexY.

% zur leitung gehoeren %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
zur_leitung_gehoeren(X, Leitung)       :- member(X, Leitung).

% nicht zur leitung gehoeren %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nicht_zur_leitung_gehoeren(X, Leitung) :- not(zur_leitung_gehoeren(X, Leitung)).



% Regeln %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Albert will nicht zur Leitung gehören, wenn Emma nicht Vorsitzende wird.
a(Leitung) :- vorsitzender(emma, Leitung).
a(Leitung) :- nicht_zur_leitung_gehoeren(albert, Leitung).

% Berta will nicht zur Leitung gehören, wenn sie über Chris stehen soll.
b(Leitung) :- nicht_zur_leitung_gehoeren(berta, Leitung).
b(Leitung) :- ist_ueber(chris, berta, Leitung).

% Berta will unter gar keinen Umständen zusammen mit Felix arbeiten.
c(Leitung) :- nicht_zur_leitung_gehoeren(berta, Leitung).
c(Leitung) :- nicht_zur_leitung_gehoeren(felix, Leitung).

% Chris will nicht mitarbeiten, wenn der Leitung Emma und Felix zusammen angehören.
d(Leitung) :- nicht_zur_leitung_gehoeren(emma, Leitung).
d(Leitung) :- nicht_zur_leitung_gehoeren(felix, Leitung).
d(Leitung) :- nicht_zur_leitung_gehoeren(chris, Leitung).

% Chris wird nicht mitarbeiten, wenn Felix Vorsitzender oder Berta Sekretär ist.
e(Leitung) :- vorsitzender(Vorsitzender, Leitung), Vorsitzender \= felix,
              sekretaer(Sekretaer, Leitung), Sekretaer \= berta.
e(Leitung) :- nicht_zur_leitung_gehoeren(chris, Leitung).

% Detlef wird nicht mit Chris oder Emma arbeiten, wenn er dem einen oder anderen unterstellt ist.
f(Leitung) :- nicht_zur_leitung_gehoeren(detlef, Leitung).
f(Leitung) :- ist_ueber(detlef, chris, Leitung),
              ist_ueber(detlef, emma, Leitung).

% Emma will nicht Stellvertreter sein.
g(Leitung) :- stellvertreter(Stellvertreter, Leitung), Stellvertreter \= emma.

% Emma will nicht Sekretär sein, wenn Detlef Mitglied der Leitung ist.
h(Leitung) :- nicht_zur_leitung_gehoeren(detlef, Leitung).
h(Leitung) :- sekretaer(Sekretaer, Leitung), Sekretaer \= emma.

% Emma will nicht zusammen mit Albert arbeiten, wenn Felix nicht der Leitung angehört.
i(Leitung) :- zur_leitung_gehoeren(felix, Leitung).
i(Leitung) :- nicht_zur_leitung_gehoeren(emma, Leitung).
i(Leitung) :- nicht_zur_leitung_gehoeren(albert, Leitung).

% Felix will nur mitarbeiten, wenn er oder Chris Vorsitzender wird.
j(Leitung) :- vorsitzender(chris, Leitung).
j(Leitung) :- vorsitzender(felix, Leitung).
j(Leitung) :- nicht_zur_leitung_gehoeren(felix, Leitung).


% Leitung belegen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

leitung(Leitung) :-
        % Auswahl von drei Personen.
        personen(Personen),
        member(Vorsitzender, Personen),
        member(Stellvertreter, Personen),
        member(Sekretaer, Personen),

        % Die drei Personen muessen sich unterscheiden.
        Vorsitzender \= Stellvertreter,
        Stellvertreter \= Sekretaer,
        Vorsitzender \= Sekretaer,

        % Zuweisung der Positionen
        Leitung = [Vorsitzender, Stellvertreter, Sekretaer],
        
        % Es muessen folgende Regeln gelten
        a(Leitung),
        b(Leitung),
        c(Leitung),
        d(Leitung),
        e(Leitung),
        f(Leitung),
        g(Leitung),
        h(Leitung),
        i(Leitung),
        j(Leitung),
        !.
