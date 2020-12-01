# Systemd

## Unit management

Find failed units
```
systemctl list-units --state=failed
```

Show dependencies of a unit
```
systemctl show -p "Wants" TARGET.target
```

Reset failed state for a unit
```
systemctl reset-failed SERVICE.service
```

Reload configuration files
```
systemctl daemon-reload 
```

## Others

Find out whether the system has finished startup procedures
```
systemctl is-system-running
```

Show DNS resolvers
```
systemd-resolve --status
```

