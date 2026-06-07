'''Trevor Lorenz, SS3 05.23.2026

Prompt the user to enter income, and married or not (1.0). Use a single input
statement. Income must be positive, and married must be 1 or 0.  Do validations
similar to the cell above.  The cell above validates only score.  The task
requires validating two inputs (so you may need two while loops inside the
outer loop)
'''


while True:
    try:
        input_list = input('Enter income and married or not (1 or 0) >').split()
        assert len(input_list) == 2
        income_str = input_list[0]
        married_str = input_list[1]

        while True:
            try:
                income = float(income_str)
                assert income > 0
                print(income)
                break

            except ValueError:
                print('Income must be a number')
                income_str = input('Enter income > ')

            except AssertionError:
                print('Income must be positive')
                income_str = input('Enter income >>')

        while True:
            try:
                married = int(married_str)
                assert married == 1 or married == 0
                print(married)
                break

            except ValueError:
                print('Married or not must be an integer')
                married_str = input('Enter Married or not (1 or 0) > ')

            except AssertionError:
                print('Married or not must be 1 or 0')
                married_str = input('Enter married or not (1 or 0) >>')
        break

    except AssertionError:
        print('You must type two inputs')
