# monitoring

Display items from a client-certificate protected Prometheus endpoint in a nice
way
```
curl \
  --silent \
  --cacert /path/to/ca/cert.pem \
  --cert /path/to/cert.pem \
  --key /path/to/key.pem https://ADDRESS:PORT/ENDPOINT \
  | less
```
