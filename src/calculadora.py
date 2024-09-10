import oper_soma
import oper_divisao
import oper_multiplicacao
import oper_subtracao

while True:
    operacao = input("Escolha a Operação (1-Soma  2-Divisão  3-Multiplicação  4-Subtração): ")

    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        if operacao == '1':
            print(f"Resultado: {num1} + {num2} = {oper_soma.soma(num1, num2)}")
        elif operacao == '4':
            print(f"Resultado: {num1} - {num2} = {oper_subtracao.subtracao(num1, num2)}")
        elif operacao == '3':
            print(f"Resultado: {num1} X {num2} = {oper_multiplicacao.multiplicacao(num1, num2)}")
        elif operacao == '2':
            if num2 != 0:
                print(f"Resultado: {num1} ÷ {num2} = {oper_divisao.divisao(num1, num2)}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        
        continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            break
    else:
        print("Selecione uma operação válida: Soma, Divisão, Multiplicação, Subtração.")
        continuar = input("Deseja tentar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break
