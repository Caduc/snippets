#
#  snippets
#

import logging
import csv
import argparse
import sys

#set basic config
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file"""
    logging.info ("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug ("Opening file for writing")
    with open (filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet

def get(name, filename):
    """ Get snippets that have been previous stored by the put function"""
    logging.info ("finding snippet for the name {} from {} ".format(name, filename))
    logging.degug ("Opening file for reading")
    with open (filename, "r") as fn:
#       for row in fn:
#           if name = The-Value-inputted-after-'get'-in-commandline:
#               Return the associated snippet and /n
#


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description ="Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="available commands")

    # Subparse for the put command
    logging.debug("Constructing put subparse")
    put_parse = subparsers.add_parser("put", help="Store a snippet")
    put_parse.add_argument("name", help="the name of the snippet")
    put_parse.add_argument("snippet", help="the snippet text")
    put_parse.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

    return parser


def main():
    """main function"""
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)
        pass

if __name__ == '__main__':
    main()




