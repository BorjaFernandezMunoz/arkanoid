import pygame as pg

from arkanoid.entidades import Pelota, Raqueta


pantalla = pg.display.set_mode((500, 200))
reloj = pg.time.Clock()
raqueta = Raqueta()
pelota = Pelota(raqueta)

raqueta.rect.left = 70
raqueta.rect.y = 70

pelota.rect.left = 0
pelota.rect.y = 50

salir = False

while not salir:
    reloj.tick(15)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            salir = True

    pantalla.fill((0,0,0))

    pulsadas = pg.key.get_pressed()
    if pulsadas[pg.K_LEFT]:
        raqueta.rect.x -= 1
    if pulsadas[pg.K_RIGHT]:
        raqueta.rect.x += 1

    pantalla.blit(raqueta.image, raqueta.rect)
    pantalla.blit(pelota.image, pelota.rect)

    if (pg.sprite.collide_rect(raqueta, pelota)):
        print("Colisión de rectángulos")
    if (pg.sprite.collide_mask(raqueta, pelota)):
        print("Colisión de máscara")

    pg.display.flip()