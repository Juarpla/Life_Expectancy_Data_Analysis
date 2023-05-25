"""
Author: Juan Plasencia

Showing Creativity:
-Identify the year and country that has the largest drop from one year to the next.
-Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
"""
#Introduction with general data
period_interested = input("\nEnter the year of interest: ")

#For max values overall
with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    max_years_old = -1.00
    max_country = ""
    max_period = "" 
    
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if years_old > max_years_old:
            max_years_old = years_old
            max_country = country_name
            max_period = period

    print(f"The overall max life expectancy is: {max_years_old:.2f} from {max_country} in {max_period}")

#For min values overall
with open("life-expectancy.csv") as life_file:
    next(life_file)

    min_years_old = 99999999.99
    min_country = ""
    min_period = ""  
 
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if years_old < min_years_old:
            min_years_old = years_old
            min_country = country_name
            min_period = period

    print(f"The overall min life expectancy is: {min_years_old:.2f} from {min_country} in {min_period}")

#For the largest drop from one year to the next
with open("life-expectancy.csv") as life_file:
    next(life_file)

    raw_data = list()

    for line in life_file:
        row = line.strip().split(",")
        raw_data.append(row)

        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

    largest_drop = 0
    largest_drop_country = ""
    largest_drop_year = 0

    for i in range(len(raw_data)-1):
        current_row = raw_data[i]
        next_row = raw_data[i + 1]
        if current_row[0] == next_row[0]:
            difference = float(current_row[3]) - float(next_row[3])
            if difference > largest_drop:
                largest_drop = difference
                largest_drop_country = current_row[0]
                largest_drop_year = current_row[2]

    print(f"The largest drop in life expectancy was {largest_drop:.2f} years in {largest_drop_country} from {largest_drop_year} to {int(largest_drop_year) + 1}.")

#Find information about the interested period
print(f"\nFor the year {period_interested}:")
#For average about the interested period
with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    sum_age = 0.00
    times = 0
    average = 0
        
    for line in life_file:
        row = line.strip().split(",")
        period = row[2]
        years_old = float(row[3])

        if period == period_interested:
            sum_age += years_old
            times += 1
    
    average = sum_age/times
    print(f"The average life expectancy across all countries was {average:.2f}")

#For max life expectancy in period interested
with open("life-expectancy.csv") as life_file:
    next(life_file)

    max_old_interested = -1.00
    max_country = ""
    
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if period == period_interested:
            if years_old > max_old_interested:
                max_old_interested = years_old
                max_country = country_name

    print(f"The max life expectancy was in {max_country} with {max_old_interested:.2f}")

#For max life expectancy in period interested
with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    min_old_interested = 99999999.99
    min_country = ""
    
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if period == period_interested:
            if years_old < min_old_interested:
                min_old_interested = years_old
                min_country = country_name

    print(f"The min life expectancy was in {min_country} with {min_old_interested:.2f}")

#Find information about the interested country
country_interested = input(f"\nEnter a country of interest: ").lower()
#For average about the interested country
with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    sum_age = 0.00
    times = 0
    average = 0
        
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if country_name.lower() == country_interested:
            sum_age += years_old
            times += 1
    
    average = sum_age/times
    print(f"The average life expectancy about {country_interested.capitalize()} across all years is {average:.2f}")

#For max life expectancy in country interested
with open("life-expectancy.csv") as life_file:
    next(life_file)

    max_old_interested = -1.00
    max_country = ""
    
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if country_name.lower() == country_interested:
            if years_old > max_old_interested:
                max_old_interested = years_old
                max_period_interested = period 

    print(f"The max life expectancy in {country_interested.capitalize()} was {max_old_interested:.2f} in {max_period_interested}")

#For max life expectancy in country interested
with open("life-expectancy.csv") as life_file:
    next(life_file)
    
    min_old_interested = 99999999.99
    min_country = ""
    
    for line in life_file:
        row = line.strip().split(",")
        country_name = row[0]
        period = row[2]
        years_old = float(row[3])

        if country_name.lower() == country_interested:
            if years_old < min_old_interested:
                min_old_interested = years_old
                min_period_interested = period 

    print(f"The min life expectancy in {country_interested.capitalize()} was {min_old_interested:.2f} in {min_period_interested}")