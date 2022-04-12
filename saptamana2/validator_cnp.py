import datetime


def read_input():
    eroare_nr_cifre = "CNP invalid: nu sunt 13 cifre"
    eroare_sex = "CNP invalid: no sex"
    eroare_data = "Data invalida"
    eroare_judet = "Judet invalid"
    eroare_nnn = "NNN invaild"
    eroare_cifra_control = "Invalid din cauza cifrei de control"

    cnp = input("Introduceti un CNP: ")
    if len(cnp) != 13:
        return eroare_nr_cifre

    # verificare sex
    if int(cnp[0]) not in range(1, 10):
        return eroare_sex

    # verificare data nasterii
    data = cnp[1:7]
    try:
        datetime.datetime.strptime(data, '%y%m%d')
    except ValueError:
        return eroare_data

    # verificare judet
    if int(cnp[7:9]) not in range(1, 47) and int(cnp[7:9]) not in range(51, 53):
        return eroare_judet

    # verificare NNN
    if int(cnp[9:12]) == 0:
        return eroare_nnn

    # verificare cifra de control
    nr_control = '279146358279'
    suma = 0

    for index, value in enumerate(nr_control):
        suma += int(cnp[index]) * int(value)

    # alta varianta
    # for i in range(0, len(cnp) - 1):
    #     sum += int(cnp[i]) * int(nr_control[i])

    c = suma % 11
    if c == 10:
        c = 1

    if c != int(cnp[12]):
        return eroare_cifra_control

    return "CNP valid"


print(read_input())

# test cnp valid 5220406478191
