import random
import time

PRIZES = [
    ('Goldfish',5),
    ('Stuffed Animal',2),
    ('Free Replay',10),
    ('2 dollars',4),
    ('Bag of Popcorn',5),
    ('Action Figure',2),
    ('Bead Necklace',2)
]

def RandomIndex(N):
    return random.randint(0,N)

def SelectPrize(prizes):
    index = RandomIndex(len(prizes))
    return prizes[index]

def RemovePrize(prizes, prize):
    index = prizes.index(prize)
    del prizes[index]


def RollForPrize(prizes):
    T = 0.01
    prize = None
    while T < 0.5:
        prize = SelectPrize(prizes)
        print(prize)
        time.sleep(T)
        T += 0.03
    print("You won:",prize)
    RemovePrize(prizes, prize)

def main():
    prize_list = []
    for p,n in PRIZES:
        for i in range(n):
            prize_list.append(p)
    RollForPrize(prize_list)


main()