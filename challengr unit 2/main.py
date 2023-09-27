class bankaccount:
def__init(self,account_number,account_holder_name,initial_balance
          self.__account_number = account_number
self.__account_holder_name = account_holder_name
self.__account_balance = initial_balance
def_deposit(self_amount):
if amount > 0
self.__account_balance += amount
print(f"withdrew ${amount}.Newbalance:${self.__account_balance}")
elif amount<0 valid
print("invalid withdrawl amount.Amount must be greater than zero.")
else:
print{"infsufficient funds for withdrawl."}