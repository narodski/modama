import logging
from flask_babel import lazy_gettext
from flask_appbuilder.models.filters import FilterRelation
from flask_appbuilder.models.sqla.filters import get_field_setup_query

log = logging.getLogger(__name__)


class FilterRelationOverlap(FilterRelation):
    name = "Filter view where relation views have items in common."

    def apply(self, query, value):
        query, field = get_field_setup_query(query, self.model,
                                             self.column_name)
        # rel_obj = self.datamodel.get_related_obj(self.column_name, value)
        return not set(query.all()).isdisjoint(set(value))


class FilterM2MRelationOverlapFunction(FilterRelation):
    name = "Filter view where relation views have items in common."

    def apply(self, query, func):
        """
        We assume that the column name is a dotted set of attributes.
        The last one in that set is a many-to-many relation, while the ones
        before (if any) are many-to-one relations, so can be traversed easily.

        Func should return the same relationship as the query. Overlap will be
        tested between the two relationships.
        """
        obj = self.model
        # Traverse the attributes and join all attributes except the last one
        attrs = self.column_name.split('.')
        for attr in attrs[:-1]:
            query = query.join(attr)
            obj = getattr(obj, attr).mapper.class_

        # Get the many-to-many property and the secondary table
        prop = getattr(obj, attrs[-1]).property
        related_table = prop.mapper.local_table
        secondary = prop.secondary
        for fk in secondary.foreign_keys:
            if fk.column.table == related_table:
                secondary_col = fk.parent
                related_col = fk.column
                break

        # Join the secondary to the query
        query = query.join(secondary)

        fkids = [getattr(v, related_col.name) for v in func()]
        log.debug("Testing fkids: {}".format(fkids))

        # Filter the query on the relationship between it and the value
        filtered = query.filter(secondary_col.in_(fkids))
        log.debug("Query: {}".format(filtered))

        return filtered
