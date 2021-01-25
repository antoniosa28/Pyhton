from datetime import datetime

def multa(tempo_A, tempo_B, distancia, vel_max):
    # Converter tempo(str) para tempo(datetime)

    tA = datetime.strptime(tempo_A, '%H:%M:%S')
    tB = datetime.strptime(tempo_B, '%H:%M:%S')

    # se a hora do ponto b for menor que a significa que o mudou
    if tB.hour < tA.hour:
        tB = datetime.strptime(str(tB.day+1) + " " + tempo_B, '%d %H:%M:%S')
    
    delta_tempo = tB - tA
    seconds = delta_tempo.total_seconds()
    hour = seconds/3600

    vel_media = distancia / hour
    vel_max_tolerada = vel_max + vel_max*0.1

    if vel_media <= vel_max_tolerada:
        return False
    return True


print(multa("09:00:00","08:00:00",100,100))