# Classe de objetos do tipo retângulo
class retangulo:
    
    # Método construtor de objetos.
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura
    
    # Método calcular a área do retângulo.
    def calcular_area(self) -> float:
        return self.largura * self.altura

    # Método calcular o perímetro do retângulo.
    def calcular_perimetro(self) -> float:
        return 2 * (self.largura + self.altura)