FROM python:3.10.11
WORKDIR /Datasets
COPY . /Datasets
RUN pip install -r requirements.txt
CMD ["python", "wsgi.py"]
