import sys
import os
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
from requests import get

def scraper():
	print("Getting data...")
	url = "https://www.blockchain.com/btc/unconfirmed-transactions"
	c1 = "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"
	c2 = "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"
	returns = get(url)
	
	print("Creating soup...")
	soup = BeautifulSoup(returns.text, "html.parser")
	hases = soup.find_all("a", class_=c1)[1:]
	info = soup.find_all("span", class_=c2)[3:]
	
	print("Filling Dataframe...")
	transactions = []
	for i in range(0,48):
		btc = info[i*3+1].text[:-4]
		dolar = info[i*3+2].text[1:].replace(',','')
		transactions.append([hases[i].text, info[i*3].text, float(btc), float(dolar)])
	
	df = pd.DataFrame(transactions, columns=["hash","time","BTC","USD"])
	df_f = df.sort_values(by=["USD"], ascending=False)
	
	print("saving result to JSON file...")
	#print(df_f.head(1))

while(True):
	os.system("clear")
	scraper()
	for i in tqdm(range(1,61)):
		sleep(1)
