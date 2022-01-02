import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

#find my ip address function
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(query):
    try:
        return wikipedia.summary(query,sentences=2)
    except Exception:
        return "Sorry, I could not find any results for your query."

def play_on_youtube(query):
    kit.playonyt(query)

def search_on_google(query):
    return kit.search(query)

def send_whatsapp_message(number,message):
    kit.sendwhatmsg_instantly(f'+91{number}',message)

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

def send_email(receiver_address,subject,message):
    try:
        email = EmailMessage()
        email['from'] = EMAIL
        email['to'] = receiver_address
        email['subject'] = subject
        email.set_content(message)
        
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.quit()
        return "Email sent successfully!"
    except Exception:
        return "Sorry, I could not send your email."

NEWS_API_KEY = config('NEWS_API_KEY')

def get_latest_news():
    news_headlines = []
    res = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general').json()
    for news in res['articles']:
        news_headlines.append(news['title'])
    return news_headlines

