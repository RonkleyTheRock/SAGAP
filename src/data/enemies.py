from config import AFFINITIES

def mk_aff(weak=(), resist=(), strong=()):
    """builds a full affinity table for an enemy. anything not listed is neutral. 'strong' means the enemy hardly felt the attack."""
    aff = {a: "Neutral" for a in AFFINITIES}

    for a in weak:
        aff[a] = "Weak"

    for a in resist:
        aff[a] = "Resist"

    for a in strong:
        aff[a] = "Strong"

    return aff
