def calc_file():
  with open("step_2.txt", 'r') as f:
    calc_string = f.read().splitlines()
    print(calc_string[27])
    for string in calc_string:
      calc = string.split(' ')
      if calc[1] == 'x':
        print(int(calc[2]) * int(calc[3]))
      elif calc[1] == '/':
        print(int(calc[2]) / int(calc[3]))
      elif calc[1] == '+':
        print(int(calc[2]) + int(calc[3]))
      elif calc[1] == '-':
        print(int(calc[2]) - int(calc[3]))

calc_file()
