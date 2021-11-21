FROM nikolaik/python-nodejs:python3.6-nodejs16

RUN apt update 
# npm install 시 필요
RUN apt install -y build-essential

RUN mkdir -p /var/www/app
WORKDIR /var/www/app

COPY . .

RUN pip install -r content_generator/requirements.txt
RUN npm install

ENV HOST 0.0.0.0

ENTRYPOINT [ "sh", "entrypoint.sh" ]
