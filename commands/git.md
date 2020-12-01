# Git

Cherry-pick a series of commits, including the first commit
([stackoverflow.com](https://stackoverflow.com/a/3933416/592207))
```
git cherry-pick "HASH_A^..HASH_B"
```

Create a patch from the last commit
```
# Note: HEAD is not a variable
git format-patch HEAD~1
```

Create a patch for a specific commit
([stackoverflow.com](https://stackoverflow.com/a/6658352/592207))
```
git format-patch -1 HASH
```

Remove merged local branches
([hacksparrow.com](https://www.hacksparrow.com/git/delete-all-branches-except-master.html))
```
git branch --merged \
  | grep --extended-regexp --invert-match "(^\*|master|dev)" \
  | xargs git branch --delete
```

Search for a string in git commit messages
([stackoverflow.com](https://stackoverflow.com/a/3826800/592207))
```
git log --grep "YOUR_STRING"
```
