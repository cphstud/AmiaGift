import settings, pygame
s = settings

def draw_window(): # Tegne grafik i vinduet
    s.Window.fill(s.WHITE)
    s.Window.blit(pygame.image.load("resources/BGIMG.png"), (0, 0))
    # hvis billede skulle skaleres: BG = pygame.transform.scale(BG_img,(width,height))

    # *** Points og levels ***
    points_hl = s.main_font.render(f"Points: {s.points}", True, (0, 0, 255))
    level_hl = s.main_font.render(f"Level: {s.level}", True, (255, 0, 0))
    s.Window.blit(points_hl, (10, 10))
    s.Window.blit(level_hl, (s.width - points_hl.get_width() - 10, 10))
    s.pygame.display.update()