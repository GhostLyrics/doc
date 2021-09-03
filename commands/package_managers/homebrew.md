# macOS: brew

Install a previous version of a package
([stackoverflow.com](https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula))
```
brew tap-new YOUR_CUSTOM/TAP_NAME
# e.g. brew tap-new ghostlyrics/local

brew extract --version "SEM_VERSION" PACKAGE YOUR_CUSTOM/TAP_NAME
# e.g. brew extract --version 2.9.2 ansible ghostlyrics/local

brew install PACKAGE@VERSION
# e.g. brew install ansible@2.9.2

brew unlink PACKAGE
# e.g. brew unlink ansible

brew link PACKAGE@VERSION
# e.g. brew link ansible@2.9.2
```

Find outdated packages or casks
```
# for formulae
brew outdated

# for casks
brew outdated --cask
```

Find reverse dependencies for a formula
([gist.github.com](https://gist.github.com/axtl/10228610#gistcomment-3623976))
```
brew uses --installed FORMULA
```
