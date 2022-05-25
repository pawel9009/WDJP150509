def otwarcie_pliku(path):
    plik = open(path, 'w')
    return plik


def zamkniecie_pliku(file):
    file.close()


def zapisz(file, text):
    if not file.closed:
        result = ''
        for char in text:
            if 97 <= ord(char) <= 122:
                continue
            else:
                result += char
        file.write(result)
    else:
        print("plik nie jest otwarty")