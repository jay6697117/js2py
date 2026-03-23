from .main import Calculator


def main() -> None:
    calculator = Calculator()

    print(f"add(2, 3) = {calculator.math['add'](2, 3)}")
    print(f"multiply(4, 6) = {calculator.math['multiply'](4, 6)}")
    print(f"capitalize('hello') = {calculator.string['capitalize']('hello')}")


if __name__ == "__main__":
    main()
