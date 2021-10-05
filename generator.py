from string import ascii_letters, digits
from secrets import choice

alphabet = ascii_letters + digits + "!#$%&()*+,-.:;<=>?@[]_{|}"


def generate_password(length):
    return "".join(choice(alphabet) for i in range(length))


if __name__ == "__main__":
    import sys

    try:
        length = int(sys.argv[1] if len(sys.argv) == 2 else 25)
        print(f"You can't use this as a password:\t{generate_password(length=length)}")
    except Exception as ex:
        raise ex
