class FightActions:
    def fight(self, defender):
        if self.power_level > defender.power_level:
            defender.hits_point -= self.power_level - defender.power_level
        elif self.power_level == defender.power_level:
            print("They are equal in strength!")
        else:
            self.hit_points -= defender.power_level - self.power_level


class CharacterAttributes:
    def set_stats(self, power_level, hit_points):
        self.power_level = power_level
        self.hit_points = hit_points


class Thanos(FightActions, CharacterAttributes):
    def __init__(self):
        self.set_stats(power_level=15, hit_points=15)

    def laugh(self):
        self.power_level += 1


class DoctorStrange(FightActions, CharacterAttributes):
    def __init__(self):
        self.set_stats(power_level=12, hit_points=15)

    def use_spell(self):
        self.power_level += 2


strange, thanos = DoctorStrange(), Thanos()

# A fight break out between strange and thanos
thanos.laugh()
thanos.fight(strange)
print("Thanos has: ", thanos.hit_points, " hitpoints left")
print("Strange has: ", strange.hit_points, " hitpoints left")
