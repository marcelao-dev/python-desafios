import random

while True:
 numero_secreto = random.randint(1,100)
 tentativas=0
 print("🎲 Bem-vindo ao jogo de adivinhar o número!")
 print("Estou pensando em um número entre 1 e 100.")

 while True:
   
  numero = int(input("Qual é seu palpite?  :"))
  tentativas +=1
  if numero < numero_secreto:
     print(f'Seu Palpite é : {numero} 🔽 Muito baixo!')
  elif numero > numero_secreto:
     print(f'Seu Palpite é : {numero} 🔽 Muito Alto!')
  elif numero == numero_secreto:
     print(f'Seu Palpite é : {numero} 🎉 Acertou! Você precisou de {tentativas} Tentativas!')
     continuar = input("Continuar? (s/n): ").strip().lower()
     if continuar not in ["s", "sim"]:
      print("Foi otimo jogar com voce!")
      exit()
     else:
       break