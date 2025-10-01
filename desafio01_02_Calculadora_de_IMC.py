peso=float(input("Informe seu Peso:  "))
altura=float(input("Informe a Sua Altura:  "))
imc=peso/(altura*altura)
#print("Seu IMC é de: ",round(imc,2))
if imc<18.5:
    print(f'Seu IMC é de: {imc:.2f}','Abaixo do peso')
elif imc<=24.9:
    print(f'Seu IMC é de: {imc:.2f}','Peso normal')
elif imc<=29.9:
    print(f'Seu IMC é de: {imc:.2f}','Sobrepeso')
elif imc<=34.9:
    print(f'Seu IMC é de: {imc:.2f}','Obesidade grau 1')
elif imc<=39.9:
    print(f'Seu IMC é de: {imc:.2f}','Obesidade grau 2')
else:
    print(f'Seu IMC é de: {imc:.2f}','Obesidade grau 3')