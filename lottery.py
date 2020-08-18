class Lottery:
    def __init__(self):
        return

    def sortByOdds(self, rules):
        rules=list(rules) # convert to list
        name_and_rules_split =[]
        rules_str_list = []
        rules_variables=[]
        results_dict = {}
        result_list = []
        names=[]
        # unpack the rules tuple of strings. "<NAME>:_<CHOICES>_<BLANKS>_<SORTED>_<UNIQUE>"
        # underscore = exactly one space, no leading zeros, no leading or trailing
        # spaces. name may contain a space, sorted will be 'T' or 'F'
        for s in rules:
            name_and_rules_split = s.split(": ")
            rules_str_list = name_and_rules_split[1].split(" ")
            name = name_and_rules_split[0]
            choices = int(rules_str_list[0])
            blanks = int(rules_str_list[1])
            if rules_str_list[2] == "T":
                sortd = True
            else:
                sortd = False
            if rules_str_list[3] == "T":
                unique = True
            else:
                unique = False
            # build a list of rules variables for each lottery entry
            rules_variables.append([name,choices,blanks,sortd,unique])
            names.append(name)
        # calculate the probability of how easy it is to win
        probability=[]
        for x in range(len(rules_variables)):
            probability.append(0) # init probability entry
            # unpack the rules into named variables
            # print(rules_variables)
            [name, choices, blanks, sortd, unique] = rules_variables[x]
            if sortd and unique:
                for y in range(blanks):
                    probability[x] += choices - y
            elif sortd and not unique:
                probability[x] = pow(choices,blanks) - blanks*choices
            elif not sortd and unique:
                probability[x] = 1 # so we don't zero out
                for y in range(blanks):
                    probability[x] *= (choices-y)
            elif not sortd and not unique:
                probability[x] = pow(choices,blanks)
        # build a dictionary of with probability * rules string
        for i in range(len(probability)):
            results_dict[probability[i]] = names[i]
        # sort the dictionary by probability (i.e. key)
        sorted_rules_variables = sorted(results_dict.items())
        #extract the rule from the sorted dictionary
        for i in sorted_rules_variables:
            result_list.append(i[1])
        print(results_dict)
        return result_list


# TEST
lottery = Lottery()
print("-----------------------")
# there is some end case I am missing here....
# rules={"INDIGO: 93 8 T F",
#     "ORANGE: 29 8 F T",
#     "VIOLET: 76 6 F F",
#     "BLUE: 100 8 T T",
#     "RED: 99 8 T T",
#     "GREEN: 78 6 F T",
#     "YELLOW: 75 6 F F"}

rules={"PICK TWO DIFFERENT: 10 2 F T",
    "PICK TWO LIMITED: 10 2 T T",
    "PICK TWO IN ORDER: 10 2 T F",
    "PIC ANY TWO: 10 2 F F"}
print(lottery.sortByOdds(rules))
