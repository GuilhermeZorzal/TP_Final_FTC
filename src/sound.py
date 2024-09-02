import pygame
import os
import platform

dir = 'sound/'

def sound_game_over():
    pygame.mixer.init()

    sound = pygame.mixer.Sound(dir+"game_over.mp3")
    sound.play()
    pygame.time.wait(5000)  
    

def sound_pocao_criada():
    pygame.mixer.init()
    
    sound = pygame.mixer.Sound(dir+"pocao_criada.wav")
    sound.play()   
    pygame.time.wait(5000)  
    
def sound_add_ingrediente():
    pygame.mixer.init()
    
    sound = pygame.mixer.Sound(dir+"ingrediente.mp3")
    sound.play()   
    pygame.time.wait(4500)  
    
    
def sound_background():
    pygame.mixer.init()
    
    pygame.mixer.music.load(dir+"background.mp3")
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(-1) 
    
def stop_background_sound():
    pygame.mixer.music.stop()
    
def sound_end():
    pygame.mixer.init()
    
    sound = pygame.mixer.Sound(dir+"end.mp3")
    sound.play()   
    pygame.time.wait(8000)