from HUD import HUD
    
class Player:
    def __init__(self, size):
        self.hud = HUD(size)
    def attacked(self, pos):
        return self.hud.boatsBoard.sink(pos)
    def attack(self, ememy, pos):
        var = ememy.attacked(pos)
        self.hud.attackBoard.bombard(pos, var)