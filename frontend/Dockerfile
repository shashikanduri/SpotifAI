FROM node:alpine as base

WORKDIR /app

COPY ./package.json ./
RUN npm install

COPY ./ ./

RUN npm run build

FROM nginx

COPY --from=base /app/nginx /etc/nginx/conf.d
COPY --from=base /app/dist /usr/share/nginx/html
EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"] 

