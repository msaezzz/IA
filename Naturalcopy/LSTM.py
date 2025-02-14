import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

def tokeniz(text):
    tokens_palabras = word_tokenize(text)
    print("Tokens de palabras:", tokens_palabras)

if __name__ == '__main__':
    tokeniz("Hola, ¿cómo estás? Espero que estés bien.")