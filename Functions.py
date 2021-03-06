# year = int(input('Enter the year: '))
# temp_year = year
# AD_or_BC = input('Enter AD or BC: ')
# month = input('Enter the month: ')
# day = int(input('Enter the day: '))
month_to_day_dict = {'January': 0, 'February': 31, 'March': 59, 'April': 90, 'May': 120, 'June': 151, 'July': 181, 'August': 213, 'September': 243, 'October': 273, 'November': 303, 'December': 334}
leap_month_to_day_dict = {'January': 0, 'February': 31, 'March': 60, 'April': 91, 'May': 121, 'June': 152, 'July': 182, 'August': 214, 'September': 244, 'October': 274, 'November': 304, 'December': 335}
reversed_month_to_day_dict = {'January': 334, 'February': 303, 'March': 273, 'April': 243, 'May': 213, 'June': 181, 'July': 151, 'August': 120, 'September': 90, 'October': 59, 'November': 31, 'December': 0}
reversed_leap_month_to_day_dict = {'January': 335, 'February': 304, 'March': 274, 'April': 244, 'May': 214, 'June': 182, 'July': 152, 'August': 121, 'September': 91, 'October': 60, 'November': 31, 'December': 0}
day_in_month_dict = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
leap_day_in_month_dict = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
months_before_august = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
months_after_august = ['September', 'October', 'November', 'December']
date = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
BC_or_AD = ('AD', 'BC')

def check_date(day, month, year):
    if month == 'February':
        if day == 29:
            if is_leap_year(year) == True:
                return True
            else:
                return False
        elif day > 29:
            return False
    if day == 31:
        if day_in_month_dict[month] == 31:
            return True
        else:
            return False

def is_leap_year(year): #Mason
    if (year % 400 == 0) and (year % 100 == 0):
        leapyear = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leapyear = True
    else:
        leapyear = False
    return leapyear

def ADBC(time):
    if time == 'BC':
        return True
    elif time == 'AD':
        return False



def final_output(year, month, day, AD_or_BC): #Mason
    if check_date(day, month, year) == False:
        return f'{month}/{day}/{year} {AD_or_BC} does not exist'
    number = days(year, day, AD_or_BC, month)
    baktun = number // 144000
    number %= 144000
    katun = number // 7200
    number %= 7200
    tun = number // 360
    number %= 360
    winal = number // 20
    number %= 20
    kin = number
    if AD_or_BC == 'BC':
        if year == 3114:
            if month == 'August':
                if day < 11:
                    return f'{-abs(baktun)}.{-abs(katun)}.{-abs(tun)}.{-abs(winal)}.{-abs(kin)}'
                else:
                    return f'{baktun}.{katun}.{tun}.{winal}.{kin}'
            elif month in months_before_august:
                return f'{-abs(baktun)}.{-abs(katun)}.{-abs(tun)}.{-abs(winal)}.{-abs(kin)}'
            else:
                return f'{baktun}.{katun}.{tun}.{winal}.{kin}'
        elif year > 3114:
            return f'{-abs(baktun)}.{-abs(katun)}.{-abs(tun)}.{-abs(winal)}.{-abs(kin)}'
        else:
            return f'{baktun}.{katun}.{tun}.{winal}.{kin}'
    else:
        return f'{baktun}.{katun}.{tun}.{winal}.{kin}'

def days(year, day, AD_or_BC, month):
    if ADBC(AD_or_BC) == True:
        days = days_from_years(year, month, day, AD_or_BC)
        return days
    else:
        days = days_from_years(year, month, day, AD_or_BC) + remaining_days(year, day, month)
        return days

def days_from_years(year, month, day, AD_or_BC): #Keegan
    if ADBC(AD_or_BC) == True:
        if year == 3114:
            if month == 'August':
                days = abs(day - 11)
                return days
            elif month in months_before_august:
                days = reversed_month_to_day_dict[month] - 11
                return days
            elif month in months_after_august:
                days = month_to_day_dict[month] + 20
                return days

        elif year > 3114:
            if is_leap_year(year) == True:
                year = abs((3114 - year) + 1)
                days = (((reversed_leap_month_to_day_dict[month]) + ((year * 365) + (year // 4) - ((year // 100) - (year // 400)))) + 224) + abs(leap_day_in_month_dict[month] - day)
                return days
            else:
                year = abs((3114 - year) + 1)
                days = (((reversed_month_to_day_dict[month]) + ((year * 365) + (year // 4) - ((year // 100) - (year // 400)))) + 225) + abs(day_in_month_dict[month] - day)
                return days
        else:
            year = 3114 - year
            days = ((year * 365) + (year // 4) - ((year // 100) - (year // 400))) + 142
            return days

    else:
        year += 3114
        year_minus_2 = year - 2
        days = ((year_minus_2 * 365) + (year_minus_2 // 4) - ((year_minus_2 // 100) - (year_minus_2 // 400))) + 142
        return days

def remaining_days(year, day, month):

    if is_leap_year(year) == True:
        days = leap_month_to_day_dict[month] + day
    else:
        days = month_to_day_dict[month] + day
    return days

