FROM ruby:latest
EXPOSE 4567
WORKDIR /cmx-api-app
COPY . /cmx-api-app

RUN chmod a+x .shipped/build ./cmx_app_start.sh .shipped/test

RUN [".shipped/build"]
CMD ./cmx_app_start.sh
