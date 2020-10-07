import os,sys,json

from hdfs3 import HDFileSystem



def recoverValue(dictionary,key_search):
	for key, value in dictionary.items():
		if key == key_search:
			return value

def GetData():
	try:
		with open('menu/cfg/conexion.json') as json_file:  
			data = json.load(json_file)
	except Exception as e:
		with open('conexion.json') as json_file:  
			data = json.load(json_file)
	return data

def GetDataConnections():
	return recoverValue(GetData(), 'Connections')

def getConnection(connValue):
	connections = GetDataConnections()
	for connection in connections:
		if connection['id']==connValue:
			return connection

conexion = getConnection(1)

try:
	hdfs=HDFileSystem(host=conexion['host']
		              ,port=conexion['port']
		              ,principal=conexion['principal']
		              ,driver=conexion['driver']
		              ,pars={'hadoop.security.authentication': 'kerberos','hadoop.rpc.protection':'authenticate'}
		              ,ticket_cache=conexion['ticket_path_cache']
		              )
	print("Conexion Exitosa")
except Exception as e:
	hdfs = None
	print("No hay conexion al servidor, se trabajara de forma local , error : {var}".format(var=str(e)))
