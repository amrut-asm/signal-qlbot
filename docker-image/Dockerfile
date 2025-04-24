FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt -y update && apt -y upgrade && apt -y install openjdk-17-jdk supervisor \
python3 pip python3-gi && pip install requests \
pydbus

RUN mkdir -p /root/.local/share/signal-cli

COPY signal-cli /root

COPY signal-qlbot.py /root

COPY qlbot.conf /etc/supervisor/conf.d

ENTRYPOINT ["/usr/bin/supervisord", "-n"]
