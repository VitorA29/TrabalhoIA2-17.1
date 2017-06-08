#!/usr/bin/

import sys
import csv
from color_print import cprint
    
def main():
    INPUT = sys.argv[1]
    OUTPUT_POS = sys.argv[2]
    OUTPUT_REL = sys.argv[3]
    OUTPUT_NEG = sys.argv[4]
    cprint("Reading " + INPUT + "...", 'b')
    cprint("Creating " + OUTPUT_POS + "...", 'b')
    kb_file_pos =  open(OUTPUT_POS, 'w')
    cprint("Creating " + OUTPUT_NEG + "...", 'b')
    kb_file_neg = open(OUTPUT_NEG, 'w')
    cprint("Creating " + OUTPUT_REL + "...", 'b')
    kb_file_rel =  open(OUTPUT_REL, 'w')
    i=0
    j=0
    k=0
    dicN={}
    dicP={}
    dicR={}
    with open(INPUT, newline='') as csvfile:
        data = csv.DictReader(csvfile)      
        for row in data:
            if(row["Action"][0] == "n"): #neg relations
                if(row["Relation"] == "generalizations"): continue
                else:
                    clause = ":- \+" + row["Relation"]
                    if(clause == "haswikipediaurl"):
                        clause = clause + "(" + row["Entity"] + ",'" + row["Value"] + "').\n"
                    else:
                        clause = clause + "(" + row["Entity"] + "," + row["Value"] + ").\n"
                    cprint(clause, 'r')
		    dicN.add(i++, clause)
                    #kb_file_neg.write(clause)

            elif(row["Action"][0] == "y"):
                if(row["Relation"] == "generalizations"):
                    clause = row["Action"][1:] + "(" + row["Entity"] + ").\n"
                    cprint(clause, 'y')
		    dicP.add(j++, clause)
                    #kb_file_pos.write(clause)
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
		    dicP.add(j++, clause)
                    #kb_file_pos.write(clause)
                    
                    clause = row["Action"].split(",")[1] + "(" + row["Entity"] + ").\n"
                    cprint(clause, 'y')
		    dicP.add(j++, clause)
                    #kb_file_pos.write(clause)
                    
                    #relations
                    clause = row["Relation"]
                    if(clause == "haswikipediaurl"):
                        clause = clause + "(" + row["Entity"] + ",'" + row["Value"] + "').\n"
                    else:
                        clause = clause + "(" + row["Entity"] + "," + row["Value"] + ").\n"
                    cprint(clause, 'y')
		    dicR.add(k++, clause)
                    #kb_file_rel.write(clause)
            else: continue
        
        lista = dicP.values()
	for clause in lista:
		kkb_file_pos.write(clause)
	lista = dicR.values()
	for clause in lista:
		kkb_file_rel.write(clause)
	lista = dicN.values()
	for clause in lista:
		kkb_file_neg.write(clause)
        kb_file_pos.close()
        kb_file_rel.close()     
        kb_file_neg.close()
    
if __name__ == "__main__":
     main()
     

