FROM node:12.18.4-alpine3.9

# ARG USER=quasar
# RUN apk add --update sudo
# RUN adduser -D $USER \
#         && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
#         && chmod 0440 /etc/sudoers.d/$USER

WORKDIR /app

COPY ./frontend/package.json /app

RUN npm install -g @quasar/cli@1.1.1
RUN npm i && npm cache clean --force
RUN npm rebuild node-sass

ENV PATH ./node_modules/.bin/:$PATH

# RUN chmod -R 771 /app
# RUN chown -R $USER:root /app
