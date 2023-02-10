import random
quote = "Most of the good programmers do programming "+ \
"not because they expect to get "+ \
"paid or get adulation by the public, "+ \
"but because it is fun to program."
num = random.randint(1,10)
print(num)
split = quote.split()
print(random.choice(split))
print(random.shuffle(split))