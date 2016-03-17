Stage 3: Create a Movie Website
===============================

This program is the fourth part of the Introduction to Programming Nanodegree at Udacity.

This is a video playlist page generator. Keeping with the RWBY theme established with the previous projects, I have set it up to create a RWBY video page that displays the different episodes from the series. The videos are from the official Rooster Teeth channel on YouTube.

`fresh_tomatoes.py` is a modified version of the one provided by Udacity.


How to Run
----------

### Step 1

You need `entertainment_center.py`, `fresh_tomatoes.py`, and `media.py`. You can clone this repository to download all the files.

### Step 2

This step depends on which OS you are running.

#### Mac and Linux

Open a terminal window at the directory containing the three files. Write in:

```
python entertainment_center.py
```

Then hit the enter key.

#### Windows

Open up `entertainment_center.py` in IDLE. In the menu, go to _Run_ and then _Run Module_.


### Step 3

The newly created `rwby_theater.html` file should automatically be opened in your browser.

From now on, you can just open this file directly with your browser. You do not have to generate a fresh page each time.


How to Customize
----------------

By changing the data in `entertainment_center.py`, or by making your own version of the file, you can create different pages. I made it as modular as I could so this would be fairly simple.

The `Video` and `Episode` classes in `media.py` will allow you to add YouTube videos, which need to be grouped into a `Playlist` object. The `Playlist` object's `title` is the label that appears in each tab, and the `type` is what each item is known as, which is really only usefule for `Episode` objects. For instance, one playlist has the `title` of `Volume 3`, and since each episode is known as a "chapter", the `type` is `Chapter`.
