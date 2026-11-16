"""Small reusable UI helpers: gradient backgrounds, text wrapping, buttons."""
import pygame


def gradient(surf, rect, top, bottom):
    """Fill rect=(x, y, w, h) with a vertical gradient from top to bottom colour."""
    x, y, w, h = rect
    for i in range(h):
        t = i / max(1, h - 1)
        c = tuple(int(top[k] + (bottom[k] - top[k]) * t) for k in range(3))
        pygame.draw.line(surf, c, (x, y + i), (x + w, y + i))


def wrap(text, font, max_w):
    """Split text into lines that fit within max_w pixels."""
    lines, line = [], ""
    for word in text.split():
        test = (line + " " + word).strip()
        if font.size(test)[0] <= max_w:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


class Button:
    def __init__(self, rect, text, color=(0, 150, 200), hover=(0, 190, 240)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.hover = hover

    def draw(self, surf, font, mouse):
        c = self.hover if self.rect.collidepoint(mouse) else self.color
        pygame.draw.rect(surf, (20, 30, 60), self.rect.move(0, 4), border_radius=14)
        pygame.draw.rect(surf, c, self.rect, border_radius=14)
        pygame.draw.rect(surf, (255, 255, 255), self.rect, 2, border_radius=14)
        label = font.render(self.text, True, (255, 255, 255))
        surf.blit(label, label.get_rect(center=self.rect.center))

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                and self.rect.collidepoint(event.pos))