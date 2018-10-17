from .views import PawikanGeneralView
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
                     PawikanNestEvaluationType,
                     PawikanFishingTurtleCondition)
from modama import db
import logging


log = logging.getLogger(__name__)


def load_base_data():
    add = db.session.add
    query = db.session.query
    commit = db.session.commit
    rollback = db.session.rollback
    if query(PawikanFacilityEncountered).count() == 0:
        for v in ["Restaurant/eatery", "Aquarium display", "Pet shop",
                  "Fresh Market", "Household", "Souvenir shop",
                  "Fishing vessel", "Resort and Tourism", "School", "Street"]:
            add(PawikanEncounterType(name=v))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(type))
                log.exception(e)

    if query(PawikanEncounterType).count() == 0:
        for type in ["Nesting", "In-water", "Nest with eggs", "Nest evaluation",
                     "Hatchlings", "Stranding", "Fisheries interaction",
                     "Trade or exhibit"]:
            add(PawikanEncounterType(name=type))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(type))
                log.exception(e)
    if query(PawikanSpecies).count() == 0:
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
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanLocationType).count() == 0:
        for loc in ['Reporting Location', "Actual Turtle/nest Location"]:
            add(PawikanLocationType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanOutcome).count() == 0:
        for loc in ['Released', "Held before release", 'Rehabilitated',
                    'Confiscated', 'Disposed']:
            add(PawikanOutcome(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanStrandingTurtleDisposition).count() == 0:
        for loc in ['Left in water', 'Left on beach', 'Buried', 'Released',
                    'Rehabilitated', 'Euthanized']:
            add(PawikanStrandingTurtleDisposition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanStrandingCause).count() == 0:
        for loc in ['Fishery interaction', 'Boat accident',
                    'Marine debris entaglment (ghost nets and others)',
                    'Marine debris ingestion', 'Others', 'Undetermined']:
            add(PawikanStrandingCause(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanInwaterType).count() == 0:
        for loc in ['Tourist Activity', 'Fisheries interaction', 'Floating']:
            add(PawikanInwaterType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanInwaterActivityType).count() == 0:
        for loc in ['On the shore', 'On a boat', 'Free diving', 'SCUBA diving',
                    'Others']:
            add(PawikanInwaterActivityType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanNestEvaluationType).count() == 0:
        for loc in ['Natural', 'Hatchery']:
            add(PawikanNestEvaluationType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanInwaterTurtleActivity).count() == 0:
        for loc in ['Swimming', 'Resting', 'Breathing', 'Floating', 'Eating',
                    'Mating']:
            add(PawikanInwaterTurtleActivity(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanNestType).count() == 0:
        for loc in ["Natural Viable", "Natural Not viable", "Natural Emerged",
                    "Hatchery"]:
            add(PawikanNestType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanNestingActionTaken).count() == 0:
        for loc in ["None", "Mark area", "Move to hatchery",
                    "Move to another site"]:
            add(PawikanNestingActionTaken(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanHatchlingLocation).count() == 0:
        for loc in ["In nest", "On the beach", "In the water"]:
            add(PawikanHatchlingLocation(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanHatchlingDisposition).count() == 0:
        for loc in ["Left alone", " Assisted to water", "Retained",
                    "Held captive"]:
            add(PawikanHatchlingDisposition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanTradeExhibitType).count() == 0:
        for loc in ["Aquarium", "Headstarting", "Market", "Household"]:
            add(PawikanTradeExhibitType(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanTradeExhibitType).count() == 0:
        for loc in ["Restaurant/eatery", "Aquarium display", "Pet shop",
                    "Fresh Market", "Household", "Souvenir shop", "Fishing vessel",
                    "Resort and Tourism", "School", "Street"]:
            add(PawikanFacilityEncountered(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanTradeTurtleCondition).count() == 0:
        for loc in ["Whole animal fresh dead", "Whole animal alive",
                    "Whole aninal stuffed", "Eggs whole", "Egg shells", "Meat",
                    "Scutes", "Processed products", "By-products", "Bones"]:
            add(PawikanTradeTurtleCondition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanTradeTurtleDisposition).count() == 0:
        for loc in ["Confiscated", "Buried", "Unknown disposal",
                    "Left at facility"]:
            add(PawikanTradeTurtleDisposition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanFishingGear).count() == 0:
        for loc in ["Active net", "Non-active net", "Non-net"]:
            add(PawikanFishingGear(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanFishingTurtleCondition).count() == 0:
        for loc in ["Alive alert", "Alive weak", "Dead",
                    "Decomposing (use codes)"]:
            add(PawikanFishingTurtleCondition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)
    if query(PawikanFishingTurtleDisposition).count() == 0:
        for loc in ["Released", "Held", "Rehabilitated", "Buried  Others"]:
            add(PawikanFishingTurtleDisposition(name=loc))
            try:
                commit()
            except Exception as e:
                rollback()
                log.warning("Failed adding {} due to error: ".format(species))
                log.exception(e)


mobile_views = [PawikanGeneralView]
name = "Pawikan"
