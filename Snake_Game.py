import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return True  # Snake collided with itself
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return False

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))


# Difficulty levels
EASY = 10
MEDIUM = 15
HARD = 20

# Display score
def display_score(surface, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)  # Set the color to black
    surface.blit(text, (10, 10))

# Display "Game Over" and final score
def display_game_over(surface, final_score):
    font_game_over = pygame.font.Font(None, 48)
    text_game_over = font_game_over.render("Game Over", True, RED)
    surface.blit(text_game_over, (WIDTH // 4, HEIGHT // 3))

    font_final_score = pygame.font.Font(None, 36)
    text_final_score = font_final_score.render(f"Your Score: {final_score}", True, RED)
    surface.blit(text_final_score, (WIDTH // 4, HEIGHT // 2))


# Display difficulty selection
def display_difficulty(surface, font):
    surface.fill(BLACK)  
    font = pygame.font.Font(None, 36)
    text = font.render("Select Difficulty:", True, WHITE)  
    surface.blit(text, (WIDTH // 4, HEIGHT // 3 - 50))

    easy_text = font.render("Easy", True, WHITE)
    medium_text = font.render("Medium", True, WHITE)
    hard_text = font.render("Hard", True, WHITE)

    surface.blit(easy_text, (WIDTH // 3, HEIGHT // 2))
    surface.blit(medium_text, (WIDTH // 3, HEIGHT // 2 + 50))
    surface.blit(hard_text, (WIDTH // 3, HEIGHT // 2 + 100))

    pygame.display.update()

    selected_difficulty = None

    while not selected_difficulty:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if WIDTH // 3 <= x <= WIDTH // 3 + 100 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
                    selected_difficulty = EASY
                elif WIDTH // 3 <= x <= WIDTH // 3 + 150 and HEIGHT // 2 + 50 <= y <= HEIGHT // 2 + 100:
                    selected_difficulty = MEDIUM
                elif WIDTH // 3 <= x <= WIDTH // 3 + 100 and HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 150:
                    selected_difficulty = HARD

    return selected_difficulty


# Main function
# ... (previous code)

# Main function
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    # Difficulty selection
    difficulty = display_difficulty(surface,font=WHITE)

    snake = Snake()
    food = Food()
    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != DOWN:
            snake.direction = UP
        elif keys[pygame.K_DOWN] and snake.direction != UP:
            snake.direction = DOWN
        elif keys[pygame.K_LEFT] and snake.direction != RIGHT:
            snake.direction = LEFT
        elif keys[pygame.K_RIGHT] and snake.direction != LEFT:
            snake.direction = RIGHT

        # Check for collision
        collision = snake.update()
        if collision:
            game_over = True

        if not game_over:
            if snake.get_head_position() == food.position:
                snake.length += 1
                food.randomize_position()
                score += 1

            surface.fill(WHITE)
            snake.render(surface)
            food.render(surface)
            display_score(surface, score)
            screen.blit(surface, (0, 0))
            pygame.display.update()
            clock.tick(difficulty)

    # Game over screen
    display_game_over(surface, score)
    pygame.display.update()

    # Display "Quit" button in the top-right corner
    font_quit = pygame.font.Font(None, 24)
    text_quit = font_quit.render("Quit", True, BLACK)
    pygame.draw.rect(surface, WHITE, (WIDTH - 50, 10, 40, 20))
    surface.blit(text_quit, (WIDTH - 45, 10))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if WIDTH - 50 <= x <= WIDTH - 10 and 10 <= y <= 30:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
