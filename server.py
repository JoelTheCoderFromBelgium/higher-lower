from flask import Flask
from random import randint
random_int = randint(0, 100)


app = Flask(__name__)

@app.route("/")
def main_page():
    return '<h1>Guess a number between and 0 and 100</h1>' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzV3cXc4aDEzYWI3Zjg2OHZsY3o4NGN2YnN2eHp2bWFyNDNmbWZtayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yWku98eNsMSZOEEWnC/giphy.gif" alt="Dancing Cat" width=500 height=500>'


@app.route("/<int:num>")
def game(num):
    if num > random_int:
        return '<h1 style="color;red:">Too High, Guess Again!</h1>' \
               '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNvcDVwZmlvaGJsbzEzNzRiMnk0b245bHF3cGhidWZxYXV1YWZkZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XJ26ITqTztKS4G50p6/giphy.gif">'
    elif num < random_int:
        return '<h1 style="color;red:>Too Low, Guess Again!</h1>' \
               '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNvcDVwZmlvaGJsbzEzNzRiMnk0b245bHF3cGhidWZxYXV1YWZkZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XJ26ITqTztKS4G50p6/giphy.gif">'
    else:
        return '<h1 style="color;green:>Yeah !!!</h1>' \
               '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmwydWxkcWljNGZua3Rscm9xYzNlNjNhOHVvdGNnenpvNHl0bTA4aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d6pNlKJlSI1PTR4Uih/giphy.gif">'

if __name__ == "__main__":
    app.run()