from cx_Freeze import setup, Executable
import pygame
from random import randint
import sys

build_exe_options = {
    "packages": ["pygame","random","sys"],
    "include_files": ["brique.png", "pilier.png", "bombe.png", "explosion.png", "joueur1.png", "joueur2.png", "boom.wav","game-over.wav","drop.wav"],
}

base = None

executables = [Executable("Projet-Bomberman-pygame.py", base=base, icon="icone.ico")]

setup(
    name="Projet-Bomberman",
    version="1.0",
    description="Jeu de NSI",
    options={"build_exe": build_exe_options},
    executables=executables
)
