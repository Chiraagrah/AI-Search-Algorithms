
import pygame
import time

# Lazy Pygame window and fonts stored as module state
_state = {
    'screen': None,
    'cell_size': 24,
    'font': None,
}


def _ensure_window(puzzle):
    if _state['screen'] is None:
        pygame.init()
        rows = puzzle.row
        cols = puzzle.col
        cs = _state['cell_size']
        width = cols * cs
        height = rows * cs
        _state['screen'] = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Fringe Visualization')
        _state['font'] = pygame.font.SysFont(None, max(12, cs // 3))


def Draw(puzzle, start, goal, fringe, explored, path=None, steps=None, show_heuristics=False):
    """Draw the puzzle using Pygame. This function is intentionally simple and
    is called repeatedly by the search algorithms to update the display.
    """
    if path is None:
        path = set()
    else:
        path = set(path)

    _ensure_window(puzzle)
    screen = _state['screen']
    cs = _state['cell_size']
    colors = {
        'wall': (40, 40, 40),
        'empty': (240, 240, 240),
        'start': (0, 200, 0),
        'goal': (200, 0, 0),
        'explored': (255, 141, 161),
        'frontier': (0, 255, 255),
        'path': (255, 200, 0),
        'text': (0, 0, 0),
    }

    # note: event handling (quit) is handled by wait_for_close()

    screen.fill((200, 200, 200))

    frontier_positions = set(node[-1].state for node in fringe)

    for i in range(puzzle.row):
        for j in range(puzzle.col):
            rect = pygame.Rect(j * cs, i * cs, cs, cs)
            pos = (i, j)
            if puzzle.puzzle[i][j] == '#':
                color = colors['wall']
            elif pos == start:
                color = colors['start']
            elif pos == goal:
                color = colors['goal']
            elif pos in path:
                color = colors['path']
            elif pos in frontier_positions:
                color = colors['frontier']
            elif pos in explored:
                color = colors['explored']
            else:
                color = colors['empty']

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (150, 150, 150), rect, 1)

            # draw heuristic value (Manhattan) in top-left if requested and not a wall
            if show_heuristics and puzzle.puzzle[i][j] != '#':
                # compute Manhattan distance to goal
                if goal is not None:
                    h = abs(goal[0] - i) + abs(goal[1] - j)
                    h_surf = _state['font'].render(str(h), True, (0, 0, 0))
                    # place small text in cell's top-left with slight padding
                    screen.blit(h_surf, (j * cs + 2, i * cs + 2))

    # draw steps counter in bottom-right (white text on black bg)
    if steps is not None:
        font = _state['font']
        rows = puzzle.row
        cols = puzzle.col
        text = f"Steps: {steps}"
        text_surf = font.render(text, True, (255, 255, 255))
        padding = 6
        # create background rect
        bg_rect = text_surf.get_rect()
        bg_rect.width += padding * 2
        bg_rect.height += padding * 2
        bg_rect.right = cols * cs - 6
        bg_rect.bottom = rows * cs - 6
        # draw black background and then text
        pygame.draw.rect(screen, (0, 0, 0), bg_rect)
        text_pos = (bg_rect.left + padding, bg_rect.top + padding)
        screen.blit(text_surf, text_pos)

    pygame.display.flip()
    # small delay so human eyes can follow updates
    time.sleep(0.01)


def wait_for_close():
    """Block until the user closes the Pygame window (or presses ESC).
    Call this after the algorithm finishes to keep the visualization visible.
    """
    if _state['screen'] is None:
        return
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        clock.tick(30)
    pygame.quit()