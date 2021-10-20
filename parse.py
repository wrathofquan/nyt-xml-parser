#!/usr/bin/env python3

""" Module Description """

# xmltotabular is designed for large, pseudo-xml. The nyt files need to be concatenated to be used efficiently in the program
# In Bash: find ./nyt_nitf_*/*/ -type f -name "*.xml" -exec cat {} + > nyt_all_articles.xml

import logging

from xmltotabular import XmlCollectionToTabular

XML_INPUT = "./data/*.xml"
CONFIG = "config.yaml"
OUTPUT_PATH = "output.sqlite"


def main():
    """ Command-line entry-point. """

    collectionTransformer = XmlCollectionToTabular(
        XML_INPUT, CONFIG, OUTPUT_PATH, output_type="sqlite", log_level=logging.DEBUG
    )
    collectionTransformer.convert()


if __name__ == "__main__":
    main()
