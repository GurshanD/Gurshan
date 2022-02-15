import pygame
import sys
import random
import time
pygame.init()
WIDTH = 800
HEIGHT = 600
red = (255,0,0)
blue = (0,0,255) 
white = (255, 255, 255)
background_colour = (0,0,0)

player_size = 50
player_position = [WIDTH/2,HEIGHT-2*player_size]

enemy_size = 50
enemy_position = [WIDTH/2,enemy_size]

x1 = player_position[0]
y1 = player_position[1]

x2 = enemy_position[0]
y2 = enemy_position[1]

esx = x2 + 25
esy = y2
psx = x1 + 25
psy = y1

speed1 = 2
speed2 = 2.5
speed3 = 3
speed4 = 4

enemy_shot_position_x = (x2+15)
enemy_shot_position_y = (y2+50)

player_shot_position_x = (x1 + 15)
player_shot_position_y = (y1)

shots_on_enemy = 0
shots_on_player = 0

enemy_shot_size = 22
player_shot_size = 22
clock = pygame.time.Clock()

did_enemy_shoot = False
did_player_shoot = False

speed = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False
def player_shot (screen, red, x1, y1, player_size, blue, x2, y2, enemy_size, player_shot_position_x, player_shot_position_y, player_shot_size, background_colour, kills_by_enemy, speed):
	while player_shot_position_y > 0:
		pygame.draw.rect(screen, red, (x1, y1, player_size, player_size)) 
		pygame.draw.rect(screen, blue, (x2, y2, enemy_size, enemy_size)) 
		pygame.draw.rect(screen, red, (player_shot_position_x, player_shot_position_y, player_shot_size, player_shot_size))
		player_shot_position_y-=speed
		pygame.display.update()
		screen.fill(background_colour)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				screen.fill(background_colour)
				if event.key == pygame.K_LEFT:
					x1 -= 50
					if x1 <= 0:
						x1 = 750 
				elif event.key == pygame.K_RIGHT:
					x1 += 50	
					if x1>750:
						x1 = 0							
				elif event.key == pygame.K_a:
					x2 -= 50
					if x2 <0:
						x1=750
				elif event.key == pygame.K_d:
					x2 += 50
					if x2 > 750:
						x2= 0
					pygame.display.update()
					screen.fill(background_colour)
			elif event.type == pygame.QUIT:
				sys.exit()	
		kills_by_enemy = Font.render(str(shots_on_player), 1, white)	
		screen.blit(kills_by_enemy, (50,150))
		kills_by_player = Font.render(str(shots_on_enemy), 1, white)
		screen.blit(kills_by_player, (50,450))
		pygame.draw.rect(screen, red, (x1, y1,player_size, player_size)) 
		pygame.draw.rect(screen, blue, (x2, y2, enemy_size, enemy_size)) 
		pygame.draw.rect(screen, red, (player_shot_position_x, player_shot_position_y, player_shot_size, player_shot_size))
		pygame.display.update()
		if (player_shot_position_x <= x2 and player_shot_position_x > (x2 + enemy_size)) or (x2 <= player_shot_position_x and x2 > (player_shot_position_x + player_shot_size)): 
 			return (False, x1, y1, x2, y2)
		elif (player_shot_position_x >= x2 and player_shot_position_x < (x2 + enemy_size)) or (x2 >= player_shot_position_x and x2 < (player_shot_position_x + player_shot_size)):
			if (player_shot_position_y>= y2 and player_shot_position_y<(y2 + enemy_size)) or (y2 >= player_shot_position_y and y2 < (player_shot_position_y + player_shot_size)):
 				return (True, x1, y1, x2, y2)
	else:
		return (None, x1, y1, x2, y2)

def enemy_shot(screen, red, x1, y1, player_size, blue, x2, y2, enemy_size, enemy_shot_position_x, enemy_shot_position_y, enemy_shot_size, background_colour, kills_by_player, speed):
	while enemy_shot_position_y < 600:
		pygame.draw.rect(screen, red, (x1, y1, player_size, player_size)) 
		pygame.draw.rect(screen, blue, (x2, y2, enemy_size, enemy_size)) 
		pygame.draw.rect(screen, blue, (enemy_shot_position_x, enemy_shot_position_y, enemy_shot_size, enemy_shot_size))
		enemy_shot_position_y+= speed
		pygame.display.update()
		screen.fill(background_colour)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				screen.fill(background_colour)
				if event.key == pygame.K_LEFT:
					x1 -= 50
					if x1 <= 0:
						x1 = 750  
				elif event.key == pygame.K_RIGHT:
					x1 += 50	
					if x1>750:
						x1 = 0
				elif event.key == pygame.K_a:
					x2 -= 50
					if x2 <0:
						x1=750
				elif event.key == pygame.K_d:
					x2 += 50
					if x2 > 750:
						x2= 0
					pygame.display.update()
					screen.fill(background_colour)
			elif event.type == pygame.QUIT:
				sys.exit()

		kills_by_enemy = Font.render(str(shots_on_player), 1, white)	
		screen.blit(kills_by_enemy, (50,150))
		kills_by_player = Font.render(str(shots_on_enemy), 1, white)
		screen.blit(kills_by_player, (50,450))
		pygame.draw.rect(screen, red, (x1, y1, player_size, player_size)) 
		pygame.draw.rect(screen, blue, (x2, y2, enemy_size, enemy_size)) 
		pygame.draw.rect(screen, blue, (enemy_shot_position_x, enemy_shot_position_y, enemy_shot_size, enemy_shot_size))
		pygame.display.update()
		if (enemy_shot_position_x <= x1 and enemy_shot_position_x > (x1 + player_size)) or (x1 <= enemy_shot_position_x and x1 > (enemy_shot_position_x + enemy_shot_size)):
 			return (False, x1, y1, x2, y2)
		elif (enemy_shot_position_x >= x1 and enemy_shot_position_x < (x1 + player_size)) or (x1 >= enemy_shot_position_x and x1 < (enemy_shot_position_x + enemy_shot_size)):
			if (enemy_shot_position_y>= x1 and enemy_shot_position_y < (y1 + player_size)) or (y1 >= enemy_shot_position_y and y1 <(enemy_shot_position_y + enemy_shot_size)):
 				return (True, x1, y1, x2, y2)
	else:
		return (None, x1, y1, x2, y2)

Font = pygame.font.SysFont(None, 35)
screen.fill(background_colour)

while game_over == False:
	enemy_shot_position_x = (x2+15)
	enemy_shot_position_y = (y2+50)
	player_shot_position_x = (x1 + 15)
	player_shot_position_y = (y1)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			screen.fill(background_colour)
#player moves
			if event.key == pygame.K_LEFT:
				x1 -= 50
				if x1 <0:
					x1 = 750 
			elif event.key == pygame.K_RIGHT:
				x1 += 50
				if x1 > 750:
					x1 = 0
			elif event.key == pygame.K_UP:	
				Player_shot_check, x1, y1, x2, y2 = player_shot(screen, red, x1, y1, player_size, blue, x2, y2, enemy_size, player_shot_position_x, player_shot_position_y, player_shot_size, background_colour, kills_by_enemy, speed)
				if Player_shot_check:
					shots_on_enemy +=1
				screen.fill(background_colour)
				kills_by_player = Font.render(str(shots_on_enemy), 1, white)
				screen.blit(kills_by_player, (50,450))
				pygame.display.update()
#enemy moves
			elif event.key == pygame.K_a:
				x2 -= 50
				if x2 <0:
					x2=750
			elif event.key == pygame.K_d:
				x2 += 50
				if x2 > 750:
					x2 = 0
			elif event.key == pygame.K_w:
				Enemy_shot_check, x1, y1, x2, y2 = enemy_shot(screen, red, x1, y1, player_size, blue, x2, y2, enemy_size, enemy_shot_position_x, enemy_shot_position_y, enemy_shot_size, background_colour, kills_by_player, speed)
				if Enemy_shot_check:
					shots_on_player +=1
				screen.fill(background_colour)
				kills_by_enemy = Font.render(str(shots_on_player), 1, white)	
				screen.blit(kills_by_enemy, (50,150))
				pygame.display.update()
		elif event.type == pygame.QUIT:
			sys.exit()

	while shots_on_player >= 6:
		screen.fill(background_colour)
		blue_won_text = Font.render(str("blue won, press any key to restart"), 2, white)	
		screen.blit(blue_won_text, (200,300))	
		pygame.display.update()	
		time.sleep(1)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:	
				if pygame.key != pygame.K_r:
					shots_on_enemy = 0
					shots_on_player = 0
					speed = 0
			elif event.type == pygame.QUIT:
				sys.exit()					
	while shots_on_enemy >= 6:
		screen.fill(background_colour)
		red_won_text = Font.render(str("red won, press any key to restart"), 2, white)	
		screen.blit(red_won_text, (200,300))	
		pygame.display.update()	
		time.sleep(1)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if pygame.key != pygame.K_r:
					shots_on_enemy = 0
					shots_on_player = 0	
					speed = 0				
			elif event.type == pygame.QUIT:
				sys.exit()	
	while speed == 0:
		pick_level = Font.render(str("what level do you choose:1/2/3/4"), 1, white)	
		screen.blit(pick_level, (200,300))	
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					speed = speed1
					screen.fill(background_colour)
					pygame.display.update()
				if event.key == pygame.K_2:
					speed = speed2
					screen.fill(background_colour)
					pygame.display.update()
				if event.key == pygame.K_3:
					speed = speed3
					screen.fill(background_colour)
					pygame.display.update()
				if event.key == pygame.K_4:
					speed = speed4
					screen.fill(background_colour)
					pygame.display.update()
			elif event.type == pygame.QUIT:
				sys.exit()	
		screen.fill(background_colour)
		screen.blit(pick_level, (200,300))	
		pygame.display.update()
	screen.fill(background_colour)
	kills_by_enemy = Font.render(str(shots_on_player), 1, white)	
	screen.blit(kills_by_enemy, (50,150))
	kills_by_player = Font.render(str(shots_on_enemy), 1, white)
	screen.blit(kills_by_player, (50,450))
	pygame.draw.rect(screen, red, (x1, y1, player_size, player_size)) 
	pygame.draw.rect(screen, blue, (x2, y2, enemy_size, enemy_size)) 
	pygame.display.update()
	#fix when enmy shoots