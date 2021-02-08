def split_and_join(line):
    lista=line.split(" ")
    nueva_cadena="-".join(lista)
    return nueva_cadena

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
