def calc_file():
  with open("step_2.txt", 'r') as f:
    calc_string = f.read().splitlines()
    for string in calc_string:
      calc = string.split(' ')
      operator = calc[1]
      intA = int(calc[2])
      intB = int(calc[3])
      if operator == 'x':
        print(intA * intB)
      elif operator == '/':
        print(intA / intB)
      elif operator == '+':
        print(intA + intB)
      elif operator == '-':
        print(intA - intB)

calc_file()
