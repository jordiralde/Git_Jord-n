class Jugador:
    
    def __init__(self, vida, armadura, fuerza) -> None:
        defensa = vida * armadura
        ataque = fuerza

    def Atacar(self):
        