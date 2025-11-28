class GroupClassifier:
    """
    Classify a region_name into one of several categories used in the project.

    Categories:
        - 'geographic'
        - 'income_group'
        - 'demographic_group'
        - 'other' (used for individual countries)

    In the main data-loading step (load_wb_data.py), we keep only entries
    classified as 'other', which correspond to country-level observations.
    These are later relabeled as 'country'.
    """

    def __init__(self):
        # Predefined group sets
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

    def classify(self, name: str) -> str:
        """Return the group type based on the region name."""
        if name in self.geographic_regions:
            return "geographic"
        if name in self.income_groups:
            return "income_group"
        if name in self.demographic_groups:
            return "demographic_group"
        return "other"  # this becomes 'country' after filtering
