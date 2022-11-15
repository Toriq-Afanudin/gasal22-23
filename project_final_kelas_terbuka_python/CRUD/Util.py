import random
import string
import time


def random_string(panjang: int) -> str:
    hasil_string = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string


def waktu():
    return time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
