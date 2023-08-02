---
title: "An Innocent Mistake"
tags:
- osint
- ctf
- payatuctf
- 2022
---

## Challenge:
<center>
![[Pasted image 20221016205222.png]]
</center>

## Description:
```
There are other websites where a **techie** can make their profile at, links to 
the central collection are here, where you can find unintended message in its 
peers, but little complex than before, you might want to visit a chef of your 
own to try the ultimate cuisine.
```

- This challenge started on a confusing note. The description bolds "techie" which suggests two things: 
	1. It just indicates to search a tech associated website like github / gitlab. 
	2. It clues us to find a user with an username "techie".
- I spent better half of my time searching for a user "techie" on websites like github, dev.to, gitlab. 
- Plus, the end part of the description had to no relation to the actual OSINT whatsoever. It just downright distracted me to search on websites like code chef, leetcode, etc.
- After spending unhealthy amount of time on tech websites searching for "techie", it clicked me!! what if this challenge is a continuation to the challenge before? As the description didn't explicitly mention to have last challenge in consideration, I was a bit skeptical to move forward.

	![[Pasted image 20221016213025.png]]
- Just for the sake of it, I searched for the username in the last OSINT challenge "Warren Hastings" on Github. I just found one user named Warren Hasting on Github and immediately knew it I'm on right path.
![[Pasted image 20221016213247.png]]

- Before moving forward, there was one clue in the tweet replies of the first challenge.
![[Pasted image 20221016213500.png]]
- The above suggested that there's a repository containing the GovGenList on "Warren Hasting's" Github.
- There were 6 repos on his github:
![[Pasted image 20221016213654.png]]
- And YEAH! GovGenList was one of em'. 
![[Pasted image 20221016213904.png]]
- GovGenList repo had just one file _Readme.md_ with the Following text:
	```
	# Governor Generals of British India before 1857
	This repository contains list of eminent Governor Generals of India before 1857
	
	Warren Hastings- 1773-1785
	Earl Cornwallis- 1786-1793
	Marquess Wellesley- 1798-1805
	George Barlow- 1805-1807
	Lord Minto- 1807-1813
	William Bentinck- 1828-1835
	Charles MetCalfe - 1835-1836
	Earl of Dalhousie - 1848-1856
	
	
	
	The Key lies where it all started, when East India Company fought and set rule **in Bengal.**
	```
- After reading the last line, I googled the part "when East India Company fought and set rule **in Bengal.**"
![[Pasted image 20221016214418.png]]
- And the answer was "The Battle of Plassey _*1757*_". Warren's account had a repository titled the same, so I scattered through that repository's text and found a base64 encoded message at the very end.
	![[Pasted image 20221016214705.png]]

	```
	T1NJTlR7R0lUSFVCX0xFQUtTfQ==
	```

- After decoding this base64 message, we get:
	```
	OSINT{GITHUB_LEAKS}
	```
- Giving us the Final Flag:

	```
	PayatuCTF{GITHUB_LEAKS}
	```

### Next Challenges:
2. 📁  [An Innocent Mistake](An%20Innocent%20Mistake.md)
3. 📁  [Welcome to my Darkside](Welcome%20to%20my%20Darkside.md)

📁  [Payatu CTF 2022](notes/Payatu_CTF/Payatu_ctf.md)