from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite animal."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
  return f'Every day I wake up and put on my {adjective} {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
  
  if number1.isdigit() and number2.isdigit():
    m = int(number1) * int(number2)
    return f'{number1} times {number2} is {m}'
  else:
    return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):

  repeat = ''

  for i in range(int(n)):
    repeat += word + ' '
  return repeat


if __name__ == '__main__':
    app.run(debug=True)
