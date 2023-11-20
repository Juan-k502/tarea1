num1=int(input("ingrese primer numero: " ));
num2=int(input("ingrese segundo numero: "));
num3=int(input("ingrese tercer numero: "));
sum = num1+num2+num3 ;
prome = sum//3;
if prome%2== 0 :
    mensaj= prome,"es par: ";
else:
    mensaj= prome,"no es par: ";
print(mensaj);
