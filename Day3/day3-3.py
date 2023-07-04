# Construa um sistema para verificar se o ano é bissexto ou não.

# 1 - Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# 2 - Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# 3 - Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# 4 - O ano é bissexto (tem 366 dias).
# 5 - O ano não é um ano bissexto (tem 365 dias).


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    elif year % 100 != 0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
