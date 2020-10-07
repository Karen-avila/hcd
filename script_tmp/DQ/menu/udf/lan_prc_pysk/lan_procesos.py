import os,sys
from subprocess import Popen, PIPE

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)



def log_imprime(proc_py):
    while True:
        output = proc_py.stdout.readline()
        if output == b'' and proc_py.poll() is not None:
            break
        if output:
            print (output.strip())
    rc = proc_py.poll()
    
    return True



def lan_prc_pyspark(resultado):    
    cmd = resultado.cmd_pyspark
    script = resultado.scp_pyspark
    args = resultado.par_pyspark
    print("lan_prc_pyspark", cmd, script, resultado.par_pyspark)
    try:
        pro_pyspark = Popen([cmd, script,args], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        logging.info("\t Processing >>>>>> ")
        (child_stdin, child_stdout, child_stderr) = (pro_pyspark.stdin, pro_pyspark.stdout, pro_pyspark.stderr)
        log_imprime(pro_pyspark)
        result , error = pro_pyspark.communicate()
        if pro_pyspark.returncode == 1:
            logging.info("\t Executed  with Error >>>>>> "+ str(error))
        elif pro_pyspark.returncode == 0:
            logging.info("\t Executed  succeeded >>>>>> ")

    except Exception as e:
        sys.stderr.write("common::main() : [ERROR]: output = %s" % (e))

    return True