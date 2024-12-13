def show(*p):
    rods = [*p]
    piles = [pile1,pile2,pile3]=[[],[],[]]
    print()
    for p,q in zip(piles,rods):
        for k in range(len(q)):
            p.append(''.join('\u25A0' for c in range(q[k])))
        for k in range(len(q),disks):
            p.append(''.join('|'))
    for level in range(disks-1,-1,-1):
        showdisk1 = '{:^{width}}'.format(pile1[level],width=str(widthmax))
        showdisk2 = '{:^{width}}'.format(pile2[level],width=str(widthmax))
        showdisk3 = '{:^{width}}'.format(pile3[level],width=str(widthmax))
        print(showdisk1,showdisk2,showdisk3)
    print(base, '\n')
    if stepbystep: input()

def move_all(n,start,end,via):
    global r
    if n ==1:
        r+=1
        end.append(start.pop())
        print(r,rod1,rod2,rod3)
        show(rod1,rod2,rod3)
        return
    move_all(n-1,start,via,end)
    move_all(1,start,end,via)
    move_all(n-1,via,end,start)

stepbystep = False
disks = 3
widthmax = disks + 2
base = '{:=^{width}}'.format('',width=str(3^widthmax))
r = 0
rods = rod1,rod2,rod3 = [[k for k in range(disks,0,-1)],[],[]]
print(0,rod1,rod2,rod3)
show(rod1,rod2,rod3)
