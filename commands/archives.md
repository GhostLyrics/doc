Store a file into an AES encrypted ZIP file ([superuser.com](https://superuser.com/a/542882/20860))
```
# Note: AES256 is not a variable
7za a OUTPUT.zip INPUT.txt -tzip -mem=AES256 -mx9 -p'PASSWORD'
```
