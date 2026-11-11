import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("dog in bamboo forest")

background_image = pygame.transform.scale(
    pygame.image.load('lib/python3.9/site-packages/pygame/siddarth/29ec0214-5d61-4c05-b517-81a5da4fdf18.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

panda_image = pygame.transform.scale(
    pygame.image.load('lib/python3.9/site-packages/pygame/siddarth/61404daf-1f05-45c9-9826-dd512cda905c.png').convert_alpha(),
    (350, 350))

panda_rect = panda_image.get_rect(
    center=(SCREEN_WIDTH//2.5 + 35, SCREEN_HEIGHT//2.5 + 125))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(panda_image, panda_rect)
        text = pygame.font.Font(None, 36).render("Hello, World!", True, (255, 255, 255))
        display_surface.blit(text, (10, 10))    
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
