from typing import Generator, Optional, Dict

from spacy import load
from spacy.tokens import Token

from back.config import FASTTEXT_KEYED_VEC_PATH, FASTTEXT_NEW_KEYED_VEC_PATH, NLP_MODEL
import re

ALPHABETIC_REGEXP = re.compile("[a-zA-Z]+")

# could improve the speed with concurrency!
# access to global dictionary..
# have a think about this later..


def load_fasttext_keys() -> Generator[str, None, None]:
    with open(FASTTEXT_KEYED_VEC_PATH, 'r') as fh:
        for line in fh:
            yield line.split(" ")[0].strip()


def load_fasttext_vecs() -> Generator[str, None, None]:
    with open(FASTTEXT_KEYED_VEC_PATH, 'r') as fh:
        for line in fh:
            yield line.split(" ")[1].strip()


def is_not_alphabetic(token: Token) -> bool:
    return None is ALPHABETIC_REGEXP.match(token.text)


def is_stop_word(token: Token):
    return token.is_stop


def normalise(token: Token) -> Optional[str]:
    return token.lemma_.lower()


def main():
    nlp = load(NLP_MODEL)
    keys = load_fasttext_keys()
    vecs = load_fasttext_vecs()
    new_keyed_vecs: Dict[str, str] = dict()
    for key, vec in zip(keys, vecs):
        token = nlp(key)[0]
        # filters
        if is_not_alphabetic(token):
            continue
        if is_stop_word(token):
            continue
        new_key = normalise(token)
        if new_key in new_keyed_vecs:
            continue
        new_keyed_vecs[new_key] = vec
        print("read:" + new_key)
    else:
        with open(FASTTEXT_NEW_KEYED_VEC_PATH, 'w') as fh:
            for new_key, vec in new_keyed_vecs.items():
                print("write:" + new_key)
                fh.write(new_key + " " + vec + "\n")


if __name__ == '__main__':
    main()
