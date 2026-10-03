from ui import enable_ansi, header, line, colorize, GREEN


def main():
    enable_ansi()

    header("SAGAP")

    print(colorize("The game has started.", GREEN))

    line()

    print("This is our new modular version.")


if __name__ == "__main__":
    main()
