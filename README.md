# AITV_Public
A TV with AI-generated content based on short text descriptions of webcam input.

# Summary

AITV is a CRT TV with a webcam that makes artwork.

Every hour, AITV recreates its art based on its surroundings. Use your IR remote to pick an art style that fits the mood.
Link units with friends and family: instead of seeing art inspired by your world, see art inspired by theirs

# How to run
In the source directory, run:
python not_main.py & python IRHandler.py & pythonGraphicsEngine.py &
On my dedicated pi, I have this run on bootup. If you're interested in this feature, I recommend **crontab -e** for Linux systems
P.S. For hiding my cursor on that system, I use **unclutter -idle 0.01**

# Background

This is an electronic art piece that's inspired by the way humans communicate. 

AITV started as a variant of Meta's Portal (a dedicated display designed to make video calling in your home easier). With Portal, users can instantly video-call into the house of a friends or family, seeing out of a dedicated device in the room - as if they were seeing through a portal into somebody else's home; into their private life. 
​

It's an unnerving idea to some. I think the reason it feels that way is that when it comes to seeing into someones life without being there yourself, the closest we (un-electronically) get to that is through language. Think about it: maybe it's a story someone tells you at the bar, or a conversation with your coworker about a memory, or the answer to "How was your day?" - no matter what, if I want to see what the world looks like through your eyes, I'm only going to find out by visualizing the words you use to describe it to me. It's a core part of the human experience. To know each other, we first need to comprehend what's said.


But think about the human-ness in the work that entails; what we see doesn't easily become words, and I believe words can't ever complete an image. There's information loss and gain that comes with language -  firstly theres the things left unsaid by the speaker, the indescribable details, the bulk of the experience. And inversely, the listener's left with the inexorable fingerprint created by their own imagination - they can never escape the impact of their own perception when reconstructing that scene inside their head.

In the end, when we communicate, not only is there imprecision due to the conversion to and from words, but that imprecision is a very particular, human imprecision, one that's deeply un-computer. And so the work of the project is primarily in finding a way for a computer to do it.


Imitating how humans connect is best done with a network of units. I'll be doing a limited commission run later this year - 10 maximum, that tune into each other using the 10 digits on the remote. Want to test one? Send me an message at dev.elliotkahn.com
