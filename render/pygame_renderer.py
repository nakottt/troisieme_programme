import pygame
import os
from core.map import deplacer_joueur

TILE_SIZE = 48
ASSETS_PATH = "assets"

def load_image(path):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))


def run_pygame(player, map_data, mobs_on_map):
    pygame.init()

    rows = len(map_data)
    cols = len(map_data[0])

    screen = pygame.display.set_mode(
        (cols * TILE_SIZE, rows * TILE_SIZE)
    )
    pygame.display.set_caption("TroisiÃ¨me Programme")

    clock = pygame.time.Clock()

    # ================= LOAD ASSETS =================
    tiles = {
        "#": load_image(os.path.join(ASSETS_PATH, "tiles", "wall.png")),
        ".": load_image(os.path.join(ASSETS_PATH, "tiles", "ground.png")),
    }

    player_sprite = load_image(
        os.path.join(ASSETS_PATH, "player", "player.png")
    )

    running = True
    direction = None

    while running and player["pv"] > 0:
        # ================= EVENTS =================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    direction = "z"
                elif event.key == pygame.K_q:
                    direction = "q"
                elif event.key == pygame.K_s:
                    direction = "s"
                elif event.key == pygame.K_d:
                    direction = "d"
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # ================= UPDATE =================
        if direction:
            player["pv"] = deplacer_joueur(
                map_data,
                direction,
                player,
                mobs_on_map
            )
            direction = None

        # ================= RENDER =================
        screen.fill((0, 0, 0))

        for y, row in enumerate(map_data):
            for x, cell in enumerate(row):
                pos = (x * TILE_SIZE, y * TILE_SIZE)

                if cell in tiles:
                    screen.blit(tiles[cell], pos)

                if cell == "P":
                    screen.blit(tiles["."], pos)   # sol sous le joueur
                    screen.blit(player_sprite, pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()