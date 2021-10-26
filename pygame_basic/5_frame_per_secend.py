import pygame

pygame.init() # 초기화

#화면 크기 설정
screen_width=480 # 가로크기
screen_height= 640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("mongmin game") # 게임이름

clock=pygame.time.Clock()

# 배경이미지 불러오기
background=pygame.image.load("C:\\Users\\Mongmin\\Documents\\simpletest\\pygame_basic\\background\\bg.jpg")

# 스프라이트(케릭터) 불러오기
character=pygame.image.load("C:\\Users\\Mongmin\\Documents\\simpletest\\pygame_basic\\background\\character.png")
character_size=character.get_rect().size # 이미지의 크기를 가져옴
character_width=character_size[0] # 케릭터 가로크기
character_hight=character_size[1] # 케릭터 세로크기
character_x_pos=(screen_width/2) - (character_width/2) # 화면 가로의 절반 크기에 해당하는곳에 위치
character_y_pos=screen_height-character_hight # 화면 세로의 절반 

# 이동할 좌표
to_x=0
to_y=0

#이동속도
character_speed=0.5
# 이벤트 루프
running=True #  게임 진행 중인지 확인
while running:
    dt=clock.tick(60)
    # print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ㅔ크
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는지
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x -=character_speed 
            elif event.key==pygame.K_RIGHT:
                to_x +=character_speed
            elif event.key==pygame.K_UP:
                to_y -=character_speed
            elif event.key==pygame.K_DOWN:
                to_y +=character_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos += to_x *dt 
    character_y_pos += to_y *dt  
    
    #가로경계값처리
    if character_x_pos <0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    #세로경계값처리
    if character_y_pos <0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_hight:
        character_y_pos=screen_height-character_hight

    screen.blit(background,(0,0)) # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면 다시그리기
# pygame 종료
pygame.quit()
