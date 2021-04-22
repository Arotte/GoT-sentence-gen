from markov_chain import MarkovModel

if __name__ == '__main__':
    # create a trigram model
    model = MarkovModel(corpus_path="./corpora/GoT/corpus.txt", n=3)

    # generate 10 random senteces
    for _ in range(10):
        print(model.sentence(min_length=5))