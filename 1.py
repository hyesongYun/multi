class Account:
    def __init__(self, account_number, name, money=0):
        self.account_number = account_number
        self.name = name
        self.money = money

    def deposit(self, input_money):
        self.money += input_money

    def withdraw(self, output_money):
        if output_money <= self.money:
            self.money -= output_money
        else:
            print("잔액이 부족합니다.")

    def display_info(self):
        print("계좌번호:", self.account_number)
        print("소유주:", self.name)
        print("잔액:", self.money)

    def __str__(self):
        return f"계좌번호: {self.account_number}\n소유주: {self.name}\n잔액: {self.money}"


if __name__ == "__main__":
    accounts = []
    while True:
        print("1.계좌 생성, 2.입금, 3.출금, 4.계좌 정보 보기, 5.종료")

        choice = input("번호를 입력하세요: ")

        if choice == "1":
            account_number = input("계좌번호를 입력하세요: ")
            name = input("소유주를 입력하세요: ")
            account = Account(account_number, name)
            accounts.append(account)
            print("계좌가 생성되었습니다.")

        elif choice == "2":
            account_number = input("입금할 계좌번호를 입력하세요: ")
            try:
              amount = int(input("입금할 금액을 입력하세요: "))
            except ValueError:
              print("적합한 값을 입력하세요.")
              continue
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    print("입금이 완료되었습니다.")
                    break
            else:
                print("일치하는 계좌가 없습니다.")

        elif choice == "3":
            account_number = input("출금할 계좌번호를 입력하세요: ")
            try:
              amount = int(input("출금할 금액을 입력하세요: "))
            except ValueError:
              print("적합한 값을 입력하세요.")
              continue
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("일치하는 계좌가 없습니다.")

        elif choice == "4":
            for account in accounts:
                print(account)

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")