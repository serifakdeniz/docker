FROM python:3.6
COPY . /root
WORKDIR  /root
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
