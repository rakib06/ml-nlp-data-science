
def lec1(example_text):
    from nltk.tokenize import  sent_tokenize, word_tokenize
    print(sent_tokenize(example_text))
    print(word_tokenize(example_text))

    for i in word_tokenize(example_text):
        print(i)


def lec2(example_sentence):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stopwords = set(stopwords.words("english"))
    print(stopwords, '\n', len(stopwords))
    words = word_tokenize(example_sentence)

    '''filtered_sentence = []
    for w in words:
        if w not in stopwords:
            filtered_sentence.append(w)'''
    filtered_sentence = [w for w in words if not w in stopwords]
    print(filtered_sentence, '\n', len(filtered_sentence))


def lec3(example_words):
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    ps = PorterStemmer()
    for w in example_words:
        print(ps.stem(w))


example_text = "hello there, how are you doing today? the weather is " \
                   "great and the sky is blue. I Love Bangladesh. " \
                   "Bangladeshi people are awesome!"

# lec1(example_text)

# lec2(example_text)

example_words = ["python", "pythoner", "pythoning", 'pythoned', 'pythonly']
lec3(example_words)