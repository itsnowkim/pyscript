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

input_text = Element("todo_input")
todo_list = Element("todo_list")

tasks = []
def add_todo(*args):
  # get input value
  value = input_text.value
  
  # create task
  task_id = f"task-{len(tasks)}"
  task = {
      "id": task_id,
      "content": value,
  }
  
  # append to list - 삭제할 때 여기서 쓰면될듯?
  tasks.append(value)
  
  task_ul = document.createElement("li")
  task_ul.id = task["id"]
  task_ul.innerText = task["content"]
  todo_list.element.appendChild(task_ul)

  input_text.clear()
