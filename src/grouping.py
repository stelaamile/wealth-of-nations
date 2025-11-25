class GroupClassifier:
    """
    A small helper class that knows how to classify a region_name
    into a group_type (geographic, income_group, demographic_group, other).
    """

    def __init__(self):
        # sets of known names for each group
        self.geographic_regions = {
            "Africa Eastern and Southern",
            "Africa Western and Central",
            "East Asia & Pacific",
            "East Asia & Pacific (excluding high income)",
            "Europe & Central Asia",
            "Latin America & Caribbean",
            "Middle East & North Africa",
            "North America",
            "South Asia",
            "Sub-Saharan Africa",
            "Caribbean small states",
            "Euro area",
            "European Union",
        }

        self.income_groups = {
            "High income",
            "Upper middle income",
            "Lower middle income",
            "Low income",
        }

        self.demographic_groups = {
            "Early-demographic dividend",
            "Late-demographic dividend",
            "Pre-demographic dividend",
            "Post-demographic dividend",
        }

    def classify(self, name):
        """
        Return the group type for a given region_name
        as a simple string.
        """
        if name in self.geographic_regions:
            return "geographic"
        if name in self.income_groups:
            return "income_group"
        if name in self.demographic_groups:
            return "demographic_group"
        return "other"
