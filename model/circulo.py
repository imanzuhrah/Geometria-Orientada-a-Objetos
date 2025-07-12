# Constante de pi
PI = 3.14159

# Classe de objetos do tipo: Círculo
class circulo:
    # Método contrutor de objetos.
    def __init__ (self, raio: float):
        self.raio = raio 

    # Método para calcular a área do Círculo.
    def calcular_area(self) -> float:
        return PI * (self.raio ** 2)
        

    # Método para calcular o perímetro do Círculo.
    def calcular_perimetro (self) -> float:
        return 2 * PI * self.raio
    