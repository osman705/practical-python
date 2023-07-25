# mortgage.py
#
# Exercise 1.9

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108


while principal > 0:
    if extra_payment_start_month < extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
        extra_payment_start_month += 1 
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)