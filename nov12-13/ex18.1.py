import sys
class Time(object):
 def __init__(self, hour=0, minute=0):
  self.hour = hour
  self.minute = minute
 def __lt__(self, other):
  return (self.hour, self.minute) < (other.hour, other.minute)
 def __gt__(self, other):
  return (self.hour, self.minute) > (other.hour, other.minute)
 def __eq__(self, other):
  return (self.hour, self.minute) == (other.hour, other.minute)
a = Time(hour=8, minute=39)
b = Time(hour=10, minute=30)

print(a < b)
