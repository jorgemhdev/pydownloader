# pydownloader: a simple way to download YouTube videos.

pydownloader is a very basic Python 3.+ script that allows you to download YouTube videos right from your command line. </br>In order to do so, it uses the pytube library.

## Requirements

The only component needed by this script to work properly is the pytube library, which can be easily installed this way:

```
$ pip install pytube3
```

## How to use pydownloader

This script is ran using the following prompt:

```
$ python pydownloader.py link
```

A working example would be:

```
$ python pydownloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

At the moment, pydownloader saves the YouTube video in the path the script is located in. I'm working in adding the "saving to custom paths" function.

## To-dos

At the moment, this tool is really basic and not polished. I'm working on adding support for more command line arguments, making it prettier and optimizing it as much as I can.</br>
As for now... I guess this is a cool proof of concept ;)

## Can I use this code?

Of course you can! Feel free to use it to learn, make it better, or whatever you want! In case you want to redistribute / reference it, simply credit me:
Jorge Martinez Hurtado (jorgemhdev)
