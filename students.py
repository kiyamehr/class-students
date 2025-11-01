class Students:
    def __init__(self, name):
        self.name = name
        self.score = []
        self.avg = 0

    def add_score(self, s_score):
        try:
            self.score.append(s_score)
        except ValueError as exc:
            raise f"Error! Your Error was: {exc}"
        except Exception as exc:
            raise f"Error! Your Error was: {exc}"

    # will return '0' if the average() isnt called
    def average(self):
        try:
            self.avg = sum(self.score) / len(self.score)

        except ZeroDivisionError as exc:
            raise f"{exc}"
        except Exception as exc:
            raise f"Error! Your Error was: {exc}"
        else:
            return f"The Average Score is '{self.avg}'"

    def get_highest(self):
        try:
            get = f"Highest Score Is: '{max(self.score)}'"
        except Exception as exc:
            raise f"{exc}"
        else:
            return get

    def get_lowest(self):
        try:
            get = f"Lowest Score Is: '{min(self.score)}'"
        except Exception as exc:
            raise f"{exc}"
        else:
            return get

    def remove_score(self, score):
        self.score.remove(score)

    def __str__(self):
        try:
            pr = f"Name: {self.name}, Avg: '{self.avg}'"
        except Exception as exc:
            raise f"{exc}"
        else:
            return pr


student1 = Students("Kia")

student1.add_score(20)
student1.add_score(17)
student1.add_score(14)
student1.add_score(14)

print(student1.average())
print(student1)
print(student1.get_highest())
print(student1.remove_score(14))
print(student1.score)
print("Test pull request")
