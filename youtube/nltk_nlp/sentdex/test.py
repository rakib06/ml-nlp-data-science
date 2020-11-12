from nltk.tokenize import  sent_tokenize, word_tokenize
example_text = "hello there, how are you doing today? the weather is" \
               "great and the sky is blue. I Love Bangladesh. " \
               "Bangladeshi people are awesome!"

# print(sent_tokenize(example_text))
# print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)


