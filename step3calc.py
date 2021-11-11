def calc_file():
  with open("step_3.txt", 'r') as f:
    calc_string = f.read().splitlines()
    for string in calc_string:
      calc = string.split(' ')

      if calc[1] != 'calc':

        print(calc_string[int(calc[1]) - 1])
        print('line number: ' + str(int(calc[1])))

      elif calc[2] == 'x':

        multiply = int(calc[3]) * int(calc[4])
        print(calc_string[multiply - 1])
        print('line number: ' + str(multiply))

      elif calc[2] == '-':

        subtract = int(calc[3]) - int(calc[4])
        print(calc_string[subtract - 1])
        print('line number: ' + str(subtract))

      elif calc[2] == '/':

        division = round(int(calc[3]) / int(calc[4]))
        print(calc_string[division - 1])
        print('line number: ' + str(division))

      elif calc[2] == '+':

        addition = int(calc[3]) + int(calc[4])
        print(calc_string[addition - 1])
        print('line number: ' + str(addition))

calc_file()