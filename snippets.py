#
#  snippets
#

import logging
import csv

#set basic config
logging.BasicConfig(filename"output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file"""
    logging.info ("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug ("Opening file")
    with open (filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet