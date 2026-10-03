from ui import enable_ansi, header
from data.floors import FLOORS


def main():
    enable_ansi()
    header("SAGAP")

    print(FLOORS[1]["name"])
    print(FLOORS[1]["boss"])
    print(FLOORS[10]["name"])
    print(FLOORS[10]["boss"])


if __name__ == "__main__":
    main()
