# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

class Message:
  def __init__(self, address, message):
    self.address = address
    self.message = message
    self.account_sid = 'ACa501a06dafed4241aa685f02efec79c0'
    self.auth_token = '33e7d7b61d55f8e49979c2d10411cfe5'
    self.client = Client(self.account_sid, self.auth_token)

  def printMessage(self):
    print("The message is " + self.message)

  def sendMessage(self):
      message = self.client.messages \
          .create(
          body=self.message,
          from_='+14054450183',
          to=self.address
      )

      print(message.sid)







