#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 3/1/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#test file for Translator class for project 4

from Translator import* #import class

url=raw_input('Enter the URL for the Morse code:') #receive URL
transTest=Translator(url) #create Translator object

transTest.display() #call the display method

sentence=raw_input('Enter a sentence in CAPS:') #receive sentence to translate

#call translate method and translate sentence
transTest.translate(sentence)

raw_input('Press ENTER to close')
