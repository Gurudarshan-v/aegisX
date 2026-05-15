import random

class RiskEngine:
    def calculate_risk(self, cvss, exposure, exploitability):
        score = (
            (cvss * 0.5) +
            (exposure * 0.3) +
            (exploitability * 0.2)
        )

        if score >= 8:
            return "Critical"

        elif score >= 6:
            return "High"

        elif score >= 4:
            return "Medium"

        return "Low"