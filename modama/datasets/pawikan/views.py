
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView
from wtforms.validators import NumberRange
from fab_addon_geoalchemy.models import GeoSQLAInterface
from flask_babel import gettext as _
import logging
# from wtforms_jsonschema2.conditions import oneOf

from modama.datasets.pawikan.models import (
    #  PawikanInwaterType, PawikanHatchlingLocation,
    #  PawikanInwaterActivityType, PawikanFacilityEncountered, PawikanOutcome,
    #  PawikanFishingTurtleCondition,
    #  PawikanTradeTurtleDisposition, PawikanTradeTurtleCondition,
    #  PawikanNestingActionTaken, PawikanStrandingCause,
    #  PawikanLocationType, PawikanNestType,
    #  PawikanEncounterType, PawikanFishingTurtleDisposition,
    #  PawikanFishingGear, PawikanTradeExhibitType,
    #  PawikanInwaterTurtleActivity, PawikanHatchlingDisposition,
    #  PawikanStrandingTurtleDisposition,
    PawikanGeneral, PawikanStranding, PawikanTradeExhibit, PawikanInWater,
    PawikanFisheriesInteraction, PawikanGeneralPicture, PawikanSpecies,
    PawikanHatchlings, PawikanTagging, PawikanNestWithEgg,
    PawikanNestEvaluation)


log = logging.getLogger(__name__)


class PawikanGeneralPictureView(ModelView):
    _pretty_name = 'General Picture'
    datamodel = GeoSQLAInterface(PawikanGeneralPicture)
    add_columns = ["picture", "general"]
    list_columns = ["picture_img_thumbnail"]
    edit_columns = ["picture"]
    show_columns = ["picture_img"]
    add_title = 'Add Picture'
    show_title = 'Picture'
    list_title = 'Pictures'
    edit_title = 'Edit Picture'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


'''
class PawikanNestingActionTakenView(ModelView):
    _pretty_name = 'Nesting Action Taken'
    datamodel = GeoSQLAInterface(PawikanNestingActionTaken)
    # add_columns = ["name", "id", "description"] +\
    #               ["nest_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["nest_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["nest_encounters"] +\
    #                [""]
    # related_views = [PawikanNestWithEggView]
    add_title = 'Add Nesting Action Taken'
    show_title = 'Nesting Action Taken'
    list_title = 'Nesting Action Takens'
    edit_title = 'Edit Nesting Action Taken'
    """
    label_columns = {
        "nest_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanTradeExhibitTypeView(ModelView):
    _pretty_name = 'Trade Exhibit Type'
    datamodel = GeoSQLAInterface(PawikanTradeExhibitType)
    # add_columns = ["name", "id", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"] +\
    #                [""]
    # related_views = [PawikanTradeExhibitView]
    add_title = 'Add Trade Exhibit Type'
    show_title = 'Trade Exhibit Type'
    list_title = 'Trade Exhibit Types'
    edit_title = 'Edit Trade Exhibit Type'
    """
    label_columns = {
        "trade_exhibit_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanInwaterTurtleActivityView(ModelView):
    _pretty_name = 'Inwater Turtle Activity'
    datamodel = GeoSQLAInterface(PawikanInwaterTurtleActivity)
    # add_columns = ["name", "id", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"] +\
    #                [""]
    # related_views = [PawikanInWaterView]
    add_title = 'Add Inwater Turtle Activity'
    show_title = 'Inwater Turtle Activity'
    list_title = 'Inwater Turtle Activitys'
    edit_title = 'Edit Inwater Turtle Activity'
    """
    label_columns = {
        "inwater_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanEncounterTypeView(ModelView):
    _pretty_name = 'Encounter Type'
    datamodel = GeoSQLAInterface(PawikanEncounterType)
    # add_columns = ["name", "id", "description"] +\
    #               ["general_reports"]
    # list_columns = ["name", "id", "description"] +\
    #                ["general_reports"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["general_reports"] +\
    #                [""]
    # related_views = [PawikanGeneralView]
    add_title = 'Add Encounter Type'
    show_title = 'Encounter Type'
    list_title = 'Encounter Types'
    edit_title = 'Edit Encounter Type'
    """
    label_columns = {
        "general_reports": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanFacilityEncounteredView(ModelView):
    _pretty_name = 'Facility Encountered'
    datamodel = GeoSQLAInterface(PawikanFacilityEncountered)
    # add_columns = ["name", "id", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"] +\
    #                [""]
    # related_views = [PawikanTradeExhibitView]
    add_title = 'Add Facility Encountered'
    show_title = 'Facility Encountered'
    list_title = 'Facility Encountereds'
    edit_title = 'Edit Facility Encountered'
    """
    label_columns = {
        "trade_exhibit_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanFishingTurtleConditionView(ModelView):
    _pretty_name = 'Fishing Turtle Condition'
    datamodel = GeoSQLAInterface(PawikanFishingTurtleCondition)
    # add_columns = ["name", "id", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"] +\
    #                [""]
    # related_views = [PawikanFisheriesInteractionView]
    add_title = 'Add Fishing Turtle Condition'
    show_title = 'Fishing Turtle Condition'
    list_title = 'Fishing Turtle Conditions'
    edit_title = 'Edit Fishing Turtle Condition'
    """
    label_columns = {
        "fisheries_interactions": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanStrandingCauseView(ModelView):
    _pretty_name = 'Stranding Cause'
    datamodel = GeoSQLAInterface(PawikanStrandingCause)
    # add_columns = ["name", "id", "description"] +\
    #               [""]
    # list_columns = ["name", "id", "description"] +\
    #                [""]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                [""] +\
    #                [""]
    # related_views = []
    add_title = 'Add Stranding Cause'
    show_title = 'Stranding Cause'
    list_title = 'Stranding Causes'
    edit_title = 'Edit Stranding Cause'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanTradeTurtleConditionView(ModelView):
    _pretty_name = 'Trade Turtle Condition'
    datamodel = GeoSQLAInterface(PawikanTradeTurtleCondition)
    # add_columns = ["name", "id", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounters"] +\
    #                [""]
    # related_views = [PawikanTradeExhibitView]
    add_title = 'Add Trade Turtle Condition'
    show_title = 'Trade Turtle Condition'
    list_title = 'Trade Turtle Conditions'
    edit_title = 'Edit Trade Turtle Condition'
    """
    label_columns = {
        "trade_exhibit_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanHatchlingLocationView(ModelView):
    _pretty_name = 'Hatchling Location'
    datamodel = GeoSQLAInterface(PawikanHatchlingLocation)
    # add_columns = ["name", "id", "description"] +\
    #               ["hatchling_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["hatchling_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["hatchling_encounters"] +\
    #                [""]
    # related_views = [PawikanHatchlingsView]
    add_title = 'Add Hatchling Location'
    show_title = 'Hatchling Location'
    list_title = 'Hatchling Locations'
    edit_title = 'Edit Hatchling Location'
    """
    label_columns = {
        "hatchling_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanLocationTypeView(ModelView):
    _pretty_name = 'Location Type'
    datamodel = GeoSQLAInterface(PawikanLocationType)
    # add_columns = ["name", "id", "description"] +\
    #               [""]
    # list_columns = ["name", "id", "description"] +\
    #                [""]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                [""] +\
    #                [""]
    # related_views = []
    add_title = 'Add Location Type'
    show_title = 'Location Type'
    list_title = 'Location Types'
    edit_title = 'Edit Location Type'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanNestTypeView(ModelView):
    _pretty_name = 'Nest Type'
    datamodel = GeoSQLAInterface(PawikanNestType)
    # add_columns = ["name", "id", "description"] +\
    #               ["nest_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["nest_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["nest_encounters"] +\
    #                [""]
    # related_views = [PawikanNestWithEggView]
    add_title = 'Add Nest Type'
    show_title = 'Nest Type'
    list_title = 'Nest Types'
    edit_title = 'Edit Nest Type'
    """
    label_columns = {
        "nest_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanFishingTurtleDispositionView(ModelView):
    _pretty_name = 'Fishing Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanFishingTurtleDisposition)
    # add_columns = ["name", "id", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"] +\
    #                [""]
    # related_views = [PawikanFisheriesInteractionView]
    add_title = 'Add Fishing Turtle Disposition'
    show_title = 'Fishing Turtle Disposition'
    list_title = 'Fishing Turtle Dispositions'
    edit_title = 'Edit Fishing Turtle Disposition'
    """
    label_columns = {
        "fisheries_interactions": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanStrandingTurtleDispositionView(ModelView):
    _pretty_name = 'Stranding Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanStrandingTurtleDisposition)
    # add_columns = ["name", "id", "description"] +\
    #               [""]
    # list_columns = ["name", "id", "description"] +\
    #                [""]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                [""] +\
    #                [""]
    # related_views = []
    add_title = 'Add Stranding Turtle Disposition'
    show_title = 'Stranding Turtle Disposition'
    list_title = 'Stranding Turtle Dispositions'
    edit_title = 'Edit Stranding Turtle Disposition'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanInwaterActivityTypeView(ModelView):
    _pretty_name = 'Inwater Activity Type'
    datamodel = GeoSQLAInterface(PawikanInwaterActivityType)
    # add_columns = ["name", "id", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"] +\
    #                [""]
    # related_views = [PawikanInWaterView]
    add_title = 'Add Inwater Activity Type'
    show_title = 'Inwater Activity Type'
    list_title = 'Inwater Activity Types'
    edit_title = 'Edit Inwater Activity Type'
    """
    label_columns = {
        "inwater_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanFishingGearView(ModelView):
    _pretty_name = 'Fishing Gear'
    datamodel = GeoSQLAInterface(PawikanFishingGear)
    # add_columns = ["name", "id", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["fisheries_interactions"] +\
    #                [""]
    # related_views = [PawikanFisheriesInteractionView]
    add_title = 'Add Fishing Gear'
    show_title = 'Fishing Gear'
    list_title = 'Fishing Gears'
    edit_title = 'Edit Fishing Gear'
    """
    label_columns = {
        "fisheries_interactions": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanInwaterTypeView(ModelView):
    _pretty_name = 'Inwater Type'
    datamodel = GeoSQLAInterface(PawikanInwaterType)
    # add_columns = ["name", "id", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["inwater_encounters"] +\
    #                [""]
    # related_views = [PawikanInWaterView]
    add_title = 'Add Inwater Type'
    show_title = 'Inwater Type'
    list_title = 'Inwater Types'
    edit_title = 'Edit Inwater Type'
    """
    label_columns = {
        "inwater_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanTradeTurtleDispositionView(ModelView):
    _pretty_name = 'Trade Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanTradeTurtleDisposition)
    # add_columns = ["name", "id", "description"] +\
    #               ["trade_exhibit_encounter"]
    # list_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounter"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["trade_exhibit_encounter"] +\
    #                [""]
    # related_views = [PawikanTradeExhibitView]
    add_title = 'Add Trade Turtle Disposition'
    show_title = 'Trade Turtle Disposition'
    list_title = 'Trade Turtle Dispositions'
    edit_title = 'Edit Trade Turtle Disposition'
    """
    label_columns = {
        "trade_exhibit_encounter": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanHatchlingDispositionView(ModelView):
    _pretty_name = 'Hatchling Disposition'
    datamodel = GeoSQLAInterface(PawikanHatchlingDisposition)
    # add_columns = ["name", "id", "description"] +\
    #               ["hatchling_encounters"]
    # list_columns = ["name", "id", "description"] +\
    #                ["hatchling_encounters"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["hatchling_encounters"] +\
    #                [""]
    # related_views = [PawikanHatchlingsView]
    add_title = 'Add Hatchling Disposition'
    show_title = 'Hatchling Disposition'
    list_title = 'Hatchling Dispositions'
    edit_title = 'Edit Hatchling Disposition'
    """
    label_columns = {
        "hatchling_encounters": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanOutcomeView(ModelView):
    _pretty_name = 'Outcome'
    datamodel = GeoSQLAInterface(PawikanOutcome)
    # add_columns = ["name", "id", "description"] +\
    #               ["general_reports"]
    # list_columns = ["name", "id", "description"] +\
    #                ["general_reports"]
    # edit_columns = ["name", "id", "description"]
    # show_columns = ["name", "id", "description"] +\
    #                ["general_reports"] +\
    #                [""]
    # related_views = [PawikanGeneralView]
    add_title = 'Add Outcome'
    show_title = 'Outcome'
    list_title = 'Outcomes'
    edit_title = 'Edit Outcome'
    """
    label_columns = {
        "general_reports": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """

'''


class PawikanFisheriesInteractionView(ModelView):
    _pretty_name = 'Fisheries Interaction'
    datamodel = GeoSQLAInterface(PawikanFisheriesInteraction)
    # add_columns = ["id", "vessel_details", "fisher_details"] +\
    #               ["turtle_disposition", "general", "gear_used", "turtle_condition"]
    # list_columns = ["id", "vessel_details", "fisher_details"] +\
    #                ["turtle_disposition", "general", "gear_used", "turtle_condition"]
    # edit_columns = ["id", "vessel_details", "fisher_details"]
    # show_columns = ["id", "vessel_details", "fisher_details"] +\
    #                ["turtle_disposition", "general", "gear_used", "turtle_condition"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Fisheries Interaction'
    show_title = 'Fisheries Interaction'
    list_title = 'Fisheries Interactions'
    edit_title = 'Edit Fisheries Interaction'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanInWaterView(ModelView):
    _pretty_name = 'In Water'
    datamodel = GeoSQLAInterface(PawikanInWater)
    # add_columns = ["id", "detailed_location", "depth"] +\
    #               ["inwater_encounter_type", "general", "your_activity", "turtle_activity"]
    # list_columns = ["id", "detailed_location", "depth"] +\
    #                ["inwater_encounter_type", "general", "your_activity", "turtle_activity"]
    # edit_columns = ["id", "detailed_location", "depth"]
    # show_columns = ["id", "detailed_location", "depth"] +\
    #                ["inwater_encounter_type", "general", "your_activity", "turtle_activity"] +\
    #                [""]
    # related_views = []
    add_title = 'Add In Water'
    show_title = 'In Water'
    list_title = 'In Water'
    edit_title = 'Edit In Water'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """

class PawikanNestWithEggView(ModelView):
    _pretty_name = 'Nest With Egg'
    datamodel = GeoSQLAInterface(PawikanNestWithEgg)
    # add_columns = ["location", "area_secure", "detailed_location", "nest_id", "id"] +\
    #               ["barangay", "action_taken", "nest_type", "general"]
    # list_columns = ["location", "area_secure", "detailed_location", "nest_id", "id"] +\
    #                ["barangay", "action_taken", "nest_type", "general"]
    # edit_columns = ["location", "area_secure", "detailed_location", "nest_id", "id"]
    # show_columns = ["location", "area_secure", "detailed_location", "nest_id", "id"] +\
    #                ["barangay", "action_taken", "nest_type", "general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Nest With Egg'
    show_title = 'Nest With Egg'
    list_title = 'Nests With Egg'
    edit_title = 'Edit Nest With Egg'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """

class PawikanTradeExhibitView(ModelView):
    _pretty_name = 'Trade Exhibit'
    datamodel = GeoSQLAInterface(PawikanTradeExhibit)
    # add_columns = ["facility_address", "unit_amount_encountered", "amount_encountered", "id", "facility_contact_person"] +\
    #               ["turtle_disposition", "facility_encountered", "turtle_condition", "general", "trade_exhibit_type"]
    # list_columns = ["facility_address", "unit_amount_encountered", "amount_encountered", "id", "facility_contact_person"] +\
    #                ["turtle_disposition", "facility_encountered", "turtle_condition", "general", "trade_exhibit_type"]
    # edit_columns = ["facility_address", "unit_amount_encountered", "amount_encountered", "id", "facility_contact_person"]
    # show_columns = ["facility_address", "unit_amount_encountered", "amount_encountered", "id", "facility_contact_person"] +\
    #                ["turtle_disposition", "facility_encountered", "turtle_condition", "general", "trade_exhibit_type"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Trade/Exhibit'
    show_title = 'Trade/Exhibit'
    list_title = 'Trade/Exhibit'
    edit_title = 'Edit Trade/Exhibit'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanSpeciesView(ModelView):
    _pretty_name = 'Species'
    datamodel = GeoSQLAInterface(PawikanSpecies)
    # add_columns = ["picture", "genus", "id", "description", "species", "common_name"] +\
    #               ["general_reports"]
    # list_columns = ["picture", "genus", "id", "description", "species", "common_name"] +\
    #                ["general_reports"]
    # edit_columns = ["picture", "genus", "id", "description", "species", "common_name"]
    # show_columns = ["picture", "genus", "id", "description", "species", "common_name"] +\
    #                ["general_reports"] +\
    #                [""]
    # related_views = [PawikanGeneralView]
    add_title = 'Add Species'
    show_title = 'Species'
    list_title = 'Species'
    edit_title = 'Edit Species'
    """
    label_columns = {
        "general_reports": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanHatchlingsView(ModelView):
    _pretty_name = 'Hatchlings'
    datamodel = GeoSQLAInterface(PawikanHatchlings)
    # add_columns = ["datetime_last_emergence", "datetime_first_emergence", "hatchery_nest", "p_color", "carapace_color", "released", "id"] +\
    #               ["hatchling_disposition", "location_of_hatchlings", "general"]
    # list_columns = ["datetime_last_emergence", "datetime_first_emergence", "hatchery_nest", "p_color", "carapace_color", "released", "id"] +\
    #                ["hatchling_disposition", "location_of_hatchlings", "general"]
    # edit_columns = ["datetime_last_emergence", "datetime_first_emergence", "hatchery_nest", "p_color", "carapace_color", "released", "id"]
    # show_columns = ["datetime_last_emergence", "datetime_first_emergence", "hatchery_nest", "p_color", "carapace_color", "released", "id"] +\
    #                ["hatchling_disposition", "location_of_hatchlings", "general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Hatchlings'
    show_title = 'Hatchlings'
    list_title = 'Hatchlings'
    edit_title = 'Edit Hatchlings'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanStrandingView(ModelView):
    _pretty_name = 'Stranding'
    datamodel = GeoSQLAInterface(PawikanStranding)
    # add_columns = ["necropsy_conducted", "cause_confirmed_by", "id", "stranding_code", "necropsy_carried_out_by", "confirmed_cause", "sample_collected"] +\
    #               ["turtle_disposition", "suspected_cause", "general"]
    # list_columns = ["necropsy_conducted", "cause_confirmed_by", "id", "stranding_code", "necropsy_carried_out_by", "confirmed_cause", "sample_collected"] +\
    #                ["turtle_disposition", "suspected_cause", "general"]
    # edit_columns = ["necropsy_conducted", "cause_confirmed_by", "id", "stranding_code", "necropsy_carried_out_by", "confirmed_cause", "sample_collected"]
    # show_columns = ["necropsy_conducted", "cause_confirmed_by", "id", "stranding_code", "necropsy_carried_out_by", "confirmed_cause", "sample_collected"] +\
    #                ["turtle_disposition", "suspected_cause", "general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Stranding'
    show_title = 'Stranding'
    list_title = 'Stranding'
    edit_title = 'Edit Stranding'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanTaggingView(ModelView):
    _pretty_name = 'Tagging'
    datamodel = GeoSQLAInterface(PawikanTagging)
    # add_columns = ["new_tags_right", "existing_tags_right", "replacement_tags_right", "new_tags_left", "id", "existing_tags_left", "replacement_tags_left", "existing_tags_origin"] +\
    #               ["general"]
    # list_columns = ["new_tags_right", "existing_tags_right", "replacement_tags_right", "new_tags_left", "id", "existing_tags_left", "replacement_tags_left", "existing_tags_origin"] +\
    #                ["general"]
    # edit_columns = ["new_tags_right", "existing_tags_right", "replacement_tags_right", "new_tags_left", "id", "existing_tags_left", "replacement_tags_left", "existing_tags_origin"]
    # show_columns = ["new_tags_right", "existing_tags_right", "replacement_tags_right", "new_tags_left", "id", "existing_tags_left", "replacement_tags_left", "existing_tags_origin"] +\
    #                ["general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Tagging'
    show_title = 'Tagging'
    list_title = 'Tagging'
    edit_title = 'Edit Tagging'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanNestEvaluationView(ModelView):
    _pretty_name = 'Nest Evaluation'
    datamodel = GeoSQLAInterface(PawikanNestEvaluation)
    # add_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "id", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"] +\
    #               ["general"]
    # list_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "id", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"] +\
    #                ["general"]
    # edit_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "id", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"]
    # show_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "id", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"] +\
    #                ["general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Nest Evaluation'
    show_title = 'Nest Evaluation'
    list_title = 'Nest Evaluation'
    edit_title = 'Edit Nest Evaluation'
    """
    label_columns = {
        "": ""
    }
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanGeneralView(BaseObservationView):
    _pretty_name = 'General'
    datamodel = GeoSQLAInterface(PawikanGeneral)
    add_columns = BaseObservationView._base_add +\
        ["location", "location_type",  # "barangay",
         "alive", "species", "lateral_scutes", "prefrontal_scutes",
         "encounter_type", "incident_description", "sex",
         "curved_carapace_length", "origin_of_report", "report_generator",
         "tagged", "outcome"]
    list_columns = BaseObservationView._base_list +\
        [
            # "location", "location_type", "barangay",
            "alive", "species", "lateral_scutes", "prefrontal_scutes",
            "encounter_type", "incident_description", "sex",
            "curved_carapace_length", "origin_of_report", "report_generator",
            "tagged", "num_pictures", "outcome"]
    # "tagging", "inwater", "hatchlings", "trade_exhibit", "stranding",
    # "nest_with_egg", "fisheries_interaction", "nest_evaluation"]
    edit_columns = BaseObservationView._base_edit +\
        ["location", "location_type",  # "barangay",
         "alive", "species", "lateral_scutes", "prefrontal_scutes",
         "encounter_type", "incident_description", "sex",
         "curved_carapace_length", "origin_of_report", "report_generator",
         ]  # "tagged", "pictures", "outcome"]
    show_columns = BaseObservationView._base_show +\
        [
            #  "location", "location_type",  # "barangay",
            "alive", "species", "lateral_scutes", "prefrontal_scutes",
            "encounter_type", "incident_description", "sex",
            "curved_carapace_length", "origin_of_report", "report_generator",
            "tagged", "num_pictures", "outcome"]
    # "tagging", "inwater", "hatchlings", "trade_exhibit", "stranding",
    # "nest_with_egg", "fisheries_interaction", "nest_evaluation"] +\
    search_exclude_columns = ["report_id", "location"]
    related_views = [PawikanGeneralPictureView, PawikanTaggingView,
                     PawikanInWaterView, PawikanHatchlingsView,
                     PawikanTradeExhibitView, PawikanStrandingView,
                     PawikanNestWithEggView, PawikanFisheriesInteractionView,
                     PawikanNestEvaluationView]
    add_title = 'Add Pawikan Encounter'
    show_title = 'Pawikan Encounter'
    list_title = 'Pawikan Encounterss'
    edit_title = 'Edit Pawikan Encounter'
    label_columns = {
        "observation_datetime": "Encounter date and time",
        "location": "Location of encounter",
        "location_type": "Type of this location",
        "barangay": "Barangay/Municipality/Province",
        "num_pictures": "Number of photos",
        "alive": "Is the turtle alive or dead?",
        "species": "Turtle Species",
        "lateral_scutes": "One side lateral scutes count",
        "prefrontal_scutes": "Prefrontal scutes count",
        "encounter_type": "Type of encounter",
        "incident_description": "Incident description",
        "sex": "Turtle sex",
        "curved_carapace_length": "Curved Carapace Length in cm",
        "origin_of_report": "Origin of report",
        "report_generator": "Contact info of person generating report",
        "tagged": "Is/was the turtle tagged?",
        "pictures": "Photos",
        "outcome": "Outcome",
        "tagging": "Tagging",
        "inwater": "In-water",
        "hatchlings": "Hatchlings",
        "trade_exhibit": "Trade and Exhibit",
        "stranding": "Stranding",
        "nest_with_egg": "Nest with egg",
        "fisheries_interaction": "Fisheries Interaction",
        "nest_evaluation": "Nest evaluation"
    }
    validators_columns = {
        'curved_carapace_length': [
            NumberRange(
                min=50, max=500,
                message=_("Please fill in a value between 50cm and 500cm."))
        ]
    }
    """
    _conditional_relations = [
    ]
    """

    # def _get_related_views_widgets(self, item, *args, **kwargs):
    #     log.debug("Getting related views widgets for {}".format(item))
    #     widgets = super()._get_related_views_widgets(item, *args, **kwargs)
    #     for widget in widgets['related_views']:
    #         log.debug("Got widget {}".format(widget))
    #     return widgets

    def _get_related_view_widget(self, item, related_view,
                                 order_column='', order_direction='',
                                 page=None, page_size=None):

        log.debug("Getting view for {}".format(related_view))
        fk = related_view.datamodel.get_related_fk(self.datamodel.obj)
        filters = related_view.datamodel.get_filters()
        # Check if it's a many to one model relation
        if related_view.datamodel.is_relation_many_to_one(fk):
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationOneToManyEqual,
                self.datamodel.get_pk_value(item))
        # Check if it's a many to many model relation
        elif related_view.datamodel.is_relation_many_to_many(fk):
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationManyToManyEqual,
                self.datamodel.get_pk_value(item))
        elif related_view.datamodel.is_relation_one_to_one(fk):
            log.debug("Got a one-to-one relation")
            backref = self.datamodel.get_related_fk(related_view.datamodel.obj)
            rel_item = getattr(item, backref)
            log.debug("backref {} rel_item {} item {}"
                      .format(backref, rel_item, item))
            if rel_item is not None:
                rel_pk = related_view.datamodel.get_pk_value(rel_item)
                return related_view._get_show_widget(rel_pk, rel_item)['show']
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationOneToManyEqual,
                self.datamodel.get_pk_value(item))
        else:
            log.error("Can't find relation on related view {0}"
                      .format(related_view.name))
            return None
        log.debug("Got a different relation")
        return related_view._get_view_widget(filters=filters,
                                             order_column=order_column,
                                             order_direction=order_direction,
                                             page=page, page_size=page_size)


appbuilder.add_view(PawikanGeneralView, "Encounters",
                    category="Pawikan")
#  appbuilder.add_view(PawikanGeneralPictureView, "Pictures", category="Pawikan")
appbuilder.add_view_no_menu(PawikanGeneralPictureView)
appbuilder.add_view_no_menu(PawikanInWaterView)
appbuilder.add_view_no_menu(PawikanHatchlingsView)
appbuilder.add_view_no_menu(PawikanStrandingView)
appbuilder.add_view_no_menu(PawikanTaggingView)
appbuilder.add_view_no_menu(PawikanNestEvaluationView)
appbuilder.add_view_no_menu(PawikanNestWithEggView)
appbuilder.add_view_no_menu(PawikanTradeExhibitView)
appbuilder.add_view_no_menu(PawikanFisheriesInteractionView)

#  appbuilder.add_view_no_menu(PawikanNestingActionTakenView)
#  appbuilder.add_view_no_menu(PawikanTradeExhibitTypeView)
#  appbuilder.add_view_no_menu(PawikanInwaterTurtleActivityView)
#  appbuilder.add_view_no_menu(PawikanEncounterTypeView)
#  appbuilder.add_view_no_menu(PawikanFacilityEncounteredView)
#  appbuilder.add_view_no_menu(PawikanFishingTurtleConditionView)
#  appbuilder.add_view_no_menu(PawikanStrandingCauseView)
#  appbuilder.add_view_no_menu(PawikanTradeTurtleConditionView)
#  appbuilder.add_view_no_menu(PawikanHatchlingLocationView)
#  appbuilder.add_view_no_menu(PawikanLocationTypeView)
#  appbuilder.add_view_no_menu(PawikanNestTypeView)
#  appbuilder.add_view_no_menu(PawikanFishingTurtleDispositionView)
#  appbuilder.add_view_no_menu(PawikanStrandingTurtleDispositionView)
#  appbuilder.add_view_no_menu(PawikanInwaterActivityTypeView)
#  appbuilder.add_view_no_menu(PawikanFishingGearView)
#  appbuilder.add_view_no_menu(PawikanInwaterTypeView)
#  appbuilder.add_view_no_menu(PawikanTradeTurtleDispositionView)
#  appbuilder.add_view_no_menu(PawikanHatchlingDispositionView)
#  appbuilder.add_view_no_menu(PawikanOutcomeView)
#  appbuilder.add_view_no_menu(PawikanSpeciesView)
