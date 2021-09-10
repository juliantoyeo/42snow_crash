<h2>Level 01</h2>

Repeated the same step as level 00, but there is no new clue on where the password for flag01 could be

Time to ask the mighty google!

![alt text](./screenshot/image1.png)

The first link looks promising, it mentioned about the following

![alt text](./screenshot/image2.png)

This link also mentioned that there is a password cracker called "John the Ripper" that could be used to crack the "/etc/passwd" or "/etc/shadow"

Since the project PDF mentioned that "If you plan to use a specific external software, you must set up a specific environment (VM, docker, Vagrant)"
Lets get a docker 🐳 to run the JOHN :sunglasses:

Guide to install docker and run ubuntu image for mac:

Install Docker Desktop for Mac

Next run this command on terminal
```console
docker run -it --name ubuntu ubuntu:xenial bash
```

Inside the docker ubuntu
```console
apt update && apt-get install john
```