from ui import enable_ansi, header
from config import DIFFICULTIES


def main():
    enable_ansi()

    header("SAGAP")

    print("Difficulties:")
    
    for difficulty, multiplier in DIFFICULTIES.items():
        print(f"{difficulty}: {multiplier}x")


if __name__ == "__main__":
    main()
