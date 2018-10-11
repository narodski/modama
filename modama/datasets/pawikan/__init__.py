# from .views import PawikanGeneralView
from .models import (PawikanEncounterType, PawikanSpecies,
                     PawikanLocationType, PawikanOutcome,
                     PawikanStrandingTurtleDisposition, PawikanStrandingCause,
                     PawikanInwaterActivityType, PawikanInwaterType,
                     PawikanInwaterTurtleActivity, PawikanNestType,
                     PawikanNestingActionTaken, PawikanHatchlingLocation,
                     PawikanHatchlingDisposition, PawikanTradeExhibitType,
                     PawikanFacilityEncountered, PawikanTradeTurtleCondition,
                     PawikanTradeTurtleDisposition, PawikanFishingGear,
                     PawikanFishingTurtleDisposition,
                     PawikanFishingTurtleCondition)
from modama import db
import logging


log = logging.getLogger(__name__)


def load_base_data():
    add = db.session.add
    commit = db.session.commit
    for type in ["Nesting", "In-water", "Nest with eggs", "Nest evaluation",
                 "Hatchlings", "Fisheries interaction", "Trade and exhibit"]:
        add(PawikanEncounterType(name=type))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(type))
            log.exception(e)
    for species in [
            ('Chelonia', 'mydas', 'Green Turtle'),
            ("Eretmochelys", "imbricata", "Hawksbill Turtle"),
            ("Dermochelys", "coriacea", "Leatherback Turtle"),
            ("Caretta", "caretta", "Loggerhead Turtle"),
            ("Lepidochelys", "olivacea", "Olive Ridley Turtle"),
            ("Unkown", "unkown", "unkown")]:
        data = dict(zip(['genus', 'species', 'common_name'], species))
        add(PawikanSpecies(**data))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Reporting Location', "Actual Turtle/nest Location"]:
        add(PawikanLocationType(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Released', "Held before release", 'Rehabilitated',
                'Confiscated', 'Disposed']:
        add(PawikanOutcome(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Left in water', 'Left on beach', 'Buried', 'Released',
                'Rehabilitated', 'Euthanized']:
        add(PawikanStrandingTurtleDisposition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Fishery interaction', 'Boat accident',
                'Marine debris entaglment (ghost nets and others)',
                'Marine debris ingestion', 'Others', 'Undetermined']:
        add(PawikanStrandingCause(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Tourist Activity', 'Fisheries interaction', 'Floating']:
        add(PawikanInwaterType(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['On the shore', 'On a boat', 'Free diving', 'SCUBA diving',
                'Others']:
        add(PawikanInwaterActivityType(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ['Swimming', 'Resting', 'Breathing', 'Floating', 'Eating',
                'Mating']:
        add(PawikanInwaterTurtleActivity(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Viable", "Not viable", "Emerged", "Hatchery"]:
        add(PawikanNestType(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["None", "Mark area", "Move to hatchery",
                "Move to another site"]:
        add(PawikanNestingActionTaken(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["In nest", "On the beach", "In the water"]:
        add(PawikanHatchlingLocation(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Left alone", " Assisted to water", "Retained",
                "Held captive"]:
        add(PawikanHatchlingDisposition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Aquarium", "Headstarting", "Market", "Household"]:
        add(PawikanTradeExhibitType(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Restaurant/eatery", "Aquarium display", "Pet shop",
                "Fresh Market", "Household", "Souvenir shop", "Fishing vessel",
                "Resort and Tourism", "School", "Street"]:
        add(PawikanFacilityEncountered(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Whole animal fresh dead", "Whole animal alive",
                "Whole aninal stuffed", "Eggs whole", "Egg shells", "Meat",
                "Scutes", "Processed products", "By-products", "Bones"]:
        add(PawikanTradeTurtleCondition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Confiscated", "Buried", "Unknown disposal",
                "Left at facility"]:
        add(PawikanTradeTurtleDisposition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Active net", "Non-active net", "Non-net"]:
        add(PawikanFishingGear(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Alive alert", "Alive weak", "Dead",
                "Decomposing (use codes)"]:
        add(PawikanFishingTurtleCondition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)
    for loc in ["Released", "Held", "Rehabilitated", "Buried  Others"]:
        add(PawikanFishingTurtleDisposition(name=loc))
        try:
            commit()
        except Exception as e:
            log.warning("Failed adding {} due to error: ".format(species))
            log.exception(e)


# mobile_views = [PawikanGeneralView]
mobile_view = []
name = "Pawikan"
