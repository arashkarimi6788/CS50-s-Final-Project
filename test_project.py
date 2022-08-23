import pytest
from project import total_payment
from project import final_dict
from project import check_category
from project import check_cost
from project import month_check

def test_total_payment():
    assert total_payment([["Category", "Cost($)", "Count/Explain", "Date"], ["CLOTHING","100","shoes","19/08/2022"], ["MEDICAL","150","Tom got flu","19/08/2022"]], 'Aug') == [["Category", "Cost($)", "Count/Explain", "Date"], ["CLOTHING","100","shoes","19/08/2022"], ["MEDICAL","150","Tom got flu","19/08/2022"], ["Total Payment Aug", 250, "----", "23/08/2022" ]]

def test_final_dict():
    assert final_dict([["Category", "Cost($)", "Count/Explain", "Date"], ["CLOTHING","100","shoes","19/08/2022"], ["MEDICAL","150","Tom got flu","19/08/2022"], ["HOUSING","650","Fruits and vegtables","19/08/2022"]]) == {"Total Housing" : 650,
                                                                                                                                                                                                                            "Total Medical" : 150,
                                                                                                                                                                                                                            "Total Rent & Loan" : 0,
                                                                                                                                                                                                                            "Total Bill & Insurance" : 0,
                                                                                                                                                                                                                            "Total Clothing" : 100,
                                                                                                                                                                                                                            "Total Etcetra" : 0
                                                                                                                                                                                                                        }
def test_check_category():
    assert check_category("housing") == True
    assert check_category("CLOTHING") == True
    assert check_category("MediCal") == True
    assert check_category("house") == False
    assert check_category("RENT") == False



def test_check_cost():
    assert check_cost("150") == True
    assert check_cost("-50") == False
    assert check_cost("0") == False
    assert check_cost("cat") == False


def test_month_check():
    assert month_check('07') == 'Jul'
    assert month_check('01') == 'Jan'
    assert month_check('11') == 'Nov'
