# macOS specific items

Find 32 bit applications (provided by [@maclemon][], useful for migration to 
Catalina)
```
mdfind "kMDItemExecutableArchitectures == '*i386*' && kMDItemExecutableArchitectures != '*x86*'"
```

Reset Launchpad (order of icons, [discussions.apple.com](https://discussions.apple.com/thread/250732225))
```
defaults write com.apple.dock ResetLaunchPad -bool true
killall Dock
```

Delete Time Machine backups ([discussions.apple.com](https://discussions.apple.com/thread/252036574?answerId=253916754022#253916754022))
```
tmutil listbackups

sudo tmutil delete -d /Volumes/YOUR-BACKUP-DRIVE/ -t YYYY-MM-DD-TIME
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
