"""The App: window, screens (title, quiz, results) and event handling."""
import math

import pygame

from data import DESTINATIONS, FAMILY_LINES, QUESTIONS, destinations_for
from scenes import build_picture
from settings import FPS, H, SCENE_SIZE, TITLE, W
from ui import Button, gradient, wrap


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.f_huge = pygame.font.SysFont("arial", 92, bold=True)
        self.f_big = pygame.font.SysFont("arial", 40, bold=True)
        self.f_med = pygame.font.SysFont("arial", 28)
        self.f_btn = pygame.font.SysFont("arial", 30, bold=True)
        self.f_small = pygame.font.SysFont("arial", 22)

        self.pictures = {k: build_picture(k) for k in DESTINATIONS}

        # title page
        self.b_begin = Button((350, 400, 300, 70), "Click to Begin", (230, 90, 60), (255, 120, 80))
        self.b_exit = Button((350, 490, 300, 70), "Exit", (80, 90, 120), (110, 120, 160))
        # quiz
        self.b_back = Button((40, 620, 140, 52), "Back", (80, 90, 120), (110, 120, 160))
        self.b_next = Button((780, 620, 180, 52), "Next", (0, 150, 90), (0, 190, 120))
        self.b_exit_small = Button((860, 20, 110, 44), "Exit", (150, 60, 60), (200, 80, 80))
        # results
        self.b_again = Button((40, 620, 220, 52), "Plan Again")
        self.b_nextdest = Button((380, 620, 240, 52), "Next Destination", (230, 90, 60), (255, 120, 80))
        self.b_exit_res = Button((780, 620, 180, 52), "Exit", (150, 60, 60), (200, 80, 80))

        self.state = "title"
        self.running = True
        self.t = 0.0
        self.reset()

    def reset(self):
        self.q = 0
        self.answers = {}
        self.typed = ""
        self.won = []
        self.page = 0

    # ------------------------------------------------------------ events
    def handle(self, e):
        if e.type == pygame.QUIT:
            self.running = False
        elif self.state == "title":
            if self.b_begin.clicked(e):
                self.reset()
                self.state = "quiz"
            elif self.b_exit.clicked(e):
                self.running = False
        elif self.state == "quiz":
            self.handle_quiz(e)
        elif self.state == "results":
            self.handle_results(e)

    def handle_quiz(self, e):
        q = QUESTIONS[self.q]
        if self.b_exit_small.clicked(e):
            self.running = False
            return
        if self.b_back.clicked(e):
            self.go_back()
            return
        if q["type"] == "text":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    self.typed = self.typed[:-1]
                elif e.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self.submit_text()
                elif e.unicode and e.unicode.isprintable() and len(self.typed) < q["max"]:
                    self.typed += e.unicode
            elif self.b_next.clicked(e):
                self.submit_text()
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            for i, rect in enumerate(self.option_rects(q)):
                if rect.collidepoint(e.pos):
                    self.answers[q["key"]] = i
                    self.advance()
                    break

    def handle_results(self, e):
        if self.b_exit_res.clicked(e):
            self.running = False
        elif self.b_again.clicked(e):
            self.reset()
            self.state = "title"
        elif self.page < len(self.won) - 1 and self.b_nextdest.clicked(e):
            self.page += 1

    # ------------------------------------------------------- quiz logic
    def submit_text(self):
        value = self.typed.strip()
        if not value:
            return
        self.answers[QUESTIONS[self.q]["key"]] = value
        self.advance()

    def advance(self):
        self.q += 1
        if self.q >= len(QUESTIONS):
            self.won = destinations_for(self.answers["interests"])
            self.page = 0
            self.state = "results"
        else:
            self.load_typed()

    def go_back(self):
        if self.q == 0:
            self.state = "title"
            return
        self.q -= 1
        self.load_typed()

    def load_typed(self):
        q = QUESTIONS[self.q]
        self.typed = str(self.answers.get(q["key"], "")) if q["type"] == "text" else ""

    def option_rects(self, q):
        return [pygame.Rect(180, 250 + i * 80, 640, 64) for i in range(len(q["options"]))]

    # ----------------------------------------------------------- drawing
    def center(self, text, font, y, color=(255, 255, 255)):
        img = font.render(text, True, color)
        self.screen.blit(img, img.get_rect(center=(W // 2, y)))

    def draw_title(self, mouse):
        gradient(self.screen, (0, 0, W, H), (40, 130, 230), (255, 190, 120))
        for i in range(5):
            cx = (self.t * 20 + i * 260) % (W + 200) - 100
            pygame.draw.ellipse(self.screen, (255, 255, 255), (cx, 70 + i * 28, 140, 44))
            pygame.draw.ellipse(self.screen, (255, 255, 255), (cx + 30, 52 + i * 28, 90, 44))
        px = (self.t * 90) % (W + 300) - 150
        py = 300 + math.sin(self.t * 2) * 14
        red = (230, 90, 60)
        pygame.draw.polygon(self.screen, (255, 255, 255),
                            [(px, py), (px + 80, py - 10), (px + 110, py), (px + 80, py + 10)])
        pygame.draw.polygon(self.screen, red,
                            [(px + 30, py), (px + 55, py - 36), (px + 70, py - 36), (px + 60, py)])
        pygame.draw.polygon(self.screen, red,
                            [(px + 30, py), (px + 55, py + 36), (px + 70, py + 36), (px + 60, py)])
        pygame.draw.polygon(self.screen, red,
                            [(px, py), (px - 14, py - 20), (px + 6, py - 20), (px + 20, py)])
        shadow = self.f_huge.render("Flight to Fun", True, (40, 50, 90))
        self.screen.blit(shadow, shadow.get_rect(center=(W // 2 + 4, 154)))
        self.center("Flight to Fun", self.f_huge, 150)
        self.center("Maldives  -  Thailand  -  England  -  and a bonus trip!", self.f_med, 235)
        self.b_begin.draw(self.screen, self.f_btn, mouse)
        self.b_exit.draw(self.screen, self.f_btn, mouse)

    def draw_quiz(self, mouse):
        gradient(self.screen, (0, 0, W, H), (30, 80, 150), (90, 180, 210))
        q = QUESTIONS[self.q]
        total = len(QUESTIONS)
        pygame.draw.rect(self.screen, (70, 110, 170), (180, 40, 640, 16), border_radius=8)
        pygame.draw.rect(self.screen, (255, 200, 60),
                         (180, 40, int(640 * self.q / total), 16), border_radius=8)
        self.center(f"Question {self.q + 1} of {total}", self.f_small, 82)
        for i, line in enumerate(wrap(q["text"], self.f_big, 840)):
            self.center(line, self.f_big, 150 + i * 48)
        if q["type"] == "text":
            box = pygame.Rect(240, 260, 520, 70)
            pygame.draw.rect(self.screen, (255, 255, 255), box, border_radius=12)
            pygame.draw.rect(self.screen, (255, 200, 60), box, 3, border_radius=12)
            cursor = "|" if int(self.t * 2) % 2 == 0 else ""
            txt = self.f_big.render(self.typed + cursor, True, (30, 40, 70))
            self.screen.blit(txt, (box.x + 18, box.y + 12))
            self.center("Type your answer, then press Enter or click Next", self.f_small, 365)
            self.b_next.draw(self.screen, self.f_btn, mouse)
        else:
            chosen = self.answers.get(q["key"])
            for i, rect in enumerate(self.option_rects(q)):
                if rect.collidepoint(mouse):
                    col = (255, 200, 60)
                elif chosen == i:
                    col = (190, 235, 200)
                else:
                    col = (235, 245, 255)
                pygame.draw.rect(self.screen, col, rect, border_radius=14)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 2, border_radius=14)
                letter = self.f_med.render("ABCD"[i] + ".", True, (30, 80, 150))
                self.screen.blit(letter, (rect.x + 20, rect.centery - letter.get_height() // 2))
                label = self.f_med.render(q["options"][i], True, (30, 40, 70))
                self.screen.blit(label, (rect.x + 70, rect.centery - label.get_height() // 2))
        self.b_back.draw(self.screen, self.f_btn, mouse)
        self.b_exit_small.draw(self.screen, self.f_small, mouse)

    def draw_results(self, mouse):
        gradient(self.screen, (0, 0, W, H), (20, 40, 100), (80, 150, 210))
        key = self.won[self.page]
        d = DESTINATIONS[key]
        name = self.answers.get("name", "Traveler")
        if len(self.won) == 1:
            self.center(f"Congratulations, {name}! You won a trip to", self.f_med, 36)
        elif self.page == 0:
            self.center(f"Congratulations, {name}! You won TWO trips! Trip 1 of 2:", self.f_med, 36)
        else:
            self.center(f"Your BONUS trip - trip {self.page + 1} of {len(self.won)}:", self.f_med, 36)
        self.center(d["name"], self.f_big, 78)

        x = (W - SCENE_SIZE[0]) // 2
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (x - 6, 106, SCENE_SIZE[0] + 12, SCENE_SIZE[1] + 12), border_radius=8)
        self.screen.blit(self.pictures[key], (x, 112))

        self.center(d["tagline"], self.f_med, 494, (255, 220, 120))
        for i, line in enumerate(wrap(d["blurb"], self.f_small, 820)):
            self.center(line, self.f_small, 530 + i * 28)
        who = FAMILY_LINES.get(self.answers.get("family", 0), "you")
        self.center(f"Pack your bags - this one is perfect for {who}!",
                    self.f_small, 592, (200, 235, 255))

        self.b_again.draw(self.screen, self.f_btn, mouse)
        if self.page < len(self.won) - 1:
            self.b_nextdest.draw(self.screen, self.f_btn, mouse)
        self.b_exit_res.draw(self.screen, self.f_btn, mouse)

    def draw(self):
        mouse = pygame.mouse.get_pos()
        if self.state == "title":
            self.draw_title(mouse)
        elif self.state == "quiz":
            self.draw_quiz(mouse)
        elif self.state == "results":
            self.draw_results(mouse)
        pygame.display.flip()

    # --------------------------------------------------------- main loop
    def run(self):
        while self.running:
            self.t += self.clock.tick(FPS) / 1000
            for e in pygame.event.get():
                self.handle(e)
            self.draw()
        pygame.quit()