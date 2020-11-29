from typing import Dict, Tuple
import numpy as np
from gensim.models.keyedvectors import Word2VecKeyedVectors
import logging
from os import path
from back.config import FASTTEXT_MODEL_PATH
import pickle
import sys
import gensim
from back.config import FASTTEXT_NEW_VEC_NORM_PKL_PATH
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import random


def load_fasttext_model() -> Word2VecKeyedVectors:
    """
    load the model from cache if stored already. if not, build the model. (will take about 10 minutes)
    :return:
    """
    logger = logging.getLogger("load_fasttext_model")
    logger.info("loading fasttext model with mmap=r...")
    model = Word2VecKeyedVectors.load(FASTTEXT_MODEL_PATH, mmap='r')
    logger.info("loading vector_norm...")
    # just a placeholder to init vectors_norm
    # once this is done, vector_norm will be initialised
    model.similar_by_word("eagle")
    return model


def all_options(fasttext_model: Word2VecKeyedVectors) -> list:
    return list(fasttext_model.vocab.keys())


def start_end(fasttext_model: Word2VecKeyedVectors) -> Tuple[str, str]:
    # for now, just return random ones.
    keys = list(fasttext_model.vocab.keys())
    start = random.choice(keys)
    end = random.choice(keys)
    return start, end


def add(fasttext_model: Word2VecKeyedVectors, first: str, second: str) -> np.ndarray:
    first_vec = fasttext_model.get_vector(first)
    second_vec = fasttext_model.get_vector(second)
    return first_vec + second_vec


def sub(fasttext_model: Word2VecKeyedVectors, first: str, second: str) -> np.ndarray:
    first_vec = fasttext_model.get_vector(first)
    second_vec = fasttext_model.get_vector(second)
    return first_vec - second_vec


def similar_by_word(fasttext_model: Word2VecKeyedVectors, word: str,  top_n: int) -> Tuple[str, float]:
    sims = fasttext_model.similar_by_word(word, top_n)
    return sims


def similar_by_vec(fasttext_model: Word2VecKeyedVectors, vec: np.ndarray, top_n: int) -> Tuple[str, float]:
    sims = fasttext_model.similar_by_vector(vec, top_n)
    return sims


