import tools as tools
import os
from random import randint as rd
import pandas as pd

rutai=os.getcwd()
rutdatos=(os.path.join(rutai,'assets'))
rutdatos=(os.path.join(rutdatos,'poketdeck.csv'))
datos=pd.read_csv(rutdatos)
#print(datos)

mapa=[]
for i in range(200):
	mapa.append(0)

calendario=tools.crear_almanaque()
empieza=rd(1,100)
termina=empieza+ 10 + rd(0,30)


print('Las inscripciones estaran disponibles en el intervalo')
tools.que_dia_es_hoy(empieza,calendario)
tools.que_dia_es_hoy(termina,calendario)

players=[]
inscritos=[]

print('\n\n\nFechas de inscripcion:')
for i in range(empieza,termina):
	if(i>37):
		break
	z=0
	listabreve=[]
	for j in range(0,5):
		if(rd(1,termina-empieza)<=(termina-empieza)//4):
			if(z==0):
				print("\n")
				tools.que_dia_es_hoy(i,calendario)
				z=1
			c=rd(0,150)
			if(mapa[c]==0):
				mapa[c]=1
				print('se inscribio' ,datos.iloc[c,1],'de tipo',datos.iloc[c,2])
				listabreve.append([c+1,datos.iloc[c,1],datos.iloc[c,2]])
				players.append([c+1,datos.iloc[c,1],datos.iloc[c,2]])
	if(len(listabreve)>0):
		inscritos.append([i,listabreve])
print(players)
print("\n\nSe inscribieron un total de",len(players),"jugadores")
