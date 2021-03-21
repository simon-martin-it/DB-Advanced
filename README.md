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

## 3: Redis
I need to install redis as I can use it as a caching mechanism.
I have reworked the programs, and now you need to the following to start:
<ul>
  <li><code>chmod +x start.sh</code></li>
  <li><code>./start.sh</code></li>
</ul>
This bash file will initialise and install mongodb and redis all at once.
Typing is tiresome!! 
Lastly run <code>python3 scraper.py</code> once more to start the scraper.

## Docker
For the last part of the exercise, we need to install Docker. Please follow the necessary steps on the Docker website to properly install Docker on your system.
<br>
I need to pour the first version of the scraper into a docker image.
<br><br>
You can find the docker image using the following link: <a href="https://hub.docker.com/r/r0620457/btc-scraper">Docker</a>

## Container Orchestration
Fancy word! This final part requires the aqcuisition of mongodb and redis images. Do this with the following commands:
<ul>
  <li><code>sudo docker pull mongo</code></li>
  <li><code>sudo docker pull redis</code></li>
</ul>

 
