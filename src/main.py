from ui import enable_ansi, header
from data.classes import CLASSES
from data.items import ITEMS


def main():
    enable_ansi()

    header("SAGAP")

    print("Classes:")

    for class_name in CLASSES:
        print(f"{class_name}")

    print("\nItems:")
    for item_name in ITEMS:
        print(f"{item_name}")


if __name__ == "__main__":
    main()
