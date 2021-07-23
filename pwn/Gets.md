# Gets
Author: Rythm

## Challenge
My favorite libc function is gets. I am very confident in its security. Connect with
```nc gets.litctf.live 1337```

## Solution
Run strings on the file and search for the flag.

Best way to do that is the command: strings yarn | grep flag

We get our flag!!

Flag: **flag{y4rn_4nd_s1lk_4r3_n1c3_but_str1ngs_1s_wh4t_g0t_th3_fl4g}**
