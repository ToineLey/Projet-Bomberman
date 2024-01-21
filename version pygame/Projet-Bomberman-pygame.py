import pygame
from random import randint
import sys

# crée une clock pour que le jeu reste à 30 fps

clock = pygame.time.Clock()

# Définir les constantes pour les couleurs
BG = (30, 128, 30)
BG2 = (30, 30, 128)
# Initialiser Pygame
pygame.init()

# Charger les images pour les textures
BRICK_IMAGE = pygame.image.load("brique.png")
PILLAR_IMAGE = pygame.image.load("pilier.png")
PLAYER1_IMAGE = pygame.image.load("joueur1.png")
PLAYER2_IMAGE = pygame.image.load("joueur2.png")
EXPLOSION_IMAGE = pygame.image.load("explosion.png")
BOMB_IMAGE = pygame.image.load("bombe.png")


class Bomb:
    portee = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 60

    def rebour(self):
        self.timer -= 1


class Bomber:
    def __init__(self, name, x, y, grille):
        self.grille = grille

        self.x = x
        self.y = y
        self.username = name
        self.dead = False
        self.cool_down = 0  # temps avant de pouvoir poser une bombe
        self.grille.cases[y][x].player = self

        self.slow = 0  # nombre de frames avant le prochain deplacement possible

    def dropbomb(self):
        """pose une bombe, si possible, sous ses pied"""
        if self.cool_down == 0 and self.grille.cases[self.y][self.x].bomb is None:
            bombb = Bomb(self.x, self.y)
            self.grille.cases[self.y][self.x].bomb = bombb
            self.cool_down += 120
            self.grille.all_bombs.append(bombb)

    def goto(self, x, y):
        """deplace le joueur aux coordonnées x,y"""
        self.x = x
        self.y = y
        self.grille.cases[y][x].player = self

    def gauche(self):
        """deplace le joueur vers la gauche si possible"""
        x = self.x - 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def droite(self):
        """deplace le joueur vers la droite si possible"""
        x = self.x + 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def haut(self):
        """deplace le joueur vers le haut si possible"""
        x = self.x
        y = self.y - 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def bas(self):
        """deplace le joueur vers le bas si possible"""
        x = self.x
        y = self.y + 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def deplacement(self, h, b, d, g):
        """gère les deplacements, si une des touche en argument est pressée"""
        if self.slow == 0:
            keys = pygame.key.get_pressed()
            if keys[h]:
                self.haut()
                self.slow = 10
            elif keys[b]:
                self.bas()
                self.slow = 10
            elif keys[d]:
                self.droite()
                self.slow = 10
            elif keys[g]:
                self.gauche()
                self.slow = 10

    def update_slow(self):
        """permet le ralentissement des déplacements, sinon instantanés"""
        if self.slow > 0:
            self.slow -= 1


class Terrain:
    LISTE = (0, 1, 2)
    VIDE = 0
    BRIQUE = 1
    PILIER = 2


class Case:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.terrain = t
        self.bomb = None
        self.explosion = 0
        self.player = None

    def explode(self):
        """gère l'explosion de la case"""
        if self.terrain == Terrain.BRIQUE:
            self.terrain = Terrain.VIDE
        elif self.player is not None:
            self.player.dead = True
        self.bomb = None
        self.explosion -= 1

    def est_libre(self):
        """teste si la case est vide et qu'il n'y a pas de joueur"""
        return self.terrain == Terrain.VIDE and self.player is None

    def __str__(self):
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0 and self.player is None and self.bomb is None and self.explosion == 0:
            return '  '
        elif self.terrain == 2:
            return '██'
        elif self.bomb is not None:
            return '!!'
        elif self.player is not None:
            return '()'
        elif self.explosion != 0:
            return '**'


class Grille:
    def __init__(self, l: int, h: int):
        self.hauteur = h
        self.largeur = l
        self.cases = [[j for j in range(l+2)] for _ in range(h+2)]
        self.exploding_bombs = []
        self.all_bombs = []

    def remplir_niveau(self, niveau):
        if niveau == 1:
            """cette méthode sert à remplir la grille de jeu pour que cela soit le niveau 1"""
            hauteur = self.hauteur+2
            largeur = self.largeur+2

            def espacement_piliers():
                return (
                    x not in (1, largeur-2) and
                    y not in (1, hauteur-2) and
                    y % 2 == 0 and
                    x % 2 == 0
                )

            def depart1():
                return (
                    y in (1, 2) and
                    x in (1, 2)
                )
            
            def depart2():
                return (
                    y in (hauteur-3, hauteur-2) and
                    x in (largeur-3, largeur-2)
                )

            def contour():
                return (
                    x in (0, largeur-1) or
                    y in (0, hauteur-1)
                )

            for y in range(len(self.cases)):
                for x in range(len(self.cases[y])):
                    alea = randint(1, 100)
                    if contour():
                        self.cases[y][x] = Case(y, x, Terrain.PILIER)
                    elif espacement_piliers():
                        self.cases[y][x] = Case(y, x, Terrain.PILIER)
                    elif depart1():
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    elif depart2():
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    else:
                        if alea <= 20:
                            self.cases[y][x] = Case(y, x, Terrain.VIDE)
                        else:
                            self.cases[y][x] = Case(y, x, Terrain.BRIQUE)
        elif niveau == 2:
            """cette méthode sert à remplir la grille de jeu pour que cela soit le niveau 2"""
            hauteur = self.hauteur+2
            largeur = self.largeur+2

            def espacement_piliers():
                return (
                    x not in (1, largeur-2) and
                    y not in (1, hauteur-2) and
                    y % 2 == 0 and
                    x % 2 == 0
                )

            def depart1():
                return (
                    y in (5, 4, 6) and
                    x in (3, 2, 4)
                )
            
            def depart2():
                return (
                    y in (hauteur-6, hauteur-5, hauteur-7) and
                    x in (largeur-3, largeur-4, largeur-5)
                )

            def contour():
                return (
                    x in (0, largeur-1) or
                    y in (0, hauteur-1)
                )

            for y in range(len(self.cases)):
                for x in range(len(self.cases[y])):
                    alea = randint(1, 100)
                    if contour():
                        self.cases[y][x] = Case(y, x, Terrain.PILIER)
                    elif espacement_piliers():
                        self.cases[y][x] = Case(y, x, Terrain.PILIER)
                    elif depart1():
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    elif depart2():
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    else:
                        if alea <= 50:
                            self.cases[y][x] = Case(y, x, Terrain.VIDE)
                        else:
                            self.cases[y][x] = Case(y, x, Terrain.BRIQUE)

    def _affichage(self):
        t2 = []
        for a in range(len(self.cases)):
            t1 = []
            for el in self.cases[a]:
                t1.append(str(el))
            t2.append(t1)
        return t2

    def get(self, x: int, y: int):
        return self.cases[y][x]

    def get_explosions(self) -> list:
        c = []
        for a in range(len(self.cases)):
            for el in self.cases[a]:
                if el.explosion != 0:
                    c.append(el)
        return c

    def update_bomb(self):
        for bomb in self.all_bombs:
            bomb.rebour()
            if bomb.timer == 0:
                self.exploding_bombs.append(bomb)

    def update_explosions(self, x, y):
        case = self.get(x, y)
        case.explosion = 15

        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y+i)
            current_case.explosion = 15
            if current_case.bomb is not None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER or current_case.terrain == Terrain.BRIQUE:
                break
            i += 1

        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y-i)
            current_case.explosion = 15
            if current_case.bomb is not None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER or current_case.terrain == Terrain.BRIQUE:
                break
            i += 1

        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x+i, y)
            current_case.explosion = 15
            if current_case.bomb is not None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER or current_case.terrain == Terrain.BRIQUE:
                break
            i += 1

        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x-i, y)
            current_case.explosion = 15
            if current_case.bomb is not None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER or current_case.terrain == Terrain.BRIQUE:
                break
            i += 1

    def bombs_explosion(self):
        for bomb in self.exploding_bombs:
            self.update_explosions(bomb.x, bomb.y)

    def explosions(self):
        for case in self.get_explosions():
            case.explode()
        for bomb in self.exploding_bombs:
            self.all_bombs.remove(bomb)
        self.exploding_bombs = []

    def manage_bombs(self):
        self.update_bomb()
        self.bombs_explosion()
        self.explosions()


LARGEUR_SPRITE = 64
HAUTEUR = 13
LARGEUR = 11


class Jeu:
    def __init__(self,selected_level,menu):
        self.menu = menu
        self.clock = pygame.time.Clock()
        self.level = selected_level
        self.screen = pygame.display.set_mode(
            ((HAUTEUR+2)*LARGEUR_SPRITE, (LARGEUR+2)*LARGEUR_SPRITE))
        pygame.display.set_caption("Bomberman")
        self.fin_de_partie = False
        self.grille = Grille(HAUTEUR, LARGEUR)
        self.grille.remplir_niveau(selected_level)
        if selected_level==1:
            self.player1 = Bomber('player1', 1, 1, self.grille)
            self.player2 = Bomber('player2', HAUTEUR, LARGEUR, self.grille)
        elif selected_level==2:
            self.player1 = Bomber('player1', 3, 5, self.grille)
            self.player2 = Bomber('player2', HAUTEUR-2, LARGEUR-4, self.grille)
        self.boom_sound = pygame.mixer.Sound("boom.wav")
        self.drop_sound = pygame.mixer.Sound("drop.wav")
        self.game_over_sound = pygame.mixer.Sound("game-over.wav")

        pygame.mixer.music.set_volume(0.2)
        self.run()

    def select_level(self):
        self.fin_de_partie = False
        self.level = self.menu.run()
        self.grille = Grille(HAUTEUR, LARGEUR)
        self.grille.remplir_niveau(self.level)
        if self.level == 1:
            self.player1 = Bomber('player1', 1, 1, self.grille)
            self.player2 = Bomber('player2', HAUTEUR, LARGEUR, self.grille)
        elif self.level == 2:
            self.player1 = Bomber('player1', 3, 5, self.grille)
            self.player2 = Bomber('player2', HAUTEUR-2, LARGEUR-4, self.grille)
        self.run()

    def restart_game(self):
        self.fin_de_partie = False
        self.grille = Grille(HAUTEUR, LARGEUR)
        self.grille.remplir_niveau(self.level)
        if self.level == 1:
            self.player1 = Bomber('player1', 1, 1, self.grille)
            self.player2 = Bomber('player2', HAUTEUR, LARGEUR, self.grille)
        elif self.level == 2:
            self.player1 = Bomber('player1', 3, 5, self.grille)
            self.player2 = Bomber('player2', HAUTEUR-2, LARGEUR-4, self.grille)
        self.run()

    def draw_end_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)

        if self.fin_de_partie == 2:
            message = 'PLAYER 2 WINS'
        elif self.fin_de_partie == 1:
            message = 'PLAYER 1 WINS'
        else:
            message = "  GAME OVER  "

        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

        pygame.time.delay(1500)

        # Revenir au menu après la fin de la partie
        self.fin_de_partie = False

        self.menu.run()

    def run(self):
        while not self.fin_de_partie:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin_de_partie = True

            self.player1.update_slow()
            self.player2.update_slow()

            self.player1.deplacement(
                pygame.K_z, pygame.K_s, pygame.K_d, pygame.K_q)
            self.player2.deplacement(
                pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)

            if pygame.key.get_pressed()[pygame.K_e]:
                self.drop_sound.play()
                self.player1.dropbomb()

            if pygame.key.get_pressed()[pygame.K_KP1] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                self.drop_sound.play()
                self.player2.dropbomb()

            self.grille.manage_bombs()

            if self.player1.cool_down > 0:
                self.player1.cool_down -= 1

            if self.player2.cool_down > 0:
                self.player2.cool_down -= 1

            if self.player1.dead:
                self.fin_de_partie = 2

            if self.player2.dead:
                self.fin_de_partie = 1

            if self.player2.dead and self.player1.dead:
                self.fin_de_partie = 3

            self.draw()

            if self.fin_de_partie:
                self.game_over_sound.play()
                self.draw_end_screen()

            self.clock.tick(60)

        pygame.quit()

    def draw(self):
        if self.level == 1:
            self.screen.fill(BG)
        elif self.level == 2:
            self.screen.fill(BG2)

        for h in range(len(self.grille.cases)):
            for l in range(len(self.grille.cases[h-1])):
                casee = self.grille.cases[h][l]
                rect = pygame.Rect(
                    l * LARGEUR_SPRITE, h * LARGEUR_SPRITE, LARGEUR_SPRITE, LARGEUR_SPRITE)

                if casee.terrain == 1:
                    self.screen.blit(BRICK_IMAGE, rect)
                elif casee.terrain == 2:
                    self.screen.blit(PILLAR_IMAGE, rect)
                elif casee.player == self.player1:
                    self.screen.blit(PLAYER1_IMAGE, rect)
                elif casee.player == self.player2:
                    self.screen.blit(PLAYER2_IMAGE, rect)
                elif casee.explosion != 0:
                    self.boom_sound.play()
                    self.screen.blit(EXPLOSION_IMAGE, rect)
                elif casee.bomb is not None:
                    self.screen.blit(BOMB_IMAGE, rect)

        pygame.display.flip()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.menu_options = ["Start Game", "Choose Level", "Quit"]
        self.selected_option = 0
        self.selected_level = 1  # Default level is 1
        self.level_selection_active = False

    def draw(self):
        self.screen.fill((32, 32, 32))

        options = self.menu_options
        if self.level_selection_active:
            options = [f"Level: {self.selected_level}"] + options

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, (i + 1) * 50))
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.level_selection_active:
                        if event.key == pygame.K_UP:
                            self.selected_level = max(1, self.selected_level - 1)
                        elif event.key == pygame.K_DOWN:
                            self.selected_level = min(2, self.selected_level + 1)
                        elif event.key == pygame.K_RETURN:
                            self.level_selection_active = False
                    else:
                        if event.key == pygame.K_UP:
                            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                        elif event.key == pygame.K_DOWN:
                            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                        elif event.key == pygame.K_RETURN:
                            if self.selected_option == 0:
                                return self.selected_level  # Start the game
                            elif self.selected_option == 1:
                                self.level_selection_active = True
                            elif self.selected_option == 2:
                                pygame.quit()
                                sys.exit()
                            elif self.selected_option == 3:
                                return "Restart Game"

            self.draw()
            self.clock.tick(30)

# ... (Your existing code)

# Code to start the game
pygame.init()
screen = pygame.display.set_mode(((HAUTEUR+2)*LARGEUR_SPRITE, (LARGEUR+2)*LARGEUR_SPRITE))
pygame.display.set_caption("Bomberman")

menu = Menu(screen)
selected_level = menu.run()  # Wait for the user to choose "Start Game" or "Quit"

if selected_level is not None:
    jeu = Jeu(selected_level, menu)
    while True:
        option = menu.run()
        if option == "Restart Game":
            selected_level = jeu.restart_game()
        else:
            break