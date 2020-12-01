# source: https://stackoverflow.com/a/40027637/592207

# set shell variable
bash_example="example"

# assign value of shell variable to jq variable and query the top level for it
jq --arg jq_example "$bash_example" '.[$jq_example].some_key' FILE
