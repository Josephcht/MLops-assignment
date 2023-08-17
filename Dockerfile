FROM python:3.10.11
WORKDIR /Datasets
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "wsgi.py"]