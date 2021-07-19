# Never Gonna Give You Up
Author: CodeTiger

## Challenge
They gave a gif and nothing else.

## Solution 

Download that gif by right clicking and pressing save as, or however you would download an image off of your web browser.

Check different things around the gif with forensics skills like running file to see what file type etc.

The most suspicious thing though is when you run binwalk, because it shows that the gif is also a zip archive.

Knowing that, unzip the image and a flag file comes out.

Flag: ```flag{y0u_g0t_r1ck_r0lled_h4h4_g3t_r3kt}```



