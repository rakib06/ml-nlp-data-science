"""
    https://ashwoolford.github.io/bnltk-documentation/
"""


# Tokenizer
from bnltk.tokenize import Tokenizers
t = Tokenizers()
print(t.bn_word_tokenizer('আমার সোনার বাংলা ।'))

# Stemmer

from bnltk.stemmer import BanglaStemmer
bn_stemmer = BanglaStemmer()
print(bn_stemmer.stem('খেয়েছিলো'))

"""
# Parts of Speech Tagger
from bnltk.bnltk_downloads import DataFiles
DataFiles().download()
"""
from bnltk.pos_tagger import PosTagger
p_tagger = PosTagger()
p_tagger.loader()
sentences = 'দুশ্চিন্তার কোন কারণই নাই'
print(p_tagger.tagger(sentences))