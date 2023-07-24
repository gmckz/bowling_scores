from lib.game import Game
from lib.frame import Frame

"""
Helper function: create frames
"""
def create_frames():
    frame1 = Frame()
    frame1.first_throw(1)
    frame1.second_throw(4)
    frame2 = Frame()
    frame2.first_throw(4)
    frame2.second_throw(5)
    frame3 = Frame()
    frame3.first_throw(6)
    frame3.second_throw(4)
    frame4 = Frame()
    frame4.first_throw(5)
    frame4.second_throw(5)
    frame5 = Frame()
    frame5.first_throw(10)
    frame6 = Frame()
    frame6.first_throw(10)
    frame7 = Frame()
    frame7.first_throw(7)
    frame7.second_throw(3)
    frame8 = Frame()
    frame8.first_throw(6)
    frame8.second_throw(4)
    frame9 = Frame()
    frame9.first_throw(10)
    frame10 = Frame()
    frame10.first_throw(2)
    frame10.second_throw(7)
    list_of_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]
    return list_of_frames

"""
When I create an instance of Game
initially it has property frames, a list of frame objects
"""
def test_initially_game_has_frame_properties():
    list_of_frames = create_frames()
    game = Game(list_of_frames)
    assert game.frames == list_of_frames

"""
When I call Games#calculate_points 
it returns the total points of all frames (sum of frame.score)
"""
def test_calculate_points_returns_total_points():
    list_of_frames = create_frames()
    game = Game(list_of_frames)
    total_points = game.calculate_points()
    assert total_points == 93
    assert game.score == 93

"""
When I call Games#tenth_frame_bonus_required and the last frame of the game is neither
a spare or a strike it returns False 
"""
def test_bonus_frame_false_when_last_frame_not_strike_or_spare():
    list_of_frames = create_frames()
    final_frame = Frame()
    final_frame.first_throw(1)
    final_frame.second_throw(1)
    list_of_frames[-1] = final_frame
    game = Game(list_of_frames)
    assert game.tenth_frame_bonus_required() == False

"""
When I call Games#tenth_frame_bonus_required and the last frame of the game is a strike
or spare it returns True 
"""
def test_bonus_frame_true():
    list_of_frames1 = create_frames()
    final_frame1 = Frame()
    final_frame1.first_throw(10)
    list_of_frames1[-1] = final_frame1
    game1 = Game(list_of_frames1)
    assert game1.tenth_frame_bonus_required() == True
    list_of_frames2 = create_frames()
    final_frame2 = Frame()
    final_frame2.first_throw(9)
    final_frame2.second_throw(1)
    list_of_frames2[-1] = final_frame2
    game2 = Game(list_of_frames2)
    assert game2.tenth_frame_bonus_required() == True

"""
When I call Games#enter_bonus_throw_s when bonus throws is required due to a 
strike in the last frame
tenth frame score is updated with bonus throws
"""

def test_enter_bonus_frame_after_strike():
    list_of_frames = create_frames()
    final_frame = Frame()
    final_frame.first_throw(10)
    list_of_frames[-1] = final_frame
    game = Game(list_of_frames)
    game.enter_bonus_throw_s(2, 3)
    assert game.frames[-1].score == 15
    assert game.frames[-1].strike == False
    assert game.frames[-1].spare == False

"""
When I call Games#enter_bonus_throws when a bonus frame is required due to a 
spare in the last frame
frames is updated with a bonus frame that has one throw
"""

def test_enter_bonus_frame_after_spare():
    list_of_frames = create_frames()
    final_frame = Frame()
    final_frame.first_throw(1)
    final_frame.second_throw(9)
    list_of_frames[-1] = final_frame
    game = Game(list_of_frames)
    game.enter_bonus_throw_s(2)
    assert game.frames[-1].score == 12
    assert game.frames[-1].strike == False
    assert game.frames[-1].spare == False

"""
When I call Games#calculate_bonus_points
any frame with a strike has its score updated with the next frames score
unless that score is a strike 
"""
def test_calculate_bonus_points_updates_strike_frame_score_with_bonus_points():
    list_of_frames = create_frames()
    game = Game(list_of_frames)
    game.calculate_bonus_points()
    frame5 = game.frames[4]
    frame6 = game.frames[5]
    frame9 = game.frames[8]
    assert frame5.score == 10
    assert frame6.score == 20
    assert frame9.score == 19

"""
When I call Games#calculate_bonus_points after calling Games#enter_bonus_frame
any frame with a spare has its score updated with the next score of the 
first throw of the next frame
"""
def test_calculcate_bonus_points_updates_spare_frame_score_with_bonus_points():
    list_of_frames = create_frames()
    game = Game(list_of_frames)
    game.calculate_bonus_points()
    frame3 = game.frames[2]
    frame4 = game.frames[3]
    frame7 = game.frames[6]
    frame8 = game.frames[7]
    assert frame3.score == 15
    assert frame4.score == 20
    assert frame7.score == 16
    assert frame8.score == 20

"""
Perfect game scores 300 points
"""
frame1 = Frame()
frame1.first_throw(10)
frame2 = Frame()
frame2.first_throw(10)
frame3 = Frame()
frame3.first_throw(10)
frame4 = Frame()
frame4.first_throw(10)
frame5 = Frame()
frame5.first_throw(10)
frame6 = Frame()
frame6.first_throw(10)
frame7 = Frame()
frame7.first_throw(10)
frame8 = Frame()
frame8.first_throw(10)
frame9 = Frame()
frame9.first_throw(10)
frame10 = Frame()
frame10.first_throw(10)
list_of_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]
game = Game(list_of_frames)
game.enter_bonus_throw_s(10, 10)
game.calculate_bonus_points()
assert game.calculate_points() == 300
assert game.score == 300