#!/usr/bin/

import sys
import csv
from os import listdir
from color_print import cprint

def main():
	
	BK_PATH = sys.argv[1]
	OUTPUT_RPOS = "rpos.pl"
	
	cprint("Creating " + OUTPUT_RPOS + "...", 'b')
	kb_file_rpos =  open(OUTPUT_RPOS, 'a')
	d = {"rpos":""}
	
	dirfiles = [f for f in listdir(BK_PATH)]
	for file_name in dirfiles:
		with open(BK_PATH + file_name, newline='') as csvfile:
			data = csv.DictReader(csvfile)
			for row in data:
				if(row["Action"][0] == "y"):
					#relations
					clause = "rel(" + row["Entity"] + "," + row["Relation"]
				
					clause = clause + ",'" + row["Value"] + "').\n" \
						if row["Relation"] == "haswikipediaurl" \
						else clause + "," + row["Value"] + ").\n"		
					if((d['rpos'].find(clause))==-1):
						cprint(clause, 'y')
						d['rpos'] += clause
				
				
	kb_file_rpos.write(d['rpos'])
	kb_file_rpos.close()
	
if __name__ == "__main__":
	 main()
