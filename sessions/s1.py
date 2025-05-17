#esmemotaghayer = meghdar
a: int = 2 #adade sahih
pi: float = 3.1415 #adade a'shari
c: float = 2.998e8 # 3 * 10^(10)
s: str = "salam" # reshte i az kalamat
s2: str = s + "chetori" # "salam chetori"
s3: str = "az" * 3 # "azazaz"
b: bool = 2.7281 ** 10 > 10 ** 2.7281 # "aya e^10 > 10^e ?"
e: float = 2.7281

s4: str = "\n" #khatte ba'di
s5: str = "\t" #boro yedune jelo

s6: str = "1395.3"


#b = a * pi
print(float(s6) + 20)

# In = int(input()) # string mide
# print(In ** 3)

# boolean operations
b2: bool = pi < c # koochak tar
b3: bool = pi >= e # bozorgtar ya mosavi
b4: bool = pi == e # mosavi
b5: bool = pi != e # aya fargh darand?

p: bool = True
q: bool = False
r1: bool = p and q
r1: bool = p or q

F = (2 + 3) / 2
Q = (p and q) or q


#
#          0 1 2 3 4 5
L: list = [1,2,3,9,8,2]
op: int = (L[3] + L[1]) # 11
tool: int = len(L) # 6

R: list[int] = list(range(0,10,2)) # [0,2,4,6,8]
R1: list[int] = list(range(6)) # [0,1,2,3,4,5]

L[1] = 30
print(L)

C:str = 'a'
ss: str = "salam!"

asci:int = ord(C) # code ascii yek character
s4: str = chr(97) # tabdile code ascii be character

print(ord(ss[0]))
st = "salam mikham beram kooh"

ssKoochik: str = ss.lower() # tabdil hame horoof be horoofe koochik
ssBozorg: str = ss.upper() # tabdile hame horoof be horoofe bozorg
ssReplace: str = ss.replace("s", "!") #  be jaye s, ! gozashtim
ssTedadeA: int = ss.count("a") # ebarate "a" chand bar tekrar shode
splitShode: list[str] = st.split(' ')

print(splitShode)
