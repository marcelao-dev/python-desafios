import time
import winsound

while True:
    try:
        n=int(input("Informe um numero positivo: "))
        if n > 0:
          break
        print("Informe um numero Valido")
    except:
       print("Digite apenas numeros")

while n>=0:
     h = n // 3600
     m = (n % 3600) // 60
     s = n % 60
     print(f"{h:02}:{m:02}:{s:02}")
     winsound.Beep(800, 300)
     time.sleep (1)
     n -= 1

print("Tempo esgotado")
winsound.Beep(1200, 6000)
