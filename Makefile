# Generate secrets for Python programs
# Use secrets in Python programs

# Make us OS-independent ... at least for MacOS and Linux
OS := $(shell uname -s)
ifeq (Linux, ${OS})
    DATE := $(shell date --iso-8601)
else
    DATE := $(shell date "+%Y-%m-%d")
endif

# Python version
PYTHON := python3
# PYLINT := ${PYTHON} -m pylint
PYLINT := pylint

HOME := ${HOME}
LIBRARY := ${HOME}/projects/p/python/library/
HERE := $(shell pwd)

.PHONY: help
help:
	cat Makefile
	echo "OS: " ${OS}
	echo "DATE: " ${DATE}
	echo "HERE: " ${HERE}

PYTHON_SOURCE = \
	secret_stash.py \
	trace_debug.py

SOURCE = \
	${PYTHON_SOURCE} \
	Makefile \
	README.md

FILES = \
	${SOURCE} \
	.gitattributes \
	.gitignore

.PHONY: install
install:
	cp secret_stash.py ${LIBRARY}

.PHONY: newsecret
newsecret:
	${PYTHON} secret_stash.py -n > ./static/.secret.json

.PHONY: checksecret
checksecret:
	${PYTHON} secret_stash.py

pylint:
	- ${PYLINT} secret_stash.py

lint: pylint

test:
	${PYTHON} secret_stash.py

# GIT operations

.PHONY: diff
diff: .gitattributes
	git diff

.PHONY: status
status:
	git status

# this brings the remote copy into sync with the local one
commit: .gitattributes
	git commit ${FILES}
	git push -u origin main

# This brings the local copy into sync with the remote (main)
pull: .gitattributes
	git pull origin main

log: .gitattributes
	git log --pretty=oneline
