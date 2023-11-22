from main import *

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

    # for object in ngasal['transition']:
    #     print(object)

# thepda=bacapda("pda.txt")
# printpda("pda.txt")

def processingpda(pda, tokens):
    state=pda['start_state']
    stack=[pda['start_stack_symbol']]
    method=pda["pda_type"] 
    cur_token = 0
    berhasil=True
    for token in tokens :
        cur_token = token
        benar=False
        # print("cur_token :",cur_token)
        # print("Stack :",stack)
        # print("state :",state)
        for object in pda["transition"]:
            if(object["current"]==state):
                if(object["input"]==cur_token):
                    if object["top"]==stack[-1]:
                        stack.pop()
                        # print(f"infotop:{stack[-1]}")
                        # print(f"statebefore:{state}")
                        if object['push'][0]!="e":
                            # stack.append(object['push'][0])
                            for any in reversed(object["push"]):
                                stack.append(any)
                        state=object['next']
                        # print(f"next:{object['next']}")
                        # print(f"push:{object['push']}")
                        # print(f"infotop2:{stack[-1]}")
                        # print(f"{object['current']} and {state}")
                        benar=True

        print(f"current token : {token}")
        print(f"current state : {state}")
        print(f"Top Stack : {stack[-1]}")
        print(stack)
        print(benar)
        print()
        if not benar:
            berhasil=False
            break #matikan break nyo kalo mau lihat semua state

    if berhasil:
        if method=="F" and state in pda['final']:
            print("YA KAMU BETUL")
        elif method=="E" and stack==[pda['start_stack_symbol']]:
            print("YA KAMU BETUL")
        else:
            print("SAYANG SEKALI KAMU SALAH")

thepda=bacapda("pda.txt")
# tokens=['<html', '>', '<head', '>', '<script', '>', '</script', '>', '</head', '>', '<body', '>', '</body', '>', '</html', '>']
tokens = print_html_tags_and_text("tes.html")
processingpda(thepda,tokens)