#!/usr/bin/env python
import argparse
import re

# Replace the string value of the following variable with your names.
ME = 'Ryan Brand';
COLLABORATORS = ["nobody"]

def process_file(infile):
    titles = set()

    # Loop through each line of the file
    for line in infile:

        # This prints each line. You will not want to remove this line.
        #print(line.rstrip())

 	# Add your code here to clean the input
 	
        title = re.search( r'<SEP>(.*)<SEP>(.*)<SEP>(.*)', line, re.M|re.I)
        #print(title.group(3))
        title = title.group(3)

        title = re.sub( r'\[.*\]', '', title)
        title = re.sub( r'\(.*\)', '', title)

        title = re.sub( r'[!&\.\?;]', '', title)
        # adds the clean line to the titles
        # you may want to keep this line
        lower_case_clean_title = title.lower()
        print(lower_case_clean_title)
        titles.add(lower_case_clean_title)

    # loop over the cleaned titles and compute the bigram counts
    bigram_count = 'SOME DATA STRUCTURE'
    for title in titles:
        pass


    # using bigram_count, find most common word following 'word'
    def most_common_word(word):
        return random.choice(choices)

    # return most common word
    return most_common_word


# DON'T WORRY ABOUT CODE BELOW HERE, IT JUST MAKES YOUR LIVE EASIER
def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    return parser.parse_args().file_name


def main():
    print('CSCI 305 Lab 1 submitted by %s' % ME)
    print('  with help from %s\n\n' % ', '.join(COLLABORATORS))
    file_name = get_file_name()
    with open(file_name, 'r') as infile:
        process_file(infile)


if __name__ == '__main__':
    main()
