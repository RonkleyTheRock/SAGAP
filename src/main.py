from ui import enable_ansi, header
from config import DIFFICULTIES
from data.classes import CLASSES


def main():
    enable_ansi()

    header("SAGAP")

    print("Available Classes:")

    for class_name in CLASSES:
        print(class_name)


if __name__ == "__main__":
    main()
