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
    logging.debug ("Opening file for reading")
    with open (filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if name == row[0]:
                print "found snippet name {} with a snippet of {} ".format(row[0], row[1])


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

    #subparse for the get command
    logging.debug("Constructing get subparse")
    get_parse = subparsers.add_parser("get", help="Get a snippet")
    get_parse.add_argument("name", help="name of snippet to be retrieved")
    get_parse.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

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
        nameo, snippeto = put(**arguments)  #as of line 62 arguments becomes a dictionary
        print "Stored '{}' as '{}'".format(snippeto, nameo)
    
    if command == "get":
        snippet = get(**arguments)
        #print "Retrieved snippet '{}' for name '{}'".format(snippet, arguments["name"])

if __name__ == '__main__':
    main()




