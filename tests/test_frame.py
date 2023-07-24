from lib.frame import Frame

"""
When I create an instance of Frame its properties are initially
score = 0, pins_remaining = 10, number of throws = 2, strike = False
and spare = False
"""
def test_frame_initialisies_with_properties():
    frame = Frame()
    assert frame.score == 0
    assert frame.pins_remaining == 10
    assert frame.number_of_throws == 2

"""
Frame#throw_is_valid returns True when valid conditions met
first throw is valid
second throw is valid 
"""
def test_throw_is_valid():
    #throw is valid = True
    frame1 = Frame()
    assert frame1.throw_is_valid(0) == True
    assert frame1.throw_is_valid(1) == True
    assert frame1.throw_is_valid(9) == True
    assert frame1.throw_is_valid(10) == True
    #throw is valid = False
    frame2 = Frame()
    assert frame2.throw_is_valid(-1) == False
    assert frame2.throw_is_valid(11) == False
    #valid first throw, second throw is valid
    frame3 = Frame()
    frame3.first_throw(8)
    assert frame3.throw_is_valid(2) == True
    assert frame3.throw_is_valid(1) == True
    assert frame3.throw_is_valid(0) == True
    #valid first throw (strike), second throw is not valid
    frame4 = Frame()
    frame4.first_throw(10)
    assert frame4.throw_is_valid(1) == False
    #valid first throw, second throw is not valid
    frame5 = Frame()
    frame5.first_throw(6)
    assert frame5.throw_is_valid(5) == False

"""
When I call Frame#first_throw 
score, pins_remaining, number_of_throws and strike are updated
"""
def test_first_throw_updates_properties():
    frame1 = Frame()
    frame1.first_throw(5)
    assert frame1.score == 5
    assert frame1.pins_remaining == 5
    assert frame1.number_of_throws == 1
    assert frame1.strike == False
    frame2 = Frame()
    frame2.first_throw(10)
    assert frame2.score == 10
    assert frame2.pins_remaining == 0
    assert frame2.number_of_throws == 0
    assert frame2.strike == True

"""
When I call Frame#first_throw with invalid throw
it returns message "Throw is invalid" 
and properties are unchanged
"""
def test_first_throw_invalid():
    frame1 = Frame()
    assert frame1.first_throw(-1) == "Throw is invalid"
    assert frame1.score == 0
    assert frame1.pins_remaining == 10
    assert frame1.number_of_throws == 2
    assert frame1.strike == False
    frame2 = Frame()
    assert frame2.first_throw(11) == "Throw is invalid"
    assert frame2.score == 0
    assert frame2.pins_remaining == 10
    assert frame2.number_of_throws == 2
    assert frame2.strike == False

"""
When I call Frame#second_throw with valid throw
properties are updated
"""
def test_second_throw_updates_properties():
    frame1 = Frame()
    frame1.first_throw(0)
    frame1.second_throw(3)
    assert frame1.score == 3
    assert frame1.pins_remaining == 7
    assert frame1.number_of_throws == 0
    assert frame1.spare == False
    frame2 = Frame()
    frame2.first_throw(7)
    frame2.second_throw(3)
    assert frame2.score == 10
    assert frame2.pins_remaining == 0
    assert frame2.number_of_throws == 0
    assert frame2.spare == True
    frame2.first_throw(0)
    frame2.second_throw(10)
    assert frame2.score == 10
    assert frame2.pins_remaining == 0
    assert frame2.number_of_throws == 0
    assert frame2.spare == True

"""
When I call Frame#second_throw with invalid throw
it returns message "Throw is invalid" and properties are unchanged
"""
def test_second_throw_invalid():
    frame1 = Frame()
    frame1.first_throw(10)
    assert frame1.second_throw(0) == "Throw is invalid"
    assert frame1.score == 10
    assert frame1.pins_remaining == 0
    assert frame1.number_of_throws == 0
    assert frame1.strike == True
    assert frame1.spare == False
    frame2 = Frame()
    frame2.first_throw(1)
    assert frame2.second_throw(10) == "Throw is invalid"
    assert frame2.score == 1
    assert frame2.pins_remaining == 9
    assert frame2.number_of_throws == 1
    assert frame2.strike == False
    assert frame2.spare == False