import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
    self.assertNotEqual(englishToFrench(''),'') # Test for null input for englishToFrench        
    self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
    self.assertNotEqual(frenchToEnglish(''),'') # Test for null input for frenchToEnglish
    self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'
        
unittest.main()