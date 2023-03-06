import pytest
from lib.password_checker import *

def test_if_identifes_valid_password():
    password_checker = PasswordChecker()
    check = password_checker.check('12345678')
    assert check == True
    
    #if not valid
    #we get an error message
    
def test_if_not_valid_returns_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        check = password_checker.check('123456')
    err_message = str(e.value)
    err_message == "Invalid password, must be 8+ characters."   