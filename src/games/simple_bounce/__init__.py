import pygame


def run():
    # Constants
    WIDTH = 1024
    HEIGHT = 576
    RADIUS = 24

    # Initialization
    pygame.init()
    clock = pygame.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    ball = pygame.Vector2(screen.width / 2, screen.height / 2)

    # Variables
    is_running = True  # game loop flag
    dt = 0  # clock time
    dx = dy = 1  # directions

    while is_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                is_running = False

        # set screen background
        screen.fill("white")

        # draw a circle on the screen
        pygame.draw.circle(screen, "black", ball, RADIUS)

        # simple bounce
        ball.x += dx * dt * 300
        ball.y += dy * dt * 300

        if ball.x <= 24 or ball.x >= WIDTH - 24:
            dx = -dx

        if ball.y <= 24 or ball.y >= HEIGHT - 24:
            dy = -dy

        # flip the screen to shows what we're doing.
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # 60 FPS

    pygame.quit()
