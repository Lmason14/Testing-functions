from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Laura")
    reminder.remind_me_to("Do the washing")
    result = reminder.remind()
    assert result == "Do the washing, Laura!"