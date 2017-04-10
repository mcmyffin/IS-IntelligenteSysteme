% Personen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
personen([albert,berta,chris,detlef,emma,felix]).

% Positionen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
vorsitzender(X,Leitung) 	:- nth1(1,Leitung,X).
stellvertreter(X,Leitung)	:- nth1(2,Leitung,X).
sekretaer(X,Leitung)		:- nth1(3,Leitung,X).

% X ueber Y in der Leitung %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ist_ueber(X,Y,Leitung)		:- member(X,Leitung) , nicht_zur_leitung_gehoeren(Y,Leitung);
								member(X,Leitung) , member(Y,Leitung),
								nth1(X_inx,Leitung,X), nth1(Y_inx,Leitung,Y),
								X_inx < Y_inx.

% zur leitung gehoeren %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%zu_leitung_gehoeren(X,Leitung) :- member(X,Leitung).

% nicht zur leitung gehoeren %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nicht_zur_leitung_gehoeren(X,[X|_]) :- ! , fail.
nicht_zur_leitung_gehoeren(X,[_|RestDerLeitung]) :- ! , nicht_zur_leitung_gehoeren(X,RestDerLeitung).
nicht_zur_leitung_gehoeren(_,[]).

% Regeln %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Albert will nicht zur Leitung gehören, wenn Emma nicht Vorsitzende wird.
a(Leitung) :- vorsitzender(emma,Leitung) ; nicht_zur_leitung_gehoeren(albert,Leitung).

% Berta will nicht zur Leitung gehören, wenn sie über Chris stehen soll.
b(Leitung) :- nicht_zur_leitung_gehoeren(berta,Leitung) ; ist_ueber(chris,berta,Leitung).

% Berta will unter gar keinen Umständen zusammen mit Felix arbeiten.
c(Leitung) :- nicht_zur_leitung_gehoeren(berta,Leitung) ; nicht_zur_leitung_gehoeren(felix,Leitung).

% Chris will nicht mitarbeiten, wenn der Leitung Emma und Felix zusammen angehören.
d(Leitung) :- nicht_zur_leitung_gehoeren(emma,Leitung) ; nicht_zur_leitung_gehoeren(felix,Leitung) ; nicht_zur_leitung_gehoeren(chris,Leitung).

% Chris wird nicht mitarbeiten, wenn Felix Vorsitzender oder Berta Sekretär ist.
e(Leitung) :- (vorsitzender(Vorsitzender,Leitung) , sekretaer(Sekretaer,Leitung) , 
				Vorsitzender \= felix , Sekretaer \= berta) ; 
			  	nicht_zur_leitung_gehoeren(chris,Leitung).

% Detlef wird nicht mit Chris oder Emma arbeiten, wenn er dem einen oder anderen unterstellt ist.
f(Leitung) :- nicht_zur_leitung_gehoeren(detlef,Leitung) ; (ist_ueber(detlef,chris,Leitung) , ist_ueber(detlef,emma,Leitung)).

% Emma will nicht Stellvertreter sein.
g(Leitung) :- stellvertreter(Stellvertreter,Leitung), Stellvertreter \= emma.

% Emma will nicht Sekretär sein, wenn Detlef Mitglied der Leitung ist.
h(Leitung) :- nicht_zur_leitung_gehoeren(detlef,Leitung) ; (sekretaer(Sekretaer), Sekretaer \= emma).

% Emma will nicht zusammen mit Albert arbeiten, wenn Felix nicht der Leitung angehört.
i(Leitung) :- member(felix,Leitung) ; nicht_zur_leitung_gehoeren(emma,Leitung) ; nicht_zur_leitung_gehoeren(albert,Leitung).

% Felix will nur mitarbeiten, wenn er oder Chris Vorsitzender wird.
j(Leitung) :- vorsitzender(chris,Leitung) ; vorsitzender(felix,Leitung) ; nicht_zur_leitung_gehoeren(felix,Leitung).


% Leitung belegen %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

leitung(Leitung) :-
	% Drei Personen gehoeren der Leitung an.
	length(Leitung,3),

	% Die Leitung besteht aus den Personen
	personen(Personen),
	member(Vorsitzender,Personen),
	member(Stellvertreter,Personen),
	member(Sekretaer,Personen),

	% Die Belegung der Leitung muss aus unterschiedlichen Personen bestehn.
	vorsitzender(Vorsitzender,Leitung),
	stellvertreter(Stellvertreter,Leitung),
	sekretaer(Sekretaer,Leitung),

	Vorsitzender \= Stellvertreter,
	Stellvertreter \= Sekretaer,
	Vorsitzender \= Sekretaer,

	% Und es gelten alle Regeln
	a(Leitung),
	b(Leitung),
	c(Leitung),
	d(Leitung),
	e(Leitung),
	f(Leitung),
	g(Leitung),
	h(Leitung),
	i(Leitung),
	j(Leitung), ! .
