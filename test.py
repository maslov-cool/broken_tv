import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 400
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for i in range(10000):
            pygame.draw.rect(screen, (random.randrange(256), random.randrange(256), random.randrange(256)), 
                            [random.random() * width, random.random() * height, 1, 1])
        
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()
