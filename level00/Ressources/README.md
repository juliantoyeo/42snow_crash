"su" command is used to switch to another user

Since the project hint that we should do "su flag00" and insert the password to pass this level,
lets investigate on the "usr" folder

First from our current location after we are connected, we must go to the root directory where everythin is located.
cd /

Next nagivate to "usr" folder
cd usr

Now we are in the /usr directory, lets try to look at all the information of the file
ls -la */*

It is proven to be very counter intuative as there is too much file to look at
So lets try to tweet the command a little bit
Since we are trying to change to user flag00 or maybe level00 we can try to use the "grep" command help us filter the info
```console
ls -la */* | grep "flag\|level"
```

![alt text](./screenshot/image1.png)
