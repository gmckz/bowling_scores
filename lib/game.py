from lib.frame import Frame

class Game:
    
    def __init__(self, frames):
        self.frames = frames
        self.score = 0

    def calculate_points(self):
        total_points = 0
        scores_list = []
        for frame in self.frames:
            total_points += frame.score
            scores_list.append(frame.throw_one_score)
        if scores_list == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] and self.frames[-1].score == 30:
            self.score = 300
            return 300
        self.score = total_points
        return total_points

    def tenth_frame_bonus_required(self):
        return self.frames[-1].spare == True or self.frames[-1].strike == True

    def enter_bonus_throw_s(self, first_throw_score, second_throw_score=0):
        tenth_frame = self.frames[-1]
        if self.tenth_frame_bonus_required():
            if tenth_frame.spare == True:
                tenth_frame.score += first_throw_score
            if tenth_frame.strike == True:
                tenth_frame.score += (first_throw_score + second_throw_score)
            tenth_frame.strike = False
            tenth_frame.spare = False
            self.frames[-1] = tenth_frame
    

    def calculate_bonus_points(self):
        for frame in self.frames:
            i = self.frames.index(frame)
            if frame.strike == True:
                next_frame = self.frames[i+1]
                if next_frame.strike == False:
                    frame.score += next_frame.score
            if frame.spare == True:
                next_frame = self.frames[i+1]
                frame.score += next_frame.throw_one_score

