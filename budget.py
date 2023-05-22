class Category:
    

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        string = "*************{0}*************\n".format(self.name)

        for transaction in self.ledger:
            transaction['description']
            stramount = str(format(float(transaction['amount']), '.2f'))
            spaces = 30 - (len(transaction['description'])  + len(stramount))
            if (spaces > 0):
                string += transaction['description'] + spaces*" " + stramount
            else:
                string += transaction['description'][:23] + " " + spaces*" " + stramount
            
            string += "\n"
        string += f"Total: {self.get_balance():>1}"
        
        return string

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, withAmount, description=""):
        """
        1. Check whether there the withdraw amount is greater than the amount available in the ledger
            a. Sum the amount together 
        2. If False then add a negative amount into the ledger return True
        3. If True do nothing and return False
        """

        transactionOccured = self.check_funds(withAmount)

        if transactionOccured:
            self.ledger.append({"amount": -withAmount, "description": description})
    
        return transactionOccured

    def get_balance(self):
        currentBalance = 0
        for i in range(0, len(self.ledger)):
            currentBalance += self.ledger[i]["amount"]
        return currentBalance

    def transfer(self, amount, destination):
        """
        1. Check whether there the withdraw amount is greater than the amount available in the ledger
            a. Sum the amount together 
        2. If False then add a negative amount into the ledger return True
        3. If True do nothing and return False
        """
        transactionOccured = self.check_funds(amount)

        
        if transactionOccured:
            destination.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            self.ledger.append({"amount": -amount, "description": "Transfer to " + destination.name})
    
        return transactionOccured
        

    def check_funds(self, amount):
        currentBalance = self.get_balance()

        

        if amount <= currentBalance:
            return True
        else:
            return False






def create_spend_chart(categories):
    total = 0
    item_balance = []
    chart = "Percentage spent by category\n"

    for item in categories:
        total_item = 0
        for transaction in item.ledger:
            if transaction['amount'] < 0:
                total_item += -transaction['amount']
        total += total_item
        item_balance.append(total_item)

    item_balancepercent = [(balance/total * 100) for balance in item_balance]


    for i in range(100, -1, -10):
       
       dots = ""
       for j in item_balancepercent:
            if j >= i:
                dots += "o"
            else:
                dots += " "
            dots += "  "
        
       # print(f"{str(i) : >3}" + "| " + dots)
       
       chart += f"{str(i) : >3}" + "| " + dots + "\n"

    chart += "    " + "-" + 3 * (len(item_balance) * "-") + "\n"
    # print("    " + "-" + 3 * (len(item_balance) * "-"))

    len_items = [len(item.name) for item in categories]
    
    max = len_items[0]
    for i in range(1, len(len_items)):
        if len_items[i] > max:
            max = len_items[i]
    
    for c in range(0, max):
        line = "     "
        i = 0
        for item in categories:
            
            if i < (len(categories) - 1):
                if c < len(item.name):
                    line += item.name[c] + "  "
                else:
                    line += " " + "  "
            else:
                if c < len(item.name):
                    line += item.name[c]
                else:
                    line += " "
            i += 1

        # print(line)
        if c != (max - 1):
            chart +=  line + "  \n"
        else:
            chart += line + "  "
    return chart

