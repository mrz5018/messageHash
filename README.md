# Message Hasher

## Description

This program is a web service that can handle HTTP requests to hash messages, store the hashes, and later look them up.  Running on a django framework the program can be accessed through the following REST calls:

- POST to 127.0.0.1:8000/messages/
	- json data in the format of {'message':[message_to_hash]}
- GET to 127.0.0.1:8000/messages/[hash_to_lookup]

## Installation Details/Prerequisites

The program runs on a virtual Python 3.X environment.  There are many methods through which the program can be set up on the server.  One example is to use nginx and uwsgi.  This creates a proxy through which HTTP data can be piped to the django program

### Setting up nginx

nginx is used to setup a proxy that passes all HTTP data from port 80 to the uwsgi application which is setup to receive on 127.0.0.1:8000 in this example.  To get nginx run the following command:

> sudo apt-get nginx

Once the program has been installed, the configuration can be set to allow port 80 to be forwarded, using a server block similar to the one shown below:

```
upstream django{
        server 127.0.0.1:29000;
}

server {
        listen 80;
        charset UTF-8;
        location / {
                proxy_pass http://127.0.0.1:8000;
        }
}
```

### Python 3.4 and virtualenv

To download the latest version of Python 3 use the following command:

> sudo apt-get python3

To isolate this install of Python on the server a virtualenv will be used.  This can be placed anywhere, and simply acts as a place to store python libraries for this environment. To set up a virtualenv run the following.

> pip install virtualenv
> virtualenv [path_of_messageHash_progject]
> cd [path_of_messageHash_progject]
> source bin/activate

**NOTE: From here on out all of the installation will take place in the virtualenv**

### Django/uwsgi

To install these frameworks run the following command on the remote server:

> pip install django
> pip install uwsgi

## Starting up the server

To run the nginx install call the following command

> sudo service nginx start

Then once the nginx server is started up, the uwsgi can be started.

> cd [path_of_messageHash_progject]/wordhash
> uwsgi --http-socket 127.0.0.1:8000 --wsgi-file wordhash/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191


