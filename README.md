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
For the second part of this exercise, we need to install MongoDB on the machine. Do this by following these commands:
<ul>
  <li><code>wget -qO https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -</code></li>
  <li><code>echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list</code></li>
  <li><code>sudo apt-get install -y mongodb-org</code></li>
  <li>Check if mongodb is running with <code> sudo systemctl status mongod</code></li>
</ul>
