import random

sqw1 = 0
sqw2 = 0
sqw3 = 0
sqw4 = 0
sqw5 = 0
sqw6 = 0
sqw7 = 0
sqw8 = 0
sqw9 = 0
sqw10 = 0
sqw11 = 0
sqw12 = 0
sqw13 = 0
sqw14 = 0
sqw15 = 0
sqw16 = 0
sqw17 = 0
sqw18 = 0
sqw19 = 0
sqw20 = 0

gfd = (open('EPL/ARS.txt', 'r'))
sqw1 = int(gfd.read())
gfd = (open('EPL/ASTON.txt', 'r'))
sqw2 = int(gfd.read())
gfd = (open('EPL/BOR.txt', 'r'))
sqw3 = int(gfd.read())
gfd = (open('EPL/BRAIT.txt', 'r'))
sqw4 = int(gfd.read())
gfd = (open('EPL/BRENT.txt', 'r'))
sqw5 = int(gfd.read())
gfd = (open('EPL/CHELS.txt', 'r'))
sqw6 = int(gfd.read())
gfd = (open('EPL/CITY.txt', 'r'))
sqw7 = int(gfd.read())
gfd = (open('EPL/CRISTAL.txt', 'r'))
sqw8 = int(gfd.read())
gfd = (open('EPL/EVE.txt', 'r'))
sqw9 = int(gfd.read())
gfd = (open('EPL/FOREST.txt', 'r'))
sqw10 = int(gfd.read())
gfd = (open('EPL/FULL.txt', 'r'))
sqw11 = int(gfd.read())
gfd = (open('EPL/LEST.txt', 'r'))
sqw12 = int(gfd.read())
gfd = (open('EPL/LIDS.txt', 'r'))
sqw13 = int(gfd.read())
gfd = (open('EPL/LIVE.txt', 'r'))
sqw14 = int(gfd.read())
gfd = (open('EPL/MU.txt', 'r'))
sqw15 = int(gfd.read())
gfd = (open('EPL/NEWCC.txt', 'r'))
sqw16 = int(gfd.read())
gfd = (open('EPL/SAUT.txt', 'r'))
sqw17 = int(gfd.read())
gfd = (open('EPL/TTH.txt', 'r'))
sqw18 = int(gfd.read())
gfd = (open('EPL/WEST.txt', 'r'))
sqw19 = int(gfd.read())
gfd = (open('EPL/WOLVES.txt', 'r'))
sqw20 = int(gfd.read())

ps1 = []
ps2 = []
ps3 = []
ps4 = []
ps5 = []
ps6 = []
ps7 = []
ps8 = []
ps9 = []
ps10 = []
ps11 = []
ps12 = []
ps13 = []
ps14 = []
ps15 = []
ps16 = []
ps17 = []
ps18 = []
ps19 = []
ps20 = []

sg1 = []
sg2 = []
sg3 = []
sg4 = []
sg5 = []
sg6 = []
sg7 = []
sg8 = []
sg9 = []
sg10 = []
sg11 = []
sg12 = []
sg13 = []
sg14 = []
sg15 = []
sg16 = []
sg17 = []
sg18 = []
sg19 = []
sg20 = []

lg1 = []
lg2 = []
lg3 = []
lg4 = []
lg5 = []
lg6 = []
lg7 = []
lg8 = []
lg9 = []
lg10 = []
lg11 = []
lg12 = []
lg13 = []
lg14 = []
lg15 = []
lg16 = []
lg17 = []
lg18 = []
lg19 = []
lg20 = []

pts1 = int()
pts2 = int()
pts3 = int()
pts4 = int()
pts5 = int()
pts6 = int()
pts7 = int()
pts8 = int()
pts9 = int()
pts10 = int()
pts11 = int()
pts12 = int()
pts13 = int()
pts14 = int()
pts15 = int()
pts16 = int()
pts17 = int()
pts18 = int()
pts19 = int()
pts20 = int()

reit1 = 0


def play(pts1, pts2, sqw1, sqw2, ps1, ps2, sg1, sg2, lg1, lg2):
    res = [1, 2, 0, 2, 1]
    reit1 = (sqw1 - sqw2)
    while reit1 > 0:
        res.append(1)
        reit1 = (reit1 - 1)
    while reit1 < 0:
        res.append(2)
        reit1 = (reit1 + 1)
    from random import choice
    char = choice(res)
    if char == 1:
        pts1 = (pts1 + 3)
        ps1.append(pts1)
        mm = ['5:0', '4:0', '3:0', '2:0', '1:0', '3:1', '2:1', '5:1', '4:2', '7:1', '8:2', '2:0', '1:0', '2:0', '1:0',
              '2:0', '1:0', '2:0', '1:0', '2:0', '1:0', '2:0', '1:0', '3:1', '2:1', '3:1', '2:1', '3:1', '2:1', '2:1',
              '2:1']
        from random import choice
        char1 = choice(mm)
        if char1 == ('5:0'):
            sg1.append(5)
            lg2.append(5)
        if char1 == ('4:0'):
            sg1.append(4)
            lg2.append(4)
        if char1 == ('3:0'):
            sg1.append(3)
            lg2.append(3)
        if char1 == ('2:0'):
            sg1.append(2)
            lg2.append(2)
        if char1 == ('1:0'):
            sg1.append(1)
            lg2.append(1)
        if char1 == ('3:1'):
            sg1.append(3)
            lg2.append(3)
            sg2.append(1)
            lg1.append(1)
        if char1 == ('2:1'):
            sg1.append(2)
            lg2.append(2)
            sg2.append(1)
            lg1.append(1)
        if char1 == ('5:1'):
            sg1.append(5)
            lg2.append(5)
            sg2.append(1)
            lg1.append(1)
        if char1 == ('4:2'):
            sg1.append(4)
            lg2.append(4)
            sg2.append(2)
            lg1.append(2)
        if char1 == ('7:1'):
            sg1.append(7)
            lg2.append(7)
            sg2.append(1)
            lg1.append(1)
        if char1 == ('8:2'):
            sg1.append(8)
            lg2.append(8)
            sg2.append(2)
            lg1.append(2)
        print(sqw1, ' ', char1, ' ', sqw2)
    elif char == 2:
        pts2 = (pts2 + 3)
        ps2.append(pts2)
        mmm = ['0:5', '0:4', '0:3', '0:2', '0:1', '1:3', '1:2', '1:5', '2:4', '1:7', '2:8', '0:1', '0:1', '0:1', '0:1',
               '0:1', '1:2', '1:2', '1:2', '1:2', '0:2', '0:2', '0:2']
        from random import choice
        char2 = choice(mmm)
        if char2 == ('0:5'):
            sg2.append(5)
            lg1.append(5)
        if char2 == ('0:4'):
            sg2.append(4)
            lg1.append(4)
        if char2 == ('0:3'):
            sg2.append(3)
            lg1.append(3)
        if char2 == ('0:2'):
            sg2.append(2)
            lg1.append(2)
        if char2 == ('0:1'):
            sg2.append(1)
            lg1.append(1)
        if char2 == ('1:3'):
            sg2.append(3)
            lg1.append(3)
            sg1.append(1)
            lg2.append(1)
        if char2 == ('1:2'):
            sg2.append(2)
            lg1.append(2)
            sg1.append(1)
            lg2.append(1)
        if char2 == ('1:5'):
            sg2.append(5)
            lg1.append(5)
            sg1.append(1)
            lg2.append(1)
        if char2 == ('2:4'):
            sg2.append(4)
            lg1.append(4)
            sg1.append(2)
            lg2.append(2)
        if char2 == ('1:7'):
            sg2.append(7)
            lg1.append(7)
            sg1.append(1)
            lg2.append(1)
        if char2 == ('2:8'):
            sg2.append(8)
            lg1.append(8)
            sg1.append(2)
            lg2.append(2)
        print(sqw1, ' ', char2, ' ', sqw2)
    elif char == 0:
        pts1 = (pts1 + 1)
        pts2 = (pts2 + 1)
        ps1.append(pts1)
        ps2.append(pts2)
        mmmm = ['1:1', '0:0', '1:1', '0:0', '1:1', '0:0', '2:2', '3:3', '4:4', '5:5']
        from random import choice
        char3 = choice(mmmm)
        if char3 == ('5:5'):
            sg2.append(5)
            lg1.append(5)
            sg1.append(5)
            lg2.append(5)
        if char3 == ('4:4'):
            sg2.append(4)
            lg1.append(4)
            sg1.append(4)
            lg2.append(4)
        if char3 == ('3:3'):
            sg2.append(3)
            lg1.append(3)
            sg1.append(3)
            lg2.append(3)
        if char3 == ('2:2'):
            sg2.append(2)
            lg1.append(2)
            sg1.append(2)
            lg2.append(2)
        if char3 == ('1:1'):
            sg2.append(1)
            lg1.append(1)
            sg1.append(1)
            lg2.append(1)

        print(sqw1, ' ', char3, ' ', sqw2)


play(pts1, pts2, sqw1, sqw2, ps1, ps2, sg1, sg2, lg1, lg2)
play(pts1, pts3, sqw1, sqw3, ps1, ps3, sg1, sg3, lg1, lg3)
play(pts1, pts4, sqw1, sqw4, ps1, ps4, sg1, sg4, lg1, lg4)
play(pts1, pts5, sqw1, sqw5, ps1, ps5, sg1, sg5, lg1, lg5)
play(pts1, pts6, sqw1, sqw6, ps1, ps6, sg1, sg6, lg1, lg6)
play(pts1, pts7, sqw1, sqw7, ps1, ps7, sg1, sg7, lg1, lg7)
play(pts1, pts8, sqw1, sqw8, ps1, ps8, sg1, sg8, lg1, lg8)
play(pts1, pts9, sqw1, sqw9, ps1, ps9, sg1, sg9, lg1, lg9)
play(pts1, pts10, sqw1, sqw10, ps1, ps10, sg1, sg10, lg1, lg10)
play(pts1, pts11, sqw1, sqw11, ps1, ps11, sg1, sg11, lg1, lg11)
play(pts1, pts12, sqw1, sqw12, ps1, ps12, sg1, sg12, lg1, lg12)
play(pts1, pts13, sqw1, sqw13, ps1, ps13, sg1, sg13, lg1, lg13)
play(pts1, pts14, sqw1, sqw14, ps1, ps14, sg1, sg14, lg1, lg14)
play(pts1, pts15, sqw1, sqw15, ps1, ps15, sg1, sg15, lg1, lg15)
play(pts1, pts16, sqw1, sqw16, ps1, ps16, sg1, sg16, lg1, lg16)
play(pts1, pts17, sqw1, sqw17, ps1, ps17, sg1, sg17, lg1, lg17)
play(pts1, pts18, sqw1, sqw18, ps1, ps18, sg1, sg18, lg1, lg18)
play(pts1, pts19, sqw1, sqw19, ps1, ps19, sg1, sg19, lg1, lg19)
play(pts1, pts20, sqw1, sqw20, ps1, ps20, sg1, sg20, lg1, lg20)
play(pts2, pts3, sqw2, sqw3, ps2, ps3, sg2, sg3, lg2, lg3)
play(pts2, pts4, sqw2, sqw4, ps2, ps4, sg2, sg4, lg2, lg4)
play(pts2, pts5, sqw2, sqw5, ps2, ps5, sg2, sg5, lg2, lg5)
play(pts2, pts6, sqw2, sqw6, ps2, ps6, sg2, sg6, lg2, lg6)
play(pts2, pts7, sqw2, sqw7, ps2, ps7, sg2, sg7, lg2, lg7)
play(pts2, pts8, sqw2, sqw8, ps2, ps8, sg2, sg8, lg2, lg8)
play(pts2, pts9, sqw2, sqw9, ps2, ps9, sg2, sg9, lg2, lg9)
play(pts2, pts10, sqw2, sqw10, ps2, ps10, sg2, sg10, lg2, lg10)
play(pts2, pts11, sqw2, sqw11, ps2, ps11, sg2, sg11, lg2, lg11)
play(pts2, pts12, sqw2, sqw12, ps2, ps12, sg2, sg12, lg2, lg12)
play(pts2, pts13, sqw2, sqw13, ps2, ps13, sg2, sg13, lg2, lg13)
play(pts2, pts14, sqw2, sqw14, ps2, ps14, sg2, sg14, lg2, lg14)
play(pts2, pts15, sqw2, sqw15, ps2, ps15, sg2, sg15, lg2, lg15)
play(pts2, pts16, sqw2, sqw16, ps2, ps16, sg2, sg16, lg2, lg16)
play(pts2, pts17, sqw2, sqw17, ps2, ps17, sg2, sg17, lg2, lg17)
play(pts2, pts18, sqw2, sqw18, ps2, ps18, sg2, sg18, lg2, lg18)
play(pts2, pts19, sqw2, sqw19, ps2, ps19, sg2, sg19, lg2, lg19)
play(pts2, pts20, sqw2, sqw20, ps2, ps20, sg2, sg20, lg2, lg20)
play(pts3, pts4, sqw3, sqw4, ps3, ps4, sg3, sg4, lg3, lg4)
play(pts3, pts5, sqw3, sqw5, ps3, ps5, sg3, sg5, lg3, lg5)
play(pts3, pts6, sqw3, sqw6, ps3, ps6, sg3, sg6, lg3, lg6)
play(pts3, pts7, sqw3, sqw7, ps3, ps7, sg3, sg7, lg3, lg7)
play(pts3, pts8, sqw3, sqw8, ps3, ps8, sg3, sg8, lg3, lg8)
play(pts3, pts9, sqw3, sqw9, ps3, ps9, sg3, sg9, lg3, lg9)
play(pts3, pts10, sqw3, sqw10, ps3, ps10, sg3, sg10, lg3, lg10)
play(pts3, pts11, sqw3, sqw11, ps3, ps11, sg3, sg11, lg3, lg11)
play(pts3, pts12, sqw3, sqw12, ps3, ps12, sg3, sg12, lg3, lg12)
play(pts3, pts13, sqw3, sqw13, ps3, ps13, sg3, sg13, lg3, lg13)
play(pts3, pts14, sqw3, sqw14, ps3, ps14, sg3, sg14, lg3, lg14)
play(pts3, pts15, sqw3, sqw15, ps3, ps15, sg3, sg15, lg3, lg15)
play(pts3, pts16, sqw3, sqw16, ps3, ps16, sg3, sg16, lg3, lg16)
play(pts3, pts17, sqw3, sqw17, ps3, ps17, sg3, sg17, lg3, lg17)
play(pts3, pts18, sqw3, sqw18, ps3, ps18, sg3, sg18, lg3, lg18)
play(pts3, pts19, sqw3, sqw19, ps3, ps19, sg3, sg19, lg3, lg19)
play(pts3, pts20, sqw3, sqw20, ps3, ps20, sg3, sg20, lg3, lg20)
play(pts4, pts5, sqw4, sqw5, ps4, ps5, sg4, sg5, lg4, lg5)
play(pts4, pts6, sqw4, sqw6, ps4, ps6, sg4, sg6, lg4, lg6)
play(pts4, pts7, sqw4, sqw7, ps4, ps7, sg4, sg7, lg4, lg7)
play(pts4, pts8, sqw4, sqw8, ps4, ps8, sg4, sg8, lg4, lg8)
play(pts4, pts9, sqw4, sqw9, ps4, ps9, sg4, sg9, lg4, lg9)
play(pts4, pts10, sqw4, sqw10, ps4, ps10, sg4, sg10, lg4, lg10)
play(pts4, pts11, sqw4, sqw11, ps4, ps11, sg4, sg11, lg4, lg11)
play(pts4, pts12, sqw4, sqw12, ps4, ps12, sg4, sg12, lg4, lg12)
play(pts4, pts13, sqw4, sqw13, ps4, ps13, sg4, sg13, lg4, lg13)
play(pts4, pts14, sqw4, sqw14, ps4, ps14, sg4, sg14, lg4, lg14)
play(pts4, pts15, sqw4, sqw15, ps4, ps15, sg4, sg15, lg4, lg15)
play(pts4, pts16, sqw4, sqw16, ps4, ps16, sg4, sg16, lg4, lg16)
play(pts4, pts17, sqw4, sqw17, ps4, ps17, sg4, sg17, lg4, lg17)
play(pts4, pts18, sqw4, sqw18, ps4, ps18, sg4, sg18, lg4, lg18)
play(pts4, pts19, sqw4, sqw19, ps4, ps19, sg4, sg19, lg4, lg19)
play(pts4, pts20, sqw4, sqw20, ps4, ps20, sg4, sg20, lg4, lg20)
play(pts5, pts6, sqw5, sqw6, ps5, ps6, sg5, sg6, lg5, lg6)
play(pts5, pts7, sqw5, sqw7, ps5, ps7, sg5, sg7, lg5, lg7)
play(pts5, pts8, sqw5, sqw8, ps5, ps8, sg5, sg8, lg5, lg8)
play(pts5, pts9, sqw5, sqw9, ps5, ps9, sg5, sg9, lg5, lg9)
play(pts5, pts10, sqw5, sqw10, ps5, ps10, sg5, sg10, lg5, lg10)
play(pts5, pts11, sqw5, sqw11, ps5, ps11, sg5, sg11, lg5, lg11)
play(pts5, pts12, sqw5, sqw12, ps5, ps12, sg5, sg12, lg5, lg12)
play(pts5, pts13, sqw5, sqw13, ps5, ps13, sg5, sg13, lg5, lg13)
play(pts5, pts14, sqw5, sqw14, ps5, ps14, sg5, sg14, lg5, lg14)
play(pts5, pts15, sqw5, sqw15, ps5, ps15, sg5, sg15, lg5, lg15)
play(pts5, pts16, sqw5, sqw16, ps5, ps16, sg5, sg16, lg5, lg16)
play(pts5, pts17, sqw5, sqw17, ps5, ps17, sg5, sg17, lg5, lg17)
play(pts5, pts18, sqw5, sqw18, ps5, ps18, sg5, sg18, lg5, lg18)
play(pts5, pts19, sqw5, sqw19, ps5, ps19, sg5, sg19, lg5, lg19)
play(pts5, pts20, sqw5, sqw20, ps5, ps20, sg5, sg20, lg5, lg20)
play(pts6, pts7, sqw6, sqw7, ps6, ps7, sg6, sg7, lg6, lg7)
play(pts6, pts8, sqw6, sqw8, ps6, ps8, sg6, sg8, lg6, lg8)
play(pts6, pts9, sqw6, sqw9, ps6, ps9, sg6, sg9, lg6, lg9)
play(pts6, pts10, sqw6, sqw10, ps6, ps10, sg6, sg10, lg6, lg10)
play(pts6, pts11, sqw6, sqw11, ps6, ps11, sg6, sg11, lg6, lg11)
play(pts6, pts12, sqw6, sqw12, ps6, ps12, sg6, sg12, lg6, lg12)
play(pts6, pts13, sqw6, sqw13, ps6, ps13, sg6, sg13, lg6, lg13)
play(pts6, pts14, sqw6, sqw14, ps6, ps14, sg6, sg14, lg6, lg14)
play(pts6, pts15, sqw6, sqw15, ps6, ps15, sg6, sg15, lg6, lg15)
play(pts6, pts16, sqw6, sqw16, ps6, ps16, sg6, sg16, lg6, lg16)
play(pts6, pts17, sqw6, sqw17, ps6, ps17, sg6, sg17, lg6, lg17)
play(pts6, pts18, sqw6, sqw18, ps6, ps18, sg6, sg18, lg6, lg18)
play(pts6, pts19, sqw6, sqw19, ps6, ps19, sg6, sg19, lg6, lg19)
play(pts6, pts20, sqw6, sqw20, ps6, ps20, sg6, sg20, lg6, lg20)
play(pts7, pts8, sqw7, sqw8, ps7, ps8, sg7, sg8, lg7, lg8)
play(pts7, pts9, sqw7, sqw9, ps7, ps9, sg7, sg9, lg7, lg9)
play(pts7, pts10, sqw7, sqw10, ps7, ps10, sg7, sg10, lg7, lg10)
play(pts7, pts11, sqw7, sqw11, ps7, ps11, sg7, sg11, lg7, lg11)
play(pts7, pts12, sqw7, sqw12, ps7, ps12, sg7, sg12, lg7, lg12)
play(pts7, pts13, sqw7, sqw13, ps7, ps13, sg7, sg13, lg7, lg13)
play(pts7, pts14, sqw7, sqw14, ps7, ps14, sg7, sg14, lg7, lg14)
play(pts7, pts15, sqw7, sqw15, ps7, ps15, sg7, sg15, lg7, lg15)
play(pts7, pts16, sqw7, sqw16, ps7, ps16, sg7, sg16, lg7, lg16)
play(pts7, pts17, sqw7, sqw17, ps7, ps17, sg7, sg17, lg7, lg17)
play(pts7, pts18, sqw7, sqw18, ps7, ps18, sg7, sg18, lg7, lg18)
play(pts7, pts19, sqw7, sqw19, ps7, ps19, sg7, sg19, lg7, lg19)
play(pts7, pts20, sqw7, sqw20, ps7, ps20, sg7, sg20, lg7, lg20)
play(pts8, pts9, sqw8, sqw9, ps8, ps9, sg8, sg9, lg8, lg9)
play(pts8, pts10, sqw8, sqw10, ps8, ps10, sg8, sg10, lg8, lg10)
play(pts8, pts11, sqw8, sqw11, ps8, ps11, sg8, sg11, lg8, lg11)
play(pts8, pts12, sqw8, sqw12, ps8, ps12, sg8, sg12, lg8, lg12)
play(pts8, pts13, sqw8, sqw13, ps8, ps13, sg8, sg13, lg8, lg13)
play(pts8, pts14, sqw8, sqw14, ps8, ps14, sg8, sg14, lg8, lg14)
play(pts8, pts15, sqw8, sqw15, ps8, ps15, sg8, sg15, lg8, lg15)
play(pts8, pts16, sqw8, sqw16, ps8, ps16, sg8, sg16, lg8, lg16)
play(pts8, pts17, sqw8, sqw17, ps8, ps17, sg8, sg17, lg8, lg17)
play(pts8, pts18, sqw8, sqw18, ps8, ps18, sg8, sg18, lg8, lg18)
play(pts8, pts19, sqw8, sqw19, ps8, ps19, sg8, sg19, lg8, lg19)
play(pts8, pts20, sqw8, sqw20, ps8, ps20, sg8, sg20, lg8, lg20)
play(pts9, pts10, sqw9, sqw10, ps9, ps10, sg9, sg10, lg9, lg10)
play(pts9, pts11, sqw9, sqw11, ps9, ps11, sg9, sg11, lg9, lg11)
play(pts9, pts12, sqw9, sqw12, ps9, ps12, sg9, sg12, lg9, lg12)
play(pts9, pts13, sqw9, sqw13, ps9, ps13, sg9, sg13, lg9, lg13)
play(pts9, pts14, sqw9, sqw14, ps9, ps14, sg9, sg14, lg9, lg14)
play(pts9, pts15, sqw9, sqw15, ps9, ps15, sg9, sg15, lg9, lg15)
play(pts9, pts16, sqw9, sqw16, ps9, ps16, sg9, sg16, lg9, lg16)
play(pts9, pts17, sqw9, sqw17, ps9, ps17, sg9, sg17, lg9, lg17)
play(pts9, pts18, sqw9, sqw18, ps9, ps18, sg9, sg18, lg9, lg18)
play(pts9, pts19, sqw9, sqw19, ps9, ps19, sg9, sg19, lg9, lg19)
play(pts9, pts20, sqw9, sqw20, ps9, ps20, sg9, sg20, lg9, lg20)
play(pts10, pts11, sqw10, sqw11, ps10, ps11, sg10, sg11, lg10, lg11)
play(pts10, pts12, sqw10, sqw12, ps10, ps12, sg10, sg12, lg10, lg12)
play(pts10, pts13, sqw10, sqw13, ps10, ps13, sg10, sg13, lg10, lg13)
play(pts10, pts14, sqw10, sqw14, ps10, ps14, sg10, sg14, lg10, lg14)
play(pts10, pts15, sqw10, sqw15, ps10, ps15, sg10, sg15, lg10, lg15)
play(pts10, pts16, sqw10, sqw16, ps10, ps16, sg10, sg16, lg10, lg16)
play(pts10, pts17, sqw10, sqw17, ps10, ps17, sg10, sg17, lg10, lg17)
play(pts10, pts18, sqw10, sqw18, ps10, ps18, sg10, sg18, lg10, lg18)
play(pts10, pts19, sqw10, sqw19, ps10, ps19, sg10, sg19, lg10, lg19)
play(pts10, pts20, sqw10, sqw20, ps10, ps20, sg10, sg20, lg10, lg20)
play(pts11, pts12, sqw11, sqw12, ps11, ps12, sg11, sg12, lg11, lg12)
play(pts11, pts13, sqw11, sqw13, ps11, ps13, sg11, sg13, lg11, lg13)
play(pts11, pts14, sqw11, sqw14, ps11, ps14, sg11, sg14, lg11, lg14)
play(pts11, pts15, sqw11, sqw15, ps11, ps15, sg11, sg15, lg11, lg15)
play(pts11, pts16, sqw11, sqw16, ps11, ps16, sg11, sg16, lg11, lg16)
play(pts11, pts17, sqw11, sqw17, ps11, ps17, sg11, sg17, lg11, lg17)
play(pts11, pts18, sqw11, sqw18, ps11, ps18, sg11, sg18, lg11, lg18)
play(pts11, pts19, sqw11, sqw19, ps11, ps19, sg11, sg19, lg11, lg19)
play(pts11, pts20, sqw11, sqw20, ps11, ps20, sg11, sg20, lg11, lg20)
play(pts12, pts13, sqw12, sqw13, ps12, ps13, sg12, sg13, lg12, lg13)
play(pts12, pts14, sqw12, sqw14, ps12, ps14, sg12, sg14, lg12, lg14)
play(pts12, pts15, sqw12, sqw15, ps12, ps15, sg12, sg15, lg12, lg15)
play(pts12, pts16, sqw12, sqw16, ps12, ps16, sg12, sg16, lg12, lg16)
play(pts12, pts17, sqw12, sqw17, ps12, ps17, sg12, sg17, lg12, lg17)
play(pts12, pts18, sqw12, sqw18, ps12, ps18, sg12, sg18, lg12, lg18)
play(pts12, pts19, sqw12, sqw19, ps12, ps19, sg12, sg19, lg12, lg19)
play(pts12, pts20, sqw12, sqw20, ps12, ps20, sg12, sg20, lg12, lg20)
play(pts13, pts14, sqw13, sqw14, ps13, ps14, sg13, sg14, lg13, lg14)
play(pts13, pts15, sqw13, sqw15, ps13, ps15, sg13, sg15, lg13, lg15)
play(pts13, pts16, sqw13, sqw16, ps13, ps16, sg13, sg16, lg13, lg16)
play(pts13, pts17, sqw13, sqw17, ps13, ps17, sg13, sg17, lg13, lg17)
play(pts13, pts18, sqw13, sqw18, ps13, ps18, sg13, sg18, lg13, lg18)
play(pts13, pts19, sqw13, sqw19, ps13, ps19, sg13, sg19, lg13, lg19)
play(pts13, pts20, sqw13, sqw20, ps13, ps20, sg13, sg20, lg13, lg20)
play(pts14, pts15, sqw14, sqw15, ps14, ps15, sg14, sg15, lg14, lg15)
play(pts14, pts16, sqw14, sqw16, ps14, ps16, sg14, sg16, lg14, lg16)
play(pts14, pts17, sqw14, sqw17, ps14, ps17, sg14, sg17, lg14, lg17)
play(pts14, pts18, sqw14, sqw18, ps14, ps18, sg14, sg18, lg14, lg18)
play(pts14, pts19, sqw14, sqw19, ps14, ps19, sg14, sg19, lg14, lg19)
play(pts14, pts20, sqw14, sqw20, ps14, ps20, sg14, sg20, lg14, lg20)
play(pts15, pts16, sqw15, sqw16, ps15, ps16, sg15, sg16, lg15, lg16)
play(pts15, pts17, sqw15, sqw17, ps15, ps17, sg15, sg17, lg15, lg17)
play(pts15, pts18, sqw15, sqw18, ps15, ps18, sg15, sg18, lg15, lg18)
play(pts15, pts19, sqw15, sqw19, ps15, ps19, sg15, sg19, lg15, lg19)
play(pts15, pts20, sqw15, sqw20, ps15, ps20, sg15, sg20, lg15, lg20)
play(pts16, pts17, sqw16, sqw17, ps16, ps17, sg16, sg17, lg16, lg17)
play(pts16, pts18, sqw16, sqw18, ps16, ps18, sg16, sg18, lg16, lg18)
play(pts16, pts19, sqw16, sqw19, ps16, ps19, sg16, sg19, lg16, lg19)
play(pts16, pts20, sqw16, sqw20, ps16, ps20, sg16, sg20, lg16, lg20)
play(pts17, pts18, sqw17, sqw18, ps17, ps18, sg17, sg18, lg17, lg18)
play(pts17, pts19, sqw17, sqw19, ps17, ps19, sg17, sg19, lg17, lg19)
play(pts17, pts20, sqw17, sqw20, ps17, ps20, sg17, sg20, lg17, lg20)
play(pts18, pts19, sqw18, sqw19, ps18, ps19, sg18, sg19, lg18, lg19)
play(pts18, pts20, sqw18, sqw20, ps18, ps20, sg18, sg20, lg18, lg20)
play(pts19, pts20, sqw19, sqw20, ps19, ps20, sg19, sg20, lg19, lg20)

play(pts1, pts2, sqw1, sqw2, ps1, ps2, sg1, sg2, lg1, lg2)
play(pts1, pts3, sqw1, sqw3, ps1, ps3, sg1, sg3, lg1, lg3)
play(pts1, pts4, sqw1, sqw4, ps1, ps4, sg1, sg4, lg1, lg4)
play(pts1, pts5, sqw1, sqw5, ps1, ps5, sg1, sg5, lg1, lg5)
play(pts1, pts6, sqw1, sqw6, ps1, ps6, sg1, sg6, lg1, lg6)
play(pts1, pts7, sqw1, sqw7, ps1, ps7, sg1, sg7, lg1, lg7)
play(pts1, pts8, sqw1, sqw8, ps1, ps8, sg1, sg8, lg1, lg8)
play(pts1, pts9, sqw1, sqw9, ps1, ps9, sg1, sg9, lg1, lg9)
play(pts1, pts10, sqw1, sqw10, ps1, ps10, sg1, sg10, lg1, lg10)
play(pts1, pts11, sqw1, sqw11, ps1, ps11, sg1, sg11, lg1, lg11)
play(pts1, pts12, sqw1, sqw12, ps1, ps12, sg1, sg12, lg1, lg12)
play(pts1, pts13, sqw1, sqw13, ps1, ps13, sg1, sg13, lg1, lg13)
play(pts1, pts14, sqw1, sqw14, ps1, ps14, sg1, sg14, lg1, lg14)
play(pts1, pts15, sqw1, sqw15, ps1, ps15, sg1, sg15, lg1, lg15)
play(pts1, pts16, sqw1, sqw16, ps1, ps16, sg1, sg16, lg1, lg16)
play(pts1, pts17, sqw1, sqw17, ps1, ps17, sg1, sg17, lg1, lg17)
play(pts1, pts18, sqw1, sqw18, ps1, ps18, sg1, sg18, lg1, lg18)
play(pts1, pts19, sqw1, sqw19, ps1, ps19, sg1, sg19, lg1, lg19)
play(pts1, pts20, sqw1, sqw20, ps1, ps20, sg1, sg20, lg1, lg20)
play(pts2, pts3, sqw2, sqw3, ps2, ps3, sg2, sg3, lg2, lg3)
play(pts2, pts4, sqw2, sqw4, ps2, ps4, sg2, sg4, lg2, lg4)
play(pts2, pts5, sqw2, sqw5, ps2, ps5, sg2, sg5, lg2, lg5)
play(pts2, pts6, sqw2, sqw6, ps2, ps6, sg2, sg6, lg2, lg6)
play(pts2, pts7, sqw2, sqw7, ps2, ps7, sg2, sg7, lg2, lg7)
play(pts2, pts8, sqw2, sqw8, ps2, ps8, sg2, sg8, lg2, lg8)
play(pts2, pts9, sqw2, sqw9, ps2, ps9, sg2, sg9, lg2, lg9)
play(pts2, pts10, sqw2, sqw10, ps2, ps10, sg2, sg10, lg2, lg10)
play(pts2, pts11, sqw2, sqw11, ps2, ps11, sg2, sg11, lg2, lg11)
play(pts2, pts12, sqw2, sqw12, ps2, ps12, sg2, sg12, lg2, lg12)
play(pts2, pts13, sqw2, sqw13, ps2, ps13, sg2, sg13, lg2, lg13)
play(pts2, pts14, sqw2, sqw14, ps2, ps14, sg2, sg14, lg2, lg14)
play(pts2, pts15, sqw2, sqw15, ps2, ps15, sg2, sg15, lg2, lg15)
play(pts2, pts16, sqw2, sqw16, ps2, ps16, sg2, sg16, lg2, lg16)
play(pts2, pts17, sqw2, sqw17, ps2, ps17, sg2, sg17, lg2, lg17)
play(pts2, pts18, sqw2, sqw18, ps2, ps18, sg2, sg18, lg2, lg18)
play(pts2, pts19, sqw2, sqw19, ps2, ps19, sg2, sg19, lg2, lg19)
play(pts2, pts20, sqw2, sqw20, ps2, ps20, sg2, sg20, lg2, lg20)
play(pts3, pts4, sqw3, sqw4, ps3, ps4, sg3, sg4, lg3, lg4)
play(pts3, pts5, sqw3, sqw5, ps3, ps5, sg3, sg5, lg3, lg5)
play(pts3, pts6, sqw3, sqw6, ps3, ps6, sg3, sg6, lg3, lg6)
play(pts3, pts7, sqw3, sqw7, ps3, ps7, sg3, sg7, lg3, lg7)
play(pts3, pts8, sqw3, sqw8, ps3, ps8, sg3, sg8, lg3, lg8)
play(pts3, pts9, sqw3, sqw9, ps3, ps9, sg3, sg9, lg3, lg9)
play(pts3, pts10, sqw3, sqw10, ps3, ps10, sg3, sg10, lg3, lg10)
play(pts3, pts11, sqw3, sqw11, ps3, ps11, sg3, sg11, lg3, lg11)
play(pts3, pts12, sqw3, sqw12, ps3, ps12, sg3, sg12, lg3, lg12)
play(pts3, pts13, sqw3, sqw13, ps3, ps13, sg3, sg13, lg3, lg13)
play(pts3, pts14, sqw3, sqw14, ps3, ps14, sg3, sg14, lg3, lg14)
play(pts3, pts15, sqw3, sqw15, ps3, ps15, sg3, sg15, lg3, lg15)
play(pts3, pts16, sqw3, sqw16, ps3, ps16, sg3, sg16, lg3, lg16)
play(pts3, pts17, sqw3, sqw17, ps3, ps17, sg3, sg17, lg3, lg17)
play(pts3, pts18, sqw3, sqw18, ps3, ps18, sg3, sg18, lg3, lg18)
play(pts3, pts19, sqw3, sqw19, ps3, ps19, sg3, sg19, lg3, lg19)
play(pts3, pts20, sqw3, sqw20, ps3, ps20, sg3, sg20, lg3, lg20)
play(pts4, pts5, sqw4, sqw5, ps4, ps5, sg4, sg5, lg4, lg5)
play(pts4, pts6, sqw4, sqw6, ps4, ps6, sg4, sg6, lg4, lg6)
play(pts4, pts7, sqw4, sqw7, ps4, ps7, sg4, sg7, lg4, lg7)
play(pts4, pts8, sqw4, sqw8, ps4, ps8, sg4, sg8, lg4, lg8)
play(pts4, pts9, sqw4, sqw9, ps4, ps9, sg4, sg9, lg4, lg9)
play(pts4, pts10, sqw4, sqw10, ps4, ps10, sg4, sg10, lg4, lg10)
play(pts4, pts11, sqw4, sqw11, ps4, ps11, sg4, sg11, lg4, lg11)
play(pts4, pts12, sqw4, sqw12, ps4, ps12, sg4, sg12, lg4, lg12)
play(pts4, pts13, sqw4, sqw13, ps4, ps13, sg4, sg13, lg4, lg13)
play(pts4, pts14, sqw4, sqw14, ps4, ps14, sg4, sg14, lg4, lg14)
play(pts4, pts15, sqw4, sqw15, ps4, ps15, sg4, sg15, lg4, lg15)
play(pts4, pts16, sqw4, sqw16, ps4, ps16, sg4, sg16, lg4, lg16)
play(pts4, pts17, sqw4, sqw17, ps4, ps17, sg4, sg17, lg4, lg17)
play(pts4, pts18, sqw4, sqw18, ps4, ps18, sg4, sg18, lg4, lg18)
play(pts4, pts19, sqw4, sqw19, ps4, ps19, sg4, sg19, lg4, lg19)
play(pts4, pts20, sqw4, sqw20, ps4, ps20, sg4, sg20, lg4, lg20)
play(pts5, pts6, sqw5, sqw6, ps5, ps6, sg5, sg6, lg5, lg6)
play(pts5, pts7, sqw5, sqw7, ps5, ps7, sg5, sg7, lg5, lg7)
play(pts5, pts8, sqw5, sqw8, ps5, ps8, sg5, sg8, lg5, lg8)
play(pts5, pts9, sqw5, sqw9, ps5, ps9, sg5, sg9, lg5, lg9)
play(pts5, pts10, sqw5, sqw10, ps5, ps10, sg5, sg10, lg5, lg10)
play(pts5, pts11, sqw5, sqw11, ps5, ps11, sg5, sg11, lg5, lg11)
play(pts5, pts12, sqw5, sqw12, ps5, ps12, sg5, sg12, lg5, lg12)
play(pts5, pts13, sqw5, sqw13, ps5, ps13, sg5, sg13, lg5, lg13)
play(pts5, pts14, sqw5, sqw14, ps5, ps14, sg5, sg14, lg5, lg14)
play(pts5, pts15, sqw5, sqw15, ps5, ps15, sg5, sg15, lg5, lg15)
play(pts5, pts16, sqw5, sqw16, ps5, ps16, sg5, sg16, lg5, lg16)
play(pts5, pts17, sqw5, sqw17, ps5, ps17, sg5, sg17, lg5, lg17)
play(pts5, pts18, sqw5, sqw18, ps5, ps18, sg5, sg18, lg5, lg18)
play(pts5, pts19, sqw5, sqw19, ps5, ps19, sg5, sg19, lg5, lg19)
play(pts5, pts20, sqw5, sqw20, ps5, ps20, sg5, sg20, lg5, lg20)
play(pts6, pts7, sqw6, sqw7, ps6, ps7, sg6, sg7, lg6, lg7)
play(pts6, pts8, sqw6, sqw8, ps6, ps8, sg6, sg8, lg6, lg8)
play(pts6, pts9, sqw6, sqw9, ps6, ps9, sg6, sg9, lg6, lg9)
play(pts6, pts10, sqw6, sqw10, ps6, ps10, sg6, sg10, lg6, lg10)
play(pts6, pts11, sqw6, sqw11, ps6, ps11, sg6, sg11, lg6, lg11)
play(pts6, pts12, sqw6, sqw12, ps6, ps12, sg6, sg12, lg6, lg12)
play(pts6, pts13, sqw6, sqw13, ps6, ps13, sg6, sg13, lg6, lg13)
play(pts6, pts14, sqw6, sqw14, ps6, ps14, sg6, sg14, lg6, lg14)
play(pts6, pts15, sqw6, sqw15, ps6, ps15, sg6, sg15, lg6, lg15)
play(pts6, pts16, sqw6, sqw16, ps6, ps16, sg6, sg16, lg6, lg16)
play(pts6, pts17, sqw6, sqw17, ps6, ps17, sg6, sg17, lg6, lg17)
play(pts6, pts18, sqw6, sqw18, ps6, ps18, sg6, sg18, lg6, lg18)
play(pts6, pts19, sqw6, sqw19, ps6, ps19, sg6, sg19, lg6, lg19)
play(pts6, pts20, sqw6, sqw20, ps6, ps20, sg6, sg20, lg6, lg20)
play(pts7, pts8, sqw7, sqw8, ps7, ps8, sg7, sg8, lg7, lg8)
play(pts7, pts9, sqw7, sqw9, ps7, ps9, sg7, sg9, lg7, lg9)
play(pts7, pts10, sqw7, sqw10, ps7, ps10, sg7, sg10, lg7, lg10)
play(pts7, pts11, sqw7, sqw11, ps7, ps11, sg7, sg11, lg7, lg11)
play(pts7, pts12, sqw7, sqw12, ps7, ps12, sg7, sg12, lg7, lg12)
play(pts7, pts13, sqw7, sqw13, ps7, ps13, sg7, sg13, lg7, lg13)
play(pts7, pts14, sqw7, sqw14, ps7, ps14, sg7, sg14, lg7, lg14)
play(pts7, pts15, sqw7, sqw15, ps7, ps15, sg7, sg15, lg7, lg15)
play(pts7, pts16, sqw7, sqw16, ps7, ps16, sg7, sg16, lg7, lg16)
play(pts7, pts17, sqw7, sqw17, ps7, ps17, sg7, sg17, lg7, lg17)
play(pts7, pts18, sqw7, sqw18, ps7, ps18, sg7, sg18, lg7, lg18)
play(pts7, pts19, sqw7, sqw19, ps7, ps19, sg7, sg19, lg7, lg19)
play(pts7, pts20, sqw7, sqw20, ps7, ps20, sg7, sg20, lg7, lg20)
play(pts8, pts9, sqw8, sqw9, ps8, ps9, sg8, sg9, lg8, lg9)
play(pts8, pts10, sqw8, sqw10, ps8, ps10, sg8, sg10, lg8, lg10)
play(pts8, pts11, sqw8, sqw11, ps8, ps11, sg8, sg11, lg8, lg11)
play(pts8, pts12, sqw8, sqw12, ps8, ps12, sg8, sg12, lg8, lg12)
play(pts8, pts13, sqw8, sqw13, ps8, ps13, sg8, sg13, lg8, lg13)
play(pts8, pts14, sqw8, sqw14, ps8, ps14, sg8, sg14, lg8, lg14)
play(pts8, pts15, sqw8, sqw15, ps8, ps15, sg8, sg15, lg8, lg15)
play(pts8, pts16, sqw8, sqw16, ps8, ps16, sg8, sg16, lg8, lg16)
play(pts8, pts17, sqw8, sqw17, ps8, ps17, sg8, sg17, lg8, lg17)
play(pts8, pts18, sqw8, sqw18, ps8, ps18, sg8, sg18, lg8, lg18)
play(pts8, pts19, sqw8, sqw19, ps8, ps19, sg8, sg19, lg8, lg19)
play(pts8, pts20, sqw8, sqw20, ps8, ps20, sg8, sg20, lg8, lg20)
play(pts9, pts10, sqw9, sqw10, ps9, ps10, sg9, sg10, lg9, lg10)
play(pts9, pts11, sqw9, sqw11, ps9, ps11, sg9, sg11, lg9, lg11)
play(pts9, pts12, sqw9, sqw12, ps9, ps12, sg9, sg12, lg9, lg12)
play(pts9, pts13, sqw9, sqw13, ps9, ps13, sg9, sg13, lg9, lg13)
play(pts9, pts14, sqw9, sqw14, ps9, ps14, sg9, sg14, lg9, lg14)
play(pts9, pts15, sqw9, sqw15, ps9, ps15, sg9, sg15, lg9, lg15)
play(pts9, pts16, sqw9, sqw16, ps9, ps16, sg9, sg16, lg9, lg16)
play(pts9, pts17, sqw9, sqw17, ps9, ps17, sg9, sg17, lg9, lg17)
play(pts9, pts18, sqw9, sqw18, ps9, ps18, sg9, sg18, lg9, lg18)
play(pts9, pts19, sqw9, sqw19, ps9, ps19, sg9, sg19, lg9, lg19)
play(pts9, pts20, sqw9, sqw20, ps9, ps20, sg9, sg20, lg9, lg20)
play(pts10, pts11, sqw10, sqw11, ps10, ps11, sg10, sg11, lg10, lg11)
play(pts10, pts12, sqw10, sqw12, ps10, ps12, sg10, sg12, lg10, lg12)
play(pts10, pts13, sqw10, sqw13, ps10, ps13, sg10, sg13, lg10, lg13)
play(pts10, pts14, sqw10, sqw14, ps10, ps14, sg10, sg14, lg10, lg14)
play(pts10, pts15, sqw10, sqw15, ps10, ps15, sg10, sg15, lg10, lg15)
play(pts10, pts16, sqw10, sqw16, ps10, ps16, sg10, sg16, lg10, lg16)
play(pts10, pts17, sqw10, sqw17, ps10, ps17, sg10, sg17, lg10, lg17)
play(pts10, pts18, sqw10, sqw18, ps10, ps18, sg10, sg18, lg10, lg18)
play(pts10, pts19, sqw10, sqw19, ps10, ps19, sg10, sg19, lg10, lg19)
play(pts10, pts20, sqw10, sqw20, ps10, ps20, sg10, sg20, lg10, lg20)
play(pts11, pts12, sqw11, sqw12, ps11, ps12, sg11, sg12, lg11, lg12)
play(pts11, pts13, sqw11, sqw13, ps11, ps13, sg11, sg13, lg11, lg13)
play(pts11, pts14, sqw11, sqw14, ps11, ps14, sg11, sg14, lg11, lg14)
play(pts11, pts15, sqw11, sqw15, ps11, ps15, sg11, sg15, lg11, lg15)
play(pts11, pts16, sqw11, sqw16, ps11, ps16, sg11, sg16, lg11, lg16)
play(pts11, pts17, sqw11, sqw17, ps11, ps17, sg11, sg17, lg11, lg17)
play(pts11, pts18, sqw11, sqw18, ps11, ps18, sg11, sg18, lg11, lg18)
play(pts11, pts19, sqw11, sqw19, ps11, ps19, sg11, sg19, lg11, lg19)
play(pts11, pts20, sqw11, sqw20, ps11, ps20, sg11, sg20, lg11, lg20)
play(pts12, pts13, sqw12, sqw13, ps12, ps13, sg12, sg13, lg12, lg13)
play(pts12, pts14, sqw12, sqw14, ps12, ps14, sg12, sg14, lg12, lg14)
play(pts12, pts15, sqw12, sqw15, ps12, ps15, sg12, sg15, lg12, lg15)
play(pts12, pts16, sqw12, sqw16, ps12, ps16, sg12, sg16, lg12, lg16)
play(pts12, pts17, sqw12, sqw17, ps12, ps17, sg12, sg17, lg12, lg17)
play(pts12, pts18, sqw12, sqw18, ps12, ps18, sg12, sg18, lg12, lg18)
play(pts12, pts19, sqw12, sqw19, ps12, ps19, sg12, sg19, lg12, lg19)
play(pts12, pts20, sqw12, sqw20, ps12, ps20, sg12, sg20, lg12, lg20)
play(pts13, pts14, sqw13, sqw14, ps13, ps14, sg13, sg14, lg13, lg14)
play(pts13, pts15, sqw13, sqw15, ps13, ps15, sg13, sg15, lg13, lg15)
play(pts13, pts16, sqw13, sqw16, ps13, ps16, sg13, sg16, lg13, lg16)
play(pts13, pts17, sqw13, sqw17, ps13, ps17, sg13, sg17, lg13, lg17)
play(pts13, pts18, sqw13, sqw18, ps13, ps18, sg13, sg18, lg13, lg18)
play(pts13, pts19, sqw13, sqw19, ps13, ps19, sg13, sg19, lg13, lg19)
play(pts13, pts20, sqw13, sqw20, ps13, ps20, sg13, sg20, lg13, lg20)
play(pts14, pts15, sqw14, sqw15, ps14, ps15, sg14, sg15, lg14, lg15)
play(pts14, pts16, sqw14, sqw16, ps14, ps16, sg14, sg16, lg14, lg16)
play(pts14, pts17, sqw14, sqw17, ps14, ps17, sg14, sg17, lg14, lg17)
play(pts14, pts18, sqw14, sqw18, ps14, ps18, sg14, sg18, lg14, lg18)
play(pts14, pts19, sqw14, sqw19, ps14, ps19, sg14, sg19, lg14, lg19)
play(pts14, pts20, sqw14, sqw20, ps14, ps20, sg14, sg20, lg14, lg20)
play(pts15, pts16, sqw15, sqw16, ps15, ps16, sg15, sg16, lg15, lg16)
play(pts15, pts17, sqw15, sqw17, ps15, ps17, sg15, sg17, lg15, lg17)
play(pts15, pts18, sqw15, sqw18, ps15, ps18, sg15, sg18, lg15, lg18)
play(pts15, pts19, sqw15, sqw19, ps15, ps19, sg15, sg19, lg15, lg19)
play(pts15, pts20, sqw15, sqw20, ps15, ps20, sg15, sg20, lg15, lg20)
play(pts16, pts17, sqw16, sqw17, ps16, ps17, sg16, sg17, lg16, lg17)
play(pts16, pts18, sqw16, sqw18, ps16, ps18, sg16, sg18, lg16, lg18)
play(pts16, pts19, sqw16, sqw19, ps16, ps19, sg16, sg19, lg16, lg19)
play(pts16, pts20, sqw16, sqw20, ps16, ps20, sg16, sg20, lg16, lg20)
play(pts17, pts18, sqw17, sqw18, ps17, ps18, sg17, sg18, lg17, lg18)
play(pts17, pts19, sqw17, sqw19, ps17, ps19, sg17, sg19, lg17, lg19)
play(pts17, pts20, sqw17, sqw20, ps17, ps20, sg17, sg20, lg17, lg20)
play(pts18, pts19, sqw18, sqw19, ps18, ps19, sg18, sg19, lg18, lg19)
play(pts18, pts20, sqw18, sqw20, ps18, ps20, sg18, sg20, lg18, lg20)
play(pts19, pts20, sqw19, sqw20, ps19, ps20, sg19, sg20, lg19, lg20)

aps1 = (sum(ps1))
aps2 = (sum(ps2))
aps3 = (sum(ps3))
aps4 = (sum(ps4))
aps5 = (sum(ps5))
aps6 = (sum(ps6))
aps7 = (sum(ps7))
aps8 = (sum(ps8))
aps9 = (sum(ps9))
aps10 = (sum(ps10))
aps11 = (sum(ps11))
aps12 = (sum(ps12))
aps13 = (sum(ps13))
aps14 = (sum(ps14))
aps15 = (sum(ps15))
aps16 = (sum(ps16))
aps17 = (sum(ps17))
aps18 = (sum(ps18))
aps19 = (sum(ps19))
aps20 = (sum(ps20))

ssg1 = int(sum(sg1))
ssg2 = int(sum(sg2))
ssg3 = int(sum(sg3))
ssg4 = int(sum(sg4))
ssg5 = int(sum(sg5))
ssg6 = int(sum(sg6))
ssg7 = int(sum(sg7))
ssg8 = int(sum(sg8))
ssg9 = int(sum(sg9))
ssg10 = int(sum(sg10))
ssg11 = int(sum(sg11))
ssg12 = int(sum(sg12))
ssg13 = int(sum(sg13))
ssg14 = int(sum(sg14))
ssg15 = int(sum(sg15))
ssg16 = int(sum(sg16))
ssg17 = int(sum(sg17))
ssg18 = int(sum(sg18))
ssg19 = int(sum(sg19))
ssg20 = int(sum(sg20))

llg1 = int(sum(lg1))
llg2 = int(sum(lg2))
llg3 = int(sum(lg3))
llg4 = int(sum(lg4))
llg5 = int(sum(lg5))
llg6 = int(sum(lg6))
llg7 = int(sum(lg7))
llg8 = int(sum(lg8))
llg9 = int(sum(lg9))
llg10 = int(sum(lg10))
llg11 = int(sum(lg11))
llg12 = int(sum(lg12))
llg13 = int(sum(lg13))
llg14 = int(sum(lg14))
llg15 = int(sum(lg15))
llg16 = int(sum(lg16))
llg17 = int(sum(lg17))
llg18 = int(sum(lg18))
llg19 = int(sum(lg19))
llg20 = int(sum(lg20))

sosg1 = int(sum(sg1) - sum(lg1))
sosg2 = int(sum(sg2) - sum(lg2))
sosg3 = int(sum(sg3) - sum(lg3))
sosg4 = int(sum(sg4) - sum(lg4))
sosg5 = int(sum(sg5) - sum(lg5))
sosg6 = int(sum(sg6) - sum(lg6))
sosg7 = int(sum(sg7) - sum(lg7))
sosg8 = int(sum(sg8) - sum(lg8))
sosg9 = int(sum(sg9) - sum(lg9))
sosg10 = int(sum(sg10) - sum(lg10))
sosg11 = int(sum(sg11) - sum(lg11))
sosg12 = int(sum(sg12) - sum(lg12))
sosg13 = int(sum(sg13) - sum(lg13))
sosg14 = int(sum(sg14) - sum(lg14))
sosg15 = int(sum(sg15) - sum(lg15))
sosg16 = int(sum(sg16) - sum(lg16))
sosg17 = int(sum(sg17) - sum(lg17))
sosg18 = int(sum(sg18) - sum(lg18))
sosg19 = int(sum(sg19) - sum(lg19))
sosg20 = int(sum(sg20) - sum(lg20))

resteams = {'arsena': aps1, 'aston ': aps2, 'bornem': aps3, 'braito': aps4, 'brentf': aps5, 'chelse': aps6,
            'city  ': aps7, 'crista': aps8, 'everto': aps9, 'forest': aps10, 'fullha': aps11, 'lester': aps12,
            'lids  ': aps13, 'liver ': aps14, 'manuni': aps15, 'newcc ': aps16, 'sautge': aps17, 'spurs ': aps18,
            'west  ': aps19, 'wolves': aps20, }
sgresteams = {'arsena': ssg1, 'aston ': ssg2, 'bornem': ssg3, 'braito': ssg4, 'brentf': ssg5, 'chelse': ssg6,
              'city  ': ssg7, 'crista': ssg8, 'everto': ssg9, 'forest': ssg10, 'fulham': ssg11, 'lester': ssg12,
              'lids  ': ssg13, 'liver ': ssg14, 'manuni': ssg15, 'newcc ': ssg16, 'sautge': ssg17, 'spurs ': ssg18,
              'west  ': ssg19, 'wolves': ssg20, }
lgresteams = {'arsena': llg1, 'aston ': llg2, 'bornem': llg3, 'braito': llg4, 'brentf': llg5, 'chelse': llg6,
              'city  ': llg7, 'crista': llg8, 'everto': llg9, 'forest': llg10, 'fulham': llg11, 'lester': llg12,
              'lids  ': llg13, 'liver ': llg14, 'manuni': llg15, 'newcc ': llg16, 'sautge': llg17, 'spurs ': llg18,
              'west  ': llg19, 'wolves': llg20, }
sogresteams = {'arsena': sosg1, 'aston ': sosg2, 'bornem': sosg3, 'braito': sosg4, 'brentf': sosg5, 'chelse': sosg6,
               'city  ': sosg7, 'crista': sosg8, 'everto': sosg9, 'forest': sosg10, 'fulham': sosg11, 'lester': sosg12,
               'lids  ': sosg13, 'liver ': sosg14, 'manuni': sosg15, 'newcc ': sosg16, 'sautge': sosg17,
               'spurs ': sosg18, 'west  ': sosg19, 'wolves': sosg20, }

sortedresteams = sorted(resteams.items(), key=lambda item: item[1], reverse=True)
sortedsgresteams = sorted(sgresteams.items(), key=lambda item: item[1], reverse=True)
sortedsogresteams = sorted(sogresteams.items(), key=lambda item: item[1], reverse=True)
sortedlgresteams = sorted(lgresteams.items(), key=lambda item: item[1])

print('Забито голов: ', sortedsgresteams[0], '          ', 'Пропущено голов: ', sortedlgresteams[0], '          ',
      'Количество очков: ', sortedresteams[0], '1 место')
print('Забито голов: ', sortedsgresteams[1], '          ', 'Пропущено голов: ', sortedlgresteams[1], '          ',
      'Количество очков: ', sortedresteams[1], '2 место')
print('Забито голов: ', sortedsgresteams[2], '          ', 'Пропущено голов: ', sortedlgresteams[2], '          ',
      'Количество очков: ', sortedresteams[2], '3 место')
print('Забито голов: ', sortedsgresteams[3], '          ', 'Пропущено голов: ', sortedlgresteams[3], '          ',
      'Количество очков: ', sortedresteams[3], '4 место')
print('Забито голов: ', sortedsgresteams[4], '          ', 'Пропущено голов: ', sortedlgresteams[4], '          ',
      'Количество очков: ', sortedresteams[4], '5 место')
print('Забито голов: ', sortedsgresteams[5], '          ', 'Пропущено голов: ', sortedlgresteams[5], '          ',
      'Количество очков: ', sortedresteams[5], '6 место')
print('Забито голов: ', sortedsgresteams[6], '          ', 'Пропущено голов: ', sortedlgresteams[6], '          ',
      'Количество очков: ', sortedresteams[6], '7 место')
print('Забито голов: ', sortedsgresteams[7], '          ', 'Пропущено голов: ', sortedlgresteams[7], '          ',
      'Количество очков: ', sortedresteams[7], '8 место')
print('Забито голов: ', sortedsgresteams[8], '          ', 'Пропущено голов: ', sortedlgresteams[8], '          ',
      'Количество очков: ', sortedresteams[8], '9 место')
print('Забито голов: ', sortedsgresteams[9], '          ', 'Пропущено голов: ', sortedlgresteams[9], '          ',
      'Количество очков: ', sortedresteams[9], '10 место')
print('Забито голов: ', sortedsgresteams[10], '          ', 'Пропущено голов: ', sortedlgresteams[10], '          ',
      'Количество очков: ', sortedresteams[10], '11 место')
print('Забито голов: ', sortedsgresteams[11], '          ', 'Пропущено голов: ', sortedlgresteams[11], '          ',
      'Количество очков: ', sortedresteams[11], '12 место')
print('Забито голов: ', sortedsgresteams[12], '          ', 'Пропущено голов: ', sortedlgresteams[12], '          ',
      'Количество очков: ', sortedresteams[12], '13 место')
print('Забито голов: ', sortedsgresteams[13], '          ', 'Пропущено голов: ', sortedlgresteams[13], '          ',
      'Количество очков: ', sortedresteams[13], '14 место')
print('Забито голов: ', sortedsgresteams[14], '          ', 'Пропущено голов: ', sortedlgresteams[14], '          ',
      'Количество очков: ', sortedresteams[14], '15 место')
print('Забито голов: ', sortedsgresteams[15], '          ', 'Пропущено голов: ', sortedlgresteams[15], '          ',
      'Количество очков: ', sortedresteams[15], '16 место')
print('Забито голов: ', sortedsgresteams[16], '          ', 'Пропущено голов: ', sortedlgresteams[16], '          ',
      'Количество очков: ', sortedresteams[16], '17 место')
print('Забито голов: ', sortedsgresteams[17], '          ', 'Пропущено голов: ', sortedlgresteams[17], '          ',
      'Количество очков: ', sortedresteams[17], '18 место')
print('Забито голов: ', sortedsgresteams[18], '          ', 'Пропущено голов: ', sortedlgresteams[18], '          ',
      'Количество очков: ', sortedresteams[18], '19 место')
print('Забито голов: ', sortedsgresteams[19], '          ', 'Пропущено голов: ', sortedlgresteams[19], '          ',
      'Количество очков: ', sortedresteams[19], '20 место')

from random import randint

gh = [sortedlgresteams[0], sortedlgresteams[1], sortedlgresteams[2]]
random.shuffle(gh)
print(' ')
print('GK OF THE SEASON: ')
print(97, gh[0])
print(94, gh[1])
print(89, gh[2])
print(' ')
cbbc = [sortedlgresteams[0], sortedlgresteams[1], sortedlgresteams[2], sortedlgresteams[3], sortedlgresteams[4],
        sortedlgresteams[5]]
random.shuffle(cbbc)
print('LB OF THE SEASON: ')
print(94, cbbc[0])
print(90, cbbc[1])
print(' ')
print('RB OF THE SEASON: ')
print(94, cbbc[2])
print(90, cbbc[3])
print(' ')
print('CB OF THE SEASON: ')
print(97, cbbc[4])
print(96, cbbc[0])
print(93, cbbc[3])
print(90, cbbc[5])
print(' ')

middef = [sortedsogresteams[0], sortedsogresteams[1], sortedsogresteams[2], sortedsogresteams[3], sortedsogresteams[4],
          sortedsogresteams[5]]
random.shuffle(middef)
print('CDM OF THE SEASON: ')
print(94, middef[0])
print(88, middef[1])
print(' ')
print('CAM OF THE SEASON: ')
print(95, middef[2])
print(89, middef[3])
print(' ')
print('CM OF THE SEASON: ')
print(98, middef[4])
print(96, middef[0])
print(93, middef[3])
print(87, middef[5])
print(' ')

strik = [sortedsgresteams[0], sortedsgresteams[1], sortedsgresteams[2], sortedsgresteams[3], sortedsgresteams[4]]
random.shuffle(strik)
print('LW OF THE SEASON: ')
print(95, strik[0])
print(91, strik[2])
print(' ')
print('RW OF THE SEASON: ')
print(95, strik[1])
print(91, strik[3])
print(' ')
print('ST OF THE SEASON: ')
print(98, strik[4])
print(94, strik[0])
print(89, strik[3])
print(' ')
