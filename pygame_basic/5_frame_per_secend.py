import pygame
####################################################################

# 기본초기화 (반드시 해야하는것들)

pygame.init() # 초기화

#화면 크기 설정
screen_width=480 # 가로크기
screen_height= 640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("mongmin game") # 게임이름

# FPS
clock=pygame.time.Clock()
####################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

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

# 적 enemy
enemy=pygame.image.load("C:\\Users\\Mongmin\\Documents\\simpletest\\pygame_basic\\background\\enemy.jpg")
enemy_size=enemy.get_rect().size # 이미지의 크기를 가져옴
enemy_width=enemy_size[0] # 케릭터 가로크기
enemy_hight=enemy_size[1] # 케릭터 세로크기
enemy_x_pos=(screen_width/2) - (enemy_width/2) # 화면 가로의 절반 크기에 해당하는곳에 위치
enemy_y_pos=(screen_height/2)-(enemy_hight/2) # 화면 세로의 절반 

#폰트 정의
game_font=pygame.font.Font(None,40) #폰트 객체 생성

#총 시간
total_time=10

# 시간 시작
start_ticks=pygame.time.get_ticks() # 시작 ticks 을 받아옴

# 이벤트 루프
running=True #  게임 진행 중인지 확인
while running:
    dt=clock.tick(60)
    # print("fps : "+str(clock.get_fps()))

    # 2. 이벤트 처리(키보드, 마우스)
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
    # 3. 게임케릭터 위치 정의
    character_x_pos += to_x *dt 
    character_y_pos += to_y *dt  
    # 4. 충돌 처리
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

    # 충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=False
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0)) # 배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks) / 1000 
    # 경과시간(ms)을 주석1000으로 나누어서 초단위로 표시
    timer=game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer,(10,10))
    
    # 만약 시간이 0 이하면 게임종료
    if total_time-elapsed_time<=0:
        print("타임아웃")
        running=False
    
    pygame.display.update() # 게임화면 다시그리기

# 종료 직전 대기
pygame.time.delay(2000) # 2초 정도 대기
# pygame 종료
pygame.quit()
