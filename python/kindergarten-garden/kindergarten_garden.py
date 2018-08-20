class Garden(object):
    def __init__(self, diagram,students = [
                    "Alice",
                    "Bob",
                    "Charlie",
                    "David",
                    "Eve",
                    "Fred",
                    "Ginny",
                    "Harriet",
                    "Ileana",
                    "Joseph",
                    "Kincaid",
                    "Larry"
                ]):
        self.students = sorted(students)
        self.plantMap = {
            'V' : "Violets",
            'G' : "Grass",
            'C' : "Clover",
            'R' : "Radishes"
        }
        self.row = diagram.split('\n')

    def plants(self,student):
        try:
            index = self.students.index(student)
        except ValueError:
            raise ValueError("invalid student")

        plantindex = index*2
        return [self.plantMap[x] for x in [self.row[0][plantindex],self.row[0][plantindex+1],self.row[1][plantindex],self.row[1][plantindex + 1]]]
