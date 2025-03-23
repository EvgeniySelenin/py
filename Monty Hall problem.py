import random

l = [0, 0, 1]

pomenyal = 0
nepomenyal = 0

for i in range(10000):
    random.shuffle(l)
    ch = random.choice(l)
    nepomenyal += ch
    if ch == 0:
        pomenyal += 1

print("Сменил дверь: ", pomenyal)
print("Не менял дверь: ", nepomenyal)
