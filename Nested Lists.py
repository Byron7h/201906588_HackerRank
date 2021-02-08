if __name__ == '__main__':
    
    est=[]
    nota=[]
    for _ in range(int(input())):
        name = input()
        est.append(name)
        score = float(input())
        nota.append(score)
    dic = dict(zip(nota,est))
    
    min1 = min(nota)
    while min(nota) == min1:
        pos = nota.index(min(nota))
        est.pop(pos)
        nota.remove(min(nota))
    
    min2=min(nota)
    finales=[]
    
    
    
    while min(nota) == min2:
        posicion = nota.index(min2)
        nota.pop(posicion)
        finales.append(est[posicion])
        est.pop(posicion)
        
    finales.sort()
    
    for a in range(0,len(finales)):
        print(finales[a]) 