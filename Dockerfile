FROM node:15.2.0

RUN mkdir -p /var/www/app
WORKDIR /var/www/app

COPY . .

RUN npm i
RUN npm run generate 

ENV HOST 0.0.0.0

CMD ["npm","run","start"]
