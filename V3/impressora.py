from layoutPiPe import codigo_impressora
from layoutCDO import codigo_impressora2
from layoutAC import codigo_impressora3
from layoutLacre import codigo_impressora4
def Impressora(dia,hora,codigo,nome,qrcode,ativo,escolha,colaborador):
    if(escolha == 'PIPE'):
        codigo_zpl = codigo_impressora(dia,hora,codigo,nome,qrcode,ativo,colaborador)
        # Configuração da porta da impressora
        port = "LPT1"  # Altere para a porta correta da sua impressora

        # Abre o arquivo de porta da impressora e envia o comando ZPL
        with open(port, "wb") as printer:
            printer.write(codigo_zpl.encode("utf-8"))

    elif(escolha =='CHAMADO'):
        codigo_zpl = codigo_impressora2(dia,hora,codigo,nome,qrcode,ativo,colaborador)
        # Configuração da porta da impressora
        port = "LPT1"  # Altere para a porta correta da sua impressora

        with open(port, "wb") as printer:
            printer.write(codigo_zpl.encode("utf-8"))

    elif(escolha == 'A/C'):
        codigo_zpl = codigo_impressora3(colaborador)
        # Configuração da porta da impressora
        port = "LPT1"  # Altere para a porta correta da sua impressora

        with open(port, "wb") as printer:
            printer.write(codigo_zpl.encode("utf-8"))

    elif (escolha == 'LACRE'):
        codigo_zpl = codigo_impressora4()
        # Configuração da porta da impressora
        port = "LPT1"  # Altere para a porta correta da sua impressora

        with open(port, "wb") as printer:
            printer.write(codigo_zpl.encode("utf-8"))
            printer.write(codigo_zpl.encode("utf-8"))





