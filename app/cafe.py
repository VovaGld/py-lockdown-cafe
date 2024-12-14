import datetime

from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        no_exception = True
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                no_exception = False
                raise OutdatedVaccineError("OutdatedVaccineError")
        else:
            no_exception = False
            raise NotVaccinatedError("NotVaccinatedError")

        if not visitor["wearing_a_mask"]:
            no_exception = False
            raise NotWearingMaskError("NotWearingMaskError")

        if no_exception:
            return f"Welcome to {self.name}"
