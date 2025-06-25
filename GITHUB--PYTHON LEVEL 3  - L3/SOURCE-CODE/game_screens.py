import pygame
import assets
import classes

def show_start_screen():
    running = True
    started = False
    clock = pygame.time.Clock()

    while not started and running:
        assets.screen.blit(assets.start_screen, (0,0))
        start_button=pygame.Rect(340, 490, 210, 60) # Creating a Rect at position of START button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(pygame.mouse.get_pos()):
                    return True, True

        pygame.display.update()
        clock.tick(60)
    return False, False

def show_main_menu():
    running = True
    clock = pygame.time.Clock()

    quick = classes.Button(240, 150, 200, 60, "Quick")
    basic = classes.Button(460, 150, 200, 60, "Basic")
    quitb = classes.Button(350, 500, 200, 60, "Quit", normal_color=(238,75,43), hover_color=(150,0,0))

    player1_box = classes.InputBox(300, 290, 300, 50)
    player2_box = classes.InputBox(300, 400, 300, 50)
    mode = None

    while running and mode is None:
        assets.screen.blit(assets.bgimg, (0,0))

        title = assets.title_font.render("Choose Game Mode!", True, (255,255,0))
        assets.screen.blit(title, (450 - title.get_width()//2, 40))

        settler1 = assets.textbox_font.render("Settler 1:", True, (255,255,255))
        assets.screen.blit(settler1, (450 - settler1.get_width()//2, 250))
        settler2 = assets.textbox_font.render("Settler 2:", True, (255,255,255))
        assets.screen.blit(settler2, (450 - settler2.get_width()//2, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None, None, None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quick.is_clicked(event.pos): 
                    mode = "quick"
                if basic.is_clicked(event.pos): 
                    mode = "basic"

                if quitb.is_clicked(event.pos): 
                    return None, None, None

                if mode:
                    n1, n2 = player1_box.text.strip(), player2_box.text.strip()
                    if n1 == "" or n2 == "":
                        mode = None
                    else:
                        return mode, n1, n2

            player1_box.handle_event(event)
            player2_box.handle_event(event)

        quick.draw(assets.screen)
        basic.draw(assets.screen)
        quitb.draw(assets.screen)
        player1_box.draw(assets.screen)
        player2_box.draw(assets.screen)

        pygame.display.update()
        clock.tick(60)

def game_over_screen(winner, mode):
    clock = pygame.time.Clock()
    main_menu_button = classes.Button(350, 300, 200, 60, "Main Menu")
    regame_button = classes.Button(350, 400, 200, 60, "Regame")
    quit_button = classes.Button(350, 500, 200, 60, "Quit", normal_color=(238,75,43), hover_color=(150,0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.is_clicked(event.pos):
                    return True, None
                elif regame_button.is_clicked(event.pos):
                    return True, mode
                elif quit_button.is_clicked(event.pos):
                    return False, None
        
        assets.screen.blit(assets.bgimg, (0,0))
        text = assets.title_font.render(f"{winner} Wins!", True, (255, 255, 0))
        assets.screen.blit(text, (450 - text.get_width()//2, 150))

        main_menu_button.draw(assets.screen)
        regame_button.draw(assets.screen)
        quit_button.draw(assets.screen)

        pygame.display.update()
        clock.tick(60)

def show_quick_info():
    clock = pygame.time.Clock()
    showing = True

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

def show_info_screen(mode):
    clock = pygame.time.Clock()
    running = True
    showing = True
    
    if mode == 'quick':
        img = pygame.image.load("media/info_quick.png")
    elif mode == 'basic':
        img = pygame.image.load("media/info_basic.png")
    
    while running and showing:
        assets.screen.blit(assets.bgimg, (0,0))        
        assets.screen.blit(img, (450-img.get_width()//2, 40))
        start = classes.Button(350, 500, 200, 60, "Start")
        start.draw(assets.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.is_clicked(event.pos): 
                    showing = False            
        
        pygame.display.update()
        clock.tick(60)

    return running