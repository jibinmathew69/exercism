class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.name_score = {
            "eggs"  : 1,
            "peanuts": 2,
            "shellfish":4,
            "strawberries":8,
            "tomatoes":16,
            "chocolate":32,
            "pollen":64,
            "cats":128
        }
        self.score_name = {
             1:"eggs"  ,
             2:"peanuts",
             4:"shellfish",
             8:"strawberries",
             16:"tomatoes",
             32:"chocolate",
             64:"pollen",
             128:"cats"
        }
        self.scores = sorted([1,2,4,8,16,32,64,128],reverse=True)
        self._lst = []

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        import math
        score = self.score
        while score > 2 ** 8:
            score -= 2 ** (int(math.log(score, 2)))
        for i in self.scores:
            if i<=score:
                self._lst.append(self.score_name[i])
                score -= i
            if score == 0:
                break

        return self._lst
