import csv
import json

csvfile = open('reglas.csv', 'r')
jsonfile = open('file.json', 'w')
encabezado = ["id","nombre","funcion","id_funcion","busqueda","remplazo"]
reader = csv.DictReader( csvfile, encabezado)
reglas =[]
dic_bus_lis={}
dic_bus={}
temp_rep_bus_lis=[]
temp_rep_rem_lis=[]
temp_rep_bus=[]
temp_rep_rem=[]


for index,row in enumerate(reader):
	regla={}
	if index!=0:

		regla[encabezado[0]]= int(row[encabezado[0]]) #id
		regla[encabezado[1]]= row[encabezado[1]] #nombre		
		if 'REPLACE_LIST'==row[encabezado[2]]:
			dic_bus_lis[encabezado[0]]=int(row[encabezado[0]])
			dic_bus_lis[encabezado[1]]=row[encabezado[1]]
			dic_bus_lis[encabezado[2]]=row[encabezado[2]]
			dic_bus_lis[encabezado[3]]=row[encabezado[3]]
			if row[encabezado[4]]:
				temp_rep_bus_lis.append(row[encabezado[4]])
				temp_rep_rem_lis.append(row[encabezado[5]])
		elif 'REPLACE'==row[encabezado[2]]:
			dic_bus[encabezado[0]]=int(row[encabezado[0]])
			dic_bus[encabezado[1]]=row[encabezado[1]]
			dic_bus[encabezado[2]]=row[encabezado[2]]
			dic_bus[encabezado[3]]=row[encabezado[3]]			
			if row[encabezado[4]]:
				temp_rep_bus.append(row[encabezado[4]])
				temp_rep_rem.append(row[encabezado[5]])			
		else:
			regla[encabezado[2]]= row[encabezado[2]] #funcion		
			regla[encabezado[3]]= int(row[encabezado[3]]) #funcion		
			regla['opc']= None
			
		
		reglas.append(regla)

reglas_unique    =list({v['id']:v for v in reglas}.values())
for r in reglas_unique:
	if dic_bus_lis['id']==r['id']:
		r['opc']= { 'busqueda':temp_rep_bus_lis,'remplazo':list(set(temp_rep_rem_lis))[0] }
	if dic_bus['id']==r['id']:
		t=[]
		if len(temp_rep_bus)==len(temp_rep_rem):
			for idx,v in enumerate(temp_rep_bus):
				t.append({'busqueda':temp_rep_bus[idx], 'remplazo':temp_rep_rem[idx]})	
		r['opc']=t

		

	#if dic_bus['id']==r['id']:


dic_reglas ={'reglas':reglas_unique}

json_object = json.dumps(dic_reglas)
print("\n\n\n\n\n",json_object)
