from gensim.models.keyedvectors import Word2VecKeyedVectors
from back.config import FASTTEXT_MODEL_PATH, FASTTEXT_KEYED_VEC_PATH
import time
import logging
from sys import stdout
import pickle
logging.basicConfig(stream=stdout, level=logging.INFO)


def main():
    logger = logging.getLogger("main")
    start = time.time()
    logging.info("loading projection weights..")
    model = Word2VecKeyedVectors.load_word2vec_format(FASTTEXT_KEYED_VEC_PATH,
                                                      # we are reading in the vector file.
                                                      binary=False)
    logger.info("computing the norm vectors...")
    model.save(FASTTEXT_MODEL_PATH)
    end = time.time()
    logger.info("elapsed:" + str(end - start))


if __name__ == '__main__':
    main()
