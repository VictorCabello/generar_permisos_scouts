from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from generar_permisos_scouts.util import Name, TemplateData
import datetime
import io


class Handler:
    """
    Handles the creation and modification of PDF overlays for scout
    authorization forms.
    """

    def __init__(self):
        """
        Initializes a PDF canvas for drawing overlay content.
        """
        self.packet = io.BytesIO()
        self.can = canvas.Canvas(self.packet, pagesize=letter)

    def add_authorization(self, date: datetime.datetime):
        """
        Draws the authorization date on the PDF canvas.

        Args:
            date (datetime.datetime): The date of authorization.
        """
        can = self.can
        day: int = date.day
        month: int = date.month
        year: int = date.year
        day_as_str: str = f"{day:02d}"
        month_as_str: str = f"{month:02d}"
        year_as_str: str = f"{year}"

        # print day
        can.drawString(300, 655, day_as_str[0])
        can.drawString(330, 655, day_as_str[1])

        # print month
        can.drawString(360, 655, month_as_str[0])
        can.drawString(390, 655, month_as_str[1])

        # print year
        can.drawString(430, 655, year_as_str[0])
        can.drawString(460, 655, year_as_str[1])
        can.drawString(490, 655, year_as_str[2])
        can.drawString(520, 655, year_as_str[3])

    def add_scout_name(self, scout: Name):
        """
        Draws the scout's first name and last names on the PDF canvas.

        Args:
            scout (Name): The scout's name object.
        """

        # print First Name
        self.can.drawString(80, 575, scout.first_name)

        # print First last name
        self.can.drawString(260, 575, scout.last_name[0])
        self.can.drawString(400, 575, scout.last_name[1])

    def add_location(self, activity_location: str):
        """
        Draws the activity location on the PDF canvas.

        Args:
            activity_location (str): The location of the activity.
        """
        self.can.drawString(80, 405, activity_location)

    def add_activity_date(self, activity_date: str):
        """
        Draws the activity date on the PDF canvas.

        Args:
            activity_date (str): The date of the activity.
        """
        self.can.drawString(140, 390, activity_date)

    def add_scouter(self, scouter_name: str):
        """
        Draws the scouter's name on the PDF canvas.

        Args:
            scouter_name (str): The name of the responsible scouter.
        """
        self.can.drawString(225, 355, scouter_name)

    def add_birth_date(self, date: datetime.datetime):
        """
        Draws the scout's birth date on the PDF canvas.

        Args:
            date (datetime.datetime): The birth date of the scout.
        """
        can = self.can
        day: int = date.day
        month: int = date.month
        year: int = date.year
        day_as_str: str = f"{day:02d}"
        month_as_str: str = f"{month:02d}"
        year_as_str: str = f"{year}"

        # print day
        can.drawString(300, 505, day_as_str[0])
        can.drawString(330, 505, day_as_str[1])

        # print month
        can.drawString(360, 505, month_as_str[0])
        can.drawString(390, 505, month_as_str[1])

        # print year
        can.drawString(430, 505, year_as_str[0])
        can.drawString(460, 505, year_as_str[1])
        can.drawString(490, 505, year_as_str[2])
        can.drawString(520, 505, year_as_str[3])

    def get_pdf(self) -> PdfReader:
        """
        Finalizes the canvas and returns a PdfReader object of the overlay.

        Returns:
            PdfReader: The PDF overlay with drawn content.
        """
        self.can.save()
        self.packet.seek(0)
        return PdfReader(self.packet)


def gen_pdf(template_path: str, data: TemplateData) -> PdfWriter:
    """
    Generates a filled PDF by overlaying scout and activity data onto a
    template.

    Args:
        template_path (str): Path to the PDF template file.
        data (TemplateData): Data to fill into the PDF.

    Returns:
        PdfWriter: The completed PDF writer object.
    """
    existing_pdf = PdfReader(template_path)
    handler = Handler()

    handler.add_authorization(data.authorization_date)
    handler.add_scout_name(data.scout_name)
    handler.add_birth_date(data.birth_date)
    handler.add_location(data.activity_location)
    handler.add_activity_date(data.activity_date)
    handler.add_scouter(data.scouter_name)

    new_pdf = handler.get_pdf()
    output = PdfWriter()

    for page_num in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[page_num]
        if page_num == 0:
            page.merge_page(new_pdf.pages[0])
        output.add_page(page)
    return output
