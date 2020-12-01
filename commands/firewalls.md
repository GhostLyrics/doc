# Firewalls

Remove a specific iptables rule
```
# Find the rule
iptables --list-rules

# Remove the rule
iptables --delete FULL_RULE_SPEC  # without the starting -A
```
