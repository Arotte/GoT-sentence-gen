# A Markov chain based sentence generator


This little script implements a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) based approach to sentence generation. It "learns" the writing style of a text corpus and tries its best to generate a new sentence. A naive and not the best approach for this kind of problem domain, but it was perfect for learning purposes.

Based on [JetBrains Academy](https://hyperskill.org/)'s Python Developer course. [Project description](https://hyperskill.org/projects/134).

# Generated Sentence Examples

**Game of Thrones Corpus:**
```
"No, no. I, I can't stay. I just wanted to make amends for what you've done."

"After what you've done? I was your age, I lived on one bowl of stew a day."

"Stark boys with honor, and they repaid me with treachery. You treated them with honor?"

"They blame you for the city's ills."   

"Someday it'll get you killed."
```

# Setup

No third party dependecies needed, the script only uses `collections`, `random` and `sys`.

Clone this repo.
```shell
> 
```

Run test script.
```shell
> python3 ./test.py
```

# Usage Example
```python
from markov_chain import MarkovModel

# create trigram model
model = MarkovModel(corpus_path="./corpora/GoT/corpus.txt", n=3)

# generate 10 random senteces
for _ in range(10):
    print(model.sentence(min_length=5))
```