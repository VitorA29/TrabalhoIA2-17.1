#!/usr/bin/

import sys
import csv
from color_print import cprint
    
def main():
    INPUT = sys.argv[1]
    OUTPUT = sys.argv[1]
    OUTPUT_FPOS = "fpos.pl"
    OUTPUT_RPOS = "rpos.pl"
    OUTPUT_FNEG = "fneg.pl"
    OUTPUT_RNEG = "rneg.pl"
    
    cprint("Reading " + INPUT + "...", 'b')
    
    cprint("Creating " + OUTPUT_FPOS + "...", 'b')
    kb_file_fpos =  open(OUTPUT_FPOS, 'a')
    cprint("Creating " + OUTPUT_RPOS + "...", 'b')
    kb_file_rpos =  open(OUTPUT_RPOS, 'a')
 
    cprint("Creating " + OUTPUT_FNEG + "...", 'b')
    kb_file_fneg = open(OUTPUT_FNEG, 'a')
    cprint("Creating " + OUTPUT_RNEG + "...", 'b')
    kb_file_rneg =  open(OUTPUT_RNEG, 'a')
    
    with open(INPUT, newline='') as csvfile:
        data = csv.DictReader(csvfile)      
        for row in data:
            if(row["Action"][0] == "n"): #neg relations
                if(row["Relation"] == "generalizations"):
                    clause = ":- \+" + row["Action"][1:] + "(" + row["Entity"] + ").\n"
                    cprint(clause, 'r')
                    kb_file_fneg.write(clause)
                else:
                    clause = "(" + row["Entity"] + ",'" + row["Value"] + "').\n" \
                        if row["Relation"] == "haswikipediaurl" \
                        else "(" + row["Entity"] + "," + row["Value"] + ").\n"
                    clause = ":- \+" + row["Relation"] + clause
                    cprint(clause, 'r')
                    kb_file_rneg.write(clause)

            elif(row["Action"][0] == "y"):
                if(row["Relation"] == "generalizations"):
                    clause = row["Action"][1:] + "(" + row["Entity"] + ").\n"
                    cprint(clause, 'y')
                    kb_file_fpos.write(clause)
                else:
                    #facts
                    clause = row["Action"].split(",")[2]
                    if(clause == "url"):
                        clause = clause + "('" + row["Value"] + "').\n"
                    elif(clause == "http" or clause == "https"):
                        clause = "url('" + row["Value"] + "').\n"
                    else:
                        clause = clause + "(" + row["Value"] + ").\n"
                    cprint(clause, 'y')
                    kb_file_fpos.write(clause)
                    
                    clause = row["Action"].split(",")[1] + "(" + row["Entity"] + ").\n"
                    cprint(clause, 'y')
                    kb_file_fpos.write(clause)
                    
                    #relations
                    clause = "(" + row["Entity"] + ",'" + row["Value"] + "').\n" \
                        if row["Relation"] == "haswikipediaurl" \
                        else "(" + row["Entity"] + "," + row["Value"] + ").\n"
                    clause = row["Relation"] + clause
                    cprint(clause, 'y')
                    kb_file_rpos.write(clause)
            else: continue
        
        kb_file_fpos.close()
        kb_file_rpos.close()
        kb_file_fneg.close()    
        kb_file_rneg.close()
    
if __name__ == "__main__":
     main()
     

