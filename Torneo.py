from random import randint as rd
from tools import milog as ln

def descalificar(players):
	size=len(players)
	p=8*8*8*8*8
	while(p>size):
		p=p//2
	print("de los que se descalificaron",size-p)
	for i in range(p,size):
		u=len(players)-1
		print(players[u])
		players.pop()
	print('\n\n\n')




def torneo(players):
    size = len(players)
    li=ln(size)
    base = []
    p = 1
    for i in range(11):
        tmp = []
        if p > size:
            break
        for j in range(p):
            tmp.append(0)
        base.append(tmp)
        p *= 2
    for j in range(0,len(players)):
        base[len(base)-1][j]=players[j]
    i=len(base)-1
    while(i>0):
        print('\n\n\nResultados de la ronda numero',li-i)
        j=0
        while(j<len(base[i])):
        	g=[0,0]
        	while 1==1:
        		gs=rd(0,1)
        		g[gs]+=1
        		if(g[gs]==2):
        			break
        	print(base[i][j],g[0],'x',g[1],base[i][j+1])
        	if(g[0]==2):
        		base[i-1][j//2]=base[i][j]
        	else:
        		base[i-1][j//2]=base[i][j+1]        	
        	j+=2
        i-=1
    return base
    