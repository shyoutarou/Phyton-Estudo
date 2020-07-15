class NovaException(Exception):
    pass

def lancador():
    raise NovaException
try:
    lancador()
except NovaException as n:
    print("Uma exceção do tipo NovaException foi lançada")
