from lib.string_builder import *

# when we dont add anything 
# it returns an empty string

def test_first_output_returns_empyty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""
    
# when we add a string
# the string is outputted

def test_adding_a_string_is_outputted():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.output() == "Hello"
    
    # when we add a single string
    #the size reflects the size of that string

def test_adding_a_string_is_outputted():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5
    
# when we add muiltiple strings
# the output is concatenated

def test_adding_muiltiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "Hello world"