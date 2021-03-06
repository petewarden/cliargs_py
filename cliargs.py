# cliargs_py - A nicer interface to command line arguments
#
# See cliargs_example.py for a demonstration of how to use this
# 
# By Pete Warden, http://petewarden.typepad.com - freely reusable with no restrictions.

import sys, string

def print_usage_and_exit(cliargs):
	print "Usage:"
	
	for long, arginfo in cliargs.items():
		short = arginfo['short']
		type = arginfo['type']
		required = (type=='required')
		optional = (type=='optional')
		description = arginfo['description']
		
		output = '-'+short+'/--'+long+' '

		if optional or required:
			output += '<value> '

		output += ': '+description

		if required:
			output += ' (required)'

		print output
	
	exit()

def get_options(cliargs):

    options = {'unnamed': [] }
    skip_next = False
    for index in range(1, len(sys.argv)):
        if skip_next:
            skip_next = False
            continue
    
        currentarg = sys.argv[index].lower()
        argparts = currentarg.split('=')
        namepart = argparts[0]

        if namepart.startswith('--'):
            longname = namepart[2:]
        elif namepart.startswith('-'):
            shortname = namepart[1:]
            longname = shortname
            for name, info in cliargs.items():
                if shortname==info['short']:
                    longname = name
                    break
        else:
            longname = 'unnamed'

        if longname=='unnamed':
            options['unnamed'].append(namepart)
        else:
            if longname not in cliargs:
                print "Unknown argument '"+longname+"'"
                print_usage_and_exit(cliargs)
            
            arginfo = cliargs[longname]
            argtype = arginfo['type']
            if argtype=='switch':
                value = True
            elif len(argparts) > 1:
                value = argparts[1]
            elif (index+1) < len(sys.argv):
                value = sys.argv[index+1]
                skip_next = True
            else:
                print "Missing value after '"+longname+"'"
                print_usage_and_exit(cliargs)

            options[longname] = value

    for longname, arginfo in cliargs.items():
        type = arginfo['type']

        if longname not in options:
            if type == 'required':
                print "Missing required value for '"+longname+"'"
                print_usage_and_exit(cliargs)
            elif type == 'optional':
                if not 'default' in arginfo:
                    die('Missing default value for '+longname)
                options[longname] = arginfo['default']
            elif type == 'switch':
                options[longname] = False
            else:
                die('Unknown type "'+type+'" for '+longname)

    return options
