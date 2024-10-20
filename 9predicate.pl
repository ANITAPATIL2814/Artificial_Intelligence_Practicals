batsman(sachin).
wiketkeeper(dhoni).
footballer(ronaldo).
cricketer(A):-batsman(A).
cricketer(A):-wiketkeeper(A).
not_cricketer(A):-footballer(A).