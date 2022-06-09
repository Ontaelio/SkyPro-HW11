class Person:
    """
    A class to store candidates' details
    """
    def __init__(self, tmp_d):
        self.id = tmp_d['id']
        self.name = tmp_d['name']
        self.picture = tmp_d['picture']
        self.position = tmp_d['position']
        self.gender = tmp_d['gender']
        self.age = tmp_d['age']
        self.skills = tmp_d['skills'].split(', ')
