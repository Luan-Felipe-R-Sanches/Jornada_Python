idade = input('Digite a sua idade: ')
sexo = input('Digite seu sexo ("M" para Masculino e "F" para Feminino: ')

if sexo.upper() == 'M' :
    if int(idade) >= 65:
        print('Parabéns! Sua aposentadoria será concebida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {65 - int(idade)} anos.')
elif sexo.upper() == 'F':
    if int(idade) >= 60:
        print('Parabéns! Sua aposentadoria será concebida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {60 - int(idade)} anos.')
else:
    print("Opção Inválida! favor tentar novamente.")