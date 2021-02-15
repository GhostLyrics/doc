# Linters

Display failing sniff codes when using [phpcs][] for use with `phpcbf`
([stackoverflow.com](https://stackoverflow.com/a/13732800/592207))
```
phcs -s FILE_OR_FOLDER
```

Automatically fix all fixable issues with the given coding standard as guideline 
using [phpcs][]'s `phpcbf`.
```
phpcbf --basepath="$PWD" --colors --standard=YOUR_STANDARD.xml YOUR_FILE_OR_FOLDER
```

Automatically fix specific issues with the given coding standard as guideline 
using [phpcs][]'s `phpcbf`.
```
phpcbf --basepath="$PWD" --colors --standard=YOUR_STANDARD.xml \
  --sniffs=VENDOR.TOPIC.SPECIFIC_SNIFF YOUR_FILE_OR_FOLDER

# sniff example: Squiz.Strings.ConcatenationSpacing
```

[phpcs]: https://github.com/squizlabs/PHP_CodeSniffer
