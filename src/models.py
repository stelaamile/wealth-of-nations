class GDPRegion:
    """
    A simple class representing a region's GDP per capita entry.

    Attributes:
        region_code (str)
        region_name (str)
        year (int)
        gdp_per_capita (float)
    """

    def __init__(self, region_code: str, region_name: str, year: int, gdp_per_capita: float):
        self.region_code = region_code
        self.region_name = region_name
        self.year = year
        self.gdp_per_capita = gdp_per_capita

    def is_high_income(self, threshold: float = 40000) -> bool:
        """
        Returns True if GDP per capita exceeds a given threshold.

        Args:
            threshold (float): Income threshold for classification.

        Returns:
            bool: True if high income.
        """
        return self.gdp_per_capita >= threshold

    def __repr__(self):
        return (f"GDPRegion(region='{self.region_name}', "
                f"year={self.year}, "
                f"gdp_per_capita={self.gdp_per_capita})")
