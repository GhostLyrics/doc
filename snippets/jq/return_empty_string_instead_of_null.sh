# https://github.com/stedolan/jq/issues/354#issuecomment-46641827

jq '.example | select (.!=null)' FILE
