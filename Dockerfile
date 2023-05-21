FROM python:3-alpine

# Label docker image
LABEL version="3.0"
LABEL maintaner="Ayushmaan Aggarwal"
LABEL release-date="2023-05-18"

WORKDIR /usr/src/app

COPY . .

# Add docker user, allow it to edit instance, and remove root user
RUN apk add shadow
RUN addgroup -S dockeruser && adduser -h /usr/src/app -S dockeruser -G dockeruser
RUN chown -R dockeruser:dockeruser /usr/src/app/instance/websites
RUN usermod -s /usr/sbin/nologin  root
RUN apk del shadow
USER dockeruser

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./scheduler.py" ]