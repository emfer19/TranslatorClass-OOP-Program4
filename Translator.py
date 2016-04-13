#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 2/29/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge, programming project 3

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University,
the Department of Mathematics and Computer Science, I affirm that I have neither given
nor received assistance on this programming assignment. This assignment represents my
individual, original effort.'''

import urllib #for use of url, no longer needed due to change to be a local file (4/13/16 lab 11)
from FileUtilities import * #to read the file easily

class Translator:
  morseCode=[] #class attribute, universal to all methods in class

  def __init__(self): #receives nothing
    self._morseDict={} #creates a dictionary for the morse
    morseFile=openFileReadRobust() #collects file and reads it into this attribute
    line=morseFile.readline()
    while line:
      data=line.split()
      self._morseDict[data[0].lower()]=data[1]
      line=morseFile.readline()
    morseFile.close()

#split code to translate into morse
  def translate(self,phrase): #receives the string containing sentence to translate
    words=phrase.lower().split() #split phrase into a list of the words, make all lower to allow any case to work
    for word in words: #translate each word separately 
      print word.upper(), 'in Morse code is'
      for i in word: #loop to do each letter separately
        print self._morseDict[i]  #print the morse for that letter

#method to print the data
  def display(self): #receives nothing
    print 'Letters of the alphabet with equivalent Morse code'
    for key,value in self._morseDict.items(): #for each item in the dictionary
      print key,value

#end of class build
if __name__=='__main__':
  code=Translator()
  code.display()
  sentence=raw_input('Enter a sentence: ')
  code.translate(sentence)
  print
  raw_input('Press ENTER to close')
