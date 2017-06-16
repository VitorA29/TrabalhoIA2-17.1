#color_print

class strcolor:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    END = '\033[0m'
    #BOLD = '\033[1m'
    #UNDERLINE = '\033[4m'
    
def cprint(srt, color):
    if(color.upper() == 'VIOLET' or color.upper() == 'V'):
        print(strcolor.VIOLET + srt + strcolor.END)
    elif(color.upper() == "BLUE" or color.upper() == 'B'):
        print(strcolor.BLUE + srt + strcolor.END)
    elif(color.upper() == "GREEN" or color.upper() == 'G'):
        print(strcolor.GREEN + srt + strcolor.END)
    elif(color.upper() == "YELLOW" or color.upper() == 'Y'):
        print(strcolor.YELLOW + srt + strcolor.END)
    elif(color.upper() == "CYAN" or color.upper() == 'C'):
        print(strcolor.CYAN + srt + strcolor.END)
    elif(color.upper() == "RED" or color.upper() == 'R'):
        print(strcolor.RED + srt + strcolor.END)
    else:
        print(srt)
