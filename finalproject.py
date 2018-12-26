import math

def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a
    list containing the words in txt after it has been “cleaned”."""
    txt = txt.lower()
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('?', '')
    txt = txt.replace('!', '')
    txt = txt.replace("'", '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')

    list_text = txt.split(' ')
    return list_text

def stem(s):
    """returns the stem of s"""
    
    if len(s) > 5 and s[-3:] == 'ies':
        s = s[:-3] 
    if len(s) > 3 and s[-1] == 's':
        s = s[:-1]       
    if s[-3:] == 'ing':
        if len(s) < 6:
            s = s
        elif s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    if len(s) > 5 and s[-3:] == 'ier':
        s = s[:-3]
    if len(s) > 4 and s[-2:] == 'er':
        if s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    if len(s) > 4 and s[0:2] == 're':
        s = s[2:]
    if len(s) > 3 and s[-1] == 'y':
        s = s[:-1]
           
    if len(s) > 5 and s[-4] == 'tion':
        s = s[:-4]
    if len(s) > 4 and s[0:2] == 'de':
        s = s[2:]
    if len(s) > 4 and s[0:3] == 'dis':
        s = s[3:]
    if len(s) > 4 and s[-3:] == 'ful':
        s = s[:-3]
    if len(s) > 4 and s[-4:] == 'ible':
        s = s[:-4]
    if len(s) > 4 and s[-4:] == 'less':
        s = s[:-4]
    if len(s) > 4 and s[-4:] == 'able':
        s = s[:-4]
    if len(s) > 3 and s[-1] == 's':
        s = s[:-1]
    if len(s) == 4 and s[-1] == 'e':
        s = s[:-1]

    return s

def compare_dictionaries(d1, d2):
    """take two feature dictionaries d1 and d2 as inputs,
    and it should compute and return their log similarity score"""
    score = 0
    total = sum([d1[x] for x in d1])

    for word in d2:
        if word in d1:
            score += d2[word] * math.log((float(d1[word])/float(total)))
        else:
            score += d2[word] * math.log((0.5/float(total)))
    return round(score, 3)

class TextModel:

    def __init__(self, model_name):
        """ that constructs a new TextModel object by accepting a string model_name as a
        parameter and initializing the following three attributes"""

        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.pronouns = {}


    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of pronouns: ' + str(len(self.pronouns))
        return s


    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """
        
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        word_list = clean_text(s)

        # Template for updating the words dictionary.
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.

        # Add code to update other feature dictionaries.
        'Update Word Lengths'
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
        'Update Stems Dictionary'
        for w in word_list:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
        'Update Snetence Lengths'
        s = s.replace('?', '.')
        s = s.replace('!', '.')
        s = s.replace(';', '.')
        list_sent = s.split('.')
        sent_len = [len(s.split()) for s in list_sent]
        sent_len = sent_len[:-1]
        for s in sent_len:
            if s not in self.sentence_lengths:
                self.sentence_lengths[s] = 1
            else:
                self.sentence_lengths[s] += 1
        'Update Pronouns'
        pronouns = ['i','me','my','mine','we','us','our','ours','you','your','yours','he','him','his','she','her','hers','it','its','they','their','theirs']
        
        for w in word_list:
            if w in pronouns:
                if w not in self.pronouns:
                    self.pronouns[w] = 1
                else:
                    self.pronouns[w] += 1
                                   
            
            

    def add_file(self, filename):

        file = open(filename, 'r', encoding='utf8', errors='ignore')

        for line in file:
            self.add_string(line)

        file.close()

    def save_model(self):
        """ saves the TextModel object self by writing
        its various feature dictionaries to files"""

        file1 = open((self.name + '_' + 'words'), 'w')
        file2 = open((self.name + '_' + 'word_lengths'), 'w')
        file3 = open((self.name + '_' + 'stems'), 'w')
        file4 = open((self.name + '_' + 'sentence_lengths'), 'w')
        file5 = open((self.name + '_' + 'pronouns'), 'w')

        file1.write(str(self.words))
        file2.write(str(self.word_lengths))
        file3.write(str(self.stems))
        file4.write(str(self.sentence_lengths))
        file5.write(str(self.pronouns))
        
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()

    def read_model(self):
        """eads the stored dictionaries for the called
        TextModel object from their files and assigns
        them to the attributes of the called TextModel"""

        file1 = open((self.name + '_' + 'words'), 'r')
        file2 = open((self.name + '_' + 'word_lengths'), 'r')
        file3 = open((self.name + '_' + 'stems'), 'r')
        file4 = open((self.name + '_' + 'sentence_lengths'), 'r')
        file5 = open((self.name + '_' + 'pronouns'), 'r')
        
        dict_str1 = file1.read()
        dict_str2 = file2.read()
        dict_str3 = file3.read()
        dict_str4 = file4.read()
        dict_str5 = file5.read()

        self.words = dict(eval(dict_str1))
        self.word_lengths = dict(eval(dict_str2))
        self.stems = dict(eval(dict_str3))
        self.sentence_lengths = dict(eval(dict_str4))
        self.pronouns = dict(eval(dict_str5))

    def similarity_scores(self,other):
    
        word_score = compare_dictionaries(self.words, other.words)
        word_lengths_score = compare_dictionaries(self.word_lengths, other.word_lengths)
        stems_score = compare_dictionaries(self.stems, other.stems)
        sentence_lengths_score = compare_dictionaries(self.sentence_lengths, other.sentence_lengths)
        pronouns_score = compare_dictionaries(self.pronouns, other.pronouns)
        return [word_score, word_lengths_score, stems_score, sentence_lengths_score, pronouns_score]

    def classify(self, source1, source2):

        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print(' scores for ' + source1.name + ': ', scores1)
        print(' scores for ' + source2.name + ': ', scores2)
        weighted_sum1 = 8*scores1[0] + 5*scores1[1] + 7*scores1[2] + 3*scores1[3] + 4*scores1[4]
        weighted_sum2 = 8*scores2[0] + 5*scores2[1] + 7*scores2[2] + 3*scores2[3] + 4*scores2[4]
        win = 0
        if weighted_sum1 > weighted_sum2:
            win = source1.name
        else:
            win = source2.name
        print(self.name + ' is more likely to have come from ' + win)
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('Obama Tweets')
    source1.add_file('obamatweets.txt')

    source2 = TextModel('Trump Tweets')
    source2.add_file('trump1.txt')

    new1 = TextModel("Cuckoo's Calling by Robert Galbraith (J.K. Rowling)")
    new1.add_file('rowling_test.txt')
    new1.classify(source1, source2)

    new2 = TextModel("WR100 Paper")
    new2.add_file('wr100_source.txt')
    new2.classify(source1, source2)

    new3 = TextModel("Becoming by Michelle Obama")
    new3.add_file('becoming.txt')
    new3.classify(source1, source2)

    new4 = TextModel("Fox News Articles")
    new4.add_file('fox_news.txt')
    new4.classify(source1, source2)

    new5 = TextModel("Trump")
    new5.add_file('testt.txt')
    new5.classify(source1, source2)

    
        
        






                
        
    
        
