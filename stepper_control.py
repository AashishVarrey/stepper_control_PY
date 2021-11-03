#necessary modules
import json
import cgi
import cgitb
cgitb.enable() 
from urllib.request import urlopen
from urllib.parse import urlencode

#api key for thingspeak channel
#change this to appropriate key!!!
api = "6RLY9LJUYXDJ84BJ"

#get data from html form
data = cgi.FieldStorage()
s1 = data.getvalue('submit')
s2 = data.getvalue('anglevalue')

#change angle to zero if zero angle button is pressed
if s1 == "Zero Angle":
  s2 = 0

#dictionary containing angle information, only append new angle information
info = {"newangle":s2}

#write angle to text file
with open('Lab5.txt','w') as f:
  json.dump(info,f)

#send angle information to thingspeak
params = {
  "api_key":api,
  1: s2
}
params = urlencode(params)
url = "https://api.thingspeak.com/update?" + params
urlopen(url)

print("Content-type: text/html\n\n")
print("""
<html>
<style>
h1 {color:red;}
</style>
<h1> Lab 5 - Motor Control </h1>
<body>
<form action="/cgi-bin/stepper_control.py" method ="POST">
Angle: <input type = "text" name= "anglevalue"> <br>
<input type = "submit" name = "submit" value = "Submit Angle">
<br>
<input type = "submit" name = "submit" value = "Zero Angle">
<br>
</form>

<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550893/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs+Time&type=line&xaxis=Time&yaxis=Motor+Angle"></iframe>
<br>
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550893/widgets/374796"></iframe>
</body>
</html>
"""
)
