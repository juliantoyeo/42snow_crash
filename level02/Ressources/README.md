<h2>Level 02</h2>

As soon as we login into level 02 we have something different this time, there is actually a file in our directory

![alt text](./screenshot/image1.png)

What is this `level02.pcap` file ? If we use cat to read it, it is very unreadable

Lets download it to our local machine using `scp` like the previous level
```console
scp -P 4242 level01@<snow_crash_ip>:/home/user/level02/level02.pcap .
```

According to Mr google and Sir Wikipedia, `pcap is Packet Capture API` which capture live network packet data

How could this file contain any clue? :thinking:
