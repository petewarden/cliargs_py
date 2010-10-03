#!/usr/bin/env python

# This is an example demonstrating how to use the cliargs command-line argument
# library. By Pete Warden, http://petewarden.typepad.com - freely reusable
# with no restrictions.

import cliargs

args = {
	'filename': {
		'short': 'f',
		'type': 'required',
		'description': 'This is a required argument, the value can be specified as either -f/--filename=<value> or -f/--filename <value>. If the argument is not specified, the script will print this usage information and exit',
		'default': ''
	},
	'queryurl': {
		'short': 'q',
		'type': 'optional',
		'description': 'This is an optional argument, if -q/--queryurl is not specified, the default value of "empty" will be set into the result array',
		'default': 'http://example.com'
	},
	'dohost': {
		'short': 'h',
		'type': 'switch',
		'description': 'Switches default to false if they\'re not included on the command line, or true if they are present (you don\'t specify a value)',
	}
}	

options = cliargs.get_options(args)

filename = options['filename']
queryurl = options['queryurl']
dohost = options['dohost']

if filename == 'bad':
    print "You gave me a filename I didn't like: '"+filename+"'";
    cliargs.print_usage_and_exit(args);

output = "All arguments set: filename='"+filename+"', queryurl='"+queryurl+"', dohost='";
if dohost:
    output += "True"
else:
    output += "False"
output += "'"
print output

unnamed = options['unnamed'];
if len(unnamed) == 0:
    print "No unnamed arguments";
else:
    print "Unnamed arguments: "+str(unnamed)
