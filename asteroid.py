import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        
        # On calcule les nouvelles trajectoires
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle) # Rotation inverse pour le deuxième morceau
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # On utilise self.position.x et self.position.y
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # On assigne la nouvelle vitesse accélérée aux nouveaux astéroïdes
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2

