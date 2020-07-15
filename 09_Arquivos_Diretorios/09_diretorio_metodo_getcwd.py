import os
import sys

# C:\Users\x_kat\Documents\Projetos\ProjectTestEnv\09_Arquivos_Diretorios
print(os.getcwd())
# os.chdir("C:\Users\x_kat\Desktop\Loterias")
# Repare que as barras tem que estar ao contrário
# ou indicar r de raw string senão dá erro de escape
# SyntaxError: (unicode error) 'unicodeescape'
# codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
os.chdir(r"C:\Users\x_kat\Desktop\Teste")
os.chdir("C:/Users/x_kat/Desktop/Teste")
# C:\Users\x_kat\Desktop\Loterias
print(os.getcwd())

print(os.listdir(os.getcwd()))
# ['Pasta1', 'Pasta2', 'Pasta3']

if (os.path.exists("PastaTST")):
    os.rmdir("PastaTST")
if (os.path.exists("PastaTST_new")):
    os.rmdir("PastaTST_new")
if (os.path.exists("PastaTST1/SubTST/SubSubTST")):
    os.removedirs("PastaTST1/SubTST/SubSubTST")

os.mkdir("PastaTST")
os.rename("PastaTST", "PastaTST_new")
os.makedirs("PastaTST1/SubTST/SubSubTST")
# ['Pasta1', 'Pasta2', 'Pasta3', 'PastaTST1', 'PastaTST_new']
print(os.listdir(os.getcwd()))

cur_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
for raiz, diretorios, arquivos in os.walk(cur_dir):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(f"   {d}/")
    for f in arquivos:
        print(f"   {f}")
    print(f"{len(diretorios)} diretorio(s), {len(arquivos)} arquiwo(s)")
