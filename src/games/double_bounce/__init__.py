import numpy as np
import pygame

# Constants
WIDTH = 1024
HEIGHT = 576
RADIUS = 24


def randGen() -> tuple:
    rng = np.random.default_rng()
    x = rng.uniform(0, WIDTH)
    y = rng.uniform(0, HEIGHT)
    return x, y


def run():
    # Initialization
    pygame.init()
    clock = pygame.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ballA = pygame.Vector2(randGen()[0], randGen()[1])
    ballB = pygame.Vector2(randGen()[0], randGen()[1])

    # Variables
    is_running = True  # game loop flag
    dt = 0  # clock time
    ballADx = ballADy = 1
    ballBDx = ballBDy = 1

    while is_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                is_running = False

        # set screen background
        screen.fill("white")

        # draw a circle on the screen
        pygame.draw.circle(screen, "darkred", ballA, RADIUS)
        pygame.draw.circle(screen, "darkblue", ballB, RADIUS)

        # simple bounce for two balls
        ballA.x += ballADx * dt * 300
        ballA.y += ballADy * dt * 300

        ballB.x += ballBDx * dt * 300
        ballB.y += ballBDy * dt * 300

        if ballA.x <= RADIUS or ballA.x >= WIDTH - RADIUS:
            ballADx = -ballADx
        if ballA.y <= RADIUS or ballA.y >= HEIGHT - RADIUS:
            ballADy = -ballADy

        if ballB.x <= RADIUS or ballB.x >= WIDTH - RADIUS:
            ballBDx = -ballBDx
        if ballB.y <= RADIUS or ballB.y >= HEIGHT - RADIUS:
            ballBDy = -ballBDy

        # collision detection
        cX = ballA.x - ballB.x
        cY = ballA.y - ballB.y
        distance = np.hypot(cX, cY)

        if distance <= 2 * RADIUS:
            ballADx = -ballADx
            ballADy = -ballADy
            ballBDx = -ballBDx
            ballBDy = -ballBDy

        # flip the screen to shows what we're doing.
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # 60 FPS

    pygame.quit()
