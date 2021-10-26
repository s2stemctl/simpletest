 import pygame

pygame.init() # 초기화

#화면 크기 설정
screen_width=480 # 가로크기
screen_height= 640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("mongmin game") # 게임이름

# 이벤트 루프
running=True #  게임 진행 중인지 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ㅔ크
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는지
            running=False


# pygame 종류
pygame.quit()
