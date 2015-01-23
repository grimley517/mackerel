#! usr/bin/env python3.4
import unittest
import mackerel as m

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass
    
    def test1(self):
        '''tests the check functionality'''
        station = 'euston'
        check1 = "e"
        check2 = "a"
        self.assertTrue(m.check(station, check1), msg = "e not found in euston")
        self.assertFalse(m.check(station, check2), msg = "a found in euston")
    
    def test2(self):
        '''Checks that the only station without the letters in mackerel 
        is st johns wood'''
        left = m.checkAll("mackerel")
        right = ["st. john's wood"] 
        msg = "the letters in mackerel appear in {0},".format(left)
        self.assertEqual(left, right, msg = msg)
    
    def test3(self):
        '''checks that the word list can be opened'''
        wordlist = m.getWords()
        #since this is a github wordlist assume that it may grow
        testlength = 235880
        msg = "the list of words has shrunk"
        self.assertGreater(len(wordlist), testlength, msg = msg)
    
    def test4(self):
        '''checks the reduced wordlist'''
        wordlist = m.getWords()
        wordlist = m.reduceWords(wordlist)
        testlength = 177176
        msg = "the list of words has shrunk to {0}".format(len(wordlist))
        self.assertGreater(len(wordlist), testlength, msg = msg)

    

if __name__ == '__main__':
    unittest.main(verbosity = 2)