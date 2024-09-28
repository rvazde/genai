#!/bin/zsh


# We use find to search recursively all files with extension .sh
# We then pipe to awk with field separator flag that splits on '/' and returns the Last Field (tailing)
# Finally, we use the field separator again in order to obtain the first element of the separation, note on '.sh$', to split only if .sh occurs at the end of the string
find . -type f -name "*.sh" | awk -F '/' '{print $NF}' | awk -F '.sh$' '{print $1}'
