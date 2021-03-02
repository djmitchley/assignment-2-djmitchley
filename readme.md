### Assignment 2

#### Due March 12, 11:59pm

In this assignment, you'll get some experience working with files and dictionaries. 
In particular, you'll learn how we can use a dictionary to generate random text.

Details for each question are included in the comments in the file assignment2.py

This assignment also contains a few files (hout.txt, glenpark.jpg, quick.txt, map) that are not part of the 
assignment, but that we'll use in class.

1. Write a function that prompts the user to input a filename, calls the getWordCount function, and
then prints the 20 most common words in that text, not counting stopwords.
      
2. Write a function called wordProbability that takes as input a word and a histogram (as created above) and returns the
probability of that word occurring. If the word is not in the histogram, return 0.

3. Write a function called getRandomWord that takes as input a histogram and returns a random word, based on this approach.

4. Now that we have this, we could try to generate random text. Write a function called randomSentence that takes a histogram as
input and randomly chooses 10 words, with the probability based on their frequency in the histogram.
   
5. So let's tweak our code above to write a helper function called getHistogram. It should take as input a list
of words, such as ['now', 'is', 'the', 'time'] and return a dictionary with the word's count in that list.
   
6.Now we're ready to build a Markov generator. This should be a function that takes two inputs: a filename and a
 starting word.
It should work like so:
 1. Read in all the words from the file into a histogram, as above. 
2. Use that histogram to generate the markovHistogram.
3. Decide on a sentence length. Let's say 15 words.
4. For i = 0 to 15,
5.  for the current word, get its histogram from the one you generated.
6.  generate a random word from that histogram, using your generateRandomWord function
7.  set the current word to be this random word.
Give this a try with a few different words from your original document and see if the sentences seem more reasonable.
 (this is basically the approach that your phone uses with predictive texting.)