"""

Implementation of SecretStash class.

Created 2024-11-21 by Marc Donner
Copyright (C) 2024 NYGeek LLC

${Id}

"""

# ----- public libraries ----- #
import os

import argparse
import json
import secrets

# ----- nygeek libraries ----- #
from trace_debug import DebugTrace

# ----- variables ----- #
DEBUG = DebugTrace(False)

class SecretStash:
    """ SecretStash implementation """
    def __init__(self, stash_path="./static/"):
        """ SecretStash instance initialization """
        self.secret = None
        self.stash_path = stash_path


    def __str__(self):
        """ render as a string """
        return json.dumps(self.__dict__)


    def new_secret(self):
        """ set a new secret """
        # Should I allow a shorter secret?
        self.secret = secrets.token_hex()
        # write it to the file
        return str(self)


    def get_secret(self):
        """ return the current secret """
        if self.secret is None:
            self.read_secret()
            if self.secret is None:
                print("get_secret(): Fail.")
        return self.secret


    def read_secret(self):
        """ is there a secret in self.stash_path? """
        # assumes path ends in '/'
        secret_filepath = self.stash_path + ".secret.json"
        if os.path.isfile(secret_filepath):
            # it exists ... try reading it
            with open(secret_filepath, encoding='utf-8') as fh:
                stashed_stash = json.load(fh)
            if stashed_stash is None:
                print("read_secret(): Fail")
            else:
                self.secret = stashed_stash['secret']
            # should handle the case when the file exists but either
            # the open() or the json.load() fails.
            return self.secret
        print("read_secret(): Fail.")
        print(f"    secret_filepath: {secret_filepath} not a file.")
        return None


def main():
    """ Handle command line arguments and then call the shell. """
    # program_name = sys.argv[0]
    parser = argparse.ArgumentParser(
            description='SecretStash.')

    parser.add_argument('-d', '--debug', dest='debug',
                        action='store_true',
                        help="Turn on debugging.")
    parser.add_argument('-p', '--path', type=str, dest='path',
                        help="Set the stash path.")
    parser.add_argument('-n', '--new', dest='new_secret',
                       action='store_true',
                       help="Generate a new secret.")
    args = parser.parse_args()

    if args.debug:
        DEBUG.set()

    if args.path:
        stash = SecretStash(stash_path=args.path)
    else:
        stash = SecretStash()

    if args.new_secret:
        print(stash.new_secret())
    else:
        stash.get_secret()
        if stash.secret is not None:
            print(f"'{stash.get_secret()}'")


if __name__ == "__main__":
    main()
