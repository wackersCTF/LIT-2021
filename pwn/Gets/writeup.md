# Gets
Author: Rythm

## Challenge
My favorite libc function is gets. I am very confident in its security. Connect with
```nc gets.litctf.live 1337```

## Solution
The title of the challenge already tells us that the challenge is going to be some type of gets buffer overflow.

First, we take a look at the c source code that they gave us.

We see that there is a strcmp function first that we need to get past.

Next, after we pass the strcmp we have to overwrite the debuf variable so it equals 0xdeadbeef.

Now we have to figure out our payload to meet the requirements.

First we know that we have to pass the strcmp, which compares our input with the string "Yes".

Now after we pass the strcmp part of the binary, we try to overwrite into the variable by adding many A's.

After trying to add many A's to our payload, we realize something is wrong.

We are now not getting past the strcmp and it sends us directly to the bottom.

Now the way that we can get past the strcmp is to send a null terminator which is \x00.

Now we have to find the proper offset to overwrite into the flag variable, which is buf.

Finding the offset was pretty simple. We just had to test A's until we got 1 A into segmentation fault which meant we started overwriting the variable. 

We find that the offset was an extra 48 A's after the 'Yes' and the null terminator, \x00, which in total gives us the offset of 52.

Now all we have to do is write the variable exactly to 0xdeadbeef.

We could do this by concatenating \xef\xbe\xad\xde or using pwntools p64(0xdeadbeef).

So now, we just had to create the program in python with the correct parts.

The total payload we were sending was ```r.sendline(b'Yes' + b'\0' + b'A'*36 + p64(0xdeadbeef) + p64(0x7ffff7fb1390))```

You can see the full program in the solve.py file.

Flag: **flag{d0_y0u_g3ts_1t}**

```Note: I am not the best at pwn so I didn't really understand exactly why this worked but I guess that it read the flag memory address as extra bytes because after looking at other writeups, I saw that all we needed to do was pass the offset and overwrite the debug variable to equal 0xdeadbeef.```
