from flask import Flask, render_template, request
from solver import solve

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    board = [[0 for _ in range(9)] for _ in range(9)]

    if request.method == "POST":
        action = request.form.get("action")

        if action == "solve":
            for i in range(9):
                for j in range(9):
                    value = request.form.get(f"cell-{i}-{j}")
                    if value and value.isdigit():
                        board[i][j] = int(value)

            solve(board)

        elif action == "reset":
            board = [[0 for _ in range(9)] for _ in range(9)]

    return render_template("index.html", board=board)
if __name__ == "__main__":
    app.run(debug=True)