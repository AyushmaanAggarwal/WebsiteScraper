FROM python:3-alpine

# Label docker image
LABEL version="3.0"
LABEL maintaner="Ayushmaan Aggarwal"
LABEL release-date="2023-05-18"

# Add docker user, allow it to edit instance, and remove root user
RUN apk add shadow
RUN addgroup -S dockeruser && adduser -S dockeruser -G dockeruser
RUN usermod -s /usr/sbin/ls  root
RUN apk del shadow
USER dockeruser

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./scheduler.py" ]