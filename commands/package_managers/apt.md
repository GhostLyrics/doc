# Debian: apt

Fix a missing apt key
```
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys KEY_ID
```

Check which package a file belongs to
([askubuntu.com](https://askubuntu.com/a/482))
```
dpkg -S FILENAME_OR_PATH
```
