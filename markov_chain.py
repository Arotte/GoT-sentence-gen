from collections import defaultdict
import random as rand
import sys


class MarkovModel:
    def __init__(self, corpus_path, n):
        self.n = n
        # load corpus
        try:
            with open(corpus_path, "r", encoding="utf-8") as f:
                # create model from tokenized (word) txt
                self.create_model(f.read().split())
        except FileNotFoundError:
            print(f"Error! Could not find file at {corpus_path}")
            sys.exit()

    def create_model(self, corpus):
        """Creates the Markov chain model from a tokenized text"""
        self.chain = defaultdict(defaultdict)
        for ngram in [  # list of n-tuples
            (" ".join(corpus[i : i + self.n]), corpus[i + self.n])
            for i in range(len(corpus) - self.n)
        ]:
            if not self.chain[ngram[0]]:  # no nodes for current head
                self.chain[ngram[0]] = defaultdict(int)  # init distribution to 0
            self.chain[ngram[0]][ngram[1]] += 1  # count tails

    def snt_ending(self, str_):
        return str_[-1] in "!?."

    def sentence(self, min_length):
        """Generates a random sentence"""
        random_sentence = []

        # select sentence starting head
        while True:
            random_head = rand.choice(list(self.chain.keys()))
            if random_head[0].isupper() and not self.snt_ending(random_head):
                random_sentence += random_head.split()
                break

        # generate sentence
        while (
            not self.snt_ending(random_sentence[-1])
            or len(random_sentence) < min_length
        ):
            current_head = " ".join(random_sentence[-self.n :])
            random_sentence.append(
                rand.choices(
                    population=list(self.chain.get(current_head).keys()),
                    weights=list(self.chain.get(current_head).values()),
                )[0]
            )
        return " ".join(random_sentence)