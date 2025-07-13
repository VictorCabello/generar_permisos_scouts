import datetime


class Name:
    """
    Represents a person's name.

    Attributes:
        first_name (str): The first name of the person.
        last_name (tuple): A tuple containing the last
                           names (e.g., paternal and maternal).
    """

    def __init__(self, first_name: str, last_name: tuple):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """
        Returns a string representation of the name in the format:
        'first_name last_name[0] last_name[1]'
        """
        return f"{self.first_name} {self.last_name[0]} {self.last_name[1]}"


class TemplateData:
    """
    Stores data required for generating a scout authorization template.

    Attributes:
        authorization_date (datetime.datetime): Date of authorization.
        scout_name (Name): Name of the scout.
        birth_date (datetime.datetime): Birth date of the scout.
        activity_name (str): Name of the activity.
        activity_date (str): Date of the activity.
        activity_location (str): Location of the activity.
        scouter_name (str): Name of the scouter.
    """

    def __init__(self,
                 authorization_date: datetime.datetime,
                 scout_name: Name,
                 birth_date: datetime.datetime,
                 activity_name: str,
                 activity_date: str,
                 activity_location: str,
                 scouter_name: str,
                 ):
        self.authorization_date = authorization_date
        self.scout_name = scout_name
        self.birth_date = birth_date
        self.activity_name = activity_name
        self.activity_date = activity_date
        self.activity_location = activity_location
        self.scouter_name = scouter_name
