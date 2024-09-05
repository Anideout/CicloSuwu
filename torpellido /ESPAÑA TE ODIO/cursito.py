# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")

#ejercicio 4.3.8
# # 1 milla = 1609.344 metros.
# # 1 galón = 3.785411784 litros.

# def liters_100km_to_miles_gallon(liters):
#     gallons = liters / 3.785411784
#     miles = 100 * 1000 / 1609.344
#     return miles / gallons

# def miles_gallon_to_liters_100km(miles):
#     km100 = miles * 1609.344 / 1000 / 100
#     liters = 3.785411784
#     return liters / km100

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))

#ejercicio 
# def multiply(a, b):
#     return a * b

# print(multiply(3, 4))    # salida: 12


# def multiply(a, b):
#     return a ** b

# print(multiply(3, 4))    # salida: None



def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
 
print(even_num_lst(11))
 





