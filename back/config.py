from pathlib import Path
from os import path
# the root directory of this project
# define the directories here
BACK_DIR = Path(__file__).resolve().parent
DATA_DIR = path.join(BACK_DIR, "data")
FASTTEXT_MODEL_PATH = path.join(DATA_DIR, "crawl-300d-2M.model")
FASTTEXT_KEYED_VEC_PATH = path.join(DATA_DIR, "crawl-300d-2M.vec")
FASTTEXT_NEW_KEYED_VEC_PATH = path.join(DATA_DIR, "crawl-300d-2M-new.vec")
FASTTEXT_NEW_VEC_NORM_PKL_PATH = path.join(DATA_DIR, "crawl-300d-2M-new.vec-norm.pkl")
MOST_FREQ_WORDS_TXT = path.join(DATA_DIR, "most_freq_words.txt")
NLP_MODEL = "en_core_web_sm"
CHOICES_TXT_PATH = path.join(DATA_DIR, "choices.txt")
