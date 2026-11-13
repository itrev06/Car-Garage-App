from drafter import *
from drafter import Picture
from dataclasses import dataclass
set_website_title("Shitty Pixel Car Garage")
set_site_information(
    author="Isabella Trevino",
    description="Make really bad pixel art of car.",
    sources="Thanks to the Drafter docs and my study group.",
    planning="",
    links=[]
)
hide_debug_information()
set_website_framed(False)
set_website_style("retro")
@dataclass
class State:
    garage: list[Car]
    latest_car: Car
    drawn_car: Picture
    car_color: str
@dataclass
class Car:
    body: list[str]
    color: str
    name: str
MATERIALS = {
    "B": "body",
    "T": "tire",
    "W": "window"
    }
COLORS = {
    "Blue": "b",
    "Red": "r",
    "Green": "g",
    "Orange": "o",
    "Pink": "p",
    "Black": "x"
    }

CARS = {
"sports": [
"        BBBBBBBBBBBBBBBBB          ",
"      BBBBBBBBBBBWWWWWWWWW         ",
"    BBBBBBBBBBBBBBWWWWWWWWWWW",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBTTTTTBBBBBBBBBBBBBBTTTTTBBBBBBB",
"  BBBTTTTTTTBBBBBBBBBBBBTTTTTTTBBB",
"     TTTTTTT            TTTTTTT",
"      TTTTT              TTTTT"
    ],
"truck": [
"                     BBBBBBBBBBBBBB",
"                    BBBBBBBBBWWWWWBW",
"                    BBBBBBBBBWWWWWWBW",
"                    BBBBBBBBBWWWWWWWBW",
"                    BBBBBBBBBWWWWWWWWBW",
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTBBBBBBBB",
"BBBBBBTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTTTBBBBBBB",
"      TTTTTTTT                         TTTTTTTT",
"      TTTTTTTT                         TTTTTTTT",
"       TTTTTT                           TTTTTT"    ],
"van": [
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWWBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBTTTTTBBBBBBBBBBBBBBBBBBBBBBBTTTTTBBBBBBB",
"    TTTTTTT                     TTTTTTT",
"    TTTTTTT                     TTTTTTT",
"     TTTTT                       TTTTT"
    ]
}

pix_ht = 10
pix_wd = 10

@route
def index(state: State)->Page:
    content = [
        Header("Shitty Pixel Car Garage"),
        "Choose a shit-box\n",
        Button("Vroom Car", "make_sports"),
        Button("Truk","make_truck"),
        Button("Mom van","make_van")
        ]
    for i, car in enumerate(state.garage):
        content.append(Div(
            color_car(car, car.color)))
        content.append(car.name)
    return Page(
        state, content)
@route                
def make_sports(state: State):
    state.latest_car = Car(CARS["sports"],"","nameless shit-box")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route                
def make_truck(state: State):
    state.latest_car = Car(CARS["truck"],"","nameless shit-box")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route                
def make_van(state: State):
    state.latest_car = Car(CARS["van"],"","nameless shit-box")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route
def choose_color(state: State, car_color:str):
    state.car_color = car_color
    state.latest_car.color = car_color
    state.drawn_car = color_car(state.latest_car,car_color)
    if state.latest_car.body == CARS["sports"]:
        return Page(
            state, [
            "NeEEeEEoOWWWWW\n",
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Div(Button("Add a spoiler","add_spoiler"))
            ])
    elif state.latest_car.body == CARS["truck"]:
        return Page(
            state, [
            "now that's a TRUK\n",
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Button("IT NEEDS BIGGER WHEELS","get_big_wheels")
            ])
    else:
        return Page(
            state, [
            "wow so hip\n",
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car"))
            ])
def color_car(car:Car,car_color:str):
    if car.body == CARS["sports"]:
        car_canvas = Picture.new(800,120)
        scale = 10
    elif car.body == CARS["truck"]:
        car_canvas = Picture.new(480,150)
        scale = 8
    elif car.body == CARS["van"]:
        car_canvas = Picture.new(800,200)
        scale = 10
    for y, row in enumerate(car.body):
        for x, pixel in enumerate(row):
           for dy in range(scale):
               for dx in range(scale):
                   if pixel == "B":
                       car_canvas.set_pixel(x*scale+dx,y*scale+dy,car_color)
                   elif pixel == "W":
                       car_canvas.set_pixel(x*scale+dx,y*scale+dy,"gray")
                   elif pixel == "T":
                       car_canvas.set_pixel(x*scale+dx,y*scale+dy,"black")
                   elif pixel == "H":
                       car_canvas.set_pixel(x*scale+dx,y*scale+dy,"goldenrod")
                   else:
                       pass
    return car_canvas
@route
def add_to_garage(state: State):
    state.garage.append(state.latest_car)
    return index(state)
@route
def name_car(state: State, car_name:str):
    state.latest_car.name = car_name
    return Page(
            state, [
            "Successfully renamed!\n",
            state.drawn_car,
            Button("Save to garage","add_to_garage"),
            Div("Current name: "+state.latest_car.name+"\n",
            TextBox("car_name",state.latest_car.name),
            Button("Change name","name_car"))
            ])
@route
def add_spoiler(state:State):
    if state.latest_car.body == CARS["sports"]:
        for y, row in enumerate(state.latest_car.body):
            spaces = "             "
            if y == 1:
                state.latest_car.body[y]="      BBBBB  "+state.latest_car.body[y]
            elif y == 2:
                state.latest_car.body[y] = "         BBB "+state.latest_car.body[y]
            elif y == 3:
                state.latest_car.body[y] = "          BBB"+state.latest_car.body[y]
            else:
                state.latest_car.body[y] = spaces+state.latest_car.body[y]
    state.drawn_car = color_car(state.latest_car,state.latest_car.color)
    return Page(
            state, [
            "NeEEeEEoOWWWWW\n",
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car"))
            ])
@route
def get_big_wheels(state:State):
    state.latest_car.body.append("BBBBBBTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTTTBBBBBBB")
    state.latest_car.body.append("BBBBBBTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTTTBBBBBBB")
    for y, row in enumerate(state.latest_car.body):
        if y==8:
            state.latest_car.body[y] = "BBBBBBBTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTBBBBBBBB"
        elif y==9:
            state.latest_car.body[y] = "BBBBBBTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTTTTBBBBBBB"
    swap_ind = -2
    for y, row in enumerate(state.latest_car.body):
        if y>10 and y<13:
            state.latest_car.body[swap_ind],state.latest_car.body[y] = state.latest_car.body[y],state.latest_car.body[swap_ind]
            swap_ind = swap_ind+1
            print(y,row)
        elif y>=13 and y<15:
            state.latest_car.body[y],state.latest_car.body[y+1]=state.latest_car.body[y+1],state.latest_car.body[y]
            print(y,row)
    state.drawn_car = color_car(state.latest_car,state.latest_car.color)
    return Page(
            state, [
            "yeeeAAAHHhhhHH\n",
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car"))
            ])
     
start_server(State([],None,None,""))

