from menu.obj.obj_clases import Menu, Archivo, Proceso, LogProcesos
from menu.menu import menu_general


if __name__ == '__main__':
    # arg = sys.argv[1:]
    arg = []
    # listScripts = list_scriptsProces(arg[0])
    dic_menu = {'opc_1': 2, 'opc_2': 1}
    archivo_1 = Archivo(1, '*', '^', True) 
    
    
    ruta_src='C:/Users/miguel.cruza/PycharmProjects/DQ/tmp/'
    #ruta_src='/dev/la/la_aficobranza/H_SINDO_SSCI_CUENTA_INDIVIDUAL/'
    #ruta_src='/dev/la/la_siais/tbalteracion/'
    #ruta_src='/dev/la/la_siais/tbatencion'

    ruta_tgt='C:/Users/miguel.cruza/PycharmProjects/DQ/tmp/dev/la/lt_siais/'
    #ruta_tgt='/dev/la/lt_siais/tbalteracion/'
    #ruta_tgt='/dev/la/lt_siais/tbatencion/'
    print ("ruta_src", ruta_src)








    lis_menu = [archivo_1]

    menu = Menu(id_menu=1, argumentos_menu=dic_menu, archivos=lis_menu,ruta_src=ruta_src, ruta_tgt=ruta_tgt)
    
    log_procesos = LogProcesos()

    
    menu_general(menu)
