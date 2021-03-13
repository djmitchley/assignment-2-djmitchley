### This assignment is drawn from material in Think Python:
### https://greenteapress.com/thinkpython/thinkpython.pdf

### In this assignment, we'll build on the work that we did in last week's lab involving counting words in a text.

### You may use any text you want - I'm including the text of Hamlet with this assignment.
### You can find other public domain, out-of-copyright texts through Project Gutenberg (http://www.gutenberg.org)

## Reminder:
## Here's the code we created in Lab 3, re-written as a function that returns a dictionary

def getWordCount(fname) :
    stopwords = ['a', 'an', 'the', 'in', 'of', 'he', 'she']
    wordCount = {}
    with open(fname) as inputFile:
        lines = inputFile.readlines()
        for line in lines:
            lowercaseLine = line.lower()
            words = lowercaseLine.split()
            for word in words:
                if word not in stopwords:  ### <-- here's the new part!
                    strippedWord = word.strip(string.punctuation)
                    if strippedWord in wordCount:
                        wordCount[strippedWord] = wordCount[strippedWord] + 1
                    else:
                        wordCount[strippedWord] = 1

    return wordCount


## 1. Write a function that prompts the user to input a filename, calls the getWordCount function, and
## then prints the 20 most common words in that text, not counting stopwords.

fname = "hamlet.txt"


def getMostCommonWords(fname) :
    wc = getWordCount(fname)
    wordList = []
    for word in wc:
        wordList.append((wc[word],word))
    wordList.sort(reverse=True)
    return wordList [:20]


## Our wordCount dictionary is an example of a data structure known as a histogram. We can use this to represent
## the probability of a particular word occurring in our source document.
### For example, if there are 100 total words (including duplicates), and the word 'cat' occurs 11 times, we can conclude
## that the probability of 'cat' occurring (written P('cat') is 11/100, or 0.11.

### 2. Write a function called wordProbability that takes as input a word and a histogram (as created above) and returns the
### probability of that word occurring. If the word is not in the histogram, return 0.

wc = getWordCount(fname)
def wordProbability(word, wordCount) :
    if word not in wordCount :
        return 0
    else:
        wordFrequency = wordCount[word]
    total = 0
    for item in wordCount:
        total = total + wordCount[item]
        if word in wordCount :
            probability = wordFrequency / total
        return probability

## new label
wc2 = wordProbability(word, wordCount)


### Now that we know how to do this, we can randomly select words based on their probability.
### To begin, let's remember how to generate a random number.

import random
val = random.random()

### this generates a random number between 0 and 1. How can we use this with our histogram?
### We start with a variable called total, initialized to zero. Then, we iterate through our histogram.
### Add the probability of the current word (which you implemented in question #2) to the total. If it's less than
### val, keep going. If it's greater than val, return the current word.

## 3. Write a function called getRandomWord that takes as input a histogram and returns a random word, based on this approach.import random

def getRandomWord(histogram) :
    histogramList = list(histogram.keys())
    randomWord = random.choice(list(wc.keys()))
    return randomWord

## new label to make it make results easier to read
wc3 = getRandomWord(histogram)

## us wc for input in getRandomWord(wc)

### 4. Now that we have this, we could try to generate random text. Write a function called randomSentence that takes a histogram as
### input and randomly chooses 10 words, with the probability based on their frequency in the histogram.

def getRandomSentence(wc) :
    return random.choices(list(wc.keys()), wc.values(), k=10)

## new label to make it make results easier to read
wc4 = getRandomSentence(wc)

### This probably doesn't look much like a sentence. There's a reason for this. Sentences have a sequential structure - the likelihood of
### a word occurring depends on what came before it. Our previous code did not take this into consideration. We were assuming
### that the frequency of a word occurring was independent of ever

### Let's try a simple extension to this, called Markov analysis. We'll assume that a word's probability depends on how often we
### see it after the word before it. Let's keep stopwords here.

import string
def getMarkovWordCount(fname) :
    wordCount = {}
    prevWord = ''
    with open(fname) as inputFile:
        ## read in all the words at once. allWords will be a list of words.
        allWords = inputFile.read().split()
        for word in allWords :
            ## lower-case and remove punctuation.
            lcWord = word.lower().strip(string.punctuation)
            print (lcWord)
            if prevWord in wordCount :
                wordCount[prevWord].extend([lcWord])
            else :
                wordCount[prevWord] = [lcWord]
            prevWord = lcWord
    return wordCount

### this generates a dictionary that maps a word to a list of all the words that follow it. That's nice, but what
### we really want is a dictionary that maps a word to all the words that follow it, with their count.
#
###  5. So let's tweak our code above to write a helper function called getHistogram. It should take as input a list
### of words, such as ['now', 'is', 'the', 'time'] and return a dictionary with the word's count in that list.

ListOfWords = ['now', 'is', 'the', 'time']

def getHistogram(ListOfWords) :
    hist= {}
    for item in ListOfWords :
        if item in hist:
            hist[item] += 1
        else:
            hist[item] = 1
    return hist

### Once we have this, we can build a tool that converts the dictionary that getMarkovWordCount created to one that
### maps a dictionary onto another dictionary - this tells us, for a given word, the frequency of all the words that
# follow it.

def buildMarkovHistogram(markovWordCount) :
    markovHist = {}
    for word in markovWordCount :
        fd = getHistogram(markovWordCount[word])
        markovHist[word] = fd

### 6.Now we're ready to build a Markov generator. This should be a function that takes two inputs: a filename and a
#### starting word.
### It should work like so:
### 1. Read in all the words from the file into a histogram, as above.
### 2. Use that histogram to generate the markovHistogram.
### 3. Decide on a sentence length. Let's say 15 words.
### 4. For i = 0 to 15,
### 5.     for the current word, get its histogram from the one you generated.
### 6.     generate a random word from that histogram, using your generateRandomWord function
### 7.     set the current word to be this random word.
### Give this a try with a few different words from your original document and see if the sentences seem more reasonable.
### (this is basically the approach that your phone uses with predictive texting.)


def MarkovHistogram(fname, start) :
    markovHist = getMarkovWordCount(fname)
    markovHistogram = buildMarkovHistogram(markovHist)
    for i in range(15) :
        firstWord = markovHistogram[start]
        nextWord = getRandomWord(firstWord)
        start = nextWord
        print(nextWord)

## start would be a word from one of the texts. From hamlet.txt in this case
