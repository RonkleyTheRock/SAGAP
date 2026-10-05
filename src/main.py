from ui import enable_ansi, header
from data.narrative import (
    GUIDE_NAME,
    GUIDE_MOTHER_LINES,
    GUIDE_SELF_LINES,
    RIDDLES,
    LORE_FRAGMENTS,
)


def main():
    enable_ansi()
    header("SAGAP")

    print("Guide:", GUIDE_NAME)
    print("Floor 1:", GUIDE_MOTHER_LINES[1])
    print("Self lines:", len(GUIDE_SELF_LINES))
    print("Riddles:", len(RIDDLES))
    print("Lore floors:", len(LORE_FRAGMENTS))


if __name__ == "__main__":
    main()
