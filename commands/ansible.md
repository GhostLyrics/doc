# Ansible

Start a playbook at a specific task
([docs.ansible.com](https://docs.ansible.com/ansible/latest/user_guide/playbooks_startnstep.html))
```
ansible-playbook PLAYBOOK.yml --start-at-task="NAME"
```

Limit execution to multiple specific hosts
([ansible-tips-and-tricks.readthedocs.io](https://ansible-tips-and-tricks.readthedocs.io/en/latest/ansible/commands/))
```
ansible-playbook PLAYBOOK.yml --limit "HOST1,HOST2,HOST3"
```

Limit execution to a group of hosts
([ansible-tips-and-tricks.readthedocs.io](https://ansible-tips-and-tricks.readthedocs.io/en/latest/ansible/commands/))
```
ansible-playbook PLAYBOOK.yml --limit "GROUP"
```

List hosts affected by a playbook
([stackoverflow.com](https://stackoverflow.com/a/28709851/592207))
```
ansible-playbook PLAYBOOK.yml --list-hosts
```

List groups a host belongs to
([stackoverflow.com](https://stackoverflow.com/a/46362955/592207))
```
ansible HOST --module-name debug --args var=group_names
```
