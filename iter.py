from itertools import permutations
import os.path
import os
#from unrar import rarfile
#rar = rarfile.RarFile('sample.rar')
#rar.extract(acknow.txt)
print('OpenAFB nin rar dosyası parola bulucusu')
print('Hangi karakterleri içerebilir?')
digits=input()

print("Kaç haneli olsun")
lenght=int(input())
print("rar ın dizini")
rarloc=input()
print("rardaki en kucuk dosyanin ismi (uzantisiyla beraber)")
fileinrar=input()
print("cikarilacak dizin")
exloc=input()
def generater(digits,lenght):
    while len(digits)<lenght:
        digits*=lenght
        count=0
        result='./'+fileinrar
    for hane in range(1,lenght+1):
        for possible in set(permutations(digits,hane)):
            ##count+=1
            #print("".join(possible))
            son="".join(possible)
            print(son)
            os.system('./unrar x'+' '+rarloc+' '+fileinrar+' '+exloc+' '+'-p'+son)
            if os.path.isfile(result):
                print(son)
                print(son)
                print(son)
                break
    print(count)
    

generater(digits,lenght)
