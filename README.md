# network-scanner

A Python program that detects when specific hosts join the network for the first time or after being disconnected for more than 15 minutes and plays a configured entry music.


## Dependencies

The script requires [Nmap](https://nmap.org/) to get the list of the hosts, and `omxplayer` to play entry music.


## Configuration

Users must be defined in `users.config`, which looks like this:

```json
[{
    "hostname": "John-PC",
    "address": "73-70-73-C7-EC-82",
    "music": "johns-entry-music.mp3"
},
{
    "hostname": "android-123467",
    "address": "03-CC-BA-2A-74-B9",
    "music": "sarahs-entry-music.mp3"
}]
```

The entry music files should be organized as follows:

```
.
|
+--- network-scanner.py
|
+--- music
	|
	+--- John-PC
	|	|
	|	+--- johns-entry-music.mp3
	|
	+--- android-123467
		|
		+--- sarahs-entry-music.mp3
```
