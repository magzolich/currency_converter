# based on current and historic data get the information about the trend of the rate and suggest if it is a good moment for
# an exchange of a given currency (or currencies)

from py_exchangeratesapi import Api
import matplotlib.pyplot as plt

api = Api('a666ca76d270bc169a5fb34feb596783')
# get the latest exchange rates
# print(api.get_rates())

# get data, specifc currency and time period
# print(api.get_rates(target_list=['EUR', 'PLN'], start_date="2024-10-20"))

day1 = {'success': True, 'timestamp': 1729468799, 'historical': True,
        'base': 'EUR', 'date': '2024-10-20', 'rates': {'EUR': 1, 'PLN': 4.305369}}
day2 = {'success': True, 'timestamp': 1729468799, 'historical': True,
        'base': 'EUR', 'date': '2024-10-19', 'rates': {'EUR': 1, 'PLN': 4.123456}}
day3 = {'success': True, 'timestamp': 1729468799, 'historical': True,
        'base': 'EUR', 'date': '2024-10-18', 'rates': {'EUR': 1, 'PLN': 4.234123}}
day4 = {'success': True, 'timestamp': 1729468799, 'historical': True,
        'base': 'EUR', 'date': '2024-10-17', 'rates': {'EUR': 1, 'PLN': 4.456123}}
day5 = {'success': True, 'timestamp': 1729468799, 'historical': True,
        'base': 'EUR', 'date': '2024-10-16', 'rates': {'EUR': 1, 'PLN': 4.354123}}

print(day1['rates']['PLN'])  # jak odwolac sie do wartosci currency exchange
print(day1['date'])  # odwolanie do daty

# lista z 5 historycznymi currency exchanges rates
hist_data = [day1['rates']['PLN'], day2['rates']['PLN'],
             day3['rates']['PLN'], day4['rates']['PLN'], day5['rates']['PLN']]
print(hist_data)

# lista z datami
dates_list = [day1['date'], day2['date'],
              day3['date'], day4['date'], day5['date']]
print(dates_list)

# chart
plt.plot(dates_list, hist_data)
plt.show()
