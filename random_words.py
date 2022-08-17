import random
class Random():
    def __init__(self):
        pass
    
    def random_word(self):
        words_list = []
        with open("words.txt","r") as file:
            for line in file:
                words_list.append(line.rstrip('\r\n'))
                
            self.word = random.choice(words_list)
            my_tuple = tuple(self.word.split(':'))
        return my_tuple
                