import pygame
import math

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 800

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Solar System Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors (RGB format)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
BLUE = (0, 100, 255)
RED = (255, 69, 0)
WHITE = (200, 200, 200)

# Sun properties
sun_x = WIDTH // 2
sun_y = HEIGHT // 2
sun_radius = 30

# Planet properties: [name, orbit_radius, planet_radius, color, angular_speed, angle]
# angular_speed determines how fast the planet moves (radians per frame)
# angle is the current position on the orbit (starts at 0)
planets = [
    ["Mercury", 80, 8, GRAY, 0.04, 0],      # Closest, fastest
    ["Venus", 130, 14, ORANGE, 0.03, 0],    # Second planet
    ["Earth", 180, 15, BLUE, 0.02, 0],      # Third planet
    ["Mars", 240, 12, RED, 0.015, 0]        # Fourth planet, slowest
]

# Font for displaying planet names
font = pygame.font.Font(None, 20)

# Animation control
paused = False

# Main game loop
running = True
while running:
    # Handle events (keyboard, mouse, window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Press SPACE to pause/resume the animation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # Fill the background with black color
    screen.fill(BLACK)

    # Draw the Sun at the center
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)

    # Draw orbit paths and planets
    for planet in planets:
        name = planet[0]
        orbit_radius = planet[1]
        planet_radius = planet[2]
        color = planet[3]
        angular_speed = planet[4]
        angle = planet[5]

        # Draw the orbit path (a thin white circle)
        pygame.draw.circle(screen, WHITE, (sun_x, sun_y), orbit_radius, 1)

        # Calculate planet position using trigonometry
        # x = center_x + radius * cos(angle)
        # y = center_y + radius * sin(angle)
        planet_x = sun_x + orbit_radius * math.cos(angle)
        planet_y = sun_y + orbit_radius * math.sin(angle)

        # Draw the planet
        pygame.draw.circle(screen, color, (int(planet_x), int(planet_y)), planet_radius)

        # Draw planet name near the planet
        text = font.render(name, True, WHITE)
        screen.blit(text, (int(planet_x) - 25, int(planet_y) - planet_radius - 20))

        # Update the angle for the next frame (only if not paused)
        if not paused:
            planet[5] += angular_speed
            # Keep angle in range [0, 2*pi] to prevent overflow
            if planet[5] > 2 * math.pi:
                planet[5] -= 2 * math.pi

    # Display pause status
    if paused:
        pause_text = font.render("PAUSED - Press SPACE to resume", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - 140, 20))
    else:
        pause_text = font.render("Press SPACE to pause", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - 100, 20))

    # Update the display
    pygame.display.flip()

    # Control frame rate (60 FPS)
    clock.tick(FPS)

# Quit Pygame
pygame.quit()