---
title: "Welcome to my Darkside"
tags:
- osint
- ctf
- payatuctf
- 2022
---

## Challenge:
<center> ![[Pasted image 20221016215800.png]] </center>

## Description
```
     Interesting, you have noob skills, but the pros have gone dark. You found the
	 previous flag, but a researcher does more than just this, see the big 
	 picture, everything is a learning source to a researcher. Identify patterns.
	 Password leads to the network where you go DARK, but you need to prepare 
	 yourself. You got everything you need, learn and decode new skills.
```

- As this Challenge explicitly says that it's a continuation of last challenges, there's no searching required at first. In the description, the only word "DARK" is capitalized. I took that in consideration for later.
	![[Pasted image 20221016221435.png]]
- Now, I got back to Warren Hasting's Github Account to scatter for any info. There was only one repository which seemed relevant i.e "DarkWeb".
![[Pasted image 20221016221514.png]]
- There were two files:
	1. PRO.html : Which had one pastebin link and nothing more relevant.
		![[Pasted image 20221016221810.png]]
		```
		https://pastebin.com/BaZ5F02e
		```
	
	2. REAME.md : Containing a paragraph on Dark Web and suspiciously had **TOR** in bold. 
		![[Pasted image 20221016222035.png]]

- I opened the pastebin link only to find that it's locked.
	![[Pasted image 20221016222125.png]]
- After some random tries like "Warren", "East of India", "The Battle of Plassey"; I remembered that **TOR** wouldn't just be an formatting error. So I tried "TOR" as the password and Voila it worked.
- After unlocking the bin, I got an Google Sheets link.
![[Pasted image 20221016222439.png]]

- Opening that link gave bunch of onion links further justifying the main theme of the challenge.
![[Pasted image 20221016222536.png]]
- I opened first 2 links and stopped by the trauma of dark web ads :( Suddenly had a look on the title of the spreadsheet, "no1337". Though at first I thought google docs had a limit of 1k cells, just for fun I went CTRL+G RETURN 1337.  and yeah, there was one link buried deep down there at cell A1337.
```
https://docs.google.com/spreadsheets/d/1Xe6v6TpIXkr6mzoZmXeAlRj8YSN0gG3kt4WOiZTbLmY/edit#gid=0
```


	![[Pasted image 20221016223134.png]]

- Opened the link on Tor Browser to find this:
	![[Pasted image 20221016223333.png]]

- The message was:
	```
		BFVAG{QNEXJRONYYGURJNL}
		found passwords are reversible NeeTrihTThirTeeN.
	```

- After some tries with vignere cipher and beaufort cipher, It clicked me that the last word "NeeTrihTThirTeeN" clued "13" a.k.a "ROT13". After decrypting it with ROT13 cipher, I got the message:
	```
		OSINT{DARKWEBALLTHEWAY}
	```
- Which gave the final flag as:
	```
		PayatuCTF{DARKWEBALLTHEWAY}
	```

### Other Challenges
1. 📁  [Catch Me If You Can](Catch%20Me%20If%20You%20Can.md)
2. 📁  [An Innocent Mistake](An%20Innocent%20Mistake.md)

📁  [Payatu CTF 2022](notes/Payatu_CTF/Payatu_ctf.md)