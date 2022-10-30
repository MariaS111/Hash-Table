import os
import string
from typing import Dict, List

STOP = '--'


def search(v: int, di: Dict[int, List[str]]) -> str:
    return di[v]
 
    
def delete(n: int, di: Dict[int, List[str]]) -> None:
    del di[n]


def hash_funct(key: str) -> int:
        number, s1, s2=0, 0, 0
        poz={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        key=key[0:2]
        key=key[::-1]
        for i in poz:
            s1=poz[key[1]]
            s2=poz[key[0]]
        number=s1*26**1+s2*26**0
        number=int(number)
        return number
 
    
def print_hash_table(dickt: Dict[int, List[str]]) -> None:
    for k in sorted(dickt.keys()):
        print (k, ':', *dickt[k]) 


def check(j: str) -> bool:
    mas = []
    spisok = string.ascii_lowercase
    for i in range(len(j)):
        if j[i] in spisok and len(j)>=2:
            mas.append(True)
        else:
            mas.append(False)   
    return all(mas)        
    
    
def main():
    dickt = {}
    while True:
        print("\nEnter value(string with letters only) for Hash Table.(Enter -- to end)")
        val = input().lower()
        if val == STOP:
            break
        else:
            while check(val) == False:
                print("\nError.\nEnter another string:")
                val = input().lower()
        v = hash_funct(val)
        if v in dickt:
            dickt[v].append(val)
        else:
            dickt[v] = [val] 
    
    
    os.system('cls')
    while True:
        print('\nChoose option:\n1 - Show Hash Table\n2 - Search by key\n3 - Delete by key\n4 - End program')
        option = int(input())
        if option not in [1, 2, 3, 4]:
            print('\nSelect possible value!')
        elif option == 1:
            print("\n______Hash Table______")   
            print_hash_table(dickt)
        elif option == 2:
            print("\n______Search by key______\nEnter key:") 
            a = int(input())
            while a not in dickt:
                print("\nInvalid data.Enter another key!")
                a=int(input())
            print("\nElement(s) with key", a , " - ", *search(a, dickt))
        elif option == 3:
            print("\n______Deletion by key_______\nEnter key:")
            b = int(input())
            while b not in dickt:
                print("\nInvalid data.Enter another key!")
                b = int(input())
            delete(b, dickt)
            print("\nElement(s) with key", b , "deleted\n")
        elif option == 4:
            return False
            


if __name__ == '__main__':
    main()