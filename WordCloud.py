import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import  ipywidgets as widgets
import fileupload
import io
import sys

file_contents = """Chapter 1

      It is a truth universally acknowledged, that a single man in
      possession of a good fortune, must be in want of a wife.

      However little known the feelings or views of such a man may be
      on his first entering a neighbourhood, this truth is so well
      fixed in the minds of the surrounding families, that he is
      considered as the rightful property of some one or other of their
      daughters.

      "My dear Mr. Bennet," said his lady to him one day, "have you
      heard that Netherfield Park is let at last?"

      Mr. Bennet replied that he had not.

      "But it is," returned she; "for Mrs. Long has just been here, and
      she told me all about it."

      Mr. Bennet made no answer.

      "Do not you want to know who has taken it?" cried his wife
      impatiently.

      "_You_ want to tell me, and I have no objection to hearing it."

      This was invitation enough.

      "Why, my dear, you must know, Mrs. Long says that Netherfield is
      taken by a young man of large fortune from the north of England;
      that he came down on Monday in a chaise and four to see the
      place, and was so much delighted with it that he agreed with Mr.
      Morris immediately; that he is to take possession before
      Michaelmas, and some of his servants are to be in the house by
      the end of next week."

      "What is his name?"""

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
      # LEARNER CODE START HERE
    frequencies= {}
    for punc in file_contents:
          if punc in punctuations:
            file_contents=file_contents.replace(punc,'')
    words = file_contents.split()
    for word in words:
          if word not in uninteresting_words:
           if word in frequencies and word not in uninteresting_words:
              frequencies[word]+=1
           else:
            frequencies[word]=1
    print(frequencies)
      
    #frequencies={"test": 100,"test3":2000,"Test2":1}
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()