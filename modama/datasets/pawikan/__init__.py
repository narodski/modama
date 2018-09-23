from .views import *
from .models import *
from modama import db


def load_base_data():
    add = db.session.add
    if db.session.query(PawikanEncounterType).count() == 0:
        add(PawikanEncounterType(name="In Water",
                                 description="Any encounter with a free turtle in the water. This excludes any fishery interactions or nesting behaviour."))
        add(PawikanEncounterType(name="Nesting",
                                 description="Any encounter with a turtle showing nesting behaviour, false nesting, digging, etc is included."))
        add(PawikanEncounterType(name="Fishery Interaction",
                                 description="Turtles encountered because of interaction with fishing activities, like accidental entrapment in fishing gear or caught on purpose."))
    if db.session.query(PawikanSpecies).count() == 0:
        add(PawikanSpecies(genus="Chelonia", species="mydas",
                           common_name="Green Turtle"))
        add(PawikanSpecies(genus="Eretmochelys", species="imbricata",
                           common_name="Hawksbill Turtle"))
        add(PawikanSpecies(genus="Dermochelys", species="coriacea",
                           common_name="Leatherback Turtle"))
        add(PawikanSpecies(genus="Caretta", species="caretta",
                           common_name="Loggerhead Turtle"))
        add(PawikanSpecies(genus="Lepidochelys", species="olivacea",
                           common_name="Olive Ridley Turtle"))


mobile_views = [PawikanEncounterView]
name = "Pawikan"
