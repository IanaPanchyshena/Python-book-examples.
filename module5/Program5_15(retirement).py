# 

# The following is used as a global constant
# The contribution rate.
contribution_rate=0.05

def main():
    gross_pay=float(input('Enter thegross pay: '))
    bonus=float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.

def show_pay_contrib(gross):
    contrib=gross*contribution_rate
    print('Contribution for gross pay: $',
           format(contrib, ',.2f'),sep='')


# The show_bonus_contib function accepts the
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib=bonus*contribution_rate
    print('Contribution for bonuses: $',
           format(contrib, ',.2f'),sep='')

# Call the main function.
main()
