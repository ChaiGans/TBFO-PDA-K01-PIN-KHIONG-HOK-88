from termcolor import colored

def bacapda(path: str) -> dict :
    pda = {
        'states' : [],
        'input_symbols' : [],
        'stack_symbols' : [],
        'start_state' : 0,
        'start_stack_symbol' : 0,
        'final' : [],
        'pda_type' : 'E',
        'transition' : [],
    }

    with open(path, 'r') as file:
        line_number = 1
        for line in file:
            if line_number==1:
                words = line.split()
                for something in words:
                    pda['states'].append(something)
            elif line_number ==2:
                words = line.split()
                for something in words:
                    pda['input_symbols'].append(something)
            elif line_number ==3:
                words = line.split()
                for something in words:
                    pda['stack_symbols'].append(something)
            elif line_number ==4:
                pda['start_state']=line.strip()
            elif line_number ==5:
                pda['start_stack_symbol']=line.strip()
            elif line_number ==6:
                words = line.split()
                for something in words:
                    pda['final'].append(something)
            elif line_number ==7:
                pda['pda_type']=line.strip()
            elif line_number >= 8:
                if line!= '\n':
                    trans ={
                        'current' : 0,
                        'input' : 0,
                        'top' : 0,
                        'next' : 0,
                        'push' : 0,
                    }

                    words = line.split()
                    word0 = words[0]
                    trans['current']=word0
                    if word0 not in pda["states"]: #otomatis masuki nama state dari transition function
                        pda["states"].append(word0)
                    word1=words[1]
                    trans['input']=word1
                    word2=words[2]
                    trans['top']=word2
                    if word2 not in pda["stack_symbols"]: #otomatis masuki stack symbol dari transition function
                        pda["stack_symbols"].append(word2) 
                    word3=words[3]
                    trans['next']=word3
                    word4=words[4]
                    trans['push']=word4.split(',')

                    if trans not in pda['transition']:
                        pda['transition'].append(trans)
                
            line_number += 1
    
    return pda


# PRINT SEMUA PDA
def printpda(string):
    ngasal=bacapda(string)
    # print(ngasal['states'])
    for object in ngasal['states']:
        print(object,end=" ")
    print()
    print(ngasal['input_symbols'])
    # print(ngasal['stack_symbols'])
    for object in ngasal['stack_symbols']:
        print(object,end=" ")
    print()
    print(ngasal['start_state'])
    print(ngasal['start_stack_symbol'])
    print(ngasal['final'])
    print(ngasal['pda_type'])

def processingpda(pda, html):
    state=pda['start_state']
    stack=[pda['start_stack_symbol']]
    method=pda["pda_type"] 
    berhasil=True
    last_temp = None
    for temp in html :
        token=temp[0]
        if last_temp is None:
            last_temp = temp
        benar=False
        if token=='notvalid':
            break
        if token=="":
            continue
        for object in pda["transition"]:
            if(object["current"]==state and object["current"]!="FINAL"):
                if(object["input"]=="e"):
                    if object["top"]==stack[-1]:
                        stack.pop()
                        if object['push'][0]!="e":
                            # stack.append(object['push'][0])
                            for any in reversed(object["push"]):
                                stack.append(any)
                        state=object['next']
            if(object["current"]==state):                        
                if(object["input"]==token):
                    if object["top"]==stack[-1]:
                        stack.pop()
                        if object['push'][0]!="e":
                            for any in reversed(object["push"]):
                                stack.append(any)
                        state=object['next']
                        benar=True

        if not benar:
            berhasil=False
            break #matikan break nyo kalo mau lihat semua state
        last_temp = temp

    if berhasil:
        if method=="F" and state in pda['final']:
            print(colored("\nCongratulations","green",attrs=['bold'])+colored(", No problems detected\n","yellow"))
        elif method=="E" and stack==[pda['start_stack_symbol']]:
            print(colored("\nCongratulations","green",attrs=['bold'])+colored(", No problems detected\n","yellow"))
        else:
            print(colored("\nError warning :","red",attrs=['bold']))
            print(colored("   Error","magenta")+" in "+colored(f"line number {last_temp[1]}","yellow"))
            if temp[0]=='notvalid':
                print(colored("syntax","blue",attrs=['underline','bold'])+colored(" error ","red",attrs=['bold']) + colored("detected\n","blue",attrs=['bold']))
            else:
                found=True
                for object in pda["transition"]:
                    if(object["current"]==state):
                        if object["top"]==stack[-1]:
                            if(object["push"][0]=="e"):
                                if(object["input"]=="e"):
                                    print("hayolo")
                                else:
                                    print(colored("expected","blue",attrs=['bold'])+f" an "+colored("'","green")+colored(f"{object['input']}","green",attrs=['underline'])+colored("'","green")+" before "+colored("'","blue")+colored(f"{temp[0]}","blue",attrs=['underline'])+colored("'\n","blue"))
                                found=True
                                break
                if not found:
                    for object in pda["transition"]:
                            if(object["current"]==state):
                                if object["top"]==stack[-1]:
                                    if(object["push"][0]!="e"):
                                        print(colored("expected","blue",attrs=['bold'])+f" an "+colored("'","green")+colored(f"{object['input']}","green",attrs=['underline'])+colored("'","green")+" before "+colored("'","blue")+colored(f"{temp[0]}","blue",attrs=['underline'])+colored("'\n","blue"))
                                        # break
    else :
        found=False
        print(colored("\nError warning :","red",attrs=['bold']))
        print(colored("   Error","magenta")+" in "+colored(f"line number {temp[1]}","yellow"))
        for object in pda["transition"]:
            if(object["current"]==state):
                if object["top"]==stack[-1]:
                    if(object["push"][0]=="e"):
                        if(object["input"]=="e"):
                            print(colored("expected ","blue",attrs=['bold'])+colored("none","green",attrs=['underline'])+" instead of "+colored("'","blue")+colored(f"{temp[0]}","blue",attrs=['underline'])+colored("'\n","blue"))
                        else:
                            print(colored("expected","blue",attrs=['bold'])+f" an "+colored("'","green")+colored(f"{object['input']}","green",attrs=['underline'])+colored("'","green")+" before "+colored("'","blue")+colored(f"{temp[0]}","blue",attrs=['underline'])+colored("'\n","blue"))
                        found=True
                        break
        if not found:
            for object in pda["transition"]:
                    if(object["current"]==state):
                        if object["top"]==stack[-1]:
                            if last_temp[0]=="<img":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("src", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            elif last_temp[0]=="<a":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("href", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            elif last_temp[0]=="<link":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("rel", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            elif last_temp[0]=="<button":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("type", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            elif last_temp[0]=="<form":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("action", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            elif last_temp[0]=="<input":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored("type", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break
                            # input_to_display = "alt" if "alt" in [obj["input"] for obj in pda["transition"]] else object["input"]
                            elif object["push"][0] != "e":
                                print(colored("expected", "blue", attrs=['bold']) + f" an " + colored("'", "green") + colored(f"{object['input']}", "green", attrs=['underline']) + colored("'", "green") + " before " + colored("'", "blue") + colored(f"{temp[0]}", "blue", attrs=['underline']) + colored("'\n", "blue"))
                                break