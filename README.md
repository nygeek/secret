# secret
manage a crytographic secret using code in github but without exposing the secret

This tiny module is used to manage a cryptograpic secret for a Google App Engine (GAE) system whose code is managed in GitHub.

The objective is to NOT store the secret in GitHub but to make it easy to manage the secret.

The secret is stored in the ./static/.secret.json file.  This is a place in the Google Cloud Storage space that is intended for relatively static files.

The secret is READ from the _stash_path/_**.secret.json**

If you want to create a .secret.json file you must capture the output of the program and put it in that file.  I have a make target that does this:

```
.PHONY: newsecret
newsecret:
	${PYTHON} secret_stash.py -n > ./static/.secret.json
```

You can check if the secret file is copacetic with this make target:
```
.PHONY: checksecret
checksecret:
	${PYTHON} secret_stash.py
```

## Manual

### usage: secret_stash.py [-h] [-d] [-p PATH] [-n]

```
options:
  -h, --help            show this help message and exit
  -d, --debug           Turn on debugging.
  -p PATH, --path PATH  Set the stash path.
  -n, --new             Generate a new secret.
```
