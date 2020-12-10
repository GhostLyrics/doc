# Windows specific items

Redirect command output to a file 
([docs.microsoft.com](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/out-file?view=powershell-6))
```
PROGRAM.exe | Out-File -FilePath OUTPUT.txt
```

Find the file system path of a program
([stackoverflow.com](https://stackoverflow.com/a/27140194/592207))
```
Get-Command PROGRAM
```
