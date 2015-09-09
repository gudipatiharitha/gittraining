#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
	names =[]
	with open (filename,'r') as f:
		data=f.read()
	year = re.search(r'Popularity\sin\s(\d{4})', data) #regEx for selecting only that string from input file
	if not year:
		sys.stderr.write("Couldn't find the year")   #if given search method didn't match , we'll show err msg and exit 
		sys.exit(1)
	year1=year.group(1) # to take only year not whole string
	names.append(year1)
	#print names
	names_and_rank=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',data) #regEx for finding all these 3 vars from file

	# what is TypeError: '_sre.SRE_Match' object is not iterable ???

	lst={}
	for rank, boyname, girlname in names_and_rank:	# To unzip the names_and_rank into three variables 
		if boyname not in lst:
			lst[boyname] = rank
		if girlname not in lst:
			lst[girlname] = rank
	sorted_names = sorted(lst.keys())
	for  in sorted_names:
		names.append(i + " " + lst[char])
	return names


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
  	names = extract_names(filename)
  text = '\n'.join(names) + '\n'
  if summary:
  	with open(filename + '.summary', 'w+') as f:
  		f.write(text)
  else:
  	print text

if __name__ == '__main__':
  main()

