import pandas as pd
import datetime
from generar_permisos_scouts.util import Name, TemplateData


def get_data_from_excel(
        scouts_path: str, activity_path: str) -> list[TemplateData]:
    """
    Reads scout and activity data from Excel files and generates a
    list of TemplateData objects.

    Args:
        scouts_path (str): Path to the Excel file containing scout information.
        activity_path (str): Path to the Excel file containing activity
                             information.

    Returns:
        list[TemplateData]: List of TemplateData objects for each scout and
                            activity combination.
    """
    scouts = pd.read_excel(scouts_path)
    activities = pd.read_excel(activity_path)
    template_data_list = []

    for _, s in scouts.iterrows():
        for _, a in activities.iterrows():
            activity: str = f"{a['Actividad']}"
            scouter: str = f"{a['Responsible']}"
            activity_date: datetime.datetime = a['Fecha']
            location: str = f"{a['Lugar']}"
            full_name: str = f"{s['Nombre']}".split()
            last_name: tuple = (full_name[-2], full_name[-1])
            first_name: str = ' '.join(full_name[:-2])
            name: Name = Name(first_name=first_name, last_name=last_name)
            birth_date: datetime.datetime = datetime.datetime.strptime(
                    s['Fecha de nacimiento'], "%d/%m/%Y")
            data = TemplateData(
                    authorization_date=datetime.datetime.now(),
                    scout_name=name,
                    birth_date=birth_date,
                    activity_name=activity,
                    activity_date=activity_date.strftime('%d-%m-%Y'),
                    activity_location=location,
                    scouter_name=scouter
            )

            template_data_list.append(data)

    return template_data_list
