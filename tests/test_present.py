import pytest   
from lib.present import Present

#when we wrap an item
#we get it back when unwrapping

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(15)
    assert present.unwrap() == 15
    
# if we unwrap before wrapping
# we get an error message

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."
    
# If we try to wrap an already wrapped present
# we get an error message

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(40)
    with pytest.raises(Exception) as e:
        present.wrap(50)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

