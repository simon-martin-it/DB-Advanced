# DB-Advanced
Welcome to my awesome repository for the assignment of Databases Advanced. Here I will upload code for the teacher to review.

## 1: Webscraper
<ul>
  <li>Clone the <a href="https://github.com/simon-martin-it/DB-Advanced">repo</a></li>
  <li>Navigate to the folder with the py file</li>
  <li>Install the required packages wtih <code>pip3 install -r req.txt</code></li>
  <li>run <code>chmod +x scraper.py</code> very annoying but yeah</li>
  <li>Run the program wtih<code>python3 scraper.py</code></li>
</ul>

## 2: MongoDB
For the second part of this exercise, we need to install MongoDB on the machine. I have written all the necessary commands in the mongod.sh script, so follow these steps to get it up and running:
<ul>
  <li><code>chmod +x mongod.sh</code></li>
  <li><code>./mongod.sh</code></li>
</ul>
Then, run<code>scraper.py</code> again.
To view the added row in the MongoDB database, use <code>db.Transactions.find()</code> in the mongo cli.
 
