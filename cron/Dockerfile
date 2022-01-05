FROM ubuntu:latest
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y install cron
COPY seed-cron /etc/cron.d/seed-cron
COPY crontask.py /tmp/crontask.py
RUN pip install requests
RUN chmod 0777 /etc/cron.d/seed-cron
RUN chmod 0755 /tmp/crontask.py
RUN crontab /etc/cron.d/seed-cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log