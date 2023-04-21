import pygame
import powerups
import os
from Zone import Zone
from Customizable_var import Custom_var
from Slider import slider
#Player 1 Variables
player1_x,player1_y,player1_vel,player1_Health,player1_bullet_shot,player1_bullet_shot_sec,player1_num_bulletshot,is_speedboosted1,PU1_time = 250,250,5,100,False,0,0,False,0

#Player Variables in general
player_wid,player_len,player_vel,first_loop,wait_reload,player1_should_reload,player2_should_reload,player_won = 40,40,5,True,0,False,False,0
#Player 2 Variables
player2_x,player2_y,player2_vel,player2_Health,player2_bullet_shot,player2_bullet_shot_sec,player2_num_bulletshot,is_speedboosted2,PU2_time = 750,250,5,100,False,0,0,False,0
#Bullet Variables
player1_bullet_cords,player2_bullet_cords = [],[]
settings_icon_image = pygame.image.load('settings.png')
settings_icon = pygame.transform.scale(settings_icon_image,(100,100))
back_icon_image = pygame.image.load('back-arrow.png')
back_icon = pygame.transform.scale(back_icon_image,(100,100))
Zone_list = [5, 5, 5]
z = Zone(Zone_list)
CV = Custom_var()
frame = 0
seconds = 0
pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('RogueShips')
PU1 = powerups.Powerups(win,"1")
PU2 = powerups.Powerups(win,"2")
sl_zone_speed = slider(win, (100, 100), 0.08, 1.19, 0.0037)
clock = pygame.time.Clock()
IsGameStart= False
Run = True
mouse_down = True
if_settings = False
Start_Title_font = pygame.font.SysFont("freesansbold.ttf",100)
Start_SubTitle_font = pygame.font.SysFont("freesansbold.ttf",50)
End_Title_font = pygame.font.SysFont("freesansbold.ttf",150)
End_SubTitle_font = pygame.font.SysFont("freesansbold.ttf",50)
Health_font = pygame.font.SysFont("freesansbold.ttf",50)

Start_Title = Start_Title_font.render("Welcome to Rogue Ships",True,(110, 22, 22))
Start_SubTitle = Start_SubTitle_font.render("Press enter to start game",True,(110, 22, 22))
End_SubTitle = End_SubTitle_font.render(f'Thank you for playing',True,(110, 22, 22))
Powerup = pygame.image.load(os.path.join('Assets','PowerUpShipGame.png'))
Powerup1 = pygame.transform.scale(Powerup,(30,30))
while not IsGameStart:
    if not if_settings:
        clock.tick(60)
        win.fill((1,14,24))
        win.blit(Start_Title,(100,400))
        win.blit(Start_SubTitle,(300,500))
        win.blit(settings_icon,(10,10))
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < 100 and mouse_pos[0] > 0 and mouse_pos[1] < 100 and mouse_pos[1] > 0 and pygame.mouse.get_pressed()[0]:
            if_settings = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            IsGameStart = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
    if if_settings:
        clock.tick(60)
        win.fill((1, 14, 24))
        win.blit(back_icon,(890,5))
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 900 and mouse_pos[0] < 1000 and mouse_pos[1] < 100 and mouse_pos[1] > 0 and pygame.mouse.get_pressed()[0]:
            if_settings = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            if event.type == pygame.MOUSEMOTION and mouse_down:
                x, y = pygame.mouse.get_pos()
                sl_zone_speed.move_slider(x, y)
        sl_zone_speed_font = Health_font.render(f'Zone Speed: {round(sl_zone_speed.bar_pos / 10, 3)}', True,
                                                (110, 22, 22))
        win.blit(sl_zone_speed_font, (200, 30))
        sl_zone_speed.draw()
        CV.Zone_speed = sl_zone_speed.bar_pos
        pygame.display.update()

while Run:
    clock.tick(60)
    win.fill((1,14,24))
    frame += 1
    if frame % 60 == 0:
        seconds += 1
        if z.in_zone((player1_x, player1_y), "1"):
            player1_Health -= 5
        if z.in_zone((player2_x, player2_y), "2"):
            player2_Health -= 5
    if seconds >= 8:
        for y in range (0,len(Zone_list)):
            Zone_list[y] += CV.Zone_speed
    ZONE_RED = (114, 50, 53)
    pygame.draw.rect(win, ZONE_RED, (0, 0, Zone_list[1], 1000))  # Zone wall 1 (left)
    pygame.draw.rect(win, ZONE_RED, (995 - Zone_list[1], 0, 1000 - Zone_list[1], 1000))  # Zone wall 1 (right)
    pygame.draw.rect(win, ZONE_RED, (0, 1000 - Zone_list[2], 1000, Zone_list[2]))  # Zone wall 2
    pygame.draw.rect(win, ZONE_RED, (0, 0, 1000, Zone_list[0]))  # Zone wall 0


    keys = pygame.key.get_pressed()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if not player1_x >= 460:
            player1_x += player1_vel
    if keys[pygame.K_w]:
        if not player1_y <= 5:
            player1_y -= player1_vel

    if keys[pygame.K_a]:
        if not player1_x <= 0:
            player1_x -= player1_vel
    if keys[pygame.K_s]:
        if not player1_y >= 953:
            player1_y += player1_vel
    if keys[pygame.K_RIGHT]:
        if not player2_x >= 953:
            player2_x += player2_vel
    if keys[pygame.K_UP]:
        if not player2_y <= 5:
            player2_y -= player2_vel
    if keys[pygame.K_LEFT]:
        if not player2_x <= 540:
            player2_x -= player2_vel
    if keys[pygame.K_DOWN]:
        if not player2_y >= 953:
            player2_y += player2_vel
    if keys[pygame.K_SPACE]:
        if not player1_bullet_shot:
            player1_bullet_shot = True
            player1_num_bulletshot += 1
            player1_bullet_cords.append([player1_x+40,player1_y+20])
    if keys[pygame.K_RCTRL]:
        if not player2_bullet_shot:
            player2_bullet_shot = True
            player2_num_bulletshot += 1
            player2_bullet_cords.append([player2_x-40, player2_y+20])

    if player1_bullet_shot:
        player1_bullet_shot_sec += 1
        if player1_bullet_shot_sec == 30:
            player1_bullet_shot = False
            player1_bullet_shot_sec = 0
    if player2_bullet_shot:
        player2_bullet_shot_sec += 1
        if player2_bullet_shot_sec == 30:
            player2_bullet_shot = False
            player2_bullet_shot_sec = 0
    PU1.make_PU()
    PU2.make_PU()
    pygame.draw.rect(win, (154, 154, 154), (player1_x, player1_y, player_wid, player_len))# player 1
    pygame.draw.rect(win, (154, 154, 154), (player2_x, player2_y, player_wid, player_len))# player 2
    #decorations
    pygame.draw.rect(win, (113,166,210), (500,0, player_wid, 1000))
    pygame.draw.rect(win, (255,0,0), (500, 0, 5, 1000))
    pygame.draw.rect(win, (255,0,0), (535, 0, 5, 1000))
    #Health
    play1_Health_out = Health_font.render(f'{player1_Health}', True, (47, 79, 79))
    play2_Health_out = Health_font.render(f'{player2_Health}', True, (47, 79, 79))
    win.blit(play1_Health_out, (20, 20))
    win.blit(play2_Health_out, (927, 20))


    if player1_num_bulletshot >= 1:
        for x in range(0, player1_num_bulletshot):
            player1_bullet_cords[x][0] += 20
        for x in range(0, player1_num_bulletshot):
            pygame.draw.rect(win, (176, 143, 38), (player1_bullet_cords[x][0], player1_bullet_cords[x][1], 10, 10))
        for x in range(1,player1_num_bulletshot):
            if player1_bullet_cords[0][0] >= 1100:
                player1_bullet_cords.pop(0)
                player1_num_bulletshot -=1
        for x in range(0,player1_num_bulletshot):
            if player1_bullet_cords[x][1] >= player2_y and player1_bullet_cords[x][1] <= player2_y + 40 and player1_bullet_cords[x][
    0] >= player2_x and player1_bullet_cords[x][0] <= player2_x + 40:
                player2_Health -= 10
                player1_bullet_cords.pop(x)
                player1_num_bulletshot -=1
                break


    if player2_num_bulletshot >= 1:
        for x in range(0, player2_num_bulletshot):
            player2_bullet_cords[x][0] -= 20
        for x in range(0, player2_num_bulletshot):
            pygame.draw.rect(win, (176, 143, 38), (player2_bullet_cords[x][0], player2_bullet_cords[x][1], 10, 10))
        for x in range(1, player2_num_bulletshot):
            if player2_bullet_cords[0][0] <= -10:
                player2_bullet_cords.pop(0)
                player2_num_bulletshot -=1
        for x in range(0,player2_num_bulletshot):
            if player2_bullet_cords[x][1] >= player1_y and player2_bullet_cords[x][1] <= player1_y + 40 and \
                    player2_bullet_cords[x][
                        0] >= player1_x and player2_bullet_cords[x][0] <= player1_x + 40:
                player1_Health -= 10
                player2_bullet_cords.pop(x)
                player2_num_bulletshot -= 1
                break
    if player1_Health <= 0:
        Run = False
        player_won = 2
    if player2_Health <= 0:
        Run = False
        player_won = 1
    if player2_Health <= 0  and player1_Health <= 0:
        Run = False
        player_won = 3
    pygame.display.update()
    if PU1.if_PUtouch((player1_x,player1_y)) and not is_speedboosted1:
        player1_vel += 5
        is_speedboosted1 = True
        PU1.detete_PU()
    if is_speedboosted1:
        PU1_time += 1
        if PU1_time == 300:
            is_speedboosted1 = False
            player1_vel -= 5
            PU1_time = 0
    if PU2.if_PUtouch((player2_x,player2_y)) and not is_speedboosted2:
        player2_vel += 5
        is_speedboosted2 = True
        PU2.detete_PU()
    if is_speedboosted2:
        PU2_time += 1
        if PU2_time == 300:
            is_speedboosted2 = False
            player2_vel -= 5
            PU2_time = 0





IsGameEnd = True
while IsGameEnd:
    clock.tick(60)
    win.fill((1,14,24))
    if not player_won == 3:
        End_Title = End_Title_font.render(f'PLAYER {player_won} WON', True, (110, 22, 22))
    else:
        End_Title = End_Title_font.render(f'TIE', True, (110, 22, 22))
    win.blit(End_Title, (100,100))
    win.blit(End_SubTitle, (300, 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()






