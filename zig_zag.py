def convert(s: str, numRows: int) -> str:
    dlugosc = len(s)
    lista = ['' for i in range(numRows)]

    for i in range(numRows):
        index=i
        krok=0
        while (index<dlugosc):
            lista[i]+=s[index]
            if(i<numRows-1 and i>0):
                if(krok % 2 != 0):
                    index+=2*i
                else:
                    index+=2*(numRows-i-1)
            elif numRows==1:
                index+=1
            else:
                index+=2*(numRows-1)
            krok += 1

    tekst="".join(lista)
    return tekst

slowo='A'
zygzak=convert(slowo, 1)
print(zygzak)
print(len(slowo))