from markov_chain import MarkovModel
from time import sleep
import sys

if __name__ == '__main__':
    # create a trigram model
    model = MarkovModel(corpus_path="./corpora/GoT/corpus.txt", n=3)

    commands = ['gimme a sentence', 'nah, a new one', 'new pls' , "still ain't the best"]

    # demo
    while True:
        sys.stdout.write("\033[0;32m")
        prompt = input('> ')
        sys.stdout.write('\033[0;0m')
        
        if prompt == 'exit':
            break

        if prompt in commands:
            sentence = model.sentence(7)

            sys.stdout.write("\033[;1m")
            for c in sentence:
                sleep(30 / 1000)
                sys.stdout.write(c)
                sys.stdout.flush()
            sys.stdout.write('\033[0;0m')
            print()