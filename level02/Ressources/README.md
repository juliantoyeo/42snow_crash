<h2>Level 02</h2>

As soon as we login into level 02 we have something different this time, there is actually a file in our directory

![alt text](./screenshot/image1.png)

What is this `level02.pcap` file? If we use cat ( command line cat, not an actual cat🐈 ) to read it, it is very unreadable

Lets download it to our local machine using `scp` like the previous level
```console
scp -P 4242 level01@<snow_crash_ip>:/home/user/level02/level02.pcap .
```

According to Mr google and Sir Wikipedia, `pcap is Packet Capture API` which capture live network packet data

How could this file contain any clue? :thinking:

It seems that we could use a program called `wireshark (https://www.wireshark.org/#download)` to analyze this packet

After we download the wireshark, we couldn't open the file because of the permissions issue, let's fix it
```console
chmod 777 level02.pcap 
```

It seems that this packet was from china :thinking:

![alt text](./screenshot/image2.png)



