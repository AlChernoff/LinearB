# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ADD entrypoint.sh entrypoint.sh
RUN chmod a+x entrypoint.sh
# ENTRYPOINT ["cat","entrypoint.sh"]
CMD ["/code/entrypoint.sh"]