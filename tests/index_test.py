import unittest
import os
import json

path = os.getcwd()

class Test(unittest.TestCase):
    def setUp(self):
        print('Test Starts')

    def test_1(self):
        with open('../metadata.json') as fp:
            comment = fp.read()
            comment = json.loads(comment)
            element1 = comment["num_tokens"]
        print('test_1')
        self.assertEqual(element1, 39157)
