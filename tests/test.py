from __future__ import print_function
import os
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_env(self):
        print('Unit Test ENV variables set')
        envs = os.environ.keys()
        for key in envs:
            print(key + ' = ' + os.environ[key])
        self.assertGreater(len(envs), 0)


if __name__ == '__main__':
    unittest.main()
