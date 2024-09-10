import oper_soma


while True:
    operacao = input("Escolha a Operação (1-Soma ): ")

    if operacao in ['1']:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        if operacao == '1':
            print(f"Resultado: {num1} + {num2} = {oper_soma.soma(num1, num2)}")    
            continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            break
        else:
          print("Selecione uma operação válida: Soma")
        continuar = input("Deseja tentar novamente? (s/n): ").strip().lower()
        if continuar != 's':
              break
