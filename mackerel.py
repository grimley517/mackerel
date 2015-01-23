#! usr/bin.env python3.4
import sys
import urllib.request

WORDS = 'https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt'

def check(station, word):
    '''checks for the letters in a word, to see if they appear ina stations name.
    returns True if they do, False otherwise
    '''
    for letter in word:
        if letter in station:
            return (True)
    return (False)
    
def checkAll(word):
    '''uses the check function to check for the presence of a word in all stations'''
    answers = []
    stationfile = open('stationlist.txt')
    for station in stationfile.read().split('\n'):
        station = station.lower()
        if "\t" in station:
            station = station.replace("\t","")
        if not check(station, word):
            answers.append(station)
    return (answers)

def getWords():
    '''extracts the words from the wordlist,
    returns them as a list of strings'''
    req = urllib.request.Request(url = WORDS)
    text = urllib.request.urlopen(req)
    answer = str(text.read())
    answers = answer.split("\\n")
    return (answers)

def reduceWords(wordlist):
    '''Knowing that mackerel is a working word, 
    we can ignore words that are smaller than 8 letters'''
    answer = []
    for word in wordlist:
        if len(word) >= len("mackerel"):
            answer.append(word)
    return (answer)

def getSingleStationMatches(wordlist):
    words = {}
    for word in wordlist:
        stations = checkAll(word)
        if len(stations) == 1:
            words[word] = stations
    return (words)
    
if __name__ == "__main__":
    wordlist = getWords()
    wordlist = reduceWords(wordlist)
    worddict = getSingleStationMatches(wordlist)
    dictlist = worddict.keys()
    newlist = sorted(dictlist, key = lambda x: len(x), reverse = True)
    for word in newlist:
        print("{1} is the only station with no letters from the word {0}\n".format(word, worddict[word][0].title()))
    print (len(worddict))
    