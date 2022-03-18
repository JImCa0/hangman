

import hangman1 as hm
wordlist = hm.load_words()
secret_word=hm.choose_word(wordlist)
hm.hangman(secret_word)