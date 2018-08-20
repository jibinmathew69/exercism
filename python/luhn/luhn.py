class Luhn(object):
    def __init__(self, card_num):
        try:
            card_num = card_num.replace(" ","")
            self.card_num = [int(x) for x in card_num]
        except:
            self.valid = False
            return
        length = len(card_num)
        if length<2:
            self.valid = False
            return

        self.valid = 0 == (sum(self.card_num[-1::-2])+sum([self.double(x) for x in self.card_num[-2::-2]]))%10

    def double(self,num):
        dnum = num*2
        if dnum>9:
            return dnum-9
        else:
            return dnum
    def is_valid(self):
        return self.valid
