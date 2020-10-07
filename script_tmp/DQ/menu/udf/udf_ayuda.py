import os,sys

class SimpleNamespace (object):
    def __init__ (self, **kwargs):
        self.__dict__.update(kwargs)
    def __repr__ (self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__

def limpia_pantalla():
	try:
		sys.stderr.write("\x1b[2J\x1b[H")
	except Exception as e:
		os.system("cls")


