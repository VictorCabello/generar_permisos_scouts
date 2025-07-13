import argparse
from generar_permisos_scouts.excel_handler import get_data_from_excel
from generar_permisos_scouts.file_handler import write_file


def main():
    parser = argparse.ArgumentParser(
            description="Generate documents based on" +
                        "excel files and a template")

    parser.add_argument(
            '--scouts',
            type=str,
            default='scouts.xlsx',
            help='Path to Excel file with scouts ' +
                 'information (default: scouts.xlsx)')

    parser.add_argument(
            '--activities',
            type=str,
            default='activities.xlsx',
            help='Path to Excel file with activities ' +
                 'information (default: activities.xlsx)')

    parser.add_argument(
            '--template',
            type=str,
            default='template.pdf',
            help='Path to Excel file with activities ' +
                 'information (default: activities.xlsx)')

    args = parser.parse_args()

    data_template_list = get_data_from_excel(
        scouts_path=args.scouts,
        activity_path=args.activities
    )

    write_file(
        data_template_list=data_template_list,
        template_path=args.template
    )
