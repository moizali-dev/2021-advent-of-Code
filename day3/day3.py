#############
### DAY 3 ###
#############

def binary_diagnostic(file):

    f = open(file, "r")

    dic = {}
    for i in f.readlines():
        binary_no = i.strip()
        for j in range(len(binary_no)):
            if j not in dic:
                dic_sub = {}
                if binary_no[j] not in dic_sub:
                    dic_sub[binary_no[j]] = 1
                else:
                    dic_sub[binary_no[j]] += 1
                dic[j] = dic_sub
            else:
                dic_sub = dic[j]
                if binary_no[j] not in dic_sub:
                    dic_sub[binary_no[j]] = 1
                else:
                    dic_sub[binary_no[j]] += 1
                dic[j] = dic_sub

    gamma_str = ""

    for k,v in dic.items():
        gamma_str += max(v, key=v.get)

    gamma = int(gamma_str,2)

    eps_str = ""

    for k,v in dic.items():
        eps_str += min(v, key=v.get)

    eps = int(eps_str,2)

    return (gamma * eps)


def binary_diagnostic_part2(file):

    f = open(file, "r")

    # Creating list of binary numbers
    binary_list = []
    for i in f.readlines():
        binary_no = i.strip()
        binary_list.append(binary_no)

    def binary_diag_dic(binary_list, idx, type):

        dic = {}

        # Save all the binary numbers in dic based on idx bit and count the 0's and 1's for idx bit
        for binary_no in binary_list:

            if binary_no[idx] not in dic:
                sub_dic = {"count" : 0, "list" : []}
                sub_dic["count"] += 1
                sub_dic["list"].append(binary_no)
                dic[binary_no[idx]] = sub_dic

            else:
                sub_dic = dic[binary_no[idx]]
                sub_dic["count"] += 1
                sub_dic["list"].append(binary_no)

        # Extract the list according to type criteria
        if type == "Oxygen":
            if dic["0"]["count"] > dic["1"]["count"]:
                new_dic = dic["0"]["list"]
            else:
                new_dic = dic["1"]["list"]
        elif type == "CO2":
            if dic["0"]["count"] > dic["1"]["count"]:
                new_dic = dic["1"]["list"]
            else:
                new_dic = dic["0"]["list"]


        return new_dic

    # Iterating over the binary list to get the binary number for Oxygen
    new_lst = binary_list
    for i in range(len(binary_list[0])):
        try:
            new_lst = binary_diag_dic(new_lst, i, "Oxygen")
        except:
            pass
    oxygen_binary = new_lst[0]

    # Iterating over the binary list to get the binary number for CO2
    new_lst = binary_list
    for i in range(len(binary_list[0])):
        try:
            new_lst = binary_diag_dic(new_lst, i, "CO2")
        except:
            pass
    co2_binary = new_lst[0]


    return (int(oxygen_binary,2) * int(co2_binary, 2))

print(binary_diagnostic("day3/day3_2021_input"))
print(binary_diagnostic_part2("day3/day3_2021_input"))