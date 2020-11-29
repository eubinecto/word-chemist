# word-chemist
## front
### To start the front end:
```
cd front/word-chemist
```
```
npm install
```
```
npm start
```

## back
end point | description |  required parameters | constraints
--- | --- | --- | --- |
`/word_chemist/all_choices`| returns all of the possible words to choose from | ... | ... |
`/word_chemist/add_or_sub`| returns `top_n` most similar words to the result of addition of subtraction on the two words. |  `op`, `first`, `second`, `top_n` | `op` must be either `sub` or `add`|
`/word_chemist/src_dest` | returns a pair of starting word & destination word | ... | ... |
`/word_chemist/cos_dist` | returns a cosine distance from `first` to `second` | `first`, `second` | ... |

