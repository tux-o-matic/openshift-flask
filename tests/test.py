from __future__ import print_function
import os
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        print('Unit Test ENV variables set')
        for key in os.environ.keys():
            print(key + ' = ' + os.environ[key])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
