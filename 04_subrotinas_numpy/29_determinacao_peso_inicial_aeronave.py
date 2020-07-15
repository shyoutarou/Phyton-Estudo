import numpy as np

print("")
print("VARIÁVEL(IS):")

# Cruise (Cruzeiro)
R = 1250  # input("Digite o valor do 'Range (R, nmi)': ")
print("Range (R, nmi) =", R)

W_Payload = 9500  # input("Digite o valor do
# 'Peso de Carga Útil (W_Payload, lbf)': ")
print("W_Payload (lbf) =", W_Payload)

V = 0.6  # input("Digite o valor da 'Velocidade (Mach)': ")
print("V (Mach) =", V)

LD_Max = 16  # input("Digite o valor da
# 'Razão de Lift-to-Drag (L/D)': ")
print("(L / D)_Max =", LD_Max)

W_Crew = 800  # input("Digite o valor do 'Peso da
# Tripulação (W_Crew, lbf)': ")
print("W_Crew (lbf) =", W_Crew)

# Warmup and Takeoff (Aquecimento e Decolagem)
W1W0_ = 0.970  # É constante, dado experimental
print("W_1 / W_0 =", W1W0_)

# Climb (Subida)
W2W1_ = 0.985  # É constante, dado experimental
print("W_2 / W_1 =", W2W1_)

# Terminar e iniciar com numero pode dar BUG
# Loiter (Órbita) First
E1_ = 3  # input("Digite o valor do
# 'Tempo da Primeira Permanência em Órbita (h)': ")
print("E_1 (h) =", E1_)

# Loiter (Órbita) Second
E2_ = 1 / 3  # input("Digite o valor do
# 'Tempo da Segunda Permanência em Órbita (h)': ")
print("E_2 (h) =", E2_)

# Landing (Pouso)
W7W6_ = 0.995  # É constante, dado experimental
print("W_7 / W_6 =", W7W6_)

# Empty Weight (Peso Seco)
tipo_de_aeronave = 12  # input("Digite o código referente à aeronave:
# 1 - Sailplane-unpowered (Planador NÃO motorizado);
# 2 - Sailplane-powered (Planador motorizado);
# 3 - Homebuilt-metal/wood (Construída com metal e madeira);
# 4 - Homebuilt-composite (Construída com materiais compósitos);
# 5 - General aviation-single engine (Monomotor de aviação geral);
# 6 - General aviation-twin engine (Bimotor de aviação geral);
# 7 - Agricutural aircraft (Aeronave agrícola);
# 8 - Twin turboprop (Bimotor turbo-hélice);
# 9 - Flying boat (Aeronave anfíbia);
# 10 - Jet trainer (Jato de treinamento);
# 11 - Jet fighter (Jato de combate);
# 12 - Military cargo/bomber (Cargueiro militar/Bombardeiro);
# 13 - Jet transport (Jato de transporte).: ")
if tipo_de_aeronave == 1:
    A = 0.86
    C_Empty = -0.05
elif tipo_de_aeronave == 2:
    A = 0.91
    C_Empty = -0.05
elif tipo_de_aeronave == 3:
    A = 1.19
    C_Empty = -0.09
elif tipo_de_aeronave == 4:
    A = 0.99
    C_Empty = -0.09
elif tipo_de_aeronave == 5:
    A = 2.36
    C_Empty = -0.18
elif tipo_de_aeronave == 6:
    A = 1.51
    C_Empty = -0.10
elif tipo_de_aeronave == 7:
    A = 0.74
    C_Empty = -0.03
elif tipo_de_aeronave == 8:
    A = 0.96
    C_Empty = -0.05
elif tipo_de_aeronave == 9:
    A = 1.09
    C_Empty = -0.05
elif tipo_de_aeronave == 10:
    A = 1.59
    C_Empty = -0.10
elif tipo_de_aeronave == 11:
    A = 2.34
    C_Empty = -0.13
elif tipo_de_aeronave == 12:
    A = 0.93
    C_Empty = -0.07
elif tipo_de_aeronave == 13:
    A = 1.02
    C_Empty = -0.06

tipo_de_enflechamento = 1  # input("Informe se a aeronave possui
# enflechamento ou NÃO:
# 0 - NÃO possui enflechamento;
# 1 - Possui enflechamento.: ")
if tipo_de_enflechamento == 0:
    K_vs = 1
elif tipo_de_enflechamento == 1:
    K_vs = 1.04

# Método Iterativo
# Perceber que, para este problema, uma tolerância de 50 lbf
# é bastante razoável
tolerancia = 50  # input("Digite o valor da 'Tolerância/Critério de
# Parada Para o Método Iterativo': ")

# CÁLCULO(S): ---

# Cruise (Cruzeiro)
R = 6076 * R  # (ft)
C = 0.5 * 1 / 3600  # (s ** (-1))
V = V * 994.8  # (ft / s)
LD = 0.866 * LD_Max
W3W2_ = np.exp(- R * C / (V * LD))
print("W_3 / W_2 =", W3W2_)

# Loiter (Órbita) First
E1_ = E1_ * 3600  # (s)
C = 0.4 * 1 / 3600  # ( s ** (-1))
W4W3_ = np.exp(- E1_ * C / LD)
print("W_4 / W_3 =", W4W3_)

# Cruise (Cruzeiro) Second
W5W4_ = W3W2_
print("W_5 / W_4 =", W5W4_)

# Loiter (Órbita) Second
E2_ = E2_ * 3600  # (s)
C = 0.4 * 1 / 3600  # (s ** (-1))
W6W5_ = np.exp(- E2_ * C / LD)
print("W_6 / W_5 =", W6W5_)

# Landing (Pouso)
W7W0_ = W1W0_ * W2W1_ * W3W2_ * W4W3_ * W5W4_ * W6W5_ * W7W6_
print("W_7 / W_0 =", W7W0_)

# Fuel Fraction (Fração de Combustível)
WfW0_ = 1.06 * (1 - W7W0_)
print("W_f / W_0 =", WfW0_)

# Perceber que, o while foi usado, pois NÃO conhecemos o número
# de iterações necessárias para que o modelo convirja.
W0_ = np.zeros(10000)
W0_[0] = np.random.randint(10000, 100000)
k = 0
while np.abs(W0_[k] - W0_[k - 1]) >= tolerancia:
    # Empty Weigth
    WeW0_ = A * W0_[k] ** C_Empty * K_vs
    W0_[k + 1] = (W_Crew + W_Payload) / (1 - WfW0_ - WeW0_)
    k = k + 1
print("W_e / W_0 =", WeW0_)

# RESULTADO(S): ---

print("")

print("RESULTADO(S):")
print("O 'chute' inicial para o W_0 é:", W0_[0], "lbf")
print("O 'Número de Iterações Para a Convergência' é de: " + str(k - 1))
print("O 'Peso Inicial da Aeronave (W_0)' é:",
      round(W0_[k - 1], 4), "lbf")