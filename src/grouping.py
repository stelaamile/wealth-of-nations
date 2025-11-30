class GroupClassifier:
    """
    Classify a region_name into one of several categories used in the project.
    ...
    """

    def __init__(self):
        # Predefined group sets
        self.geographic_regions = {
            # --- CRITICAL ADDITIONS ---
            "Arab World", # MISSING AGGREGATE
            "World", # MISSING AGGREGATE
            "Least Developed Countries", # MISSING AGGREGATE
            "Fragile and conflict affected situations", # MISSING AGGREGATE
            # --- END CRITICAL ADDITIONS ---
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
            # --- CRITICAL ADDITIONS ---
            "IDA countries", # MISSING AGGREGATE (International Development Association)
            "IBRD countries", # MISSING AGGREGATE (International Bank for Reconstruction and Development)
            # --- END CRITICAL ADDITIONS ---
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
