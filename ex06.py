def bissexto(ano):
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        return True
    return False

def dia_anterior(data):
    dia, mes, ano = data.split('-')

    mes_dict = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    if dia == '01' and mes == '01':
        return '{}-{}-{}'.format('31', '12', int(ano)-1)

    if dia == '01' and mes=='03' and bissexto(int(ano)):
        return '29-02-{}'.format(ano)

    if dia == '01':
        mes = int(mes)-1
        dia = mes_dict[str(mes)]
        return '{}-0{}-{}'.format(dia, mes, ano)

    return '{}-{}-{}'.format(int(dia)-1, mes, ano)

dia_anterior('01-03-2020')