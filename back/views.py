from flask import Flask, jsonify, request
from back.errors import InvalidRequestError
from back.utils import load_fasttext_model, all_options, add, sub, similar_by_vec

app = Flask(__name__)
# this should be setup
FASTTEXT_MODEL = load_fasttext_model()
VALID_OPS = ("add", "sub")


# handler for invalid request
@app.errorhandler(InvalidRequestError)
def handle_invalid_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/word_chemist/all_options')
def api_all_options():
    global FASTTEXT_MODEL
    """
    api for getting all vocabulary in word2vec
    """
    # this is required
    # make sure you.. normalise the case.
    return jsonify(all_options(FASTTEXT_MODEL))


@app.route("/word_chemist/add_or_sub")
def api_add_or_sub():
    op = request.args.get("op")
    first = request.args.get("first")
    second = request.args.get("second")
    top_n = request.args.get("top_n", type=int)
    global FASTTEXT_MODEL
    if op not in VALID_OPS:
        raise InvalidRequestError
    elif op == "add":
        res = add(FASTTEXT_MODEL, first, second)
    else:
        res = sub(FASTTEXT_MODEL, first, second)
    sims = similar_by_vec(FASTTEXT_MODEL, res, top_n)
    return jsonify(sims)
