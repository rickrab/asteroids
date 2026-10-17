from asteroid import *
from asteroidfield import *
import asteroidfield
from constants import *
from logger import log_state
from player import *
import pygame

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidf = AsteroidField()

    running = True
    while running:
        log_state()
        dt = clock.tick(60) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




        updatable.update(dt)
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()







if __name__ == "__main__":
    main()
