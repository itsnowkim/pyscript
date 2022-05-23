import random

number_input = Element("number_input")
result = Element("result")

def play_game(*args):
  user_guess = number_input.value
  machine_guess = random.randint(1,50)
  if int(user_guess) == machine_guess:
    result.element.innerText = "You win!"
  else:
    result.element.innerText = f"You lost! The machine chose {machine_guess}!"