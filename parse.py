import sys

cpe = (sys.argv[1:])
cpe_array = ''.join(cpe).split(":")

part = ["h","o","a"]
logical = ["*","-"]

def check_cpe(string,array):
    if (array[0] != "cpe" or array[1] != "2.3"):
        raise ValueError('To nie jest ciąg CPE 2.3')
    elif (len(array)!= 13):
        raise ValueError('Niepoprawny ciąg CPE 2.3')
    elif (string[0]==":") or (string[-1]==":"):
        raise ValueError('Niepoprawny ciąg CPE 2.3')
    elif (array[2] not in part and array[2] not in logical):
        raise ValueError('Niepoprawny ciąg CPE 2.3')
    

def correct_dividing(cpe_array):
    final_list = []
    used_words = []
    for n in range(len(cpe_array)):
        if cpe_array[n]=="":
            raise ValueError('Niepoprawny ciąg CPE 2.3')
        if (cpe_array[n][-1]=="\\") and (n!=len(cpe_array)):
            final_list.append(cpe_array[n]+":"+cpe_array[n+1])
            used_words.append(cpe_array[n+1])
        else:
            if cpe_array[n] not in used_words:
                final_list.append(cpe_array[n])
    return final_list

def fix_logical_values(cpe_array):
    for field in cpe_array:
        i = cpe_array.index(field)
        if i<2:
            continue
        if field=="*":
            cpe_array[i]="ANY"
        elif field=="-":
            cpe_array[i]="NA"
        else:
            cpe_array[i] = add_quoting(field)
             
def add_quoting(s):
    result = ""
    idx = 0
    embedded = False
    while idx < len(s):
        c = s[idx]
        if c.isalnum() or c == "_":
            result = result+c
            idx = idx + 1
            embedded = True
            continue
        elif c=="\\":
            result = result+s[idx:idx+1]
            idx = idx + 1
            embedded = True
            continue
        elif c=="*":
            if idx == 0 or idx == len(s)-1:
                result = result + c
                idx = idx+1
                embedded = True
                continue
            else:
                raise ValueError()
        elif c=="?":
            if (idx == 0) or (idx == len(s)-1) or (not embedded and s[idx-1]=="?") or (embedded and s[idx+1]=="?"):
                result = result+c
                idx = idx+1
                embedded = False
                continue
            else:
                raise ValueError()
        result = result + "\\" + c
        idx = idx+1
        embedded = True  
    return result

final_list = correct_dividing(cpe_array)

check_cpe(cpe,final_list)

fix_logical_values(final_list)

cpeDict = {
    "part":str(final_list[2]),
    "vendor":str(final_list[3]),
    "product":str(final_list[4]),
    "version":str(final_list[5]),
    "update":str(final_list[6]),
    "edition":str(final_list[7]),
    "language":str(final_list[8]),
    "sw_edition":str(final_list[9]),
    "target_sw":str(final_list[10]),
    "target_hw":str(final_list[11]),
    "other":str(final_list[12]),
}

print("\nPLAIN PYTHON DICT:\n")
print (cpeDict,"\n")

print("FIXED DOUBLE BACKSLASH PYTHON STRING:\n")
print (f"{{'part': '{final_list[2]}', 'vendor': '{final_list[3]}', 'product': '{final_list[4]}', 'version': '{final_list[5]}', 'update': '{final_list[6]}', 'edition': '{final_list[7]}', 'language': '{final_list[8]}', 'sw_edition': '{final_list[9]}', 'target_sw': '{final_list[10]}', 'target_hw': '{final_list[11]}', 'other': '{final_list[12]}'}}")

dict = f"{{\n'part': '{final_list[2]}',\n'vendor': '{final_list[3]}',\n'product': '{final_list[4]}',\n'version': '{final_list[5]}',\n'update': '{final_list[6]}',\n'edition': '{final_list[7]}',\n'language': '{final_list[8]}',\n'sw_edition': '{final_list[9]}',\n'target_sw': '{final_list[10]}',\n'target_hw': '{final_list[11]}',\n'other': '{final_list[12]}'\n}}"

with open('cpeDict.txt', 'w', encoding='utf-8') as f:
    f.write(dict)



