import sys
import os
import json
import redis
import zlib
import pickle
import pandas as pd
import pymongo as pm
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
from requests import get

def connect():
	print("Connecting to MongoDB Database...")
	client = pm.MongoClient("mongodb://localhost:27017/")
	db = client["DB-Advanced"]
	return db["Transactions"]

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
	for i in range(0,49):
		btc = info[i*3+1].text[:-4]
		dolar = info[i*3+2].text[1:].replace(',','')
		transactions.append([hases[i].text, info[i*3].text, float(btc), float(dolar)])

	df = pd.DataFrame(transactions, columns=["hash","time","BTC","USD"])

	print("Saving everything to Redis...")
	r = redis.StrictRedis(host="localhost", port=6379, db=0)
	r.setex("key", 60, zlib.compress(pickle.dumps(df)))

	print("Sorting and saving result to JSON file...")
	df_f = pickle.loads(zlib.decompress(r.get("key"))).sort_values(by=["USD"], ascending=False).head(1)
	t_info = {
		"Hash": df_f.iloc[0]["hash"],
		"Time": df_f.iloc[0]["time"],
		"BTC": df_f.iloc[0]["BTC"],
		"USD": df_f.iloc[0]["USD"]
	}

	with open(df_f.iloc[0]["hash"] + ".json", "w", encoding="utf-8") as f:
		json.dump(t_info, f, ensure_ascii=False, indent=4)

	print("Inserting into MongoDB Table...")
	return t_info


while(True):
	os.system("clear")
	db = connect()
	db.insert_one(scraper())
	for i in tqdm(range(1,61)):
		sleep(1)
