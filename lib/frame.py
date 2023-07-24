class Frame:

    def __init__(self):
        self.score = 0
        self.throw_one_score = 0
        self.throw_two_score = 0
        self.pins_remaining = 10
        self.number_of_throws = 2
        self.strike = False
        self.spare = False
    
    def first_throw(self, pins_knocked):
        if self.number_of_throws == 2 and self.throw_is_valid(pins_knocked):
            self.score = pins_knocked
            self.throw_one_score = pins_knocked
            self.pins_remaining -= pins_knocked
            if pins_knocked < 10:
                self.number_of_throws = 1
            else:
                self.number_of_throws = 0
                self.strike = True
        else:
            return "Throw is invalid"
        
    def second_throw(self, pins_knocked):
        if self.number_of_throws == 1 and self.throw_is_valid(pins_knocked):
            self.score += pins_knocked
            self.throw_two_score = pins_knocked
            self.pins_remaining -= pins_knocked
            self.number_of_throws = 0
            if self.pins_remaining == 0:
                self.spare = True
        else:
            return "Throw is invalid"
        
    def throw_is_valid(self, pins_knocked):
        return 0 <= pins_knocked <= self.pins_remaining and self.number_of_throws > 0
        