import pygame
import json
import random
import sys
from theme import Colors, UI

# Initialize Pygame
pygame.init()

class HangmanGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((UI.WIDTH, UI.HEIGHT))
        pygame.display.set_caption("Neo-Hangman")
        self.clock = pygame.time.Clock()
        self.load_words()
        
        # Game State
        self.state = "MENU" # MENU, PLAYING
        self.reset_game()
        self.font_large = pygame.font.SysFont("Verdana", 60, bold=True)
        self.font_medium = pygame.font.SysFont("Arial", 32)
        self.font_small = pygame.font.SysFont("Arial", 20)
        
        self.running = True

    def load_words(self):
        try:
            with open("words.json", "r") as f:
                data = json.load(f)
                self.categories = data["Categories"]
        except Exception as e:
            print(f"Error loading words: {e}")
            self.categories = {"General": ["PYTHON", "CODE", "GAMING"]}

    def reset_game(self, category=None):
        if not category:
            self.current_category = random.choice(list(self.categories.keys()))
        else:
            self.current_category = category
            
        self.word = random.choice(self.categories[self.current_category]).upper()
        self.guessed_letters = set()
        self.errors = 0
        self.max_errors = 6
        self.game_over = False
        self.won = False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == "MENU":
                if event.key == pygame.K_RETURN:
                    self.state = "PLAYING"
                return

            if self.game_over:
                if event.key == pygame.K_RETURN:
                    self.state = "MENU"
                    self.reset_game()
                return

            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).upper()
                if letter not in self.guessed_letters:
                    self.guessed_letters.add(letter)
                    if letter not in self.word:
                        self.errors += 1
                        if self.errors >= self.max_errors:
                            self.game_over = True
                            self.won = False
                    
                    # Check win condition
                    if all(l in self.guessed_letters for l in self.word):
                        self.game_over = True
                        self.won = True

    def draw_hangman(self, x, y):
        # Base/Gallows
        color = Colors.SECONDARY
        width = 5
        
        # Base
        pygame.draw.line(self.screen, color, (x - 100, y + 300), (x + 100, y + 300), width)
        # Vertical pole
        pygame.draw.line(self.screen, color, (x - 50, y + 300), (x - 50, y), width)
        # Horizontal pole
        pygame.draw.line(self.screen, color, (x - 50, y), (x + 50, y), width)
        # Rope
        pygame.draw.line(self.screen, color, (x + 50, y), (x + 50, y + 40), width)

        # Character (Draw based on errors)
        char_color = Colors.PRIMARY
        if self.errors >= 1: # Head
            pygame.draw.circle(self.screen, char_color, (x + 50, y + 70), 30, width)
        if self.errors >= 2: # Body
            pygame.draw.line(self.screen, char_color, (x + 50, y + 100), (x + 50, y + 200), width)
        if self.errors >= 3: # Left Arm
            pygame.draw.line(self.screen, char_color, (x + 50, y + 120), (x + 10, y + 160), width)
        if self.errors >= 4: # Right Arm
            pygame.draw.line(self.screen, char_color, (x + 50, y + 120), (x + 90, y + 160), width)
        if self.errors >= 5: # Left Leg
            pygame.draw.line(self.screen, char_color, (x + 50, y + 200), (x + 10, y + 260), width)
        if self.errors >= 6: # Right Leg
            pygame.draw.line(self.screen, char_color, (x + 50, y + 200), (x + 90, y + 260), width)

    def draw_menu(self):
        self.screen.fill(Colors.BACKGROUND)
        title_surf = self.font_large.render("NEO-HANGMAN", True, Colors.PRIMARY)
        title_rect = title_surf.get_rect(center=(UI.WIDTH // 2, 200))
        self.screen.blit(title_surf, title_rect)
        
        start_surf = self.font_medium.render("Press ENTER to Start", True, Colors.TEXT)
        start_rect = start_surf.get_rect(center=(UI.WIDTH // 2, UI.HEIGHT // 2 + 50))
        self.screen.blit(start_surf, start_rect)
        
        cat_info = f"Current Category: {self.current_category}"
        cat_surf = self.font_small.render(cat_info, True, Colors.GRAY)
        cat_rect = cat_surf.get_rect(center=(UI.WIDTH // 2, UI.HEIGHT - 100))
        self.screen.blit(cat_surf, cat_rect)

    def draw_playing(self):
        self.screen.fill(Colors.BACKGROUND)
        
        # Category Label
        cat_surf = self.font_medium.render(f"Category: {self.current_category}", True, Colors.GRAY)
        self.screen.blit(cat_surf, (UI.PADDING, UI.PADDING))
        
        # Word Display
        word_text = self.get_display_word()
        word_surf = self.font_large.render(word_text, True, Colors.TEXT)
        word_rect = word_surf.get_rect(center=(UI.WIDTH // 2, UI.HEIGHT - 150))
        self.screen.blit(word_surf, word_rect)
        
        # Hangman Drawing
        self.draw_hangman(UI.WIDTH // 2, 100)
        
        # Guessed Letters
        guessed_text = "Guessed: " + ", ".join(sorted(list(self.guessed_letters)))
        guessed_surf = self.font_small.render(guessed_text, True, Colors.GRAY)
        self.screen.blit(guessed_surf, (UI.PADDING, UI.HEIGHT - 50))
        
        # Game Over Overlays
        if self.game_over:
            overlay = pygame.Surface((UI.WIDTH, UI.HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            self.screen.blit(overlay, (0, 0))
            
            msg = "MISSION ACCOMPLISHED" if self.won else f"SYSTEM FAILURE: {self.word}"
            color = Colors.SUCCESS if self.won else Colors.ERROR
            
            msg_surf = self.font_large.render(msg, True, color)
            msg_rect = msg_surf.get_rect(center=(UI.WIDTH // 2, UI.HEIGHT // 2))
            self.screen.blit(msg_surf, msg_rect)
            
            hint_surf = self.font_medium.render("Press ENTER for Menu", True, Colors.TEXT)
            hint_rect = hint_surf.get_rect(center=(UI.WIDTH // 2, UI.HEIGHT // 2 + 80))
            self.screen.blit(hint_surf, hint_rect)

    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def draw(self):
        if self.state == "MENU":
            self.draw_menu()
        else:
            self.draw_playing()
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_input(event)
            
            self.draw()
            self.clock.tick(UI.FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()
