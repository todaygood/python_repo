#!/usr/bin/python -tt
#
# A simple tool to check ABI compliance.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

__author__ = "Jon Masters <jcm@redhat.com>"
__version__ = "2.0"
__date__ = "2011/05/23"
__copyright__ = "Copyright (C) 2011 Red Hat, Inc"
__license__ = "GPL"

import getopt
import os
import re
import string
import sys

true = 1
false = 0

def read_abi_whitelist(whitelist_file):
	'''Read in the ABI whitelist'''

	if not os.path.isfile(whitelist_file):
		print "WARNING: Cannot read whitelist file"
		sys.exit(1)

	kabi_file = open(whitelist_file,"r")
	symbols = []

	while true:
		in_line = kabi_file.readline()

		if in_line == "":
			break
		if in_line == "\n":
			continue
		string.split(in_line)
		if in_line[0] == '[':
			whitelist_name=in_line[1:-2]
			continue
		symbol=in_line[1:-1]

		symbols.append(symbol)

	return symbols

def read_module(module):
	'''Read in symbols from a module'''

	symbols = []

	if not os.path.isfile(module):
		print "WARNING: Cannot read module file"
		sys.exit(1)

	if module[-2:] == "ko":
		nm = os.popen('readelf -sW ' + module + ' | sed -nre \'s:.*UND (.*):\\1:p\'')
	else:
		nm = open(module,"r")

	while true:
		in_line = nm.readline()
		if (not len(in_line)):
			break

		if (len(in_line) and in_line[-1]) == '\n':
				in_line = in_line[:-1]
		if (len(in_line) and in_line[-1]) == '\r':
				in_line = in_line[:-1]
		if (not len(in_line)):
			continue

		if in_line[0] == ".":
			in_line = in_line[1:]

		symbols.append(in_line)

	nm.close()

	return symbols

def abi_check(whitelist, module):
	'''Check ABI compliance of a set of symbols.'''

	misssyms = []

	for modsym in module:
		if modsym not in whitelist:
			misssyms.append(modsym)

	return misssyms

def main():
	'''Main function entry point for abi_check ABI compliance tester.'''

	kernel = ''
	arch = ''
	whitelist = ''
	whitelist_package = ''
	module = ''
	opts = []
	args = []

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'k:w:')
	except:
		pass

	uname = os.popen('uname -r')
	kernel = uname.readline()[:-1]
	uname.close()

	uname = os.popen('uname -m')
	arch = uname.readline()[:-1]
	uname.close()

	rpmquery = os.popen('rpm -q --queryformat \'%{VERSION}-%{RELEASE}\' kabi-whitelists')
	whitelist_package = rpmquery.readline()
	rpmquery.close()

	print "Red Hat Enterprise Linux 6 ABI Checker"
	print "--------------------------------------"
	print ""
	print "ABI Checker version: " + __version__

	for o, v in opts:

		if o == '-w':
			whitelist = v

	if whitelist == '':
		whitelist = '/lib/modules/kabi/'+'kabi_whitelist'+'_'+arch

	if args == []:
		print "Usage: ./rhel6_kabi_check [-w whitelist] module"
		print ""
		print "Specifying the whitelist path is optional. By default the reference"
		print "files for the current minor release of Red Hat Enterprise Linux 6 will"
		print "be used (/lib/modules/kabi), as supplied by the kabi-whitelists package."
		print ""
		print "The module is either a filename ending in a .ko postfix, or is otherwise"
		print "assumed to be a text file containing a list of symbols."
		print ""
		print "Example of checking a pre-built module:"
		print "    ./abi_check e1000e.ko"
		print ""
		print "Example of checking against a text file symbol dump"
		print "(produced using a utility such as nm, or readelf as in"
		print " readelf -sW e1000e.ko | sed -nre 's:.*UND (.*):\\1:p'"
		print " and saved to a text file such as e1000e_syms.txt):"
		print "   ./abi_check e1000e_syms.txt"
		print ""
		sys.exit(1)

	module = args[0]

	print ""
	print "Module:    " + module
	print "Kernel:    " + kernel
	print "Whitelist: " + whitelist + " " + "(" + whitelist_package + ")"
	print ""

	try:
		whitelist_symbols = read_abi_whitelist(whitelist)

		module_symbols = read_module(module)

		missing_abi_symbols = abi_check(whitelist_symbols, module_symbols)

	except:
		print "WARNING: An error occured running this program."
		sys.exit(1)

	if missing_abi_symbols != []:
		print "WARNING: The following symbols are used by your module"
		print "WARNING: and are not on the ABI whitelist."
		print ""
		for sym in missing_abi_symbols:
			print "symbol: " + sym
	else:
		print "NOTE: Your module seems to use only official ABI."
		print ""
		print "NOTE: This does not constitute Red Hat certification"
		print "NOTE: Red Hat does not support third party modules."

	print ""

if __name__ == '__main__':
	main()
