'''
This program allows the user to enter a company's Ticker name, and displays the company info and stock info, as well as a table of prices
'''

import yfinance as yf, format_num

name = input("Get stocks for (e.g. MSFT or AAPL): ")

print("Connecting to API...")
data = yf.Ticker(name)

if data.info['regularMarketPrice'] is not None:

  print('\n\nGeneral info\n')

  try:
    print('ZIP:', data.info['zip'])
  except:
    pass

  try:
    print('Sector:', data.info['sector'])
  except:
    pass

  try:
    print('Employees:', data.info['fullTimeEmployees'])
  except:
    pass

  try:
    print('Based in:', ', '.join([data.info['city'], data.info['country']]))
  except:
    pass

  try:
    print('Website:', data.info['website'])
  except:
    pass

  try:
    print('Gross profits: $', format_num.format_num(data.info['grossProfits']), ' ', format_num.estimate(data.info["grossProfits"]), sep='')
  except:
    pass


  print('\n\nStocks\n')

  try:
    print('Current price: $', data.info['currentPrice'], sep='')
  except:
    pass

  try:
    print('Quarterly growth (%):', round(data.info['earningsQuarterlyGrowth'], 3))
  except:
    pass

  try:
    print('200-day average: $', data.info['twoHundredDayAverage'], sep='')
  except:
    pass

  try:
    print('Five-year average yield (%):', round(data.info['fiveYearAvgDividendYield'], 2))
  except:
    pass

  try:
    print('Twelve-month high: $', data.info['fiftyTwoWeekHigh'], sep='')
  except:
    pass

  try:
    print('Twelve-month low: $', data.info['fiftyTwoWeekLow'], sep='')
  except:
    pass


  print('\n\nHistory\n')
  history = input('Time (d, wk, mo, y, max): ')
  print('')
  print(data.history(period=history))

else:

  print('Not found.')