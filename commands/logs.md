# Logs

Empty out (truncate) an existing file
```
truncate --size 0 FILE
```

Reduce size of a systemd journal based on time ([ma.ttis.be](https://ma.ttias.be/clear-systemd-journal/))
```
journalctl --vacuum-time=TIME

# example
journalctl --vacuum-time=10d
```

Reduce size of a systemd journal based on disk usage ([ma.ttis.be](https://ma.ttias.be/clear-systemd-journal/))
```
journalctl --vacuum-size=SIZE

# example
journalctl --vacuum-size=2G
```
