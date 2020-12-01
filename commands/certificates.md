# Certificates

Connect directly to a host using openssl
```
openssl s_client -connect YOUR.EXAMPLE.HOST:PORT
```
 
Connect directly with gnu-tls without SNI
```
gnutls-cli --disable-sni YOUR.EXAMPLE.HOST
```

Specify your own certificates when connecting via curl
```
curl --cafile /PATH/TO/FILE https://YOUR.EXAMPLE.HOST
```

Scan a host for only certificate related information using [testssl][]
```
testssl.sh --server-defaults https://YOUR.EXAMPLE.HOST
```

[testssl]: https://github.com/drwetter/testssl.sh
