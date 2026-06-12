import pygame
import sys


class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_power = 12
        self.ground_level = y
        self.is_jumping = False

    def move(self, dx, dy=0):
        """Move the character horizontally by dx pixels"""
        self.x += dx * self.speed
        # Keep character within screen bounds horizontally
        self.x = max(0, min(self.x, self.screen.get_width() - 20))

    def jump(self):
        """Make the character jump if on the ground"""
        if not self.is_jumping:
            self.velocity_y = -self.jump_power
            self.is_jumping = True

    def update(self):
        """Update character physics (gravity and jumping)"""
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Check if character reached ground level
        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.velocity_y = 0
            self.is_jumping = False

    def draw(self):
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, 20, 20))
        pygame.draw.circle(self.screen, "red", (self.x + 5, self.y + 5), 3)
        pygame.draw.circle(self.screen, "red", (self.x + 15, self.y + 5), 3)


# This function is called when you run this file, and is used to test the Character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_character():
    # TODO: change this function to test your class
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        character.draw()
        pygame.display.update()


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_character()
