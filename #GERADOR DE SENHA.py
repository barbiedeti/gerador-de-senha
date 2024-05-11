#GERADOR DE SENHA

import random
import string

def gerar_senha(len_pass = 10):
    ascii_options = string.ascii_letters
    digit_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + digit_options + punt_options

    senha = ''
    for i in range(0, len_pass):
        digit = random.choice(options)
        senha += digit

    return senha

choice_user = input('A sua senha precisa de quantos digitos? ')
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print('Digite um número válido.')
    exit()

response = gerar_senha(len_pass=choice_user)
print(f'Sua senha é: {response}')
