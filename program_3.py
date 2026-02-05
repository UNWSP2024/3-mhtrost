# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	                            Price Per Pound
# 2 pounds or less   	                    $1.50
# Over 2 pounds but not more than 6 pounds  $3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	                        $4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):

    weight = float(input('Enter the weight of the package: '))

    if weight <= 2:
        price = weight * 1.50
        print(f'Your shipping cost is:, {price:.2f}')
    if weight >= 3 and weight <= 6:
        price = weight * 3.00
        print(f'Your shipping cost is:, {price:.2f}')
    if weight >= 6.1 and weight <= 10:
        price = weight * 4.00
        print(f'Your shipping cost is:, {price:.2f}')
    if weight >= 10.1:
        price = weight * 4.75
        print(f'Your shipping cost is:, {price:.2f}')
