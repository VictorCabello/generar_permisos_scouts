import os
from generar_permisos_scouts.pdf_handler import gen_pdf
from generar_permisos_scouts.util import TemplateData
from tqdm import tqdm


def write_file(data_template_list: list[TemplateData],
               template_path: str) -> None:
    """
    Generates PDF files for each scout's activity permission using a template.

    Args:
        data_template_list (list[TemplateData]): List of data objects
                                                 containing scout and
                                                 activity info.
        template_path (str): Path to the PDF template file.

    Creates:
        PDF files in the 'output' directory, named as
        '{activity}_{scout_name}.pdf'.
    """
    os.makedirs('output', exist_ok=True)

    for data in tqdm(data_template_list):
        name = str(data.scout_name).replace(" ", "_")
        activity = data.activity_name.replace(" ", "_")
        output = gen_pdf(template_path, data)
        with open(f"output/{activity}_{name}.pdf", "wb") as output_pdf:
            output.write(output_pdf)
