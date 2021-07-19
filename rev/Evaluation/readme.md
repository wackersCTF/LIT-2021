# Evaluation
by eyangch

## Challenge
Here’s an evaluation copy of my flag checker! I hid the flag in the evaluation copy though…

## Solution (by xenonminer)
All the evals check from the evals before it. If we delete one eval, we get this:

<img src="https://user-images.githubusercontent.com/86171033/126106511-8ab71a56-bc3a-46df-82c4-39b43efc8dc7.png" alt="image" width=800>

We can then run a solve script that looks like this to get our flag!
```
i = "x6wpf6vZ|w6sZq5kZv4Zk54q1fvpcg5~bdic"

for char in i:
    print(chr(ord(char)^5))
```

flag: ```flag{0bfusc4t10n_1s_n0t_v3ry_s3cur3}```
