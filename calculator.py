def basic_calc():
  operator = input('Enter operator: ')
  intA = int(input('Enter number: '))
  intB = int(input('Enter number: '))

  if operator == '+':
    print(intA + intB)
  elif operator == '-':
    print(intA - intB)
  elif operator == 'x':
    print(intA * intB)
  elif operator == '/':
    print(intA / intB)
  else:
    print('Try again')
