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

import urllib #for use of url

class Translator:
  morseCode=[] #class attribute, universal to all methods in class

  def __init__(self,morseURL): #receives a string containing the URL for the data
    connection=urllib.urlopen(morseURL) #opens a connection to url
    morseCodeData=connection.read() #read in data
    morseCodeData=morseCodeData.split() #split on space
    connection.close()
    Translator.morseCode=morseCodeData #even index are morse, odd are letters

#split code to translate into morse
  def translate(self,phrase): #receives the string containing sentence to translate
    words=phrase.upper().split() #split phrase into a list of the words, make all caps to allow lowercase to work
    for word in words: #translate each word separately 
      print word,'in Morse code is'
      for i in word: #loop to do each letter separately
        for letter in range(0,len(Translator.morseCode),2): #find the corresponding letter in the list data
          if i==Translator.morseCode[letter]: #check if they match
            print Translator.morseCode[letter+1] #print the morse for that letter

#method to print the data
  def display(self): #receives nothing
    print 'Letters of the alphabet with equivalent Morse code'
    for i in range(0,len(Translator.morseCode),2): #loop to control line prints
      print Translator.morseCode[i]+'  '+Translator.morseCode[i+1]
