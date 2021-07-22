#!/bin/bash
# source: https://unix.stackexchange.com/a/446848/91122

condition="$1"

# the second flag will only be passed if `condition` is not empty
example_script_call --parameter1 ${condition:+"--parameter2=$condition"}
