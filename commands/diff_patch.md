# Diffing & Patching

Create a patch file from the diff of two files 
([gitlab.com: omnibus-gitlab](https://gitlab.com/gitlab-org/build/omnibus-gitlab-mirror/blob/19108ff4405fc108272a0e36478aa153a8d77366/doc/development/creating-patches.md#diff-command))
```
diff --new-file --text --unified --recursive ORIGINAL.rb INPUT.rb > OUTPUT.patch
```
