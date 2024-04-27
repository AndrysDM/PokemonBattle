from random import randint as rd
import os

def crear_almanaque():
	calendario={1:[31,'enero'],2:[28,'febrero'],	3:[31,'marzo'],4:[30,'abril'],5:[31,'mayo'],
	6:[30,'junio'],7:[31,'julio'],8:[31,'agosto'],
	9:[30,'septiembre'],10:[31,'octubre'],
	11:[30,'noviembre'],12:[31,'diciembre']
	}
	return calendario

def que_dia_es_hoy(x,calendario):
	i=1
	while(x>calendario[i][0]):
		x-=calendario[i][0]
		i+=1
	print(x,calendario[i][1])
	
def numero_de_dia(x,s,calendario):
	i=1
	x*=1
	while(s!=calendario[i][1]):
		x+=calendario[i][0]
		i+=1
	print(x)
	
def revolver(players):
	deck=[]
	rev=[]
	for i in range (0,len(players)):
		rev.append(0)
	while(len(deck)!=len(players)):
		c=rd(0,len(players)-1)
		if(rev[c]==1):
			continue
		else:
			deck.append(players[c])
			rev[c]=1
	players[:]=deck[:]
	
def milog(x):
	r=0
	while(x>0):
		r+=1
		x=x//2
	return r			
	
def noesunnumero(c):
	for i in "0s123456789":
		if(c==i):
			return 0
	return 1

def inicializar_fotos(ruta):
	dir={}
	for arch in os.listdir(ruta):
		p=''
		for c in arch :
			if(noesunnumero(c)):
				break
			p+=c
		d=os.path.join(ruta,arch)
		dir[int(p)]=d
	return dir
	

def Tplayers(players,pokemon):
	k=[]
	for i in players:
		p=[pokemon[i[0]],i[1],i[2]]
		k.append(p)
	return k

def Tinscrip(inscript,poke):
	k=[]
	for i in inscript:
		r=[]
		for j in i[1]:
			r.append([poke[j[0]],j[1],j[2]])
		k.append(r)
	return k