from lib.report_length import *

def test_report_length_returns_correct_length():
    result = report_length('Hello')
    assert result == "This string was 5 characters long."
    
    
def test_report_length_given_int():
    result = report_length('5')
    assert result == "This string was 1 characters long."