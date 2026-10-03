from ui import enable_ansi, header
from data.enemies import ENEMIES, FLOOR_ENEMY_POOL, MINIBOSSES, FINAL_BOSS


def main():
    enable_ansi()

    header("SAGAP")

    print(f"Regular enemies: {len(ENEMIES)}")
    print(f"Floors with enemy pools: {len(FLOOR_ENEMY_POOL)}")
    print(f"Mini-bosses: {len(MINIBOSSES)}")
    print(f"Final boss: {FINAL_BOSS['name']}")


if __name__ == "__main__":
    main()
