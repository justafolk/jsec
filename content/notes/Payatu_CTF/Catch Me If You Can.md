---
title: "Catch Me If You Can"
tags:
- osint
- ctf
- payatuctf
- 2022
---

## Challenge :
<center> <img src="../Pasted image 20221016200904.png" /></center>

## Description:

```
Use your OSINT skills to identify various places where data can be collected from, on the Internet.
Image is posted with tag #Goa2022, find the image with correct description that will give you the 
address to the flag. The flag_is_the_name.
Flag format: `PayatuCTF{The_Full_Name}`
```

- As the first 2 lines of the description suggests to search through popular social media posts consisting a hashtag #GOA2022 and a distinctive description, my first thought was to search the user on Instagram. After a thorough search through all posts tagged #GOA2022 which were posted within a justifiable timeline, I couldn't really find any distinctive posts. Time to move on.
- Second Place to search was twitter. Within a few seconds of scrolling through twitter's latest tab with the #GOA2022 tag, I came across the following post.

<center> <img src="../Pasted image 20221016201758.png" /> </center>



- As this was quite a suggestive post, I was pretty sure this is the right path to follow.
- Now following the description _"the image with correct description that will give you the 
address to the flag."_, I saw there was a alternative string attached to the post. 
<center> <img src="../Pasted image 20221016202114.png" /> 

 
```
Alternative String: 15.4470235,73.8533068
```
</center>

- At this point, the whole challenge was just super obvious. I tracked these coordinates to 
<center> <img src="../Pasted image 20221016202513.png"> </center>

- As the description said, _"The flag_is_the_name."_ I deducted the final flag to be:
```
PayatuCTF{Bambolim_Beach_Resort}
```

### Other Challenges
2. 📁  [An Innocent Mistake](An%20Innocent%20Mistake.md)
3. 📁  [Welcome to my Darkside](Welcome%20to%20my%20Darkside.md)





📁  [Payatu CTF 2022](notes/Payatu_CTF/Payatu_ctf.md)