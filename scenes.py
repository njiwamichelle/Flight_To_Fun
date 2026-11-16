"""Pictures of each destination, drawn with code.

If you put real photos in an "images" folder next to main.py, named
maldives.jpg, thailand.jpg, england.jpg and japan.jpg (or .png), they are
used instead of the drawings.
"""
import math
import os
import random

import pygame

from data import DESTINATIONS
from settings import SCENE_SIZE
from ui import gradient

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- Maldives
def _palm(s, x, y, h, lean):
    top = (x + lean, y - h)
    pygame.draw.polygon(s, (120, 80, 45),
                        [(x - 7, y), (x + 7, y), (top[0] + 3, top[1]),
                         (top[0] - 3, top[1])])
    for ang in (-170, -145, -120, -95, -65, -40, -15):
        a = math.radians(ang)
        mid = (top[0] + 38 * math.cos(a), top[1] + 38 * math.sin(a) - 14)
        end = (top[0] + 78 * math.cos(a), top[1] + 78 * math.sin(a) + 14)
        pygame.draw.lines(s, (30, 140, 60), False, [top, mid, end], 6)
    pygame.draw.circle(s, (90, 55, 30), top, 6)
    pygame.draw.circle(s, (90, 55, 30), (top[0] - 8, top[1] + 8), 5)


def _bungalow(s, x, y, water_y):
    for sx in range(x + 6, x + 100, 24):
        pygame.draw.line(s, (110, 80, 50), (sx, y + 8), (sx, water_y + 6), 4)
    pygame.draw.rect(s, (140, 100, 60), (x - 6, y, 112, 10))
    pygame.draw.rect(s, (245, 232, 205), (x + 10, y - 44, 80, 44))
    pygame.draw.polygon(s, (170, 120, 60),
                        [(x, y - 44), (x + 50, y - 80), (x + 100, y - 44)])
    pygame.draw.rect(s, (90, 60, 40), (x + 42, y - 28, 16, 28))
    pygame.draw.rect(s, (120, 190, 230), (x + 16, y - 34, 18, 16))
    pygame.draw.rect(s, (120, 190, 230), (x + 66, y - 34, 18, 16))


def scene_maldives(s):
    w, h = s.get_size()
    hor = int(h * 0.52)
    gradient(s, (0, 0, w, hor), (70, 160, 235), (200, 235, 250))
    pygame.draw.circle(s, (255, 244, 170), (620, 80), 42)
    pygame.draw.circle(s, (255, 250, 210), (620, 80), 30)
    for cx, cy, r in ((150, 70, 26), (190, 62, 34), (235, 72, 24),
                      (440, 110, 22), (475, 104, 30)):
        pygame.draw.circle(s, (255, 255, 255), (cx, cy), r)
    gradient(s, (0, hor, w, h - hor), (60, 215, 215), (0, 95, 150))
    gradient(s, (0, hor, w, 40), (140, 240, 230), (60, 215, 215))
    rnd = random.Random(3)
    for _ in range(40):
        wx, wy = rnd.randint(0, w), rnd.randint(hor + 10, h - 5)
        pygame.draw.line(s, (200, 250, 250), (wx, wy), (wx + 22, wy), 2)
    pygame.draw.ellipse(s, (245, 225, 170), (w - 280, hor - 18, 260, 50))
    _palm(s, w - 190, hor + 4, 110, 18)
    _palm(s, w - 120, hor + 6, 90, -14)
    _bungalow(s, 70, hor + 110, hor + 125)
    _bungalow(s, 240, hor + 150, hor + 168)
    pygame.draw.line(s, (140, 100, 60), (170, hor + 120), (240, hor + 156), 6)


# ---------------------------------------------------------------- Thailand
def scene_thailand(s):
    w, h = s.get_size()
    hor = int(h * 0.58)
    gradient(s, (0, 0, w, hor), (255, 140, 90), (255, 215, 140))
    pygame.draw.circle(s, (255, 235, 150), (560, hor - 40), 60)
    gradient(s, (0, hor, w, h - hor), (230, 130, 90), (70, 70, 110))
    # temple
    cx = 250
    pygame.draw.rect(s, (200, 40, 40), (cx - 90, hor - 50, 180, 60))
    pygame.draw.polygon(s, (240, 190, 40),
                        [(cx - 110, hor - 50), (cx, hor - 110), (cx + 110, hor - 50)])
    pygame.draw.polygon(s, (200, 40, 40),
                        [(cx - 80, hor - 90), (cx, hor - 150), (cx + 80, hor - 90)])
    pygame.draw.polygon(s, (240, 190, 40),
                        [(cx - 55, hor - 130), (cx, hor - 190), (cx + 55, hor - 130)])
    pygame.draw.line(s, (240, 190, 40), (cx, hor - 190), (cx, hor - 225), 4)
    pygame.draw.rect(s, (90, 30, 20), (cx - 14, hor - 28, 28, 38))
    # longtail boat
    bx, by = 520, hor + 55
    pygame.draw.polygon(s, (120, 60, 30),
                        [(bx, by), (bx + 190, by), (bx + 160, by + 26), (bx + 30, by + 26)])
    pygame.draw.polygon(s, (230, 70, 80),
                        [(bx - 30, by - 14), (bx, by), (bx + 40, by), (bx + 30, by - 10)])
    pygame.draw.line(s, (80, 50, 30), (bx + 190, by), (bx + 330, by + 50), 5)
    pygame.draw.circle(s, (60, 60, 60), (bx + 330, by + 50), 8)
    pygame.draw.rect(s, (255, 220, 80), (bx + 60, by - 36, 70, 36))
    pygame.draw.polygon(s, (230, 70, 80),
                        [(bx + 50, by - 36), (bx + 95, by - 62), (bx + 140, by - 36)])
    # market stalls
    cols = [(230, 60, 90), (60, 170, 220), (250, 190, 50), (110, 200, 110)]
    for i in range(4):
        sx = 30 + i * 150
        sy = h - 75
        pygame.draw.rect(s, (60, 40, 30), (sx + 6, sy, 6, 60))
        pygame.draw.rect(s, (60, 40, 30), (sx + 108, sy, 6, 60))
        for k in range(6):
            c = cols[i] if k % 2 == 0 else (255, 255, 255)
            pygame.draw.polygon(s, c, [(sx + k * 20, sy - 4), (sx + k * 20 + 20, sy - 4),
                                       (sx + k * 20 + 20, sy + 14), (sx + k * 20 + 10, sy + 22),
                                       (sx + k * 20, sy + 14)])
        pygame.draw.rect(s, (120, 80, 50), (sx + 10, sy + 36, 100, 22))
        pygame.draw.circle(s, (255, 90, 90), (sx + 40, sy + 32), 9)
        pygame.draw.circle(s, (255, 210, 70), (sx + 70, sy + 32), 9)
        pygame.draw.circle(s, (120, 220, 120), (sx + 95, sy + 32), 9)
    # lanterns
    for lx in (330, 400, 470):
        pygame.draw.line(s, (60, 40, 30), (lx, 0), (lx, 40), 2)
        pygame.draw.ellipse(s, (255, 90, 60), (lx - 14, 38, 28, 36))
        pygame.draw.line(s, (255, 220, 120), (lx - 12, 56), (lx + 12, 56), 2)


# ----------------------------------------------------------------- England
def scene_england(s):
    w, h = s.get_size()
    hor = int(h * 0.68)
    gradient(s, (0, 0, w, hor), (140, 165, 195), (215, 225, 235))
    for cx, cy, r in ((120, 70, 34), (165, 60, 44), (215, 72, 32), (560, 50, 36),
                      (610, 44, 46), (665, 58, 32), (400, 110, 26), (435, 104, 34)):
        pygame.draw.circle(s, (245, 247, 250), (cx, cy), r)
    pygame.draw.ellipse(s, (90, 170, 80), (-80, hor - 40, 520, 160))
    pygame.draw.ellipse(s, (70, 150, 70), (300, hor - 20, 600, 180))
    pygame.draw.rect(s, (80, 80, 90), (0, hor + 50, w, h))
    pygame.draw.line(s, (245, 245, 245), (0, hor + 100), (w, hor + 100), 4)
    # clock tower
    tx = 330
    stone = (205, 180, 120)
    pygame.draw.rect(s, stone, (tx - 30, hor - 210, 60, 215))
    pygame.draw.rect(s, (185, 160, 100), (tx - 38, hor - 250, 76, 50))
    pygame.draw.polygon(s, (90, 100, 110),
                        [(tx - 40, hor - 250), (tx, hor - 335), (tx + 40, hor - 250)])
    pygame.draw.line(s, (90, 100, 110), (tx, hor - 335), (tx, hor - 355), 3)
    pygame.draw.circle(s, (250, 250, 240), (tx, hor - 220), 20)
    pygame.draw.circle(s, (60, 60, 60), (tx, hor - 220), 20, 3)
    pygame.draw.line(s, (40, 40, 40), (tx, hor - 220), (tx, hor - 234), 3)
    pygame.draw.line(s, (40, 40, 40), (tx, hor - 220), (tx + 9, hor - 215), 3)
    for yy in range(hor - 180, hor - 10, 40):
        for xx in (tx - 14, tx + 6):
            pygame.draw.rect(s, (130, 110, 70), (xx, yy, 8, 22))
    # palace wing
    pygame.draw.rect(s, (215, 190, 135), (tx + 40, hor - 70, 230, 76))
    for i in range(7):
        pygame.draw.rect(s, (130, 110, 70), (tx + 55 + i * 31, hor - 55, 12, 28))
    # red double-decker bus
    bx, by = 520, hor + 55
    pygame.draw.rect(s, (215, 30, 40), (bx, by - 80, 200, 80), border_radius=8)
    pygame.draw.line(s, (150, 20, 30), (bx, by - 40), (bx + 200, by - 40), 3)
    for i in range(5):
        pygame.draw.rect(s, (190, 225, 245), (bx + 14 + i * 36, by - 72, 26, 24))
        pygame.draw.rect(s, (190, 225, 245), (bx + 14 + i * 36, by - 34, 26, 22))
    for wx in (bx + 40, bx + 160):
        pygame.draw.circle(s, (30, 30, 30), (wx, by + 2), 15)
        pygame.draw.circle(s, (170, 170, 170), (wx, by + 2), 6)
    # trees
    for tx2 in (60, 700):
        pygame.draw.rect(s, (95, 65, 40), (tx2 - 6, hor - 10, 12, 50))
        pygame.draw.circle(s, (45, 125, 55), (tx2, hor - 30), 34)
        pygame.draw.circle(s, (55, 140, 65), (tx2 - 18, hor - 14), 24)


# ------------------------------------------------------------------- Japan
def scene_japan(s):
    w, h = s.get_size()
    hor = int(h * 0.66)
    gradient(s, (0, 0, w, hor), (150, 205, 245), (255, 230, 235))
    pygame.draw.circle(s, (255, 90, 90), (640, 70), 34)
    # Mount Fuji
    mx = 300
    pygame.draw.polygon(s, (95, 110, 160), [(mx - 260, hor), (mx, 70), (mx + 260, hor)])
    pygame.draw.polygon(s, (250, 250, 255),
                        [(mx - 62, 150), (mx, 70), (mx + 62, 150), (mx + 36, 138),
                         (mx + 14, 160), (mx - 12, 140), (mx - 36, 162)])
    pygame.draw.rect(s, (70, 150, 90), (0, hor, w, h - hor))
    pygame.draw.ellipse(s, (130, 195, 230), (60, hor + 40, 340, 80))
    # pagoda
    px, py = 600, hor + 20
    for i in range(5):
        tw = 70 - i * 9
        ty = py - i * 44
        pygame.draw.rect(s, (235, 225, 205), (px - tw + 14, ty - 34, 2 * tw - 28, 34))
        pygame.draw.rect(s, (190, 40, 40), (px - tw + 14, ty - 34, 6, 34))
        pygame.draw.rect(s, (190, 40, 40), (px + tw - 20, ty - 34, 6, 34))
        pygame.draw.polygon(s, (60, 60, 75),
                            [(px - tw - 18, ty - 34), (px + tw + 18, ty - 34),
                             (px + tw - 6, ty - 50), (px - tw + 6, ty - 50)])
    pygame.draw.line(s, (60, 60, 75), (px, py - 5 * 44 - 6), (px, py - 5 * 44 - 40), 4)
    # torii gate
    gx, gy = 120, hor + 40
    pygame.draw.rect(s, (210, 50, 40), (gx, gy - 90, 12, 90))
    pygame.draw.rect(s, (210, 50, 40), (gx + 90, gy - 90, 12, 90))
    pygame.draw.polygon(s, (210, 50, 40),
                        [(gx - 22, gy - 90), (gx + 124, gy - 90), (gx + 108, gy - 108),
                         (gx - 6, gy - 108)])
    pygame.draw.rect(s, (210, 50, 40), (gx - 6, gy - 74, 114, 10))
    # cherry blossoms
    rnd = random.Random(7)
    for tx2, ty2 in ((470, hor + 10), (700, hor + 40), (40, hor + 20)):
        pygame.draw.rect(s, (100, 70, 55), (tx2 - 6, ty2 - 40, 12, 60))
        for _ in range(26):
            ox, oy = rnd.randint(-48, 48), rnd.randint(-48, 12)
            pygame.draw.circle(s, rnd.choice([(255, 183, 205), (255, 205, 220), (250, 160, 190)]),
                               (tx2 + ox, ty2 - 50 + oy), rnd.randint(9, 16))
    for _ in range(40):
        pygame.draw.circle(s, (255, 200, 215),
                           (rnd.randint(0, w), rnd.randint(hor - 20, h - 5)), 3)


SCENES = {
    "maldives": scene_maldives,
    "thailand": scene_thailand,
    "england": scene_england,
    "japan": scene_japan,
}


def build_picture(key):
    """Return a Surface for the destination: a real photo if present, else the drawing."""
    for ext in ("jpg", "jpeg", "png"):
        path = os.path.join(HERE, "images", f"{DESTINATIONS[key]['image']}.{ext}")
        if os.path.exists(path):
            try:
                img = pygame.image.load(path).convert()
                return pygame.transform.smoothscale(img, SCENE_SIZE)
            except pygame.error:
                pass
    surf = pygame.Surface(SCENE_SIZE)
    SCENES[key](surf)
    return surf