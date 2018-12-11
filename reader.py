# Ahmed Mustafa
# 12/05/18
#
# this does not work for all cases or scale currently (ie nested lists, dicts of lists)
import json

"""
Extracts all of the ice cream flavors it can find from a json

@param: dict of ice_cream flavors
@out: list of flavors in dict
"""
# TO DO: make type and search recursive
# TO DO: pretty print solution
def find_flavors(sample):
    flavors = []
    for k, v in sample.items():
        if isinstance(v, dict):
            flavors.append(v.get("flavor"))
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    flavors.append(i.get("flavor"))
    return flavors

if __name__ == '__main__':
    # ask for file name to get flavors from
    ice_creams = raw_input("What is your ice cream json?\n")
    # TO DO: serialize input and process in chunks
    # TO DO: flatten json
    try:
        with open(ice_creams) as f:
            test = json.load(f)
    except IOError:
        print "Your file does not exist (or you spelled it wrong)!"
        exit(0)
    find_flavors(test)


