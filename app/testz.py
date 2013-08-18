from nose.tools import *

# implementation

def sumz(a, b):
  return a + b


def test_sumz():
  assert_equal(sumz(1, 3), 4)
