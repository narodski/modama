from flask_appbuilder import Model
from sqlalchemy import (Column, Integer, String, ForeignKey, Text,
                        UniqueConstraint, Enum, DateTime)
from sqlalchemy.orm import relationship
from modama.models.dataset_base import (BaseObservation, Sex, Barangay)
from flask_appbuilder.models.mixins import ImageColumn
from modama.models.common import ModamaAuditMixin
from modama.utils import make_image
from flask_appbuilder.filemanager import ImageManager
from flask import url_for
from fab_addon_geoalchemy.models import Geometry
import enum


class PawikanYesNoEnum(enum.Enum):
    Yes = 'yes'
    No = 'no'


class PawikanBlackWhiteEnum(enum.Enum):
    black = 'black'
    white = 'white'


class PawikanTagOriginEnum(enum.Enum):
    foreign = 'foreign'
    philippine = 'philippine'


class PawikanAliveDeadEnum(enum.Enum):
    alive = 'alive'
    dead = 'dead'


class PawikanTradeUnitEnum(enum.Enum):
    kgs = "kgs"
    pieces = "pieces"


class PawikanStrandingCodeEnum(enum.Enum):
    code1 = "CODE 1"
    code2 = "CODE 2"
    code3 = "CODE 3"
    code4 = "CODE 4"
    code5 = "CODE 5"
    code6 = "CODE 6"
    code7 = "CODE 7"


class PawikanGeneralPicture(Model, ModamaAuditMixin):
    id = Column(Integer, primary_key=True)
    picture = Column(ImageColumn(size=(2048, 2048, False),
                                 thumbnail_size=(800, 800, True)))
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', backref='pictures')

    def picture_img(self):
        im = ImageManager()
        alt = str(self.encounter)
        link_url = url_for('PawikanGeneralPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self.encounter)
        link_url = url_for('PawikanGeneralPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url_thumbnail(self.picture),
                              link_url, alt)
        else:
            return make_image(None, link_url, alt)


class PawikanSpecies(Model):
    id = Column(Integer, primary_key=True)
    genus = Column(String(255), nullable=False)
    species = Column(String(255), nullable=False)
    common_name = Column(String(255))
    description = Column(Text)
    picture = Column(ImageColumn(size=(800, 800, True),
                                 thumbnail_size=(100, 100, True)))

    __table_args__ = (UniqueConstraint('genus', 'species',
                                       name='scientific_name_uc'),)

    def picture_img(self):
        im = ImageManager()
        alt = str(self)
        link_url = url_for('PawikanSpeciesView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self)
        link_url = url_for('PawikanSpeciesView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url_thumbnail(self.picture),
                              link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def __repr__(self):
        if self.common_name is not None:
            return self.common_name
        else:
            return "%s %s" % (self.genus, self.species)


class PawikanEncounterType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanLocationType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanOutcome(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanStrandingCause(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanStrandingTurtleDisposition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanGeneral(BaseObservation):
    __versioned__ = {}

    id = Column(Integer, ForeignKey('base_observation.id'), primary_key=True)
    encounter_type_id = Column(Integer,
                               ForeignKey('pawikan_encounter_type.id'),
                               nullable=False)
    encounter_type = relationship(PawikanEncounterType,
                                  backref='general_reports')
    alive = Column(Enum(PawikanAliveDeadEnum), nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    location_type_id = Column(Integer, ForeignKey('pawikan_location_type.id'),
                              nullable=False)
    location_type = relationship(PawikanLocationType)
    barangay_id = Column(Integer, ForeignKey('barangay.id'), nullable=False)
    barangay = relationship(Barangay)

    stranding = relationship("PawikanStranding", back_populates='general',
                             uselist=False)
    inwater = relationship("PawikanInWater", back_populates='general',
                           uselist=False)
    tagging = relationship("PawikanTagging", back_populates='general',
                           uselist=False)
    nest_with_egg = relationship("PawikanNestWithEgg",
                                 back_populates='general', uselist=True)
    nest_evaluation = relationship("PawikanNestEvaluation",
                                   back_populates='general', uselist=True)
    hatchlings = relationship("PawikanHatchlings", back_populates='general',
                              uselist=False)
    trade_exhibit = relationship('PawikanTradeExhibit',
                                 back_populates='general', uselist=False)
    fisheries_interaction = relationship('PawikanFisheriesInteraction',
                                         back_populates='general',
                                         uselist=False)
    species_id = Column(Integer, ForeignKey('pawikan_species.id'),
                        nullable=False)
    species = relationship(PawikanSpecies, backref='general_reports')
    lateral_scutes = Column(Integer, nullable=False)
    prefrontal_scutes = Column(Integer, nullable=False)

    incident_description = Column(Text)
    sex_id = Column(Integer, ForeignKey('sex.id'))
    sex = relationship(Sex)
    curved_carapace_length = Column(Integer)

    origin_of_report = Column(Text)
    report_generator = Column(Text)

    tagged = Column(Enum(PawikanYesNoEnum), nullable=False, default="No")

    outcome_id = Column(Integer, ForeignKey('pawikan_outcome.id'))
    outcome = relationship(PawikanOutcome, backref="general_reports")

    @property
    def num_pictures(self):
        return len(self.pictures)

    __mapper_args__ = {
        'polymorphic_identity': 'pawikan'
    }

    def __repr__(self):
        return "%s, %s" % (self.created_on, str(self.species))


class PawikanStranding(Model):

    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='stranding',
                           uselist=False)

    stranding_code = Column(Enum(PawikanStrandingCodeEnum), nullable=False)

    turtle_disposition_id = Column(
        Integer,
        ForeignKey('pawikan_stranding_turtle_disposition.id'),
        nullable=False)
    turtle_disposition = relationship(PawikanStrandingTurtleDisposition)
    suspected_cause_id = Column(Integer,
                                ForeignKey('pawikan_stranding_cause.id'),
                                nullable=False)
    suspected_cause = relationship(PawikanStrandingCause)
    confirmed_cause = Column(Text)
    cause_confirmed_by = Column(Text)
    sample_collected = Column(Enum(PawikanYesNoEnum), nullable=False)
    necropsy_conducted = Column(Enum(PawikanYesNoEnum), nullable=False)
    necropsy_carried_out_by = Column(Text)


class PawikanInwaterType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanInwaterActivityType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanInwaterTurtleActivity(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanInWater(Model):

    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='inwater',
                           uselist=False)

    inwater_encounter_type_id = Column(Integer,
                                       ForeignKey('pawikan_inwater_type.id'),
                                       nullable=False)
    inwater_encounter_type = relationship(PawikanInwaterType,
                                          backref="inwater_encounters")

    your_activity_id = Column(Integer,
                              ForeignKey('pawikan_inwater_activity_type.id'),
                              nullable=False)
    your_activity = relationship(PawikanInwaterActivityType,
                                 backref="inwater_encounters")
    detailed_location = Column(Text)
    depth = Column(Integer)

    turtle_activity_id = Column(
        Integer, ForeignKey('pawikan_inwater_turtle_activity.id'),
        nullable=False)
    turtle_activity = relationship(PawikanInwaterTurtleActivity,
                                   backref="inwater_encounters")


class PawikanTagging(Model):

    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='tagging',
                           uselist=False)

    existing_tags_origin = Column(Enum(PawikanTagOriginEnum),
                                  nullable=False)
    existing_tags_left = Column(Text)
    existing_tags_right = Column(Text)
    new_tags_left = Column(Text)
    new_tags_right = Column(Text)
    replacement_tags_left = Column(Text)
    replacement_tags_right = Column(Text)


class PawikanNestType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanNestingActionTaken(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanNestWithEgg(Model):

    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='nest_with_egg',
                           uselist=True)

    nest_type_id = Column(Integer, ForeignKey('pawikan_nest_type.id'),
                          nullable=False)
    nest_type = relationship(PawikanNestType, backref='nest_encounters')

    barangay_id = Column(Integer, ForeignKey('barangay.id'), nullable=False)
    barangay = relationship(Barangay)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    detailed_location = Column(Text)
    nest_id = Column(String)
    action_taken_id = Column(Integer,
                             ForeignKey('pawikan_nesting_action_taken.id'))
    action_taken = relationship(PawikanNestingActionTaken,
                                backref="nest_encounters")
    area_secure = Column(Enum(PawikanYesNoEnum))


class PawikanNestEvaluation(Model):
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='nest_evaluation',
                           uselist=True)

    number_of_eggs_known = Column(Enum(PawikanYesNoEnum), nullable=False)
    nest_id = Column(String)

    num_eggs_s = Column(Integer)
    num_eggs_uht = Column(Integer)
    num_eggs_uh = Column(Integer)
    num_eggs_lpe = Column(Integer)
    num_eggs_dpe = Column(Integer)
    num_eggs_ud = Column(Integer)
    num_eggs_p = Column(Integer)
    num_eggs_din = Column(Integer)
    num_eggs_lin = Column(Integer)
    num_emerged = Column(Integer)

    @property
    def clutch_size(self):
        return sum([i or 0 for i in [
            self.num_emerged + self.num_eggs_lin + self.num_eggs_din +
            self.num_eggs_ud + self.num_eggs_uh + self.num_eggs_uht +
            self.num_eggs_dpe + self.num_eggs_lpe + self.num_eggs_p +
            self.num_eggs_u]])

    @property
    def emergence_success(self):
        if self.num_emerged is not None and self.clutch_size > 0:
            return int(round(self.num_emerged/self.clutch_size * 100, 0))
        elif all((self.num_eggs_s is not None, self.num_eggs_lin is not None,
                  self.num_eggs_din is not None and self.clutch_size > 0)):
            return int(round((self.num_eggs_s - (self.num_eggs_lin
                                                 + self.num_eggs_din)) /
                             self.clutch_size * 100, 0))
        return None

    @property
    def hatchling_success(self):
        if self.num_emerged is not None and self.clutch_size > 0:
            return int(round((self.num_emerged + self.num_eggs_lin
                              + self.num_eggs_din)/self.clutch_size * 100, 0))
        elif self.num_eggs_s is not None and self.clutch_size > 0:
            return int(round(self.num_eggs_s/self.clutch_size * 100, 0))
        return None


class PawikanHatchlingLocation(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanHatchlingDisposition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanHatchlings(Model):
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='hatchlings',
                           uselist=False)

    hatchery_nest = Column(Enum(PawikanYesNoEnum), nullable=False)

    location_of_hatchlings_id = Column(
        Integer, ForeignKey('pawikan_hatchling_location.id'), nullable=False)
    location_of_hatchlings = relationship(PawikanHatchlingLocation,
                                          backref='hatchling_encounters')

    datetime_first_emergence = Column(DateTime(timezone=True))
    datetime_last_emergence = Column(DateTime(timezone=True))
    carapace_color = Column(Enum(PawikanBlackWhiteEnum), nullable=False)
    p_color = Column(Enum(PawikanBlackWhiteEnum), nullable=False)

    hatchling_disposition_id = Column(
        Integer, ForeignKey('pawikan_hatchling_disposition.id'),
        nullable=False)
    hatchling_disposition = relationship(PawikanHatchlingDisposition,
                                         backref="hatchling_encounters")

    released = Column(Enum(PawikanYesNoEnum), nullable=False)


class PawikanTradeExhibitType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanFacilityEncountered(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanTradeTurtleCondition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanTradeTurtleDisposition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanTradeExhibit(Model):
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral', back_populates='trade_exhibit',
                           uselist=False)

    trade_exhibit_type_id = Column(Integer,
                                   ForeignKey('pawikan_trade_exhibit_type.id'),
                                   nullable=False)
    trade_exhibit_type = relationship(PawikanTradeExhibitType,
                                      backref='trade_exhibit_encounters')
    facility_encountered_id = Column(
        Integer, ForeignKey('pawikan_facility_encountered.id'), nullable=False)
    facility_encountered = relationship(PawikanFacilityEncountered,
                                        backref='trade_exhibit_encounters')

    turtle_condition_id = Column(
        Integer, ForeignKey('pawikan_trade_turtle_condition.id'),
        nullable=False)
    turtle_condition = relationship(PawikanTradeTurtleCondition,
                                    backref='trade_exhibit_encounters')

    amount_encountered = Column(Integer)
    unit_amount_encountered = Column(Enum(PawikanTradeUnitEnum))

    turtle_disposition_id = Column(
        Integer, ForeignKey('pawikan_trade_turtle_disposition.id'))
    turtle_disposition = relationship(PawikanTradeTurtleDisposition,
                                      backref='trade_exhibit_encounter')
    facility_address = Column(Text)
    facility_contact_person = Column(Text)


class PawikanFishingGear(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanFishingTurtleCondition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanFishingTurtleDisposition(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return str(self.name)


class PawikanFisheriesInteraction(Model):
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, ForeignKey('pawikan_general.id'),
                        nullable=False)
    general = relationship('PawikanGeneral',
                           back_populates='fisheries_interaction',
                           uselist=False)

    fisher_details = Column(Text)
    vessel_details = Column(Integer)
    fishing_gear_id = Column(Integer, ForeignKey('pawikan_fishing_gear.id'))
    gear_used = relationship(PawikanFishingGear,
                             backref='fisheries_interactions')
    turtle_condition_id = Column(
        Integer, ForeignKey('pawikan_fishing_turtle_condition.id'),
        nullable=False)
    turtle_condition = relationship(PawikanFishingTurtleCondition,
                                    backref='fisheries_interactions')

    turtle_disposition_id = Column(
        Integer, ForeignKey('pawikan_fishing_turtle_disposition.id'))
    turtle_disposition = relationship(PawikanFishingTurtleDisposition,
                                      backref='fisheries_interactions')
