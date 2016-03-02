#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 2/29/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

import urllib #because of use of url

class Translator:
  morseCode=[] #class attribute, universal to class

  def __init__(self,morseURL):
    connection=urllib.urlopen(morseURL) #opens a connection to url
    morseCodeData=connection.read() #read in data
    morseCodeData=morseCodeData.split() #split on space
    connection.close()
    Translator.morseCode=morseCodeData #even index are morse, odd are letters

#
  def translate(self,phrase):
    words=phrase.split()
    for word in words:
      print word,'in Morse code is'
      for i in word:
        for letter in range(0,len(Translator.morseCode),2):
          if i==Translator.morseCode[letter]:
            print Translator.morseCode[letter+1]

  def display(self):
    print 'Letters of the alphabet with equivalent Morse code'
    for i in range(0,len(Translator.morseCode),2):
      print Translator.morseCode[i]+'  '+Translator.morseCode[i+1]
