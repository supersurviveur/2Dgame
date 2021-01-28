import pygame
surface=pygame.image.load("./textures/sheet.png")
i = 0
for line in range(0, 128, 16):
    for column in range(256, 272, 16):
        rect = pygame.Rect(column, line, 16, 16)
        new_s = surface.subsurface(rect)
        pygame.image.save(new_s, "textures/floornewnew{}.png".format(i))
        i += 1