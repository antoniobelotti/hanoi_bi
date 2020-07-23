hanoi(1, Source, Destination, _) :-
    atomic_list_concat([Source, Destination], " -> ", Move),
    write(Move), nl.

hanoi(N, Source, Destination, Tmp) :-
    K is N-1,
    hanoi(K, Source, Tmp, Destination),
    atomic_list_concat([Source, Destination], " -> ", Move),
    write(Move), nl,
    hanoi(K, Tmp, Destination, Source).

merge_towers(1, Source, Destination, Tmp):-
    hanoi(1, Source, Destination, Tmp).

merge_towers(N, Source, Destination, Tmp):-
    K is N-1,
    J is N+(N-1),
    merge_towers(K, Destination, Source, Tmp),
    hanoi(J, Source, Destination, Tmp).

hanoi_bicolor_merged_tower(1, Source, Destination, Tmp):-
    hanoi(1, Source, Destination, Tmp).

hanoi_bicolor_merged_tower(N, Source, Destination, Tmp):-
    K is N-1,
    hanoi(N, Source, Destination, Tmp),
    hanoi_bicolor_merged_tower(K, Destination, Source, Tmp).

hanoi_bicolor(N, Source1, Source2, Tmp):-
    K is 2*N,
    merge_towers(N, Source2, Source1, Tmp),
    hanoi_bicolor_merged_tower(K, Source1, Source2, Tmp).