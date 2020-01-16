class Person:

    def __init__(self, person_id, first_name, last_name, email, eating, allergies):

        self.person_id = person_id

        self.first_name = first_name

        self.last_name = last_name

        self.email = email

        self.eating = eating

        self.allergies = allergies

        

class Team:

    def __init__(self, team_id, adress, appetizer_id, main_course_id, dessert_id, latitude, longitude):

        self.team_id = team_id

        self.adress = adress

        self.appetizer_id = appetizer_id

        self.main_course_id = main_course_id

        self.dessert_id = dessert_id

        self.latitude = latitude

        self.longitude = longitude 

        self.eating = "normal"

        self.course = ""

        self.members = []

        self.guests = []

        

    def add_member(self, member):

        self.members.append(member)

    

    def add_guests(self, guests):

        self.guests.append(guests)



teams = []



def team_id_exists(id):

    team_exists = False

    for team in teams:

        if(team.team_id == id):

            team_exists = True

    return team_exists

    

def get_team_by_id(id):

    for team in teams:

        if(int(team.team_id) == int(id)):

            t = team

            break

        else:

            t = None

    return t

for team in teams:

    img_file = ""

    if(int(team.team_id) == int(team.appetizer_id)):

        img_file = "vorspeise.png"

        team.course = "Vorspeise"

    elif(int(team.team_id) == int(team.main_course_id)):

        img_file = "hauptgang.png"

        team.course = "Hauptgang"

    elif(int(team.team_id) == int(team.dessert_id)):

        img_file = "nachspeise.png"

        team.course = "Nachspeise"

    else:

        img_file = "keingang.png"

        

    if(team.eating == "normal"):

        img_path = "omni"

    elif(team.eating == "Vegetarisch"):

        img_path = "vegie"

    else:

        img_path = "vegan"

        

    team_name = ""

    for member in team.members:

        if(team_name == ""):

            team_name = member.last_name + " & "

        else:

            team_name = team_name + member.last_name

        print(team_name)

    

    ap_team = get_team_by_id(int(team.appetizer_id))

    if(ap_team!=None):

        vorspeise = str(team.appetizer_id)

        if(ap_team.guests!=None):

            for guest in ap_team.guests:

                vorspeise = vorspeise + ", (" + str(guest) + ")" 

    

    mc_team = get_team_by_id(int(team.main_course_id))

    if(mc_team!=None):

        hauptgang = str(team.main_course_id)

        if(ap_team.guests!=None):

            for guest in mc_team.guests:

                hauptgang = hauptgang + ", (" + str(guest) + ")" 

        

    d_team = get_team_by_id(int(team.dessert_id))

    if(d_team!=None):

        dessert = str(team.dessert_id)

        if(ap_team.guests!=None):

            for guest in d_team.guests:

                dessert = dessert + ", (" + str(guest) + ")" 

        

    if(team.course == "Vorspeise" and team.guests!=None):

        for guest in team.guests:

            team.appetizer_id = team.appetizer_id + "," + str(guest)

    if(team.course == "Hauptgang" and team.guests!=None):

        for guest in team.guests:

            team.main_course_id = team.main_course_id + "," + str(guest)

    if(team.course == "Nachspeise" and team.guests!=None):

        for guest in team.guests:

            team.dessert_id = team.dessert_id + "," + str(guest)


templatefile = open('anmeldung.html','r')

htmltext = templatefile.read()




htmlfile = open("dinner.html",'w') 

htmlfile.write(htmltext)

htmlfile.close()