# Importação do pacote e dos módulos orientados a objeto
from .model import circulo
from .model import retangulo

# Apresenta as opções de calculo
print('Opções geométricas disponíveis:')
print('1 - Área e Perímetro de um Círculo')
print('2 - Área e Perímetro de um Retângulo')

# Solicita a opção do usuário.
escolha = input('Digite o número da opção desejada: ')

# Executa os cálculos geométricos
match escolha:
    case '1':
        raio = float(input('Digite o raio do círculo:'))

        # Instância de um objeto do tipo círculo
        meu_circulo = circulo(raio)

        # Calcula a área e o perímetro
        area = meu_circulo.calcular_area()
        perimetro = meu_circulo.calcular_perimetro()

        # Exibe os dois resultados
        print(f'A área do círculo é: {area:.2f}')
        print(f'O perímetro do círculo é: {perimetro: .2f}')

    case '2':
        largura = float(input('Digite a largura do retângulo:'))
        altura = float(input('Digite a altura do retângulo:'))

        # Instância de um objeto do tipo retângulo
        meu_retangulo = retangulo(largura, altura)

        # Calcula a área e o perímetro
        area = meu_retangulo.calcular_area()
        perimetro = meu_retangulo.calcular_perimetro()

        # Exibe os dois resultados
        print(f'A área do retângulo é: {area:.2f}')
        print(f'O perímetro do retângulo é: {perimetro: .2f}')



    case _:
        print('Opção Inválida...')
        exit()

