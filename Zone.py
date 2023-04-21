class Zone:
    def __init__(self,Zone):
        self.Zone = Zone

    def in_zone(self,player_cords,player):
        """if player == "1":
            if player_cords[0] > self.Zone[1] and (player_cords[1] > self.Zone[0] and player_cords[1] < self.Zone[2]):
                return True
            else:
                return False
        elif player == "2":
            if player_cords[0] < 1000 - self.Zone[1] and (player_cords[1] > self.Zone[0] and player_cords[1] < self.Zone[2]):
                return True
            else:
                return False"""

        if player == "1":
            if player_cords[0] < self.Zone[1] or (player_cords[1] > 0 and player_cords[1] < self.Zone[0]) or (player_cords[1] < 1000 and player_cords[1] > 1000 - self.Zone[2]):
                return True
            else:
                return False
        elif player == "2":
            if player_cords[0] > 1000 - self.Zone[1] or (player_cords[1] > 0 and player_cords[1] < self.Zone[0]) or (player_cords[1] < 1000 and player_cords[1] > 1000 - self.Zone[2]):
                return True
            else:
                return False

    def increase_zone(self,amount):
        for y,x in enumerate(self.Zone):
            self.Zone[y] += amount

