FROM python:3.10

WORKDIR /home


ENV SPIKE_API_KEY="Your telegram API key here"

COPY pip_requirements.txt ./

RUN apt update && apt install ffmpeg -y
RUN pip install -r pip_requirements.txt

COPY *.py ./

ENTRYPOINT ["python", "server.py"]
