This is a <H1>Hand-Tight® Chia Plot Manager.</H1>  It is mainly designed for converting OG solo plots to portable (poolable?) plots
so as to maintain a minimum amount of unused hard drive space but also maximize R/W
performance, but it could just as easily be used as a regular plot manager with minimal tweaking.  Speaking of tweaking, this thing is pretty deeply configured to my personal machine so... yeah...
sorry? <i>(not sorry.)</i>

It'll take some work to run it properly on a computer other than mine is what I'm saying.
Unless you are somehow equally as weird about naming things.

But give it a go if you'd like, I'd welcome any suggestions for increasing its portability.


<H2>Here's what do:</H2>

HDDs are Bitches.  Bitches' directory names end with *bitch, and they all live in the bitchdir.
Adjectives or adverbs describing each Bitch are the primary identifiers of the Bitch (e.g.
'ugly' is the Bitch whose mountpoint is bitchdir/uglybitch).  Each bitchdir has a subdirectory
"old" that contains all of the OG solo plots.  New portable plots are placed on the Bitch's root.

At this time I am manually "toggling" Bitches on and off with commenting and appending their
primary identifiers to a -- you guessed it -- bitchlist.

Bitches who are turned off are ignored.  Bitches who are turned on will (in this order):
  - receive a plot if they have plenty of free space -- no need to do anything else to these,
              hence the prioritization.
  - receive a plot AFTER deleting ~4-5 non-portable (old) plots when free space is below 456GB,
              this frees enough space to ensure max transfer rate for the next few plots.
  - receive a plot if they have enough space for one, but not plenty of space,
              and are out of old ones to delete -- these go slower, hence the deprioritization.

It's set up to use madMAx43v3r's "madmax" plotter and expects to find chia_plot as an executable on the Path.  Yes
I know the madmax plotter is already a plot manager in and of itself.  I didn't like how it handled plot off-copying from the plotter drive nor its lack of using an "intermediate" caching SSD.  And I wanted more control over what happens between plots, such as deleting old plots and scheduling larger copies.

The mighty Dickweasel and his trusty sidekick Turdburglar are both NVMe plotting drives.  They
also reside in the bitchdir, though not by choice -- originally they did not.  The degenerate
Shiteater also lives in the bitchdir, where it always has been (and where it shall ever remain).

Shiteater is a buffer SSD that holds plots fresh off the plotter.  Shiteater is not strictly
necessary.  But don't tell it I said that.  I do get better performance when shiteater catches
from turdburglar and then passes to Bitches than when turdburglar goes straight to the Bitches,
as shiteater is quicker on its feet which then frees turdburglar to do the thing I'm paying it
to do sooner.

Silliness aside, a lot of how this works revolves around using a standardized naming scheme
like the offensive and unnecessary one I came up with during a period of utter frustration
back in May.

<i><b>*Note to self: write more of this later but either make it actually funny or actually useful.</b></i>
