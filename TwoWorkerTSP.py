from itertools import permutations
dotcount = int(input("How many nodes are there to visit?"))
def matrix (distances):
    return(distances)
distances = matrix([[0,0,0,0,0,0,0],
             [0,9999,75,25,30,90,40],
             [0,75,9999,10,85,25,55],
             [0,25,10,9999,100,65,70],
             [0,30,85,100,9999,20,15],
             [0,90,25,65,20,9999,17],
             [0,40,55,70,15,17,9999]])
start = int(input("Chose a starting node"))

l1,l2,l3,l4,l5 = [],[],[],[],[]
dots = []
for b in range (1,dotcount+1):
    dots.append(b)

for i in range (1,dotcount):
    perm1 = list(permutations(dots,i))
    for b in range (0,len(perm1)):
        perm1[b] = list(perm1[b])
    if i ==1:
        l1 = perm1
    elif i ==2:
        l2 = perm1
    elif i ==3:
        l3 = perm1
    elif i == 4:
        l4 = perm1
    elif i == 5:
        l5 = perm1

def remover(a):
    for i in a:
        c = i.reverse()
        if c in a:
            a.remove(c)
    return(a)

remover(l2)
remover(l3)
remover(l4)
remover(l5)
routerlist = [l1,l2,l3,l4,l5]
cycle = 0
minn = 9999999
for i in range (0,3):
    lists = routerlist[i]
    for couples in lists:
        for k in routerlist[dotcount-2-i]:
            for onlyelmnt in couples:
                if onlyelmnt in k:
                    continue
                else:
                    w1 = 0
                    w2 = 0
                    for onlyelmnt in couples:
                        if onlyelmnt == couples[-1]:
                            break
                        else:
                            sonraki = couples.index(onlyelmnt)+1
                        w1+=distances[onlyelmnt][couples[sonraki]]
                    for m in k:
                        otherone = k.index(m)+1
                        if m == k[-1]:
                            break
                        w2+=distances[m][k[otherone]]
                    if w1+w2 <= minn:
                        chosencouples = couples
                        chosenk = k
                        W1 = w1
                        W2 = w2
                        minn = w1+w2
print("Minimum tour costs ",minn, " Km.")
print("worker one has traveled for ", W1, "Km. And worker two has traveled for ", W2, " Km.")
print("Chosen routes are: ",chosencouples, " and ", chosenk, "for each co-workers.")
