from typing import Generator


def frequency_generator() -> Generator[int, None, None]:
    with open("frequencies.txt", "r") as fp:
        for line in fp:
            yield int(line)


def main():
    result: int = 0
    for frequency in frequency_generator():
        result += frequency
    return result


if __name__ == "__main__":

    print(main())
