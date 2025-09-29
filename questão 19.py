peso=float(input("escreva seu peso"))
altura=float(input("escreva sua altura"))
imc=peso/altura**2
if(imc<18.5):
    print("abaixo do peso")
elif(imc<24.9):
    print("peso normal")
elif(imc<29.9):
    print("sobrepeso")
else:
    print("obesidade")