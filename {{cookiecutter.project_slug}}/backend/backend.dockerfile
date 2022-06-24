FROM python

WORKDIR /backend

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt && chmod +x entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/backend/entrypoint.sh"]