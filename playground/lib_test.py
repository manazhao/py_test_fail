import unittest

from playground.lib import print_message
from playground.lib import print_string


class LibTest(unittest.TestCase):

  def testPrint(self):
    print_message()
    print_string()


if __name__ == '__main__':
  unittest.main()
