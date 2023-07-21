from datetime import datetime

def dia():
    # Pegando o dia
    data_var = datetime.now().strftime("%d/%m/%Y")
    return data_var

def hora():
    # Pegando a Hora
    now = datetime.now()
    hora_atual = now.strftime("%H:%M:%S")
    return hora_atual