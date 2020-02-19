import datetime


class Event:
    def __init__(self, time, description, duration= 24):
        self.time = time
        self.description = description
        self.duration = duration

    def changetime(self, time):
        self.time = time


class Assignment:
    def __init__(self, time, description, duration=24):
        self.time = time
        self.description = description
        self.duration = duration

    def changetime(self, time):
        self.time = time


class Work:
    def __init__(self, time, description, duration=24):
        self.time = time
        self.description = description
        self.duration = duration

    def changetime(self, time):
        self.time = time


class Meeting:
    def __init__(self, time, description, duration=24):
        self.time = time
        self.description = description
        self.duration = duration

    def changetime(self, time):
        self.time = time
