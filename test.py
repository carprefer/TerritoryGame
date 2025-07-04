import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

# 슬라이더 설정
slider_rect = pygame.Rect(50, 80, 300, 10)
handle_radius = 10
handle_x = slider_rect.x + 150  # 초기 위치
dragging = False

running = True
while running:
    screen.fill((30, 30, 30))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mouse_x - handle_x) < handle_radius and abs(mouse_y - slider_rect.y) < 20:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    if dragging:
        handle_x = max(slider_rect.x, min(mouse_x, slider_rect.x + slider_rect.width))

    # 슬라이더 그리기
    pygame.draw.rect(screen, (200, 200, 200), slider_rect)
    pygame.draw.circle(screen, (100, 200, 255), (handle_x, slider_rect.y + 5), handle_radius)

    # 볼륨 값 계산 (0.0 ~ 1.0)
    volume = (handle_x - slider_rect.x) / slider_rect.width
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Volume: {volume:.2f}", True, (255, 255, 255))
    screen.blit(text, (150, 120))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
