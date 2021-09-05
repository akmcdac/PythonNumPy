from abc import ABC, abstractmethod


class CharacterAttributes(ABC):

    def set_stats(self, power_level, hit_points):
        self.power_level = power_level
        self.git_points = hit_points

    @property
    @abstractmethod
    def use_power(self):
        pass


class Arena:
    def __init__(self):
        self._fighter = []

    def enter(self, fighter):
        self._fighter.append(fighter)

    def fight(self):
        for fighter in self._fighter:
            fighter.use_power

        for fighter in self._fighter:
            for otherFighter in self._fighter:
                if fighter is not otherFighter and fighter.power_level > otherFighter.power_level:
                    otherFighter.hit_points -= fighter.power_level - otherFighter.power_level


class Thanos(CharacterAttributes):
    def __init__(self):
        self.set_stats(power_level=15, hit_points=15)

    @property
    def use_power(self):
        self.power_level += 2


class DoctorStrange(CharacterAttributes):
    def __init__(self):
        self.set_stats(power_level=12, hit_points=15)

    @property
    def use_power(self):
        self.power_level += 1


strange, thanos = DoctorStrange(), Thanos()
arena = Arena()

arena.enter(strange)
arena.enter(thanos)
arena.fight()

# A fight break out between strange and thanos!
print("Thanos has: ", thanos.hit_points, " hitpoints left")
print("Strange has: ", strange.hit_points, " hitpoints left")
