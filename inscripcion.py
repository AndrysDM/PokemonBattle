import tools as tools
from random import randint as rd

mapa=[]
for i in range(10001):
	mapa.append(0)

calendario=tools.crear_almanaque()
empieza=rd(1,300)
termina=rd(empieza+10,365)
print('Las inscripciones estaran disponibles en el intervalo')
tools.que_dia_es_hoy(empieza,calendario)
tools.que_dia_es_hoy(termina,calendario)

players=[]
print('\n\n\nFechas de inscripcion:')
for i in range(empieza,termina):
	z=0
	for j in range(0,5):
		if(rd(1,termina-empieza)<(termina-empieza)//4):
			if(z==0):
				print("\n")
				tools.que_dia_es_hoy(i,calendario)
				z=1
			c=rd(1000,9999)
			if(mapa[c]==0):
				mapa[c]=1
				print('se inscribio' ,c)
				players.append(c)

print("\n\nSe inscribieron un total de",len(players),"jugadores")
