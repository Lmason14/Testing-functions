from lib.gratitudes import *

def test_string_is_added_and_returned():
    gratitudes = Gratitudes()
    gratitudes.add('animals')
    assert gratitudes.format() == "Be greatful for: animals"