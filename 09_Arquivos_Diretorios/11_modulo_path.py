import os
import time

# C:\Users\x_kat\Documents\Projetos\ProjectTestEnv\09_Arquivos_Diretorios\ceps.csv
print(os.path.abspath("ceps.csv"))
# ProjectTestEnv
print(os.path.basename(r'\Users\x_kat\Documents\Projetos\ProjectTestEnv'))
# \Users\x_kat\Documents\Projetos
print(os.path.dirname(r'\Users\x_kat\Documents\Projetos\ProjectTestEnv'))
# \Users\x_kat\Documents\Projetos\ProjectTestEnv\XXXXX\YYYYY
print(os.path.join(r'\Users\x_kat\Documents\Projetos\ProjectTestEnv', 'XXXXX', 'YYYYY'))
# ('\\Users\\x_kat\\Documents\\Projetos\\ProjectTestEnv\\09_Arquivos_Diretorios', 'ceps.csv')
print(os.path.split(r'\Users\x_kat\Documents\Projetos\ProjectTestEnv\09_Arquivos_Diretorios\ceps.csv'))
# ('\\Users\\x_kat\\Documents\\Projetos\\ProjectTestEnv\\09_Arquivos_Diretorios\\ceps', '.csv')
print(os.path.splitext(r'\Users\x_kat\Documents\Projetos\ProjectTestEnv\09_Arquivos_Diretorios\ceps.csv'))

print(os.path.isfile("ceps.csv")) # True
print(os.path.isdir("ceps.csv"))  # False
print(os.path.isdir("09_Arquivos_Diretorios")) # False
print(os.path.isdir(r"\Users\x_kat\Documents\Projetos")) # True
# help(os.path)

for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)

dir = "ceps.csv"
print(f'Nome: {dir}')
print(f'Tamanho: {os.path.getsize(dir)}')  # 153
# Sun Mar 22 19:23:59 2020
print(f'Criado: {time.ctime(os.path.getctime(dir))}')
# Sun Mar 22 19:24:11 2020
print(f'Modificado: {time.ctime(os.path.getmtime(dir))}')
# Sun Mar 22 19:24:11 2020
print(f'Acessado: {time.ctime(os.path.getatime(dir))}')