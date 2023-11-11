from flask import Flask, render_template, request

app = Flask(__name__)

map_size = 10
map = [['.' for row in range(map_size)] for column in range(map_size)]
player_pos = {"x": map_size // 2, "y": map_size // 2}
map[player_pos.get("x")][player_pos.get("y")] = "@"

@app.route("/")
def index():
    return render_template("index.html", map=map)

@app.route("/move", methods=['POST'])
def move():
    global player_pos
    future_player_pos = player_pos.copy()
    direction = str(request.form.get("direction"))
    match direction:
        case 'up':
            future_player_pos["y"] = future_player_pos.get("y") - 1
        case 'down':
            future_player_pos["y"] = future_player_pos.get("y") + 1
        case 'right':
            future_player_pos["x"] = future_player_pos.get("x") + 1
        case 'left':
            future_player_pos["x"] = future_player_pos.get("x") - 1
    if ((future_player_pos["x"] >= 0 and future_player_pos["x"] < map_size) and (future_player_pos["y"] >= 0 and future_player_pos["y"] < map_size)):
        map[player_pos.get("y")][player_pos.get("x")] = "."
        player_pos = future_player_pos
        map[player_pos.get("y")][player_pos.get("x")] = "@"
    return index()

app.run(port=8080)