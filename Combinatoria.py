import keyboard
import itertools
def select_nums ():
    Nums=[]
    while True:
        Check=input("Ingrese los numeros que quiera o ingrese listo si no quiere poner mas: ")
        if Check.isdigit() == True:
            Nums.append(Check)
        elif Check=="listo":
            break
    return Nums

n = select_nums()
print (n)

def select_op (numeros):
    while True:
        RTA=[]
        Choose=input("Elija: \n1-Permutación Sin Repetición \n2-Permutación Con Repetición \n3-Permutación Circular \n")
        if Choose.isdigit():
            if int(Choose) > 0 and int(Choose) < 4:
                if Choose == "1":
                    for permutacion_sr in itertools.permutations(numeros):
                        RTA.append(permutacion_sr)
                    print(RTA)
                    break
                elif Choose =="2":
                    RTA.append(list(itertools.product(numeros,repeat=len(numeros))))
                    print(RTA)
                    break
                elif Choose =="3":
                    if len(numeros) > 1:
                        print("No se puede hacer permutacion circular con esos valores")
                        break
                    else:
                        resultado=1
                        Num=int(numeros[0])
                        print(Num)
                        for i in range(Num):
                            if i==0:
                                i=i+1
                            resultado*=i
                            RTA.append(resultado)
                        print(RTA)
                        break
            else:
                print("Elija un número entre 0 y 3")
        else:
            print("Elija un número entre 0 y 3")

select_op(n)