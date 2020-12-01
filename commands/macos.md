# macOS specific items

Find 32 bit applications (provided by [@maclemon][], useful for migration to 
Catalina)
```
mdfind "kMDItemExecutableArchitectures == '*i386*' && kMDItemExecutableArchitectures != '*x86*'"
```

Open tmux with [iTerm2][] native tabs
```
# initial session creation
tmux -CC

# attach to running session
tmux -CC a
```

[@maclemon]: https://twitter.com/MacLemon
[iTerm2]: https://github.com/gnachman/iTerm2
