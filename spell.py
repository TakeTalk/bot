from textblob import Word


def correct(word):
    
    word = Word(word)
    
    result = word.correct()
    
    return result
