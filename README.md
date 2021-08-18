# list-universe
A simple script to list and count the packages that were installed from Ubuntu's Universe repository

To use: 
1. Update the package indexes:
`sudo apt update`
1. Ensure you have the relevant dependencies 
   1. on 18.04 or earlier (this is normally already installed):
`sudo apt install python3-apt`
   1. on 20.04 or later (these are normally already installed):
`sudo apt install python3-apt python3-distro`
1. Download the Python file:
`wget https://github.com/Hooloovoo/list-universe/raw/main/list_universe.py`
1. Run with:
`python3 list_universe.py`

You should see output such as:
```
$ python3 list_universe.py 
akqml Ubuntu focal universe
apt-transport-https Ubuntu focal-updates universe
asciinema Ubuntu focal universe
[...]
webcamoid-plugins Ubuntu focal universe
305 packages from Ubuntu universe
```

Or, if there are no packages installed from Universe:
```
$ python3 list_universe.py
0 packages from Ubuntu universe
```
