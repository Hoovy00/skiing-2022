from re import X
import pygame

win = pygame.display.set_mode((1080,800))
pygame.display.set_caption("Skiing")

class Player(object):
    X = 75
    Y = 250
    WIDTH = 50
    HEIGHT = 50
    SPEED = 5

class Color(object):
    WHITE = (178, 178, 178)
    BLUE = (0, 0, 178)
    RED = (178, 0, 0)
    GREEN = (0, 178, 0)
    BACKGROUND = (125, 79, 185)

class Game(object):

    def __init__(self):
        """initializes the class"""
        pygame.init()
        self.game_objects = []

    def add_game_objects(self, *list_of_game_objects, **dict_of_game_objects):
        """ activates add_game_object """
        for game_object in list_of_game_objects:
            self.add_game_object(game_object)
        for game_object_id, game_object in dict_of_game_objects.items():
            self.add_game_object(game_object)

    def add_game_object(self, game_object):
        """appends game objects"""
        self.game_objects.append(game_object)

    def get_game_objects_with_attribute(self, attribute_name):
        """returns game objects with specific attributes"""
        return [game_object for game_object in self.game_objects if hasattr(game_object, attribute_name)]

    def draw(self):
        """used to store things that need to be drawn"""
        drawables = self.get_game_objects_with_attribute("draw")
        for drawable in drawables:
            drawable.draw()

    def handle_movement(self):
        """used to store things that need to move"""
        movables = self.get_game_objects_with_attribute("movement")
        for movable in movables:
            movable.movement()

    def handle_collisions(self):
        """used to store things that need to collide"""
        collidables = self.get_game_objects_with_attribute("handle_collisions")
        for collidable in collidables:
            collidable.handle_collisions(collidables)
        
    def loop(self):
        run = True
        while run:
            pygame.time.delay(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
            self.handle_movement()
            self.handle_collisions()

            pygame.display.update()

class Slope(object):

    def draw(self):
        win.fill(Color.BACKGROUND)

class Skier(object):

    def __init__(self):
        self.x = Player.X
        self.y = Player.Y
        self.speed = Player.SPEED
        self.finished = False

    def draw(self):
        pygame.draw.rect(win, Color.WHITE, (self.x, self.y, Player.WIDTH, Player.HEIGHT))

    def movement(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def handle_collisions(self, collidables):

        if self.x >= Goal.X and self.y >= Goal.Y:
            self.finished = True

        if self.finished:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.finished = False
                self.speed = Player.SPEED
            else:
                self.speed = 0

class Tree(object):

    def __init__(self, points) -> None:
        self.points = points

    def draw(self):
        pygame.draw.polygon(surface = win, color = Color.GREEN, points = self.points)

    def handle_collisions(self, collidables):
        pass

class Forest(object):

    def __init__(self):
        self.children = []

    def add(self, *points):
        self.children.append(Tree(points))
        return self

    def draw(self):
        for child in self.children:
            child.draw()

    def handle_collisions(self, collidables):
        for child in self.children:
            child.handle_collisions(collidables)

class Mountain(object):

    def __init__(self, points) -> None:
        self.points = points

    def draw(self):
        pygame.draw.polygon(surface = win, color = Color.BLUE, points = self.points)

    def handle_collisions(self, collidables):
        pass

class Mountains(object):

    def __init__(self):
        self.children = []

    def add(self, *points):
        self.children.append(Mountain(points))
        return self

    def draw(self):
        for child in self.children:
            child.draw()

    def handle_collisions(self, collidables):
        for child in self.children:
            child.handle_collisions(collidables)

class Gate(object):

    def draw(self):
        pass

    def handle_collisions(self, collidables):
        pass

class Start(object):

    def draw(self):
        pygame.draw.rect(win, Color.WHITE, (Player.X, Player.Y, Player.WIDTH, Player.HEIGHT))

class Goal(object):
    X = 1000
    Y = 720

    def draw(self):
        pygame.draw.rect(win, Color.WHITE, (self.X, self.Y, Player.WIDTH, Player.HEIGHT))

game = Game()

game.add_game_objects(
    slope = Slope(),
    start = Start(),
    skier = Skier(),
    mountains = Mountains().
        add((900, 350), (1000, 350), (950, 300)).
        add((600, 500), (750, 500), (675, 400)).
        add((50, 200), (150, 200), (100, 150)),
    forest = Forest(). #pin
        add((50, 200), (60, 200), (55, 190)).
        add((70, 200), (80, 200), (75, 190)).
        add((80, 200), (90, 200), (85, 190)).
        add((75, 190), (85, 190), (80, 180)).
        add((250, 150), (260, 150), (255, 140)).
        add((240, 140), (250, 140), (245, 130)).
        add((230, 130), (240, 130), (235, 120)).
        add((220, 120), (230, 120), (225, 110)).
        add((210, 110), (220, 110), (215, 100)).
        add((200, 100), (210, 100), (205, 90)).
        add((190, 90), (200, 90), (195, 80)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)).
        add((50, 200), (60, 200), (55, 190)),
    gate = Gate(),
    goal = Goal()
)
game.loop()

pygame.quit()