class School(object):
    def __init__(self, name):
        self.schoolName = name
        self.grades = {}

    def grade(self,n):
        if n not in self.grades:
            return set()
        return self.grades[n]

    def add(self,student,grade):
        if grade not in self.grades:
            self.grades[grade] = set()

        self.grades[grade].add(student)

    def sort(self):
        temp = []
        for key in sorted(self.grades):
            temp.append((key,tuple(sorted(self.grades[key]))))

        return temp