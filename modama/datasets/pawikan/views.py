from modama import appbuilder
from modama.views.dataset_base import (BaseObservationView, BaseModamaView,
                                       BaseVerificationView)
from wtforms.validators import NumberRange
from modama.views.validators import ValueRequired
from fab_addon_geoalchemy.models import GeoSQLAInterface
from flask_babel import gettext as _
import logging
from wtforms import DateTimeField, validators, StringField
from wtforms.widgets import HTMLString
from modama.widgets import DateTimeTZPickerWidget, StaticTextWidget
from wtforms_jsonschema2.conditions import oneOf

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
    PawikanNestEvaluation, PawikanYesNoEnum)


log = logging.getLogger(__name__)


class PawikanGeneralPictureView(BaseModamaView):
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
class PawikanNestingActionTakenView(BaseModamaView):
    _pretty_name = 'Nesting Action Taken'
    datamodel = GeoSQLAInterface(PawikanNestingActionTaken)
    # add_columns = ["name", "description"] +\
    #               ["nest_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["nest_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanTradeExhibitTypeView(BaseModamaView):
    _pretty_name = 'Trade Exhibit Type'
    datamodel = GeoSQLAInterface(PawikanTradeExhibitType)
    # add_columns = ["name", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanInwaterTurtleActivityView(BaseModamaView):
    _pretty_name = 'Inwater Turtle Activity'
    datamodel = GeoSQLAInterface(PawikanInwaterTurtleActivity)
    # add_columns = ["name", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanEncounterTypeView(BaseModamaView):
    _pretty_name = 'Encounter Type'
    datamodel = GeoSQLAInterface(PawikanEncounterType)
    # add_columns = ["name", "description"] +\
    #               ["general_reports"]
    # list_columns = ["name", "description"] +\
    #                ["general_reports"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanFacilityEncounteredView(BaseModamaView):
    _pretty_name = 'Facility Encountered'
    datamodel = GeoSQLAInterface(PawikanFacilityEncountered)
    # add_columns = ["name", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanFishingTurtleConditionView(BaseModamaView):
    _pretty_name = 'Fishing Turtle Condition'
    datamodel = GeoSQLAInterface(PawikanFishingTurtleCondition)
    # add_columns = ["name", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanStrandingCauseView(BaseModamaView):
    _pretty_name = 'Stranding Cause'
    datamodel = GeoSQLAInterface(PawikanStrandingCause)
    # add_columns = ["name", "description"] +\
    #               [""]
    # list_columns = ["name", "description"] +\
    #                [""]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanTradeTurtleConditionView(BaseModamaView):
    _pretty_name = 'Trade Turtle Condition'
    datamodel = GeoSQLAInterface(PawikanTradeTurtleCondition)
    # add_columns = ["name", "description"] +\
    #               ["trade_exhibit_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["trade_exhibit_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanHatchlingLocationView(BaseModamaView):
    _pretty_name = 'Hatchling Location'
    datamodel = GeoSQLAInterface(PawikanHatchlingLocation)
    # add_columns = ["name", "description"] +\
    #               ["hatchling_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["hatchling_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanLocationTypeView(BaseModamaView):
    _pretty_name = 'Location Type'
    datamodel = GeoSQLAInterface(PawikanLocationType)
    # add_columns = ["name", "description"] +\
    #               [""]
    # list_columns = ["name", "description"] +\
    #                [""]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanNestTypeView(BaseModamaView):
    _pretty_name = 'Nest Type'
    datamodel = GeoSQLAInterface(PawikanNestType)
    # add_columns = ["name", "description"] +\
    #               ["nest_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["nest_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanFishingTurtleDispositionView(BaseModamaView):
    _pretty_name = 'Fishing Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanFishingTurtleDisposition)
    # add_columns = ["name", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanStrandingTurtleDispositionView(BaseModamaView):
    _pretty_name = 'Stranding Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanStrandingTurtleDisposition)
    # add_columns = ["name", "description"] +\
    #               [""]
    # list_columns = ["name", "description"] +\
    #                [""]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanInwaterActivityTypeView(BaseModamaView):
    _pretty_name = 'Inwater Activity Type'
    datamodel = GeoSQLAInterface(PawikanInwaterActivityType)
    # add_columns = ["name", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanFishingGearView(BaseModamaView):
    _pretty_name = 'Fishing Gear'
    datamodel = GeoSQLAInterface(PawikanFishingGear)
    # add_columns = ["name", "description"] +\
    #               ["fisheries_interactions"]
    # list_columns = ["name", "description"] +\
    #                ["fisheries_interactions"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanInwaterTypeView(BaseModamaView):
    _pretty_name = 'Inwater Type'
    datamodel = GeoSQLAInterface(PawikanInwaterType)
    # add_columns = ["name", "description"] +\
    #               ["inwater_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["inwater_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanTradeTurtleDispositionView(BaseModamaView):
    _pretty_name = 'Trade Turtle Disposition'
    datamodel = GeoSQLAInterface(PawikanTradeTurtleDisposition)
    # add_columns = ["name", "description"] +\
    #               ["trade_exhibit_encounter"]
    # list_columns = ["name", "description"] +\
    #                ["trade_exhibit_encounter"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanHatchlingDispositionView(BaseModamaView):
    _pretty_name = 'Hatchling Disposition'
    datamodel = GeoSQLAInterface(PawikanHatchlingDisposition)
    # add_columns = ["name", "description"] +\
    #               ["hatchling_encounters"]
    # list_columns = ["name", "description"] +\
    #                ["hatchling_encounters"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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


class PawikanOutcomeView(BaseModamaView):
    _pretty_name = 'Outcome'
    datamodel = GeoSQLAInterface(PawikanOutcome)
    # add_columns = ["name", "description"] +\
    #               ["general_reports"]
    # list_columns = ["name", "description"] +\
    #                ["general_reports"]
    # edit_columns = ["name", "description"]
    # show_columns = ["name", "description"] +\
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

class PawikanNestWithEggView(BaseModamaView):
    _pretty_name = 'Nest With Egg'
    datamodel = GeoSQLAInterface(PawikanNestWithEgg)
    add_columns = ["nest_type", "nester_observed", "action_taken",
                   "area_secure", "nest_id"] +\
                  ["general"]
    list_columns = ["nest_type", "nester_observed", "action_taken",
                    "area_secure", "nest_id"]
    edit_columns = ["nest_type", "nester_observed", "action_taken",
                    "area_secure", "nest_id"]
    show_columns = ["nest_type", "nester_observed", "action_taken",
                    "area_secure", "nest_id"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    add_title = 'Add Nest With Egg'
    show_title = 'Nest With Egg'
    list_title = 'Nests With Egg'
    edit_title = 'Edit Nest With Egg'
    label_columns = {
        "nest_type": "Nest Type",
        "nester_observed": "Was the nester observed at the same time?",
        "action_taken": "Action taken",
        "area_secure": "Is the area secure?",
        "nest_id": "ID/number of the nest"
    }
    """
    validators_columns = {}
    _conditional_relations = [
    ]
    """

class PawikanTradeExhibitView(BaseModamaView):
    _pretty_name = 'Trade Exhibit'
    datamodel = GeoSQLAInterface(PawikanTradeExhibit)
    add_columns = ["trade_exhibit_type", "facility_encountered",
                   "turtle_condition", "amount_encountered",
                   "unit_amount_encountered", "facility_address",
                   "facility_contact_person", "turtle_disposition"] +\
                  ["general"]
    edit_columns = ["trade_exhibit_type", "facility_encountered",
                    "turtle_condition", "amount_encountered",
                    "unit_amount_encountered", "facility_address",
                    "facility_contact_person", "turtle_disposition"]
    list_columns = ["trade_exhibit_type", "facility_encountered",
                    "turtle_condition", "amount_encountered",
                    "unit_amount_encountered", "facility_address",
                    "facility_contact_person", "turtle_disposition"]
    show_columns = ["trade_exhibit_type", "facility_encountered",
                    "turtle_condition", "amount_encountered",
                    "unit_amount_encountered", "facility_address",
                    "facility_contact_person", "turtle_disposition"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    add_title = 'Add Trade or Exhibit'
    show_title = 'Trade or Exhibit'
    list_title = 'Trade or Exhibit'
    edit_title = 'Edit Trade or Exhibit'
    label_columns = {
        "trade_exhibit_type": "Type of trade or  exhibit encounter",
        "facility_encountered": "Facility encountered",
        "turtle_condition": "Turtle condition",
        "amount_encountered": "Amount encountered",
        "unit_amount_encountered": "Unit of the amount",
        "facility_address": "Address of the facility",
        "facility_contact_person": "Contact details of person",
        "turtle_disposition": "Disposition"
    }
    """
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanSpeciesView(BaseModamaView):
    _pretty_name = 'Species'
    datamodel = GeoSQLAInterface(PawikanSpecies)
    # add_columns = ["picture", "genus", "description", "species", "common_name"] +\
    #               ["general_reports"]
    # list_columns = ["picture", "genus", "description", "species", "common_name"] +\
    #                ["general_reports"]
    # edit_columns = ["picture", "genus", "description", "species", "common_name"]
    # show_columns = ["picture", "genus", "description", "species", "common_name"] +\
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


class PawikanHatchlingsView(BaseModamaView):
    _pretty_name = 'Hatchlings'
    datamodel = GeoSQLAInterface(PawikanHatchlings)
    add_columns = ["location_of_hatchlings", "datetime_first_emergence",
                   "datetime_last_emergence", "p_color", "carapace_color",
                   "hatchling_disposition", "released", "hatchery_nest"] +\
                  ["general"]
    edit_columns = ["location_of_hatchlings", "datetime_first_emergence",
                    "datetime_last_emergence", "p_color", "carapace_color",
                    "hatchling_disposition", "released", "hatchery_nest"]
    show_columns = ["location_of_hatchlings", "datetime_first_emergence",
                    "datetime_last_emergence", "p_color", "carapace_color",
                    "hatchling_disposition", "released", "hatchery_nest"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    list_columns = ["location_of_hatchlings", "datetime_first_emergence",
                    "datetime_last_emergence", "p_color", "carapace_color",
                    "hatchling_disposition", "released", "hatchery_nest"]
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
    label_columns = {
        "location_of_hatchlings": "Location of hatchlings",
        "datetime_first_emergence": "Date and time of first emergence",
        "datetime_last_emergence": "Date and time of last emergence",
        "p_color": "P color",
        "carapace_color": "Carapace color",
        "hatchling_disposition": "Disposition of hatchlings",
        "released": "Were all hatchlings released?",
        "hatchery_nest": "Hatchery nest",
    }
    validators_columns = {
        'hatchery_nest': [ValueRequired(PawikanYesNoEnum.no,
                                        'Please submit hatchlings from a'
                                        ' hatchery as "Nest evaluation"')]
    }
    """
    _conditional_relations = [
    ]
    """
    edit_form_extra_fields = {'datetime_first_emergence':
                              DateTimeField('Date and time of first emergence',
                                            validators=[validators.required()],
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget()),
                              'datetime_last_emergence':
                              DateTimeField('Date and time of last emergence',
                                            validators=[validators.required()],
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget())}
    add_form_extra_fields = {'datetime_first_emergence':
                             DateTimeField('Date and time of first emergence',
                                           validators=[validators.required()],
                                           format='%Y-%m-%d %H:%M:%S%z',
                                           widget=DateTimeTZPickerWidget()),
                             'datetime_last_emergence':
                             DateTimeField('Date and time of last emergence',
                                           validators=[validators.required()],
                                           format='%Y-%m-%d %H:%M:%S%z',
                                           widget=DateTimeTZPickerWidget())}


class PawikanStrandingView(BaseModamaView):
    _pretty_name = 'Stranding'
    datamodel = GeoSQLAInterface(PawikanStranding)
    add_columns = ["stranding_code", "turtle_disposition", "suspected_cause",
                   "confirmed_cause", "cause_confirmed_by", "sample_collected",
                   "necropsy_conducted", "necropsy_carried_out_by", "general"]
    list_columns = ["stranding_code", "turtle_disposition", "suspected_cause",
                    "confirmed_cause", "cause_confirmed_by", "sample_collected",
                    "necropsy_conducted", "necropsy_carried_out_by"]
    show_columns = ["stranding_code", "turtle_disposition", "suspected_cause",
                    "confirmed_cause", "cause_confirmed_by", "sample_collected",
                    "necropsy_conducted", "necropsy_carried_out_by"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    edit_columns = ["stranding_code", "turtle_disposition", "suspected_cause",
                    "confirmed_cause", "cause_confirmed_by", "sample_collected",
                    "necropsy_conducted", "necropsy_carried_out_by", "general"]
    # related_views = []
    add_title = 'Add Stranding'
    show_title = 'Stranding'
    list_title = 'Stranding'
    edit_title = 'Edit Stranding'
    label_columns = {
        "stranding_code": "Stranding Code",
        "turtle_disposition": "Disposition of Turtle",
        "suspected_cause": "Suspected cause",
        "confirmed_cause": "Confirmed cause",
        "cause_confirmed_by": "Stranding cause confirmed by",
        "sample_collected": "Tissue sample collected?",
        "necropsy_conducted": "Was necropsy conducted?",
        "necropsy_carried_out_by": "Necropsy carried out by"
    }
    """
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanTaggingView(BaseModamaView):
    _pretty_name = 'Tagging'
    datamodel = GeoSQLAInterface(PawikanTagging)
    add_columns = ["existing_tags_origin", "existing_tags_left",
                   "existing_tags_right", "new_tags_left", "new_tags_right",
                   "replacement_tags_left", "replacement_tags_right",
                   "reminders", "general"]
    show_columns = ["existing_tags_origin", "existing_tags_left",
                    "existing_tags_right", "new_tags_left", "new_tags_right",
                    "replacement_tags_left", "replacement_tags_right"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    edit_columns = ["existing_tags_origin", "existing_tags_left",
                    "existing_tags_right", "new_tags_left", "new_tags_right",
                    "replacement_tags_left", "replacement_tags_right",
                    "reminders"]
    list_columns = ["existing_tags_origin", "existing_tags_left",
                    "existing_tags_right", "new_tags_left", "new_tags_right",
                    "replacement_tags_left", "replacement_tags_right"]

    add_title = 'Add Tagging'
    show_title = 'Tagging'
    list_title = 'Tagging'
    edit_title = 'Edit Tagging'
    label_columns = {
        "existing_tags_origin": "Origin of existing tags",
        "existing_tags_left": "Existing tags left",
        "existing_tags_right": "Existing tags right",
        "new_tags_left": "New tags left",
        "new_tags_right": "New tags right",
        "replacement_tags_left": "Replacement tags left",
        "replacement_tags_right": "Replacement tags right"
    }
    """
    validators_columns = {}
    _conditional_relations = [
    ]
    """
    edit_form_extra_fields = {'reminders':
                              StringField('Reminders',
                                          widget=StaticTextWidget(
                                              HTMLString("<ul><li>Do not remove existing, non-damaged, readable tags.</li><li>Do not remove foreign tags.</li><li>Tags should be applied as prescribed</li></ul>")))}

    add_form_extra_fields = {'reminders':
                             StringField('Reminders',
                                         widget=StaticTextWidget(
                                             HTMLString("asdsadasd")))}


class PawikanNestEvaluationView(BaseModamaView):
    _pretty_name = 'Nest Evaluation'
    datamodel = GeoSQLAInterface(PawikanNestEvaluation)
    add_columns = ["nest_evaluation_type", "nest_id", "number_of_eggs_known",
                   "num_eggs_s", "num_eggs_uht", "num_eggs_uh", "num_eggs_lpe",
                   "num_eggs_dpe", "num_eggs_ud", "num_eggs_p", "num_eggs_din",
                   "num_eggs_lin", "num_emerged"] +\
                  ["general"]
    show_columns = ["nest_evaluation_type", "nest_id", "number_of_eggs_known",
                    "num_eggs_s", "num_eggs_uht", "num_eggs_uh", "num_eggs_lpe",
                    "num_eggs_dpe", "num_eggs_ud", "num_eggs_p", "num_eggs_din",
                    "num_eggs_lin", "num_emerged"] +\
                   ["clutch_size", "emergence_success", "hatchling_success"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    list_columns = ["nest_evaluation_type", "nest_id", "number_of_eggs_known",
                    "num_eggs_s", "num_eggs_uht", "num_eggs_uh", "num_eggs_lpe",
                    "num_eggs_dpe", "num_eggs_ud", "num_eggs_p", "num_eggs_din",
                    "num_eggs_lin", "num_emerged"] +\
                   ["clutch_size", "emergence_success", "hatchling_success"]
    edit_columns = ["nest_evaluation_type", "nest_id", "number_of_eggs_known",
                    "num_eggs_s", "num_eggs_uht", "num_eggs_uh", "num_eggs_lpe",
                    "num_eggs_dpe", "num_eggs_ud", "num_eggs_p", "num_eggs_din",
                    "num_eggs_lin", "num_emerged"]

    # list_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"] +\
    #                ["general"]
    # edit_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"]
    # show_columns = ["num_eggs_din", "num_eggs_uh", "number_of_eggs_known", "num_eggs_s", "nest_id", "num_eggs_lin", "num_eggs_p", "num_eggs_uht", "num_eggs_ud", "num_eggs_dpe", "num_emerged", "num_eggs_lpe"] +\
    #                ["general"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Nest Evaluation'
    show_title = 'Nest Evaluation'
    list_title = 'Nest Evaluation'
    edit_title = 'Edit Nest Evaluation'
    label_columns = {
        "nest_evaluation_type": "Is the nest",
        "nest_id": "Nest ID/Number",
        "number_of_eggs_known": "Is the number of eggs known?",
        "num_eggs_s": "Eggs completely hatched (S)",
        "num_eggs_uht": "Eggs unhatched with full embryo (UHT)",
        "num_eggs_uh": "Eggs unhatched but fertile (UT)",
        "num_eggs_lpe": "Live pipped eggs (LPE)",
        "num_eggs_dpe": "Dead pipped eggs (DPE)",
        "num_eggs_ud": "Eggs with no visible development",
        "num_eggs_p": "Predated eggs",
        "num_eggs_din": "Dead hatchlings in nest",
        "num_eggs_lin": "Live hatchlings in nest",
        "num_emerged": "Emerged hatchlings",
        "clutch_size": "Clutch size",
        "emergence_success": "Emergence success (%)",
        "hatchling_success": "Hatchling success (%)"
    }
    validators_columns = {
        "num_eggs_s": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_uht": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_uh": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_lpe": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_dpe": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_ud": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_p": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_din": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_eggs_lin": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")],
        "num_emerged": [NumberRange(min=0, max=300, message="Please enter a number between 0 and 300")]
    }
    """
    _conditional_relations = [
    ]
    """


class PawikanFisheriesInteractionView(BaseModamaView):
    _pretty_name = 'Fisheries Interaction'
    datamodel = GeoSQLAInterface(PawikanFisheriesInteraction)
    add_columns = ["fisher_details", "vessel_details", "gear_used",
                   "turtle_condition", "turtle_disposition"] +\
                  ["general"]
    edit_columns = ["fisher_details", "vessel_details", "gear_used",
                    "turtle_condition", "turtle_disposition"]
    list_columns = ["fisher_details", "vessel_details", "gear_used",
                    "turtle_condition", "turtle_disposition"]
    show_columns = ["fisher_details", "vessel_details", "gear_used",
                    "turtle_condition", "turtle_disposition"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    # list_columns = ["vessel_details", "fisher_details"] +\
    #                ["turtle_disposition", "general", "gear_used", "turtle_condition"]
    # edit_columns = ["vessel_details", "fisher_details"]
    # show_columns = ["vessel_details", "fisher_details"] +\
    #                ["turtle_disposition", "general", "gear_used", "turtle_condition"] +\
    #                [""]
    # related_views = []
    add_title = 'Add Fisheries Interaction'
    show_title = 'Fisheries Interaction'
    list_title = 'Fisheries Interactions'
    edit_title = 'Edit Fisheries Interaction'
    label_columns = {
        "fisher_details": "Fisher details",
        "vessel_details": "Vessel details (tonnage)",
        "gear_used": "Gear used",
        "turtle_condition": "Condition of turtle",
        "turtle_disposition": "Disposition of turtle"
    }
    """
    validators_columns = {}
    _conditional_relations = [
    ]
    """


class PawikanInWaterView(BaseModamaView):
    _pretty_name = 'In Water'
    datamodel = GeoSQLAInterface(PawikanInWater)
    add_columns = ["inwater_encounter_type", "your_activity", "depth",
                   "turtle_activity"] +\
                  ["general"]
    list_columns = ["inwater_encounter_type", "your_activity", "depth",
                    "turtle_activity"]
    show_columns = ["inwater_encounter_type", "your_activity", "depth",
                    "turtle_activity"] +\
                   ['created_by', 'created_on', 'changed_by', 'changed_on']
    edit_columns = ["inwater_encounter_type", "your_activity", "depth",
                    "turtle_activity"]
    # list_columns = ["detailed_location", "depth"] +\
    #                ["inwater_encounter_type", "general", "your_activity", "turtle_activity"]
    # edit_columns = ["detailed_location", "depth"]
    # show_columns = ["detailed_location", "depth"] +\
    #                ["inwater_encounter_type", "general", "your_activity", "turtle_activity"] +\
    #                [""]
    # related_views = []
    add_title = 'Add In Water'
    show_title = 'In Water'
    list_title = 'In Water'
    edit_title = 'Edit In Water'
    label_columns = {
        "inwater_encounter_type": "Type of in-water encounter",
        "your_activity": "Your activity",
        "depth": "Depth in m",
        "turtle_activity": "Turtle activity"
    }
    validators_columns = {
        "depth": [NumberRange(min=0, max=70, message="Please enter a depth"
                              " between 0m (surface) and 70m.")],
    }
    """
    _conditional_relations = [
    ]
    """


class PawikanGeneralView(BaseObservationView):
    _pretty_name = 'General'
    datamodel = GeoSQLAInterface(PawikanGeneral)
    add_columns = BaseObservationView._base_add +\
        ["location", "location_type", "detailed_location",  # "barangay",
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
        ["location", "location_type", 'detailed_location',  # "barangay",
         "alive", "species", "lateral_scutes", "prefrontal_scutes",
         "encounter_type", "incident_description", "sex",
         "curved_carapace_length", "origin_of_report", "report_generator",
         ]  # "tagged", "pictures", "outcome"]
    show_columns = BaseObservationView._base_show +\
        [
            # "location",
            "location_type", "detailed_location",  # "barangay",
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
    add_fieldsets = edit_fieldsets = [
        (
            "Base",
            {'fields': ['observation_datetime']}
        ),
        (
            "Location",
            {'fields': ['location', 'location_type', 'detailed_location']}
        ),
        (
            "Turtle",
            {'fields': ['alive', 'species', 'lateral_scutes',
                        'prefrontal_scutes', 'curved_carapace_length', 'sex']}
        ),
        (
            "This encounter",
            {'fields': ['encounter_type', 'incident_description',
                        'origin_of_report', 'report_generator', 'tagged',
                        'outcome']}
        )

    ]
    show_fieldsets = [
        (
            "Base",
            {'fields': ['observation_datetime', 'report_id', 'created_by', 'created_on', 'changed_by', 'changed_on']}
        ),
        (
            "Location",
            {'fields': ['location', 'location_type', 'detailed_location']}
        ),
        (
            "Turtle",
            {'fields': ['alive', 'species', 'lateral_scutes',
                        'prefrontal_scutes', 'curved_carapace_length', 'sex']}
        ),
        (
            "This encounter",
            {'fields': ['encounter_type', 'incident_description',
                        'origin_of_report', 'report_generator', 'tagged',
                        'outcome', 'num_pictures']}
        )
    ]

    add_title = 'Add Pawikan Encounter'
    show_title = 'Pawikan Encounter'
    list_title = 'Pawikan Encounters'
    edit_title = 'Edit Pawikan Encounter'
    label_columns = {
        "observation_datetime": "Encounter date and time",
        "location": "Location of encounter",
        "location_type": "Type of this location",
        "detailed_location": "Detailed location description",
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
        ],
        'lateral_scutes': [
            NumberRange(
                min=4, max=9,
                message=_("There must be between 4 and 9 scutes."))
        ],
        'prefrontal_scutes': [
            NumberRange(
                min=2, max=10,
                message=_("There can be no more than 10 scutes and a minimum of 2."))
        ]
    }
    _conditional_relations = [
        oneOf({
            PawikanStrandingView: {'encounter_type': 'Stranding'},
            PawikanInWaterView: {'encounter_type': 'In-water'},
            PawikanHatchlingsView: {'encounter_type': 'Hatchlings'},
            PawikanNestWithEggView: {'encounter_type': 'Nest with eggs'},
            PawikanTradeExhibitView: {'encounter_type': 'Trade or exhibit'},
            PawikanTaggingView: {'tagged': 'yes'},
            PawikanNestEvaluationView: {'encounter_type': 'Nest evaluation'},
            PawikanFisheriesInteractionView: {'encounter_type': 'Fisheries interaction'},
        })
    ]

class PawikanGeneralVerificationView(BaseVerificationView, PawikanGeneralView):
    __pretty_name = 'Verification'

    list_columns = BaseVerificationView._base_list +\
        [
            # "location", "location_type", "barangay",
            "alive", "species", "lateral_scutes", "prefrontal_scutes",
            "encounter_type", "incident_description", "sex",
            "curved_carapace_length", "origin_of_report", "report_generator",
            "tagged", "num_pictures", "outcome"]
    # "tagging", "inwater", "hatchlings", "trade_exhibit", "stranding",
    # "nest_with_egg", "fisheries_interaction", "nest_evaluation"]
    edit_columns = BaseVerificationView._base_edit +\
        ["location", "location_type", 'detailed_location',  # "barangay",
         "alive", "species", "lateral_scutes", "prefrontal_scutes",
         "encounter_type", "incident_description", "sex",
         "curved_carapace_length", "origin_of_report", "report_generator",
         ]  # "tagged", "pictures", "outcome"]
    show_columns = BaseVerificationView._base_show +\
        [
            # "location",
            "location_type", "detailed_location",  # "barangay",
            "alive", "species", "lateral_scutes", "prefrontal_scutes",
            "encounter_type", "incident_description", "sex",
            "curved_carapace_length", "origin_of_report", "report_generator",
            "tagged", "num_pictures", "outcome"]

    edit_fieldsets = [
        (
            "Base",
            {'fields': ['observation_datetime', 'verified', 'created_by']}
        ),
        (
            "Location",
            {'fields': ['location', 'location_type', 'detailed_location']}
        ),
        (
            "Turtle",
            {'fields': ['alive', 'species', 'lateral_scutes',
                        'prefrontal_scutes', 'curved_carapace_length', 'sex']}
        ),
        (
            "This encounter",
            {'fields': ['encounter_type', 'incident_description',
                        'origin_of_report', 'report_generator', 'tagged',
                        'outcome']}
        )

    ]


appbuilder.add_view(PawikanGeneralView, "Encounters",
                    category="Pawikan")
appbuilder.add_view(PawikanGeneralVerificationView, "Verify",
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
