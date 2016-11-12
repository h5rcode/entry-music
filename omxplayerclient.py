import subprocess

def play_sound(file_to_play):
	subprocess.call(["omxplayer", file_to_play]);
