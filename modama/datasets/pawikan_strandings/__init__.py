from .views import *
from .models import *
from modama import db


def load_base_data():
    add = db.session.add
    if db.session.query(PawikanStrandingSpecies).count() == 0:
        add(PawikanStrandingSpecies(genus="Chelonia", species="mydas",
                                    common_name="Green Turtle"))
        add(PawikanStrandingSpecies(genus="Eretmochelys",
                                    species="imbricata",
                                    common_name="Hawksbill Turtle"))
        add(PawikanStrandingSpecies(genus="Dermochelys",
                                    species="coriacea",
                                    common_name="Leatherback Turtle"))
        add(PawikanStrandingSpecies(genus="Caretta", species="caretta",
                                    common_name="Loggerhead Turtle"))
        add(PawikanStrandingSpecies(genus="Lepidochelys",
                                    species="olivacea",
                                    common_name="Olive Ridley Turtle"))


mobile_views = [PawikanStrandingView]
name = "Pawikan Stranding"
