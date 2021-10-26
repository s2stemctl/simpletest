import pygame

pygame.init() # 초기화

#화면 크기 설정
screen_width=480 # 가로크기
screen_height= 640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("mongmin game") # 게임이름

# 배경이미지 불러오기
# background=pygame.image.load("C:\\Users\\Mongmin\\Documents\\simpletest\\pygame_basic\\background\\bg.jpg")

# 이벤트 루프
running=True #  게임 진행 중인지 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ㅔ크
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는지
            running=False
    # screen.blit(background,(0,0)) # 배경그리기
    screen.fill((0,0,255))
    pygame.display.update() # 게임화면 다시그리기
# pygame 종류
pygame.quit()
