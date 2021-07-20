# Rythm
by CodeTiger

## Challenge
What is that strange melody composed of only 4 notes I hear? I must decrypt it!
(Hint: You might need relative/perfect pitch for this challenge)

## Solution
The first part is relatively straightforward: transcribe the audio file into notes on paper (or computer) that you can later decrypt (I have that attached as a text file). A mentor suggested to use Audacity and analyze the wav file as a spectogram.

We get only four notes (c,d,e,f).
With the encoding ```c = 0, d = 1, e = 2, f = 3```, we get something in base 4. 

https://gchq.github.io/CyberChef/#recipe=From_Base(4)&input=MTIxMjEgMjMwMTIgMDExMjEgMzEzMjMgMDMwMTEgMTMzMDMgMTAxMjAgMzEzMTAgMTMxMTAgMzEwMTIgMzAxMjMgMDEzMjEgMTEzMzEgMjIwMDMgMTAxMjEgMDExMzMgMTMxMDAgMzAwMTEgMzMxMzAgMDAzMDEgMDMxMDEgMzIxMTEgMzMxMzEgMDEyMjAgMDMwMTAgMzExMTEgMzMxMzAgMDAzMDEgMDMwMzEgMjAzMDMgMDMxMzMgMQ

Here our mentor helped us out. He explained that the original choice I made to assume the number was in base 10 was flawed. The decoded number ```3338241147601821936650239700754550939646579824366592729534951546312574147730661508641565389693``` represents the ```3338241147601821936650239700754550939646579824366592729534951546312574147730661508641565389693```th state. We can make sense of this number by converting it to an array of bytes:

```
>>> print((3338241147601821936650239700754550939646579824366592729534951546312574147730661508641565389693).to_bytes(50, "big"))

b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00flag{1_4ctu4lly_h4d_t0_p14y_th15_p13c3}'
```

Flag: ```flag{1_4ctu4lly_h4d_t0_p14y_th15_p13c3}```
