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
set_website_style("none")
set_website_style("98")
"""
Welcome to the worst car garage in the world. Ya got 6 paint colors to choose from, four models,
and they all look like crap. As an act of good faith, there are limited modifications that
make your shitboxes look moderately better, but
honestly its all hot garbage.
"""
@dataclass
class Car:
    body: list[str]
    color: str
    name: str
    model: str
@dataclass
class State:
    garage: list[Car]
    latest_car: Car
    drawn_car: Picture
    car_color: str
    bmess_index: int
    smess_index: int
    vmess_index: int
    tmess_index: int

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
    ],
"decal_van": [
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWBB",
"BBBBBBBBBBUUBBBBBHBBBBBBBBWWWWWWWWWBB",
"BBBBBBBBBBMUUBBBHBBBBBBBBBWWWWWWWWWWBB",
"BBBBBBBBBMMUUUUUBBBBBBBBBBWWWWWWWWWWWBBB",
"BBBBBBBBMMMUUTUUUUUUBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBMMMMMUUUUUUUUUBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBMMMMMUUUUUBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBTTTTTBBBBBBBBBBBBBBBBBBBBBBBTTTTTBBBBBBB",
"    TTTTTTT                     TTTTTTT",
"    TTTTTTT                     TTTTTTT",
"     TTTTT                       TTTTT"
],
"bus": [
"   BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"   BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWBBBBBBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWWBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWWWBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWWWWBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWWWWWBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTBBBBBBB",
"    TTTTTTT                                                                       TTTTTTT",
"    TTTTTTT                                                                       TTTTTTT",
"     TTTTT                                                                         TTTTT"
],
"fullbus": [
"   BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"   BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
" BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBWWWWWWWWWBBBBBWWWWWWWWWWWWBBBBBBBB",
"BBBBBBBBWWWYYYWWWBBWWWTTTWWWBBWWWDDDWWWBBWWWDDDWWWBBWWWTTTWWWBBBBBWWWWWWWWWWWWWBBB",
"BBBBBBBBWWWPPPWWWBBWWWDDDWWWBBWWWPPPWWWBBWWWVVVWWWBBWWWEEEWWWBBBBBWWWWWWWWWWWWWWBBB",
"BBBBBBBBWWWPPPWWWBBWWWDDDWWWBBWWWPPPWWWBBWWWVVVWWWBBWWWEEEWWWBBBBBWWWWWWWWWWWWWWWBBB",
"BBBBBBBBWWSSSSSWWBBWWFFFFFWWBBWWLLLLLWWBBWWSSSSSWWBBWWFFFFFWWBBBBBWWWWWWWWWWWWWWWWBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBHHHHH",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
"BBBBBTTTTTBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBTTTTTBBBBBBB",
"    TTTTTTT                                                                       TTTTTTT",
"    TTTTTTT                                                                       TTTTTTT",
"     TTTTT                                                                         TTTTT"
]
}


@route
def index(state: State)->Page:
    content = [
        Header("Shitty Pixel Car Garage"),
        "Choose a shit-box\n",
        Button("Vroom Car", "make_sports"),
        Button("Truk","make_truck"),
        Button("Mom van","make_van"),
        Button("SkooBus","make_bus"),
        Header("Your Garage:")
        ]
    if not state.garage:
        content.append(Div("wow such empty"))
    for i, car in enumerate(state.garage):
        content.append(change_margin(Div(
            color_car(car, car.color)),"20px"))
        content.append(car.name)
    return Page(
        state, content)
@route                
def make_sports(state: State):
    state.latest_car = Car(CARS["sports"].copy(),"","nameless shit-box","sports")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Yellow","Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route                
def make_truck(state: State):
    state.latest_car = Car(CARS["truck"].copy(),"","nameless shit-box","truck")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Yellow","Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route                
def make_van(state: State):
    state.latest_car = Car(CARS["van"].copy(),"","nameless shit-box","van")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Yellow","Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
@route
def make_bus(state: State):
    state.latest_car = Car(CARS["bus"].copy(),"","detention center transport","bus")
    return Page(
        state, [
        "Choose a body paint color",
        RadioButtonGroup("car_color", ["Yellow","Green","Blue","Red","Pink","Black","Orange"]),
        Button("Apply","choose_color")
        ])
bus_messages = ["but can your stang haul THIS MUCH ass?\n","Martha why did we have so many kids\n","please let this be a normal field trip\n","that'll be two dollars\n","where does it go? nobody knows\n"]
sports_messages = ["NeEEeEEoOWWWWW\n","kachow\n","she's hp maxxing","i am speed (Pixar please don't sue me)\n","the only way to improve this is some dumb-ass underglow\n"]
truck_messages = ["now that's a TRUK\n","country roooooaaads\n","ford eff wun fitty\n","murica\n"]
van_messages = ["wow so hip\n","ready for soccer practice\n","bringing the orange slices and kaprisuns\n","hey kid you want some candy?\n","put the pedal to the metal, ma!\n"]
@route
def choose_color(state: State, car_color:str):
    state.car_color = car_color
    state.latest_car.color = car_color
    state.drawn_car = color_car(state.latest_car,car_color)
    if state.latest_car.body == CARS["sports"]:
        if state.smess_index <= 4:
            display_mess = sports_messages[state.smess_index]
            state.smess_index += 1
        else:
            state.smess_index = 0
            display_mess = sports_messages[state.smess_index]
        return Page(
            state, [
            display_mess,
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Div(Button("Add a spoiler","add_spoiler"))
            ])
    elif state.latest_car.body == CARS["truck"]:
        if state.tmess_index < 4:
            display_mess = truck_messages[state.tmess_index]
            state.tmess_index += 1
        else:
            state.tmess_index = 0
            display_mess = truck_messages[state.tmess_index]
        return Page(
            state, [
            display_mess,
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Button("IT NEEDS BIGGER WHEELS","get_big_wheels")
            ])
    elif state.latest_car.body == CARS["bus"]:
        if state.bmess_index <= 4:
            display_mess = bus_messages[state.bmess_index]
            state.bmess_index += 1
        else:
            state.bmess_index = 0
            display_mess = bus_messages[state.bmess_index]
        return Page(
            state, [
            display_mess,
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Button("Pick up some kiddos","add_kids")
            ])
    else:
        if state.vmess_index <= 4:
            display_mess = van_messages[state.vmess_index]
            state.vmess_index += 1
        else:
            state.vmess_index = 0
            display_mess = van_messages[state.vmess_index]
        return Page(
            state, [
            display_mess,
            state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car")),
            Button("Make it radical","van_decal")
            ])
def color_car(car:Car,car_color:str):
    if car.model == "sports":
        car_canvas = Picture.new(600,120)
        scale = 10
        car_width = max(len(row) for row in car.body)
        xoffset = (600 - car_width*scale) // 2
        yoffset = (120 - len(car.body)*scale) // 2
    elif car.model == "truck":
        car_canvas = Picture.new(480,150)
        scale = 8
        car_width = max(len(row) for row in car.body)
        xoffset = (480 - car_width*scale) // 2
        yoffset = (150 - len(car.body)*scale) // 2
    elif car.model == "van":
        car_canvas = Picture.new(700,200)
        scale = 10
        car_width = max(len(row) for row in car.body)
        xoffset = (700 - car_width*scale) // 2
        yoffset = (200 - len(car.body)*scale) // 2
    elif car.model == "bus":
        car_canvas = Picture.new(700,200)
        scale = 7
        car_width = max(len(row) for row in car.body)
        xoffset = (700 - car_width*scale) // 2
        yoffset = (200 - len(car.body)*scale) // 2
    for y, row in enumerate(car.body):
        for x, pixel in enumerate(row):
           for dy in range(scale):
               for dx in range(scale):
                   if pixel == "B":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,car_color)
                   elif pixel == "W":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"lightcyan")
                   elif pixel == "T":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"black")
                   elif pixel == "H":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"goldenrod")
                   elif pixel == "U":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"white")
                   elif pixel == "M":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"deeppink")
                   elif pixel == "Y":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"darkkhaki")
                   elif pixel == "D":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"sienna")
                   elif pixel == "S":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"royalblue")
                   elif pixel == "P":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"bisque")
                   elif pixel == "F":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"orangered")
                   elif pixel == "L":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"mediumpurple")
                   elif pixel == "V":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"peru")
                   elif pixel == "E":
                       car_canvas.set_pixel((x*scale+xoffset)+dx,y*scale+yoffset+dy,"papayawhip")
                   else:
                       pass
    return car_canvas
@route
def van_decal(state:State):
    state.latest_car.body = CARS["decal_van"].copy()
    state.drawn_car = color_car(state.latest_car, state.latest_car.color)
    return Page(state,[
        "radical\n",
        state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car"))
        ])
@route
def add_kids(state:State):
    state.latest_car.body = CARS["fullbus"].copy()
    state.drawn_car = color_car(state.latest_car, state.latest_car.color)
    return Page(state,[
        "captives acquired",
        state.drawn_car,
            Div(Button("Save to garage","add_to_garage")),
            Div("You have created: "+state.latest_car.name+"\n",
            "Give it a name",
            TextBox("car_name"),
            Button("Change name","name_car"))
        ])
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
     
start_server(State([],None,None,"",0,0,0,0))

