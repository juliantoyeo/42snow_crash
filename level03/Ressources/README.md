<h2>Level 03</h2>

This time we are welcomed with a single file called `level03`

We don't have much clue on this file unlike the previous level

After a some search in google, here is a good link for read
`https://opensource.com/article/20/4/linux-binary-analysis`

We will first be suggested to use the command `file` to know which that type of file is this

![alt text](./screenshot/image1.png)

Now we could see that the file is `ELF 32-bit LSB executable` and with another quick search, if seems that we can run this file like a `C binary executable`, so lets go and run this file to see what it does

![alt text](./screenshot/image2.png)

The file just print `Exploit me` and nothing else, lets try the other command that where suggested by the previous link to anaylize further

`ltrace` is a good command to analyze an executable, it give us the information of what is the function, including the parameters as well as the return value that the executable is using.

![alt text](./screenshot/image3.png)

From the analysis made by ltrace, we can see that the "Exploit me" was a result from the `echo` command using a system call.

![alt text](./screenshot/image4.png)

Here `ls -la` we can see that the `level03` executable has the permission of `-rwsr-sr-x`

The `s` in the permission, means that this executable will be run as the file owner itself, and in this case, the executable will be run as the user `flag03`