import pygame
import os


def drawSquare(screen, color):
    # Dibuixa una taula 9x9
    margin_left = 60
    margin_top = 60
    cell_size = 40
    wide = 3
    for k in range(10):
        # Files horitzontals
        pygame.draw.line(
            screen,
            color,
            [margin_left, margin_top + k * cell_size],
            [margin_left + 9 * cell_size, margin_top + k * cell_size],
            wide if k % 3 == 0 else 1,
        )
        # Columnes verticals
        pygame.draw.line(
            screen,
            color,
            [margin_left + k * cell_size, margin_top],
            [margin_left + k * cell_size, margin_top + 9 * cell_size],
            wide if k % 3 == 0 else 1,
        )


def drawValues(t, t_original, screen, color_original, color_new):
    fontV = pygame.font.Font("freesansbold.ttf", 26)
    margin_left = 60
    margin_top = 60
    cell_size = 40
    for r in range(9):
        for c in range(9):
            value = str(t[r][c]) if t[r][c] else ""
            if str(t_original[r][c]) != "":
                text = fontV.render(value, True, color_original)
            else:
                text = fontV.render(value, True, color_new)
            text_rect = text.get_rect(
                center=(
                    margin_left + c * cell_size + cell_size // 2,
                    margin_top + r * cell_size + cell_size // 2,
                )
            )
            screen.blit(text, text_rect)


def draw(tauler, tauler_original):
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (1100, 120)
    pygame.init()

    BLACK = (0, 0, 0)
    GRAY = (220, 220, 220)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    size = [500, 500]
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    pygame.display.set_caption("Sudoku")

    screen.fill(WHITE)

    font = pygame.font.Font("freesansbold.ttf", 16)
    # Números centrats amb les columnes
    for c in range(9):
        num = str(c + 1)
        text = font.render(num, True, BLACK, WHITE)
        text_rect = text.get_rect(center=(55 + c * 40 + 25, 40))
        screen.blit(text, text_rect)
    # Lletres centrades amb les files
    for r in range(9):
        letter = chr(ord("A") + r)
        text = font.render(letter, True, BLACK, WHITE)
        text_rect = text.get_rect(center=(40, 60 + r * 40 + 25))
        screen.blit(text, text_rect)

    drawSquare(screen, GREEN)
    drawValues(tauler, tauler_original, screen, BLACK, GRAY)

    pygame.display.flip()
