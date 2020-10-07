import os,sys,json
import time, ast


def recoverValue(dictionary,key_search):
	for key, value in dictionary.items():
		if key == key_search:			
			return value

def GetData(file=None):
	json_file=open('menu/cfg/{file}'.format(file=file))
	data = json.load(json_file)	
	b=json.dumps(data) #String to json
	return data

def GetDataConnections():
	return recoverValue(GetData(), 'Connections')

def cfg_obt_dato_reglas():
	return recoverValue(GetData('reglas.json'), 'Reglas')

def cfg_obt_par_pyspark(file):
	return GetData(file)


reglas = cfg_obt_dato_reglas()
