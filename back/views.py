from flask import Flask, jsonify, request
from flask_cors import CORS

from back.errors import InvalidRequestError
from back.utils import load_fasttext_model, load_choices, add, sub, similar_by_vec, similar_by_word, cos_dist
import random

app = Flask(__name__)
cors = CORS(app)
# this should be setup
FASTTEXT_MODEL = load_fasttext_model()
CHOICES = load_choices(FASTTEXT_MODEL)

VALID_OPS = ("add", "sub")

# must exist in back/data/choices.txt
SRC_DEST = (
    ("possible", "screwed")
)


# handler for invalid request
@app.errorhandler(InvalidRequestError)
def handle_invalid_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/word_chemist/all_choices')
def api_all_choices():
    global CHOICES
    """
    api for getting all vocabulary in word2vec
    """
    return jsonify(CHOICES)


@app.route("/word_chemist/add_or_sub")
def api_add_or_sub():
    global FASTTEXT_MODEL
    op = request.args.get("op")
    first = request.args.get("first")
    second = request.args.get("second")
    top_n = request.args.get("top_n", type=int, default=20)
    if op not in VALID_OPS:
        raise InvalidRequestError
    elif op == "add":
        res = add(FASTTEXT_MODEL, first, second)
    else:
        res = sub(FASTTEXT_MODEL, first, second)
    sims = similar_by_vec(FASTTEXT_MODEL, res, top_n)
    return jsonify(sims)


@app.route("/word_chemist/similar_by_word")
def api_similar_by_word():
    global FASTTEXT_MODEL
    word = request.args.get("word")
    top_n = request.args.get("top_n", type=int, default=20)
    sims = similar_by_word(FASTTEXT_MODEL, word, top_n)
    return jsonify(sims)


@app.route("/word_chemist/src_dest")
def api_src_dest():
    global SRC_DEST
    pair = random.choice(SRC_DEST)
    return jsonify(pair)


@app.route("/word_chemist/cos_dist")
def api_cos_dist():
    global FASTTEXT_MODEL
    first = request.args.get("first")
    second = request.args.get("second")
    dist = cos_dist(FASTTEXT_MODEL, first, second)
    return jsonify(dist)
