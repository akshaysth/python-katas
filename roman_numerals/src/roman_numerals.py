# import pretty_errors


def to_roman(val: int) -> str:
    roman = ""
    for val > 0:
        if val >= 1000:
            i = val / 1000
            roman += int(i) * "M"
            val = val - val * val / 1000
        elif val >= 100:
            i: int = val / 100
            roman += int(i) * "M"

    return roman


def from_roman(roman_num: str) -> int:
    return roman_num


def main():
    print(f"{to_roman(123)} = ")
    print(f"{to_roman(2000)} = ")


if __name__ == "__main__":
    main()
