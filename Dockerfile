FROM python:3.7

WORKDIR /LNUBOT_v1

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN export PYTHONPATH='${PYTHONPATH}:/LNUBOT_v1'

COPY . .

CMD ["python", "./bot.py"]
