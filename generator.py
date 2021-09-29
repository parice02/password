from string import ascii_letters, digits
from secrets import choice

alphabet = ascii_letters + digits + "!#$%&()*+,-.:;<=>?@[]_{|}"


def generate(length=8):
    return "".join(choice(alphabet) for i in range(length))


if __name__ == "__main__":
    import sys

    try:
        length = int(sys.argv[1])
        print(generate(length=length))
    except Exception:
        raise ValueError
