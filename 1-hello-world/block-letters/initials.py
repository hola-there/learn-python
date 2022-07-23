# Ola B
# I like tinkering and coding

# Constants
height_of_letter = 7
width_of_letter = 5

def print_final_row(all_row_letter_arrays):
  array_size = len(all_row_letter_arrays)
  height_of_letter_to_array_index = height_of_letter - 1
  i = 0
  while i <= height_of_letter_to_array_index:
    temp = " "
    for x in all_row_letter_arrays:
      temp += str(x[i]) + " "
    print(temp)
    i += 1

# Convert coordinates of letter to array of rows
def convert_coors_to_row(special_letter_array):
  #print(special_letter_array)
  array_rows_printed = []
  letter_to_use = special_letter_array[0]
  #print(letter_to_use)
  for x in special_letter_array[1]:
    current_row = ""
    i = 1
    while i <= width_of_letter:
      if i in x:
        current_row += letter_to_use
        i += 1
      else:
        current_row += " "
        i += 1
    array_rows_printed.append(current_row)
  return array_rows_printed

def a():
  letter = 'A'
  letter_array = [[3],[2,4],[1,5],[1,2,3,4,5],[1,5],[1,5],[1,5]]
  return [letter, letter_array]
def b():
  letter = 'B'
  letter_array = [[1,2,3,4],[1,5],[1,5],[1,2,3,4],[1,5],[1,5],[1,2,3,4]]
  return [letter, letter_array]
def c():
  letter = 'C'
  letter_array = [[2,3,4],[1,5],[1],[1],[1],[1,5],[2,3,4]]
  return [letter, letter_array]
def d():
  letter = 'D'
  letter_array = [[1,2,3,4],[1,5],[1,5],[1,5],[1,5],[1,5],[1,2,3,4]]
  return [letter, letter_array]
def e():
  letter = 'E'
  letter_array = [[1,2,3,4,5],[1],[1],[1,2,3],[1],[1],[1,2,3,4,5]]
  return [letter, letter_array]
def f():
  letter = 'F'
  letter_array = [[1,2,3,4,5],[1],[1],[1,2,3],[1],[1],[1]]
  return [letter, letter_array]
def g():
  letter = 'G'
  letter_array = [[2,3,4],[1,5],[1],[1,2,3,4,5],[1,5],[1,5],[2,3,4]]
  return [letter, letter_array]
def h():
  letter = 'H'
  letter_array = [[1,5],[1,5],[1,5],[1,2,3,4,5],[1,5],[1,5],[1,5]]
  return [letter, letter_array]
def i():
  letter = 'I'
  letter_array = [[1,2,3,4,5],[1],[1],[1],[1],[1],[1,2,3,4,5]]
  return [letter, letter_array]
def j():
  letter = 'J'
  letter_array = [[1,2,3,4,5],[3],[3],[3],[1,3],[1,3],[2,3]]
  return [letter, letter_array]
def k():
  letter = 'K'
  letter_array = [[1,5],[1,4],[1,3],[1,2],[1,3],[1,4],[1,5]]
  return [letter, letter_array]
def l():
  letter = 'L'
  letter_array = [[1],[1],[1],[1],[1],[1],[1,2,3,4,5]]
  return [letter, letter_array]
def m():
  letter = 'M'
  letter_array = [[1,5],[1,2,4,5],[1,2,4,5],[1,3,5],[1,5],[1,5],[1,5]]
  return [letter, letter_array]
def n():
  letter = 'N'
  letter_array = [[1,5],[1,2,5],[1,3,5],[1,4,5],[1,5],[1,5],[1,5]]
  return [letter, letter_array]
def o():
  letter = 'O'
  letter_array = [[2,3,4],[1,5],[1,5],[1,5],[1,5],[1,5],[2,3,4]]
  return [letter, letter_array]
def p():
  letter = 'P'
  letter_array = [[1,2,3,4],[1,5],[1,5],[1,2,3,4],[1],[1],[1]]  
  return [letter, letter_array]
def q():
  letter = 'Q'
  letter_array = [[2,3,4],[1,5],[1,5],[1,5],[1,5],[1,4],[2,3,5]]
  return [letter, letter_array]
def r():
  letter = 'R'
  letter_array = [[1,2,3,4],[1,5],[1,5],[1,2,3,4],[1,3],[1,4],[2,3,5]]
  return [letter, letter_array]
def s():
  letter = 'S'
  letter_array = [[2,3,4],[1,5],[1],[2,3,4],[5],[1,5],[2,3,4]]
  return [letter, letter_array]
def t():
  letter = 'T'
  letter_array = [[1,2,3,4,5],[3],[3],[3],[3],[3],[3]]
  return [letter, letter_array]
def u():
  letter = 'U'
  letter_array = [[1,5],[1,5],[1,5],[1,5],[1,5],[1,5],[2,3,4]]
  return [letter, letter_array]
def v():
  letter = 'V'
  letter_array = [[1,5],[1,5],[1,5],[1,5],[1,5],[2,4],[3]]
  return [letter, letter_array]  
def w():
  letter = 'W'
  letter_array = [[1,5],[1,5],[1,5],[1,3,5],[1,2,4,5],[1,2,4,5],[1,5]]
  return [letter, letter_array]
def x():
  letter = 'X'
  letter_array = [[1,5],[1,5],[2,4],[3],[2,4],[1,5],[1,5]]
  return [letter, letter_array]
def y():
  letter = 'Y'
  letter_array = [[1,5],[2,4],[3],[3],[3],[3],[3]]
  return [letter, letter_array]
def z():
  letter = 'Z'
  letter_array = [[1,2,3,4,5],[5],[4],[3],[2],[1],[1,2,3,4,5]]
  return [letter, letter_array]
def default():
  return "This is not a letter so....it isn't handled at the moment"

switcher = {
  'a': a,
  'b': b,
  'c': c,
  'd': d,
  'e': e,
  'f': f,
  'g': g,
  'h': h,
  'i': i,
  'j': j,
  'k': k,
  'l': l,
  'm': m,
  'n': n,
  'o': o,
  'p': p,
  'q': q,
  'r': r,
  's': s,
  't': t,
  'u': u,
  'v': v,
  'w': w,
  'x': x,
  'y': y,
  'z': z,
}

def make_a_letter(letter):
  return switcher.get(letter.lower(), default)()

first_letter = make_a_letter('o')
second_letter = make_a_letter('g')
all_letters = [convert_coors_to_row(first_letter), convert_coors_to_row(second_letter)]
#print(all_letters)
print_final_row(all_letters)

