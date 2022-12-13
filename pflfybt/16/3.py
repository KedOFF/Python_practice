from tabulate import tabulate

def print_ip_table(reach_ip, unreach_ip):
   
    main_dict = {}
    main_dict["Reachable"] = reach_ip
    main_dict["Unreachable"] = unreach_ip
    return print(tabulate(main_dict, headers = "keys"))

if __name__  == "__main__":
    reach_ip = ["10.1.1.1", "10.1.1.2"]
    unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print (print_ip_table(reach_ip, unreach_ip))
