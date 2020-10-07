import os,sys,json
from io import open
#from types import SimpleNamespace


def GetData(file=None):
	json_file=open('{file}'.format(file=file))
	data = json.load(json_file)	
	b=json.dumps(data) #String to json
	return b	
	return data

def cfg_obt_par_pyspark(file):
	#return SimpleNamespace(**GetData(file))
	return GetData(file)




