FROM node:16.9.0

RUN mkdir -p /var/www/app
WORKDIR /var/www/app

COPY . .

RUN npm install

ENV HOST 0.0.0.0

ENTRYPOINT [ "sh", "entrypoint.sh" ]
