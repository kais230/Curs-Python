from datetime import datetime

def check_control_digit(cnp):
    check_number = "279146358279"
    sum = 0
    control_digit = 0
    for i in range(0,12):
        sum += int(check_number[i]) * int(cnp[i])
    if sum % 11 == 10:
        control_digit = 1
    else:
        control_digit = sum % 11
    if control_digit != int(cnp[-1]):
        raise "Cifra de control invalida"

def check_NNN(cnp):
    if cnp[9:12].isdigit() and int((cnp)[9:12]) >= 1:
        pass
    else:
        raise "NNN Not Valid"

def county_check(cnp):
    counties = ["%.2d" % i for i in range(1,47)]
    counties.append('51')
    counties.append('52')
    inserted_county = cnp[6:8]
    if inserted_county in counties:
        pass
    else:
        raise 'cod judet invalid'

def check_cnp(cnp):

    if len(cnp) != 13:
        return 'Numar invalid de caractere'
    try:
        if not cnp.isdigit():
            raise ValueError
    except ValueError:
        return 'Ai introdus un caracter invalid'


    if int(cnp[0]) not in range(1, 10, 1):
        return 'Prima cifra invalida'
    try:
        datetime.strptime(cnp[1:7], '%y%m%d')
    except ValueError:
        return 'Ai introdus o data invalida\nFormatul trebuie sa fie YYMMDD'
    county_check(cnp)
    check_NNN(cnp)
    check_control_digit(cnp)
    return 'CNP-ul introdus este valid'


#print(check_cnp('5a11102018178'))
#print(check_cnp('6211102018178'))
#print(check_cnp('a211102018178'))
#print(check_cnp('-211102018178'))
#print(check_cnp('-211102018178asdd'))
#print(check_cnp('6211102018174'))
print(check_cnp('5200229986791'))