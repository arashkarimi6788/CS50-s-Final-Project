import sys
from tabulate import tabulate
from datetime import datetime
import csv
from csv import writer

def main():
    data = []
    column_name = ["Category", "Cost($)", "Count/Explain", "Date"]
    data.append(column_name)
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    if sys.argv[1].lower() != "household.csv":
        sys.exit("No such file")
    else:
        print("Reading Backup File is DONE!")
    with open('household.csv','r') as file_data:
            for line in csv.reader(file_data):
                data.append(line)
    global now
    now = datetime.now()
    m = now.strftime("%m")

    if (data[-1][-1][3:5]) != (now.strftime("%m")):
        open("household.csv", 'w', newline='')
    str_month = month_check(m)

    while True:
        try:
            f_dict = {}
            f_list = []
            f_dict["Category"] = input("Please select category: Housing, Medical, Bill & Insurance, Clothing, Rent & Loan, and Etcetra: ")
            if check_category(f_dict["Category"]):
                while True:
                    try:
                        f_dict["Cost($)"] = input("How much did you pay? ")
                        if check_cost(f_dict["Cost($)"]):
                            f_list.append(f_dict["Category"].upper())
                            f_list.append(f_dict["Cost($)"])
                            f_dict["Count/Explain"] = input("Explain more or insert the count: ")
                            f_list.append(f_dict["Count/Explain"])
                            f_dict["Date"] = now.strftime("%d/%m/%Y")
                            f_list.append(f_dict["Date"])
                            with open("household.csv", 'a', newline='') as file_data:
                                writer_object = writer(file_data)
                                writer_object.writerow(f_list)
                            data.append(f_list)
                            break
                        else:
                            pass
                    except EOFError:
                        break
            else:
                pass
        except EOFError:
            break
    total_pay = total_payment(data, str_month)
    print()
    print(tabulate(total_pay[1:], headers=column_name, tablefmt="fancy_grid"))
    specific_expenses = final_dict(data)

    print("You have spent in particular:")
    for i in specific_expenses:
        print(f"{i:24} : {specific_expenses[i]:<10}")


def total_payment(data, m):
    total_payment = 0
    global now
    now = datetime.now()
    for i in range(1, len(data)):
        total_payment += int(data[i][1])
    data.append([f"Total Payment {m}", total_payment, "----", now.strftime("%d/%m/%Y")])
    return data

def final_dict(data):
    count_dict = {"Total Housing" : 0,
                  "Total Medical" : 0,
                  "Total Rent & Loan" : 0,
                  "Total Bill & Insurance" : 0,
                  "Total Clothing" : 0,
                  "Total Etcetra" : 0
                }

    for item in data:
        if item[0] == "HOUSING":
            count_dict["Total Housing"] += int(item[1])
        elif item[0] == "MEDICAL":
            count_dict["Total Medical"] += int(item[1])
        elif item[0] == "RENT & LOAN":
            count_dict["Total Rent & Loan"] += int(item[1])
        elif item[0] == "BILL & INSURANCE":
            count_dict["Total Bill & Insurance"] += int(item[1])
        elif item[0] == "ETCETRA":
            count_dict["Total Etcetra"] += int(item[1])
        elif item[0] == "CLOTHING":
            count_dict["Total Clothing"] += int(item[1])
    return count_dict

def check_category(c):
    if c.lower() in ["housing", "medical", "bill & insurance", "clothing", "rent & loan", "etcetra"]:
        return True
    else:
        return False

def check_cost(cost):
    try:
        if int(cost) > 0:
            return True
        else:
            raise ValueError
    except ValueError:
        return False


def month_check(m):
    month = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
    return month[m]

if __name__ == "__main__":
    main()
