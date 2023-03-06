from lib.counter import *

    # when we add dont add any numbers
    # it returns with zero
    

def test_counter_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
    
    # when we add a single number to the counter
    # it is reflected in the final count
    
    
def test_counter_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
    
    
    # when we add multiple numbers to the counter
    # the sum of those numbers is the final count


def test_counter_adds_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(7)
    counter.add(2)
    assert counter.report() == "Counted to 9 so far."