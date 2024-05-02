FROM python:3.9.19-bookworm as python

WORKDIR /app

RUN apt-get update && apt-get install -y \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

COPY model.py model.py

CMD [ "python","-u", "./main.py" ]

