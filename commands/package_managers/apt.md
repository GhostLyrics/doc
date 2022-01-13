# Debian: apt

Fix a missing apt key
```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys KEY_ID
```

Check which package a file belongs to
([askubuntu.com](https://askubuntu.com/a/482))
```
dpkg -S FILENAME_OR_PATH
```
