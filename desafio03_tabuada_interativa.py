while True:
    numero = int(input('Digite um numero para ver a tabuada: '))
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero*i}')
    continuar = input("Quer ver outra tabuada? (s/n): ").strip().lower()
    if continuar not in ["s", "sim"]:
        print("Obrigado por usar a Tabuada!")
        break