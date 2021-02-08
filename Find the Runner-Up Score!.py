if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    lista2=[]
    for dato in lista:
        if dato not in lista2:
            lista2.append(dato)
    lista2.sort() 
    posicion= len(lista2)-2   
    print(lista2[posicion])
