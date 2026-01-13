import pygame,sys,scorecalcfunctions as scorecalc
from pathlib import Path

# Get folder where the script resides
BASE_DIR = Path(__file__).parent

output_dir = BASE_DIR / 'output'
output_dir.mkdir(exist_ok=True)

font_dir = BASE_DIR / 'Fonts'
font_dir.mkdir(exist_ok=True)

score_h_file = output_dir / 'Score (H).txt'
score_a_file = output_dir / 'Score (A).txt'
racecount_file = output_dir / 'racecount.txt'
light_font_file = font_dir /  'IBMPlexSans-Light.ttf'
bold_font_file = font_dir / 'IBMPlexSans-Bold.ttf'

#STILL TO BE DONE:
# Show current text
# Confirm button to input all text values
# Update race count automatically
# Show points score by each team
# Text boxes for penalties

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([640,720])

#font initialization
# font initialization with pathlib (cross-platform)
base_font = pygame.font.Font(str(light_font_file), 14)
unedited_font = pygame.font.Font(str(bold_font_file), 12)
title_font = pygame.font.Font(str(bold_font_file), 20)
button_font = pygame.font.Font(str(bold_font_file), 20)
scoreboard_font = pygame.font.Font(str(bold_font_file), 25)


#variable initialization
race_count = 1 #Shows what race it should be
race_results = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

# color initializaiton
color_passive = pygame.Color('grey80')
color_active = pygame.Color('blue')
button_active = pygame.Color('forestgreen')
manual_active = pygame.Color('orange')
reset_button_active = pygame.Color('red')

#enter inputs button
check_button_input_active = False
check_button_input_user_text = 'CHECK'
check_button_input_rect = pygame.Rect(10,230,50,30)
check_button_input_color = color_passive
check_button_output = ['','','','','','','','']

#confirm inputs button
confirm_manual_button_input_active = False
confirm_manual_button_input_user_text = 'CONFIRM'
confirm_manual_button_input_rect = pygame.Rect(10,600,60,30)
confirm_manual_button_input_color = color_passive

#confirm inputs button
confirm_button_input_active = False
confirm_button_input_user_text = 'CONFIRM'
confirm_button_input_rect = pygame.Rect(10,440,60,30)
confirm_button_input_color = color_passive

#reset inputs button
reset_button_input_active = False
reset_button_input_user_text = 'RESET'
reset_button_input_rect = pygame.Rect(10,650,60,30)
reset_button_input_color = color_passive

#home team initialization
home_team_spots_active = False
home_team_spots_user_text = ''
home_team_spots_input_rect = pygame.Rect(10,50,150,24)
home_team_spots_color = color_passive

#away team initialization
home_team_penalty_active = False
home_team_penalty_user_text = ''
home_team_penalty_input_rect = pygame.Rect(10,100,150,24)
home_team_penalty_color = color_passive

#awayteampen intialization
away_team_penalty_active = False
away_team_penalty_user_text = ''
away_team_penalty_input_rect = pygame.Rect(10,150,150,24)
away_team_penalty_color = color_passive

#race count intialization
race_count_active = False
race_count_user_text = str(race_count)
race_count_input_rect = pygame.Rect(10,200,150,24)
race_count_color = color_passive

#home team score initialization
home_team_score_active = False
home_team_score_user_text = ''
home_team_score_input_rect = pygame.Rect(10,500,150,24)
home_team_score_color = color_passive

#away team score initialization
away_team_score_active = False
away_team_score_user_text = ''
away_team_score_input_rect = pygame.Rect(10,550,150,24)
away_team_score_color = color_passive


while True:
    #variable initialization within loop
    home_team_score = scorecalc.status()[0]
    away_team_score = scorecalc.status()[1]
    race_count_text = scorecalc.status()[2]

    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                home_team_score_active = False
                away_team_score_active = False
                home_team_spots_active = False
                home_team_penalty_active = False
                away_team_penalty_active = False
                race_count_active = False
                check_button_input_active = False
                confirm_button_input_active = False
                confirm_manual_button_input_active = False
                reset_button_input_active = False
                if home_team_score_input_rect.collidepoint(event.pos):
                    home_team_score_active = True
                if away_team_score_input_rect.collidepoint(event.pos):
                    away_team_score_active = True
                if home_team_spots_input_rect.collidepoint(event.pos):
                    home_team_spots_active = True
                if home_team_penalty_input_rect.collidepoint(event.pos):
                    home_team_penalty_active = True
                if away_team_penalty_input_rect.collidepoint(event.pos):
                    away_team_penalty_active = True
                if race_count_input_rect.collidepoint(event.pos):
                    race_count_active = True
                if check_button_input_rect.collidepoint(event.pos):
                    check_button_input_active = True
                    check_button_output = scorecalc.results(home_team_spots_user_text,home_team_penalty_user_text,away_team_penalty_user_text)
                if confirm_button_input_rect.collidepoint(event.pos):
                    confirm_button_input_active = True
                    #this code will need an if statement for when scores need to be typed in manually
                    score_h_file.write_text(str(check_button_output[6]))
                    score_a_file.write_text(str(check_button_output[7]))
                    race_count = int(race_count_user_text)
                    race_results[race_count-1] = [check_button_output[0],check_button_output[1]]
                    if race_count < 12:
                            race_count += 1
                            racecount_file.write_text(f'Race {str(race_count)}')

                    home_team_spots_user_text = ''
                    home_team_penalty_user_text = '0'
                    away_team_penalty_user_text = '0'
                    race_count_user_text = str(race_count)
                    check_button_output = ['', '', '', '', '', '', '', '']
                if confirm_manual_button_input_rect.collidepoint(event.pos):
                    if (home_team_score_user_text != '0' or '') and (away_team_score_user_text != '0' or ''):
                        confirm_manual_button_input_active = True
                        #this code will need an if statement for when scores need to be typed in manually
                        score_h_file.write_text(str(home_team_score_user_text))
                        score_a_file.write_text(str(away_team_score_user_text))
                        race_count = int(race_count_user_text)
                        if race_count < 12:
                            race_count += 1
                            racecount_file.write_text(f'Race {str(race_count)}')

                        home_team_spots_user_text = ''
                        home_team_penalty_user_text = '0'
                        away_team_penalty_user_text = '0'
                        race_count_user_text = str(race_count)
                        check_button_output = ['', '', '', '', '', '', '', '']
                if reset_button_input_rect.collidepoint(event.pos):
                    scorecalc.reset()
                    reset_button_input_active = True
                    home_team_spots_user_text = ''
                    home_team_score_user_text = ''
                    away_team_score_user_text = ''
                    home_team_penalty_user_text = '0'
                    away_team_penalty_user_text = '0'
                    race_count = 1
                    race_count_user_text = '1'
                    check_button_output = ['', '', '', '', '', '', '', '']
                    race_results = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

        if event.type == pygame.KEYDOWN:
            if home_team_score_active:
                if event.key == pygame.K_BACKSPACE:
                    home_team_score_user_text = home_team_score_user_text[:-1]
                else:
                    home_team_score_user_text += event.unicode
            if away_team_score_active:
                if event.key == pygame.K_BACKSPACE:
                    away_team_score_user_text = away_team_score_user_text[:-1]
                else:
                    away_team_score_user_text += event.unicode
            if home_team_spots_active:
                if event.key == pygame.K_BACKSPACE:
                    home_team_spots_user_text = home_team_spots_user_text[:-1]
                else:
                    home_team_spots_user_text += event.unicode
            if home_team_penalty_active:
                if event.key == pygame.K_BACKSPACE:
                    home_team_penalty_user_text = home_team_penalty_user_text[:-1]
                else:
                    home_team_penalty_user_text += event.unicode
            if away_team_penalty_active:
                if event.key == pygame.K_BACKSPACE:
                    away_team_penalty_user_text = away_team_penalty_user_text[:-1]
                else:
                    away_team_penalty_user_text += event.unicode
            if race_count_active:
                if event.key == pygame.K_BACKSPACE:
                    race_count_user_text = race_count_user_text[:-1]
                else:
                    race_count_user_text += event.unicode


    #BAR ON TOP
    pygame.draw.rect(screen, pygame.Color('floralwhite'), pygame.Rect(0,0,640,28), 0)
    pygame.draw.rect(screen, pygame.Color('grey1'), pygame.Rect(0, 0, 640, 28), 2)

    # DRAWING ENTER BUTTON
    pygame.draw.rect(screen,check_button_input_color,check_button_input_rect,2)
    check_button_input_text_surface = button_font.render(check_button_input_user_text, True,(0,0,0))
    screen.blit(check_button_input_text_surface,(check_button_input_rect.x+10,check_button_input_rect.y))
    check_button_input_rect.w = max(check_button_input_text_surface.get_width()+20,30)
    if check_button_input_rect.collidepoint(pygame.mouse.get_pos()):
        check_button_input_color = button_active
    else:
        check_button_input_color = color_passive

    # DRAWING CONFIRM BUTTON
    pygame.draw.rect(screen,confirm_button_input_color,confirm_button_input_rect,2)
    confirm_button_input_text_surface = button_font.render(confirm_button_input_user_text, True,(0,0,0))
    screen.blit(confirm_button_input_text_surface,(confirm_button_input_rect.x+10,confirm_button_input_rect.y))
    confirm_button_input_rect.w = max(confirm_button_input_text_surface.get_width()+20,30)
    if confirm_button_input_rect.collidepoint(pygame.mouse.get_pos()):
        confirm_button_input_color = button_active
    else:
        confirm_button_input_color = color_passive
    if confirm_button_input_active:
        screen.blit(unedited_font.render(f'All Values Have Been Entered!', True, (0, 0, 0)),
                    (10, 470))

    # DRAWING CONFIRM MANUAL BUTTON
    pygame.draw.rect(screen,confirm_manual_button_input_color,confirm_manual_button_input_rect,2)
    confirm_manual_button_input_text_surface = button_font.render(confirm_manual_button_input_user_text, True,(0,0,0))
    screen.blit(confirm_manual_button_input_text_surface,(confirm_manual_button_input_rect.x+10,confirm_manual_button_input_rect.y))
    confirm_manual_button_input_rect.w = max(confirm_manual_button_input_text_surface.get_width()+20,30)
    if confirm_manual_button_input_rect.collidepoint(pygame.mouse.get_pos()):
        confirm_manual_button_input_color = manual_active
    else:
        confirm_manual_button_input_color = color_passive
    if confirm_manual_button_input_active:
        screen.blit(unedited_font.render(f'All Values Have Been Entered!', True, (0, 0, 0)),
                    (10, 580))

    # DRAWING RESET BUTTON
    pygame.draw.rect(screen,reset_button_input_color,reset_button_input_rect,2)
    reset_button_input_text_surface = button_font.render(reset_button_input_user_text, True,(0,0,0))
    screen.blit(reset_button_input_text_surface,(reset_button_input_rect.x+10,reset_button_input_rect.y))
    reset_button_input_rect.w = max(reset_button_input_text_surface.get_width()+20,30)
    if reset_button_input_rect.collidepoint(pygame.mouse.get_pos()):
        reset_button_input_color = reset_button_active
    else:
        reset_button_input_color = color_passive
    if reset_button_input_active:
        screen.blit(unedited_font.render(f'All Values Have Been Reset!', True, (0, 0, 0)),
                    (10, 630))

    #INPUTS FOR THE HOME SCORE BOX
    pygame.draw.rect(screen,home_team_score_color,home_team_score_input_rect,2)
    home_team_score_text_surface = base_font.render(home_team_score_user_text + " |", True,(0,0,0))
    screen.blit(home_team_score_text_surface,(home_team_score_input_rect.x+10,home_team_score_input_rect.y+3))
    home_team_score_input_rect.w = max(home_team_score_text_surface.get_width()+25,200)
    if home_team_score_active:
        home_team_score_color = color_active
    else:
        home_team_score_color = color_passive

    #INPUTS FOR THE AWAY SCORE BOX
    pygame.draw.rect(screen,away_team_score_color,away_team_score_input_rect,2)
    away_team_score_text_surface = base_font.render(away_team_score_user_text + " |", True,(0,0,0))
    screen.blit(away_team_score_text_surface,(away_team_score_input_rect.x+10,away_team_score_input_rect.y+3))
    away_team_score_input_rect.w = max(away_team_score_text_surface.get_width()+25,200)
    if away_team_score_active:
        away_team_score_color = color_active
    else:
        away_team_score_color = color_passive

    #INPUTS FOR THE HOME BOX
    pygame.draw.rect(screen,home_team_spots_color,home_team_spots_input_rect,2)
    home_team_spots_text_surface = base_font.render(home_team_spots_user_text + " |", True,(0,0,0))
    screen.blit(home_team_spots_text_surface,(home_team_spots_input_rect.x+10,home_team_spots_input_rect.y+3))
    home_team_spots_input_rect.w = max(home_team_spots_text_surface.get_width()+25,200)
    if home_team_spots_active:
        home_team_spots_color = color_active
    else:
        home_team_spots_color = color_passive

    #INPUTS FOR THE HOME TEAM PEN BOX
    pygame.draw.rect(screen,home_team_penalty_color,home_team_penalty_input_rect,2)
    home_team_penalty_text_surface = base_font.render(home_team_penalty_user_text + " |", True,(0,0,0))
    screen.blit(home_team_penalty_text_surface,(home_team_penalty_input_rect.x+10,home_team_penalty_input_rect.y+3))
    home_team_penalty_input_rect.w = max(home_team_penalty_text_surface.get_width()+25,200)
    if home_team_penalty_active:
        home_team_penalty_color = color_active
    else:
        home_team_penalty_color = color_passive

    #INPUTS FOR THE AWAY TEAM PEN BOX
    pygame.draw.rect(screen,away_team_penalty_color,away_team_penalty_input_rect,2)
    away_team_penalty_text_surface = base_font.render(away_team_penalty_user_text + " |", True,(0,0,0))
    screen.blit(away_team_penalty_text_surface,(away_team_penalty_input_rect.x+10,away_team_penalty_input_rect.y+3))
    away_team_penalty_input_rect.w = max(away_team_penalty_text_surface.get_width()+25,200)
    if away_team_penalty_active:
        away_team_penalty_color = color_active
    else:
        away_team_penalty_color = color_passive

    #INPUTS FOR THE RACE COUNT BOX
    pygame.draw.rect(screen,race_count_color,race_count_input_rect,2)
    race_count_text_surface = base_font.render(race_count_user_text + " |", True,(0,0,0))
    screen.blit(race_count_text_surface,(race_count_input_rect.x+10,race_count_input_rect.y+3))
    race_count_input_rect.w = max(race_count_text_surface.get_width()+20,30)
    if race_count_active:
        race_count_color = color_active
    else:
        race_count_color = color_passive

    #Constant Text Lines
    screen.blit(title_font.render('Lawrence\'s Stream Hosting Score Tracker', True, (0, 0, 0)),(120,0)) # Top Bar
    screen.blit(unedited_font.render('Insert home team placements for race:', True,(0,0,0)), (home_team_spots_input_rect.x,home_team_spots_input_rect.y-15)) #covers home_team_spots_user_text
    screen.blit(unedited_font.render('Insert home team score: (Manual)', True, (0, 0, 0)),
                (home_team_score_input_rect.x, home_team_score_input_rect.y - 15))  # covers home_team_score_user_text
    screen.blit(unedited_font.render('Insert away team score: (Manual)', True, (0, 0, 0)),
                (away_team_score_input_rect.x, away_team_score_input_rect.y - 15))  # covers away_team_score_user_text
    screen.blit(unedited_font.render('Insert home team penalties for race:', True, (0, 0, 0)), (home_team_penalty_input_rect.x,home_team_penalty_input_rect.y-15)) #covers home_team_penalty_user_text
    screen.blit(unedited_font.render('Insert away team penalties for race:', True, (0, 0, 0)), (
    away_team_penalty_input_rect.x, away_team_penalty_input_rect.y - 15))  # covers home_team_penalty_user_text
    screen.blit(unedited_font.render('Insert Current Race:', True, (0, 0, 0)),(race_count_input_rect.x, race_count_input_rect.y - 15))  # covers race_count_user_text
    screen.blit(unedited_font.render(f'Home Team Race Score: {check_button_output[0]}', True, (0, 0, 0)),(10,270))
    screen.blit(unedited_font.render(f'Away Team Race Score: {check_button_output[1]}', True, (0, 0, 0)), (10, 290))
    screen.blit(unedited_font.render(f'Home Team Spots: {check_button_output[2]}', True, (0, 0, 0)), (10, 310))
    screen.blit(unedited_font.render(f'Away Team Spots: {check_button_output[3]}', True, (0, 0, 0)), (10, 330))
    screen.blit(unedited_font.render(f'Home Team Penalty: {check_button_output[4]}', True, (0, 0, 0)), (10, 350))
    screen.blit(unedited_font.render(f'Away Team Penalty: {check_button_output[5]}', True, (0, 0, 0)), (10, 370))
    screen.blit(unedited_font.render(f'Home Team Total Score: {check_button_output[6]}', True, (0, 0, 0)), (10, 390))
    screen.blit(unedited_font.render(f'Away Team Total Score: {check_button_output[7]}', True, (0, 0, 0)), (10, 410))
    screen.blit(scoreboard_font.render(f'Current Score', True, (0, 0, 0)), (330, 30))
    screen.blit(title_font.render(f'| Home Team | {home_team_score} - {away_team_score} | Away Team |', True, (0, 0, 0)), (250, 60))
    screen.blit(title_font.render(f'{race_count_text}', True, (0, 0, 0)),(390, 85))
    screen.blit(scoreboard_font.render(f'Race History', True, (0, 0, 0)), (340, 110))
    for i in range(12):
        try:
            screen.blit(title_font.render(f'| Home Team {race_results[i][0]} - {race_results[i][1]} Away Team | {int(race_results[i][0]) - int(race_results[i][1])}', True, (0, 0, 0)),(250, 140+(i*20)))
        except ValueError:
            screen.blit(title_font.render(
                f'| Home Team {race_results[i][0]} - {race_results[i][1]} Away Team |',
                True, (0, 0, 0)), (250, 140 + (i * 20)))
    pygame.display.flip()
    clock.tick(60)