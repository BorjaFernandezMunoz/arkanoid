import pygame as pg

from __init__ import ANCHO, ALTO
from escenas import MejoresJugadores, Partida, Portada


class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            MejoresJugadores(self.pantalla),
        ]

    def jugar(self):
        """
        Bucle principal
        """
        for escena in self.escenas:
            acabar_juego = escena.bucle_principal()
            if acabar_juego:
                print('La escena me pide que acabe el juego')
                break 

        pg.quit()

if __name__ == '__main__':
    print('Arrancamos el juego desde game.py que tiene Arkanoid')
    juego = Arkanoid()
    juego.jugar()