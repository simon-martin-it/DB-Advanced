FROM ubuntu:latest
MAINTAINER simon-martin-it
COPY . .
RUN apt-get update -y
RUN apt-get install git python3 python3-pip -y
RUN apt-get install redis-server -y
RUN git clone https://github.com/simon-martin-it/DB-Advanced.git
RUN cd DB-Advanced
RUN pip3 install -r req.txt
RUN pip3 install requests
RUN pip3 install pymongo
RUN chmod +x start.sh
CMD ["./start.sh"]
CMD ["python3", "scraper.py"]
