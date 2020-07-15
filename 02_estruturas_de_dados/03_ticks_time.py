import time

ticks = time.time()
# Ticks desde 12:00am, January 1, 1970: 1583115679.9241986
print("Ticks desde 12:00am, January 1, 1970:", ticks)

print(time.ctime(ticks))  # Wed Mar  4 10:36:46 2020

# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=4,
# tm_hour=10, tm_min=36, tm_sec=46, tm_wday=2, tm_yday=64, tm_isdst=0)
print(time.gmtime(ticks))
print("gmtime" + str(time.gmtime()))

agora = time.localtime()

# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=4,
# tm_hour=10, tm_min=36, tm_sec=46, tm_wday=2, tm_yday=64, tm_isdst=0)
print(agora)

print(f"Ano: {agora.tm_year}")      # Ano: 2020
print(f"Mes: {agora.tm_mon}")       # Mes: 3
print(f"Dia: {agora.tm_mday}")      # Dia: 4
print(f"Hora: {agora.tm_hour}")     # Hora: 10
print(f"Minuto: {agora.tm_min}")    # Minuto: 41
print(f"Segundo: {agora.tm_sec}")   # Segundo: 19
print(f"Oia da senana: {agora.tm_wday}")        # Oia da senana: 2
print(f"Dia no ano: {agora.tm_yday}")           # Dia no ano: 64
print(f"Horario de verao: {agora.tm_isdst}")    # Horario de verao: 0
