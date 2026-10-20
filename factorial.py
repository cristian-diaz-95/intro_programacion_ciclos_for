"""
calcualr un factorial de un numero
fact(n):1*2*3......*n:0!=1
ejemplo: 5!=1*2*3*4*5=120
"""
n=int(input(" ingrese el valor de n: "))
if n ==0:
    print(1)
elif n>0:
    fact=1
    for n in range(1,n+1):
        fact=fact*n
    print(n,"!= ",fact)
    
else:
    print("error n debe ser mayor o igual a cero ")
