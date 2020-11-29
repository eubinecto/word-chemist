
from back.utils import load_fasttext_model
from threading import Semaphore
import time
from back.utils import cos_dist
import json


def main():
    fasttext_model = load_fasttext_model()
    # https://stackoverflow.com/a/43067907
    dist1 = cos_dist(fasttext_model, "company", "student")
    dist2 = cos_dist(fasttext_model, "company", "salesman")
    # if you add up student & salesman, you get a teacher!
    # this is a nice example


if __name__ == '__main__':
    main()
