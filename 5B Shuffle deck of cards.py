import random,itertools
deck=list(itertools.product(range(1,14),["spade","club","heart","diamond"]))
random.shuffle(deck)
print(deck)
for i in range(5):
    print(deck[i][0],"to",deck[i][1])
