FROM almalinux/9-minimal

WORKDIR /app

RUN microdnf install -y python3 python3-pip && \
    microdnf clean all

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]