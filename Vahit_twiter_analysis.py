import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time
import Utils_cagri as util
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import pandas as pd
import numpy as np
from os import path
from PIL import Image
import textblob
from textblob import TextBlob
from textblob import Word
import  seaborn as sns
import datetime
import matplotlib.pyplot as plt
atık=["https","t","o","bir","ne","neden","ve", "bu", "bir", "ile", "as", "veya", "icin", "boyle", "ad", "soyad", "iliskin", "dosya", "esas",
                "adi", "soyadi", '', "muvekkilimin",
                "gore", "nedeniyle", "adres", "fazla", "az", "tc", "itibaren", "tckimlik", "olarak", "sonra", "no",
                "ne", "niye", "neden", "nicin", "dolayi","co","da","mi","togg https","co","a","b","c","d","w","x","e","f","g","h","ı",
      "i","o","j","k","l","m","n","u","bi","si","ha","o","ö","p","r","s","ş","t","u","ü","v","y","z","nasil","mu","ki","cok","https t","t co","RT","https  t"
      "değil","var","vardır","diğer","için","https://t.co/","t.co","https://t","t","t.co/","https   t","https  t", "teşekkür","teşekkürler","Çok teşekkür"
      ]
df=pd.DataFrame()




df_dısPolitika=pd.read_csv("Vahit.csv",index_col=0)
df_dısPolitika["Created at"]=pd.to_datetime(df_dısPolitika["Created at"])
df_dısPolitika["Year"]=df_dısPolitika["Created at"].apply(lambda x: x.year)
df_dısPolitika["Month"]=df_dısPolitika["Created at"].apply(lambda x: x.month)
df_dısPolitika["Day"]=df_dısPolitika["Created at"].apply(lambda x: x.day)
df_dısPolitika["Hour"]=df_dısPolitika["Created at"].apply(lambda x: x.hour)
df_dısPolitika['Text'] = df_dısPolitika['Text'].str.replace('[^\w\s]','')
df_dısPolitika['Text'] = df_dısPolitika['Text'].str.replace('\d','')
df_dısPolitika['Text'] = df_dısPolitika['Text'].apply(lambda x: str(x))
df_dısPolitika['Text']=df_dısPolitika['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
at=df_dısPolitika['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
at=pd.DataFrame(at,columns=['Text'])
df_dısPolitika['Text']=at['Text']
yorum = " ".join(i for i in df_dısPolitika.Text)
text=WordCloud(background_color="black",contour_color="firebrick",contour_width=3,max_words=1000).generate(yorum)
plt.figure(1)
plt.imshow(text,interpolation="bilinear")
plt.axis("off")
plt.show()

plt.figure(2)
a=sns.barplot(x=[f"{i[0]}/{i[1]}"for i in df_dısPolitika.groupby(["Year","Month"])["Like Count"].sum().index.to_list()],
            y=df_dısPolitika.groupby(["Year","Month"])["Like Count"].sum())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Like Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin ay kırılımlı like sayısı")
plt.show()

plt.figure(3)
a=sns.barplot(x=df_dısPolitika.groupby(["Hour"])["Like Count"].sum().index.to_list(),
            y=df_dısPolitika.groupby(["Hour"])["Like Count"].sum())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Like Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin saat kırılımlı like sayısı")
plt.show()


plt.figure(3)
a=sns.barplot(x=[f"{i[0]}/{i[1]}"for i in df_dısPolitika.groupby(["Year","Month"])["Like Count"].count().index.to_list()],
            y=df_dısPolitika.groupby(["Year","Month"])["Like Count"].count())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin ay kırılımlı tweet sayısı")
plt.show()

plt.figure(4)
a=sns.barplot(x=df_dısPolitika.groupby(["Hour"])["Like Count"].count().index.to_list(),
            y=df_dısPolitika.groupby(["Hour"])["Like Count"].count())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Like Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin saat kırılımlı tweet sayısı")
plt.show()


plt.figure(5)
a=sns.barplot(x=[f"{i[0]}/{i[1]}"for i in df_dısPolitika.groupby(["Year","Month"])["Retweet Count"].sum().index.to_list()],
            y=df_dısPolitika.groupby(["Year","Month"])["Retweet Count"].sum())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Retweet Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin ay kırılımlı retweet sayısı")
plt.show()

plt.figure(6)
a=sns.barplot(x=df_dısPolitika.groupby(["Hour"])["Retweet Count"].sum().index.to_list(),
            y=df_dısPolitika.groupby(["Hour"])["Retweet Count"].sum())
util.show_values(a)
plt.xlabel("Date")
plt.ylabel("Retweet Count")
plt.xticks(rotation=45)
plt.title("Vahit Keskin saat kırılımlı retweet sayısı")
plt.show()