"""
https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74/train/python
"""


def zombie_shootout(zombies, distance, ammo):
    shot = 0
    while distance >= 0:
        if zombies == 0:
            return f"You shot all {shot} zombies."
        if distance <= 0:
            return f"You shot {shot} zombies before being eaten: overwhelmed."
        if ammo <= 0 and zombies > 0:
            return f"You shot {shot} zombies before being eaten: ran out of ammo."

        zombies -= 1
        shot += 1
        ammo -= 1
        distance -= 0.5


if __name__ == '__main__':
    print(zombie_shootout(100, 8, 200))