#lab 1
import smbus
import time

address = 0x68
register = 0x00
bus = smbus.SMbus(1)
Fixtime = [0x00,0x00,0x18,0x03,0x12,0x06,0x19]

def ds3231SetTime():
    bus.write_12c_block_data(address, register, Fixtime)

def ds3231ReadTime():
    return bus.read_12c_block_data(address, register,7)

ds3231SetTime()
ds3231ReadTime()

#lab2

from pyswip import Prolog
prolog = Prolog()
prolog.consult('bird.pl')
prolog.assertz('color(blue)')
prolog.assertz('serson(all_year)')
prolog.assertz('size(small)')
for result in prolog.query('bird(X)'):
    print(result['X'])

#lab2.5
from pyswip import Prolog, registerForeign

def hello(t):
    print('Hello,',t)
hello.arity = 1

registerForeign(hello)

prolog = Prolog()
prolog.assertz('father(michael, john)')#注意一下这里的空格有无效果
prolog.assertz('father(michael, gina)')
print(list(prolog.query('father(michael,X),hello(X)')))

#lab3
/* animal.pro
    animal identification game.
    start with ?- go. */
go :- hypothesize(Animal),
    write('I guess that the animal is: '),
    write(Animal),
    nl,
    undo.

/* hypotheses to be tested */
hypothesize(cheetah) :- cheetah, !.
hypothesize(tiger) :- tiger, !.
hypothesize(giraffe) :- giraffe, !.
hypothesize(zebra) :- zebra, !.
hypothesize(ostrich) :- ostrich, !.
hypothesize(penguin) :- penguin, !.
hypothesize(albatross) :- albatross, !.
hypothesize(unknown). /* no diagnosis */

/* animal identification rules */
cheetah :- mammal,
    carnivore,
    verify(has_tawny_color),
    verify(has_dark_spots).
tiger :- mammal,
    carnivore,
    verify(has_tawny_color),
    verify(has_black_stripes).
giraffe :- ungulate,
    verify(has_long_neck),
    verify(has_long_legs).
zebra :- ungulate,
    verify(has_black_stripes).
ostrich :- bird,
    verify(does_not_fly),
    verify(has_long_neck).
penguin :- bird,
    verify(does_not_fly),
    verify(swims),
    verify(is_black_and_white).
albatross :- bird,
    verify(appears_in_story_Ancient_Mariner),
    verify(flys_well).

/* classification rules */
mammal :- verify(has_hair), !.
mammal :- verify(gives_milk).
bird :- verify(has_feathers), !.
bird :- verify(flys),
    verify(lays_eggs).
carnivore :- verify(eats_meat), !.
carnivore :- verify(has_pointed_teeth),
    verify(has_claws),
    verify(has_forward_eyes).
ungulate :- mammal,
    verify(has_hooves), !.
ungulate :- mammal,
    verify(chews_cud).
/* how to ask questions */
ask(Question) :-
    write('Does the animal have the following attribute: '),
    write(Question),
    write('? '),
    read(Response),
    nl,
    ( (Response == yes ; Response == y)
        ->
        assert(yes(Question)) ;
        assert(no(Question)), fail).
:- dynamic yes/1,no/1.

/* How to verify something */
verify(S) :-
    (yes(S)
    ->
    true ;
    (no(S)
    ->
    fail ;
    ask(S))).

/* undo all yes/no assertions */
undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.