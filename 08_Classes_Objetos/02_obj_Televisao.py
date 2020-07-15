class Televisao: 
    def __init__(self, min, max): 
        self.ligada = False 
        self.canal = 2 
        self.cmin = min 
        self.cmax = max 

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin: 
            self.canal -= 1 

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax: 
            self.canal += 1

tv = Televisao(1, 15)  
print(tv.ligada)        # False

print(tv.canal)         # 2

tv_sala = Televisao(1, 2) 
tv_sala.ligada = True
tv_sala.canal = 4
print(tv.canal)         # 2

print(tv_sala.canal)    # 4

 
tv_sala.muda_canal_para_cima() 
tv_sala.muda_canal_para_cima()
print(tv.canal)         # 2

tv.muda_canal_para_baixo() 
print(tv.canal)         # 1

for x in range(0, 10):
    tv.muda_canal_para_cima()
    # 2/3/4/5/6/7/8/9/10/11/
    print(str(tv.canal) + '/', end='')

print("")

for x in range(0, 20):
    tv_sala.muda_canal_para_baixo()
    # 3/2/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/
    print(str(tv_sala.canal) + '/', end='')


