# hh parser

It's an app that has been created as a test-task for Консорциум "Кодекс" company

# Install
```bash
git clone https://github.com/nbox363/hh_parser.git
cd hh_parser
```
Create a virtualenv and activate it:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install pip packages:
```bash
$ pip install -r requirements.txt
```

# Run
```bash
$ docker run -d -p 5672:5672 rabbitmq
```
```bash
$ python main.py
```
