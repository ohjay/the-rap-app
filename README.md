# the-rap-app
A real-time rap generator built at Cal Hacks 2015. Find it [here](https://www.ocf.berkeley.edu/~owenmj/) or, unofficially, at [ocf.sexy/owenmj](https://www.ocf.berkeley.edu/~owenmj/).

_Note: As of October 30, 2015, only Chrome users can enjoy the full functionality of this website. This is due to the fact that our app uses the [Web Speech API](https://dvcs.w3.org/hg/speech-api/raw-file/tip/speechapi.html) to provide support for continuous voice recognition – unfortunately, Chrome seems to be the only browser that backs said specification._

### What it does:
Rap App processes speech input, where a break/pause signifies the end of a line. For every such line, it provides the user with a rhyme based on the final word in the phrase. For example, if you were to say "_Yo yo yo my name is Jerry_," Rap App might respond with the word "hairy."

The webpage also allows the user to select from five different instrumentals, so that everyone can rap to his/her beat of choice.

### Why we made it:
We wanted to make something cool and interactive. No, none of us can actually freestyle (...well). Also, a big shoutout to banana chips and coconut strips for inspiring this app in the first place!

### How it works:
Our "advanced" lookup algorithm searches for a rhyme by comparing IPA suffixes to each other (using pronunciation data from the [Moby Project](https://en.wikipedia.org/wiki/Moby_Project#Pronunciator)). These comparisons are made via methods on a trie, which is affectionately referred to as our "mobytrie." Yes, that was indeed relevant.

The lookup function also sports a few other upgrades/optimizations, such that it can find a match for theoretically ANY word. See [`js/rhyme_lookup.js`](js/rhyme_lookup.js) and [`js/trie.js`](js/trie.js) for more information.

### Who contributed:
Rap App was developed by three UC Berkeley students: Owen Jow, Sagang Wee, and Sam Choi.

### W[h]ere you expecting anything else?
If so, drop us a line at the-rap-app@gmail.com! Or just create an issue (preferred).
