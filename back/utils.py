from typing import Tuple
import numpy as np
from gensim.models.keyedvectors import Word2VecKeyedVectors
import logging
from back.config import FASTTEXT_MODEL_PATH, CHOICES_TXT_PATH
import sys
import random
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# Stop words
STOP_WORDS = set(
    """
a about above across after afterwards again against all almost alone along
already also although always am among amongst amount an and another any anyhow
anyone anything anyway anywhere are around as at
back be became because become becomes becoming been before beforehand behind
being below beside besides between beyond both bottom but by
call can cannot ca could
did do does doing done down due during
each eight either eleven else elsewhere empty enough even ever every
everyone everything everywhere except
few fifteen fifty first five for former formerly forty four from front full
further
get give go
had has have he hence her here hereafter hereby herein hereupon hers herself
him himself his how however hundred
i if in indeed into is it its itself
keep
last latter latterly least less
just
made make many may me meanwhile might mine more moreover most mostly move much
must my myself
name namely neither never nevertheless next nine no nobody none noone nor not
nothing now nowhere
of off often on once one only onto or other others otherwise our ours ourselves
out over own
part per perhaps please put
quite
rather re really regarding
same say see seem seemed seeming seems serious several she should show side
since six sixty so some somehow someone something sometime sometimes somewhere
still such
take ten than that the their them themselves then thence there thereafter
thereby therefore therein thereupon these they third this those though three
through throughout thru thus to together too top toward towards twelve twenty
two
under until up unless upon us used using
various very very via was we well were what whatever when whence whenever where
whereafter whereas whereby wherein whereupon wherever whether which while
whither who whoever whole whom whose why will with within without would
yet you your yours yourself yourselves
""".split()
)


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


def load_choices() -> list:
    choices = list()
    with open(CHOICES_TXT_PATH, 'r') as fh:
        for line in fh:
            choices.append(line.strip())
    return choices


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


def cos_dist(fasttext_model: Word2VecKeyedVectors, first: str, second: str) -> float:
    return fasttext_model.distance(first, second)


def similar_by_word(fasttext_model: Word2VecKeyedVectors, word: str,  top_n: int) -> Tuple[str, float]:
    sims = fasttext_model.similar_by_word(word, topn=top_n)
    return sims


def similar_by_vec(fasttext_model: Word2VecKeyedVectors, vec: np.ndarray, top_n: int) -> Tuple[str, float]:
    sims = fasttext_model.similar_by_vector(vec, topn=top_n)
    return sims


