import os, sys
from datetime import datetime

class LogProcesos(object):
    # The class "constructor" - It's actually an initializer
    fmt_date       = '%Y-%m-%d %H:%M:%S'
    fh_inicio      = datetime.now().strftime(fmt_date)
    ds_conexion    = ''
    fh_ini_copia   = ''
    fh_fin_copia   = ''
    ds_copia_estatus     = 'iniciado'
    fh_ini_export  = ''
    fh_fin_export  = ''
    ds_export_estatus     = 'iniciado'
    fh_ini_proceso = ''
    fh_fin_proceso = ''
    ds_proceso_estatus     = 'iniciado'
    fh_ini_sube_lt = ''
    fh_fin_sube_lt = ''
    ds_sube_lt_estatus     = 'iniciado'
    evidencia_lt   = ''
    evidencia_lt_info=''    
    fh_final       = ''
    ds_estatus     = 'iniciado'
    nu_lin_malas   = 0
    li_lin_malas   = 0

    def __init__(self, id=0, nombre='', ruta_src='',ruta_tgt=''):
        self.id = id
        self.nombre = nombre
        self.ruta_src = ruta_src
        self.ruta_tgt = ruta_tgt

    def recupera_duracion(self, fh_ini, fh_fin):
        if fh_ini and fh_fin:
            resultado = divmod( (datetime.strptime(fh_fin,self.fmt_date) -datetime.strptime(fh_ini,self.fmt_date)).total_seconds(),60)
            duracion  = str(int(resultado[0]))+' min '+str(int(resultado[1]))+' seg'
            return duracion            
        else:
            return '- min - seg'

    def log_dict(self):
        if int(self.id) != 0:
            print("algo va mal")
        ds_estatus = 'Sin Estatus'
        

        duracion_copia   = self.recupera_duracion(self.fh_ini_copia   , self.fh_fin_copia   )
        duracion_proceso = self.recupera_duracion(self.fh_ini_proceso , self.fh_fin_proceso )
        duracion_export  = self.recupera_duracion(self.fh_ini_export  , self.fh_fin_export  )
        duracion         = self.recupera_duracion(self.fh_inicio      , self.fh_final       )
        return {'id': self.id,
                'nombre': self.nombre,
                'conexion': self.ds_conexion,
                'ruta_src': self.ruta_src,
                'ruta_tgt': self.ruta_tgt,                
                'copia'  : { 'inicio': self.fh_ini_copia  , 'fin':self.fh_fin_copia   ,'estatus':self.ds_copia_estatus   ,'duracion':duracion_copia   },
                'proceso': { 'inicio': self.fh_ini_proceso, 'fin':self.fh_fin_proceso ,'estatus':self.ds_proceso_estatus ,'duracion':duracion_proceso },
                'export' : { 'inicio': self.fh_ini_export , 'fin':self.fh_fin_export  ,'estatus':self.ds_export_estatus  ,'duracion':duracion_export  },
                'evidencia' : { 'ls': self.evidencia_lt ,   'info' : self.evidencia_lt_info ,   'estatus': self.ds_sube_lt_estatus},             
                'ds_estatus': self.ds_estatus,
                'lineas_malas':  { 'cantidad': self.nu_lin_malas ,'lineas': self.li_lin_malas},
                'log' :  { 'inicio' :self.fh_inicio ,   'fin':self.fh_final, 'duracion': duracion }

                }



"""
log = LogProcesos(id=0, ruta_src='juan')
print(log.fh_inicio, log.ds_estatus, log.log_dic())
"""
