import pygame
import sys

class AboutSection:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.credits = ["Survival Game".center(100," "), "Developed by SAV_vy Marvericks".center(80," "), "Music by ~".center(100," "), "Artwork by ~".center(100," ")]
        self.credit_texts = [self.font.render(credit, True, (255, 0, 0)) for credit in self.credits]
        self.credit_positions = [i * self.credit_texts[0].get_height() for i in range(len(self.credits))]
        self.speed = 1

    def update(self):
        for i in range(len(self.credits)):
            self.credit_positions[i] -= self.speed
            if self.credit_positions[i] + self.credit_texts[i].get_height() < 0:
                self.credit_positions[i] = self.screen.get_height()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(len(self.credits)):
            self.screen.blit(self.credit_texts[i], (10, self.credit_positions[i]))

    def run(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()

            pygame.display.flip()
            clock.tick(60)  # Set the frame rate

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("About Section")

    about_section = AboutSection(screen)
    about_section.run()

