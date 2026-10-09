
import random

from data.classes import CLASSES
from config import MAGIC_AFFINITIES
from ui import (
    header, colorize, CYAN, BOLD, YELLOW, GREEN,
    MAGENTA, RED, WHITE, ITALIC
)
from combat.targeting import (
    choose_enemy, choose_character, alive_party, alive_enemies
)
from combat.helpers import (
    affinity_multiplier, apply_status, apply_buff,
    classify, record_knowledge
)
from combat.attacks import deal_attack
from systems.progression import unlocked_skills
