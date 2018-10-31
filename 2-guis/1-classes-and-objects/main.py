from bot import Bot
from superbot import SuperBot
from flyingbot import FlyingBot

beep = Bot("Beep")
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()
print(beep)

astro = SuperBot("Astro")
astro.display_super_power_level()
print(astro)

boop = FlyingBot("Boop")
boop.display_hover()
print(boop)
