p: bool = True
q: bool = False
if True:
    #badane
    print("oomad tooye shart! #0")

if p and q:
    print("oomad tooye shart! #1")
else:
    print("nayoomad too sharte 1! :(")
if p or q:
    print("oomad tooye shart! #2")

if (p and q) or p:
    print("oomad tooye shart! #3")

if q:
    print("q true ast!")
elif (q and p) or q:
    print("(q and p) or q == True hastesh!")
else:
    print("hich sharti bargharar nabood!")
i: int = 0
n: int = int(input("Chand ta setare mikhay? "))
while i < n:
    print('*', end="")
    i = i + 1
print()

print(list(range(0,10,1)))
l: list[str] = ["ali", "sajjad", "morteza", "nima", "hamed"]
l2: list[int] = [2, 1, 8, 10]
s: int = 0
for a in range(0, 12):
    print(a)


i: int = 0
n: int = int(input("Chand ta setare mikhay? "))
while i < n:
    print('*', end="")
    i = i + 1
print()
for i in range(0, n):
    print('*', end="")

# bebinim aya yek ozv dar yek list vojood darad?
ayaPeydaShode: bool = False
chiziKeDonbaleshim: int = 20
L: list[int] = [1,10,16,20,2,79,5, 20]
i: int = 0
for a in L:
    if a == chiziKeDonbaleshim:
        ayaPeydaShode = True # chizi ke mikham peyda shode
        break # bia birun az halghe
    i += 1 # -= /= *=
print(ayaPeydaShode)
print(i) # mibinim ke ta akhare list nemire va vaghti peyda karde oomade birun

# chand ta az yek ozv tooye yek list darim?
c: int = 0 # te'dad
for a in L:
    if a == chiziKeDonbaleshim:
        c += 1
print(str(c) + " ta az chizi ke mikhaym too list hast!")

# chappe a'dad az 1 ta 20 bejoz oonayi ke mazrabe 5 hastan
for i in range(1,21):
    if i % 5 == 0:
        continue # baghieye in bakhsh az halghe ro vel kon, boro i ba'di
    print(i)

#halgheye too dar too
#jadvale zarb 10x10
for i in range(1,11):
    for j in range(1,11):
        print(f"{j * i}, \t", end="")
    if i != 10:
        print()

#bubble sort
l: list[int] = [1,12,3,86, 87, 21, 19,22]
for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[j] >  l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)

def F(x):
    return x * x
a = F(2)
print(a)