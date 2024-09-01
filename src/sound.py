import pygame

def sound_game_over():
    pygame.mixer.init()

    sound = pygame.mixer.Sound("sound/game_over.mp3")
    sound.play()
    pygame.time.wait(5000)  # Espera 2 segundos para garantir que os sons sejam ouvidos
    

def sound_pocao_criada():
    pygame.mixer.init()
    
    sound = pygame.mixer.Sound("sound/pocao_criada.wav")
    sound.play()   
    pygame.time.wait(2000)  # Espera 2 segundos para garantir que os sons sejam ouvidos
    
def sound_add_ingrediente():
    pygame.mixer.init()
    
    sound = pygame.mixer.Sound("sound/ingrediente.mp3")
    sound.play()   
    pygame.time.wait(2000)  # Espera 2 segundos para garantir que os sons sejam ouvidos
    
    
def sound_background():
    pygame.mixer.init()
    
    pygame.mixer.music.load("sound/background.mp3")
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume da música
    pygame.mixer.music.play(-1) 
    
def stop_background_sound():
    pygame.mixer.music.stop()