#linux yum install python3
#pip3 install line-bot-sdk
#pip3 install netifaces
from linebot import LineBotApi
from linebot.models import TextSendMessage
import netifaces as ni
import subprocess

CHANNEL_ACCESS_TOKEN = "GQqR+YSGVHlUSrZcZtZeWGZJus7EZayo7qEZXvjHt6AbcSrsEPTvetC1q2Ssw4AQAyHyZuTC6OFiFSLA7hs+aY93RmX3QpSvzxHBJP1cg6stvTVs3qd7xToKjBQaZgTim41s62fpgm32sWv4dMTW6wdB04t89/1O/w1cDnyilFU="

#netifaces.interfaces()
#netifaces.gateways()
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']

a,b = subprocess.Popen("ping google.com -c4 | grep rtt && date +%Y-%m-%d' '%T",stdout=subprocess.PIPE,shell=True).communicate()

r = float(str(a).split("/")[4])
if r < 10:
    net = "良好"
elif r > 13:
    net = "不佳"
else:
    net = "尚可"

l = str(a).split("\\n")[1]+" "+"program started from"+" "+ip+","+" "+"rtt(avg):"+str(r)+" "+"ms"
print(l)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text = "Jeff-日誌系統已經啟動! IP:"+ip+",網路狀態"+net+"!"))

o = open("log.txt","a")
o.write(l+"\n")
o.close()
