#[PT-Br]Validação de número de cartão de crédito
def sum_digits(number):
    return sum(int(d) for d in str(number))

cardnumber = input('Digite o número do cartão de crédito: ')


if len(cardnumber) == 16:
    print('Entrada válida')

    #Cada dígito do cartão é multiplicado por 2 se a posição for par
    cardnumber_multiplied = [int(digit) * 2 if i % 2 != 1 else int(digit) for i, digit in enumerate(cardnumber)]

    #Se o dígito for maior que 9, chama sum_digits para somar os dígitos
    cardnumber_higher = [sum_digits(digit) if digit > 9 else digit for digit in cardnumber_multiplied]

    print('Número do cartão após multiplicação:', cardnumber_multiplied)
    print('Número do cartão após somar dígitos maior que 10:', cardnumber_higher)
    print('A soma dos dígitos é: ' + str(sum(cardnumber_higher)))
    #Soma de todos os dígitos do cartão
    total_sum = sum(cardnumber_higher)

    #Se a soma de todos os dígitos termina em 0, cartão é válido
    if str(total_sum)[-1] == '0':
        print('O cartão é válido')

    #Se a soma de todos os dígitos não termina em 0, cartão é inválido
    else:
        print('O cartão é inválido')

#Se o cartão não contém 16 dígitos, a entrada é inválida
else:
    print('Entrada inválida, cartão não contém 16 dígitos')
    print('Cartão inserido:', cardnumber)