# Requirements

In order to run this project, a few programs must be installed:

- Docker
- Python >=3.9

I will assume everything is run on Windows 10.

# Installing dependencies

After cloning the project, make sure to create a virtual environemtn with your favorite tool. We will use `virtualenv`. Go to the cloned directory and execute these commands:

```bash
pip install virtualenv
python -m virtualenv venv
source ./venv/Scripts/activate
pip install -r requirements.txt
```

# Start Kafka

Open up Docker dashboard and then from the project root run:

```bash
docker-compose up -d
```

Now Kafka's endpoints are exposed at localhost:9092.

# Start backend simulation

Open up 4 terminals from the root of the project folder and run these scripts:

- analytics.py
- email.py
- transaction.py

using this command:

```bash
python [script].py
```

You should see each file logging "[File name] listening...".

Lastly, run `order_backend.py` to see how Kafka handles 10 000 processes. To do this, in the fourth terminal run:

```bash
python order_backend.py
```

And there we go. In order to play around with the constants, you can edit the `constants.py` file.
