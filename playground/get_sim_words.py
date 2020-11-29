
from back.utils import load_fasttext_model
from threading import Semaphore
import time
from back.utils import similar_by_word
import json


def main():
    fasttext_model = load_fasttext_model()
    student_vec = fasttext_model.get_vector("student")
    company_vec = fasttext_model.get_vector("company")
    sims = similar_by_word(fasttext_model, student_vec + company_vec, top_n=20)
    for sim in sims:
        print(sim)


if __name__ == '__main__':
    main()
