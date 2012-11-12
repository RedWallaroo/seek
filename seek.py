''' Seek
 A command line tool written in Python similar to grep.
'''
import os
import sys

import optparse

import seek_functions

def main(args):
    parser = optparse.OptionParser('\nUsage: %prog [--options] [pattern] [source] [symbol] [destination]')

    parser.add_option("-p", "--pattern_file",
                      action="store_true",
                      dest="pattern_file",
                      default=False,
                      help="Pull search_terms from a file. Search terms must be separated by a newline.")
    parser.add_option("-i", "--ignore_case",
                      action="store_true",
                      dest="ignore_case",
                      default=False,
                      help="Performs case-insensitve search")
    parser.add_option("-S", "--starts_with",
                      action="store_true",
                      dest="starts_with",
                      default=False,
                      help="Searches for any lines with words that start with search term")
    parser.add_option("-s", "--line_starts_with",
                      action="store_true",
                      dest="line_starts_with",
                      default=False,
                      help="Searches for any lines where the line starts with search term")
    parser.add_option("-e", "--line_ends_with",
                      action="store_true",
                      dest="line_ends_with",
                      default=False,
                      help="Searches for any lines where the line ends with search term")
    parser.add_option("-E", "--ends_with",
                      action="store_true",
                      dest="ends_with",
                      default=False,
                      help="Searches for any lines with words that end with search term")
    parser.add_option("-w", "--match_whole_word",
                      action="store_true",
                      dest="match_whole_word",
                      default=False,
                      help="Searches for any lines with words that as a whole match the search_term")
    parser.add_option("-r", "--recursive_dir",
                      action="store_true",
                      dest="recursive_dir",
                      default=False,
                      help="Searches recursively for any lines containing search_term in files within indicated directory")
    parser.add_option("-l", "--list_filenames",
                      action="store_true",
                      dest="list_filenames",
                      default=False,
                      help="Searches for any files containing search_term in current directory and returns filenames")
    parser.add_option("-y", "--synonym_search",
                      action="store_true",
                      dest="synonym_search",
                      default=False,
                      help="Searches for any files containing a match for the search_term and *any* of the synonym words returned from the dictionary API")

    (opts, args) = parser.parse_args(args)

    if len(args) < 1:
        parser.error("wrong number of arguments")
    elif len(args) == 1:
        #Searching in current directory
        current_directory = os.getcwd()
        args = args[0], current_directory.split()
    elif len(args) == 2:
        #Search location provided. No need to modify
        args = args[0], args[1].split()
    elif len(args) > 2:
        #Search in multiple locations.
        locations = []
        for x in range(1,len(args)):
          locations.append(args[x])
        args = args[0],locations

    if opts.pattern_file:
        seek_functions.pattern_file(args)
    elif opts.ignore_case:
        seek_functions.basic_search(args, ignore_case=True)
    elif opts.starts_with:
        seek_functions.starts_with(args)
    elif opts.line_starts_with:
        seek_functions.line_starts_with(args)
    elif opts.line_ends_with:
        seek_functions.line_ends_with(args)
    elif opts.ends_with:
        seek_functions.ends_with(args)
    elif opts.match_whole_word:
        seek_functions.match_whole_word(args)
    elif opts.recursive_dir:
        seek_functions.recursive_dir(args)
    elif opts.list_filenames:
        seek_functions.list_filenames(args)
    elif opts.synonym_search:
        seek_functions.synonym_search(args)
    else:
        seek_functions.basic_search(args, ignore_case=False)

if __name__ == "__main__":
    main(sys.argv[1:])
