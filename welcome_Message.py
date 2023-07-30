# import gtts
# from playsound import playsound
# tts = gtts.gTTS("welcome back kia   noosh." , lang='en')
# tts.save("hello.mp3")
# playsound("hello.mp3")
#
import datetime
import psutil as sensors

from imap_tools import MailBox, AND
import pytz

utc=pytz.UTC


five_dayes_befor = datetime.datetime.now() - datetime.timedelta(days = 5)
five_dayes_befor = utc.localize(five_dayes_befor)

mb = MailBox("imap.gmail.com").login("kia.vadaei@gmail.com", "mqjfoytfssggqtgk")
messages = mb.fetch(criteria=AND(seen=False, from_="gmail.com"),
                        mark_seen=False,
                        bulk=True)
i = 0
senders = []
for msg in messages:
  # msg.date = utc.localize(msg.date)
  if msg.date > five_dayes_befor :
      senders.append(msg.from_values.name)
  i += 1
  if i == 10:
    break


import pyttsx3

now = datetime.datetime.now()
charge_p = sensors.sensors_battery().percent

engine = pyttsx3.init()

text0 = "welcome back kia   noosh."
if(now.hour < 12 and now.hour > 23):
    text1 = 'Good Morning sir.'
elif(now.hour < 17 and now.hour > 11):
    text1 = 'Good AfterNoon sir.'
elif(now.hour < 22 and now.hour > 16):
    text1 = 'Good Evening sir.'
elif(now.hour < 24 and now.hour > 21):
    text1 = 'Good Night sir.'
else:
    text1 = 'Good Day sir.'

text2 = 'today is: ' + str(now.day) + 'th of ' + str(now.strftime("%B")) +' of ' + str(now.year)
text3 = 'the time is: ' +str(now.hour) + ' and ' + str(now.minute)
engine.setProperty("voice", engine.getProperty("voices")[0].id)
engine.setProperty("rate", 170)

engine.say(text0)
engine.say(text1)
engine.say(text2)
engine.say(text3)
engine.say('Your laptop battery has ' + str(charge_p) + '% charge')
if charge_p < 60 :
    engine.say('I suggest you connect it to the charger')
if len(senders) == 0:
    engine.say('You have not received any new emails in the last 5 days')
elif len(senders) == 1:
    engine.say('You have found ' + str(len(senders)) + ' new emails from: ' + senders[0])
else:
    engine.say('You have found ' + str(len(senders)) + ' new emails from these people: ')
    for s in senders:
        engine.say(s)
# play the speech
engine.runAndWait()
