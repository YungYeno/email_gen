import json
from random import randint
from colorama import init, Fore

# initialize colours
init()
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
WHITE = Fore.WHITE
CYAN = Fore.CYAN


def intro():
    print(f"""{CYAN}      
 ______     __    __     ______     __     __            ______     ______     __   __    
/\  ___\   /\ "-./  \   /\  __ \   /\ \   /\ \          /\  ___\   /\  ___\   /\ "-.\ \   
\ \  __\   \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \____     \ \ \__ \  \ \  __\   \ \ \-.  \  
 \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_____\     \ \_____\  \ \_____\  \ \_\\"\_\ 
  \/_____/   \/_/  \/_/   \/_/\/_/   \/_/   \/_____/      \/_____/   \/_____/   \/_/ \/_/ 
                                            
                                                        {WHITE}-- Made with ❤️  by YY

    """)


# Reads and opens the correct json files
def read_json():
    with open('names.json') as name:
        names = json.load(name)
    with open('surnames.json') as surname:
        surnames = json.load(surname)

    return names, surnames


# Collects all given data to craft the appropriate amount of e-mails. Generated email are collected in list and returned.
def generate(names, surnames, max_email):
    hosts = ["@gmail", "@hotmail", "@outlook", "@protonmail", "@aol", "@yahoo", "@zoho", "@gmx"]
    generated = []
    for i in range(0, max_email):
        email = names[randint(0, len(names) - 1)] + "_" + surnames[randint(0, len(surnames) - 1)] + hosts[
            randint(0, len(hosts) - 1)] + ".com"
        generated.append(email)
    return generated


# Save generated e-mails in 'generated.txt'.
def write_txt(generated, max_email):
    with open('generated.txt', 'w') as file:
        for email in generated:
            file.write("%s\n" % email)
        print(f"{GREEN}[ ✅ ]{WHITE} all {GREEN}{max_email}{WHITE} emails are saved in {GREEN}generated.txt{WHITE} ! ")


# Save generated e-mails in 'generated.csv'.
def write_csv(generated, max_email):
    file = open('generated.csv', 'w')
    for email in generated:
        file.write("%s\n" % email)
    print(f"{GREEN}- ✅{WHITE} all {GREEN}{max_email}{WHITE} emails are saved in {GREEN}generated.csv{WHITE} ! ")


# Print all generated e-mails in command line.
def output(generated, max_email):
    print(f"{GREEN}- ✅ {WHITE}generated {GREEN}{max_email}{WHITE} emails -> \n")
    for email in generated:
        print(email)
