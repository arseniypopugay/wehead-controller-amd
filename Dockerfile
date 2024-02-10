FROM ghcr.io/merklebot/hackathon-arm-image:master as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ARG TARGETOS
ARG TARGETARCH

ARG Version
ARG GitCommit
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" 

ENV HEADID=""
# HEADTOKEN Must be empty (Please check a docs https://doc.clickup.com/6656751/p/h/6b4qf-27775/012c44047324368)
ENV HEADTOKEN=""
ENV HEADURI="test-avatar-srv-2-ule2kkd6ca-wl.a.run.app"

COPY requirements.txt requirements.txt
RUN python3.8 -m pip install -r requirements.txt
COPY . .

CMD ["python3.8", "main.py"]