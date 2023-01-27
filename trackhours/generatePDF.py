import datetime
#
from collections import OrderedDict
from pathlib import Path

from reportlab.lib import colors
# EOB Class
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus import TableStyle


def extend_item(query):
    doc = SimpleDocTemplate("table_grids.pdf", pagesize=letter)
    story = []
    te_dhenat_e_mija = [['Name', 'Start', 'End', 'delta', ]]

    for item in query:
        print(item.start_time)

        # get_img_path = Path(item['image'].replace("http://127.0.0.1:8000", "."))
        get_img_path = './media/logo.png'
        img = Image(get_img_path, 115, 134)

        element = [item.day, item.start_time,
                   item.end_time, item.delta_time,
                   ]

        tblStyle = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ('VALIGN', (0, 0), (0, -1), 'MIDDLE'), ])
        headTblStyle = TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
            ('RIGHTPADDING', (-1, 0), (-1, -1), 1),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONT', (0, 1), (0, 1), 'Helvetica', 16)
        ])

        # dataHead = [[logo_img, f'{fist_name} {last_name}\n'
        #                        f'{company_namme}\n'
        #                        f'{city}\n'
        #                        f'{province}\n'
        #                        f'{street}\n'
        #                        f'{apartment}\n'
        #                        f'{zipcode}\n'
        #                        f'{phone}\n'
        #                        f'{email}'], ['Paymet Summary', f'Order Date: {date}'], [' ', ' ']]
        # data_total = [[' '], [f'Total:  {paid_amount}£']]
        # data_total_style = TableStyle([('FONT', (0, 1), (0, 1), 'Helvetica', 16),
        #                                ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        #                                ('RIGHTPADDING', (0, 1), (0, 1), 1)])
        # data_total_table_col_width = [579]
        # colWidth = [290, 290]
        data_col_width = [114, 180, 180, 55,]
        # headTable = Table(dataHead, colWidths=colWidth)
        # headTable.setStyle(headTblStyle)
        # totalTable = Table(data_total, colWidths=data_total_table_col_width)
        # totalTable.setStyle(data_total_style)
        # story.append(headTable)
        te_dhenat_e_mija.append(element)
        data = te_dhenat_e_mija
        #
        tbl = Table(data, colWidths=data_col_width)
        tbl.setStyle(tblStyle)

        story.append(tbl)
        # story.append(totalTable)

        doc.build(story)
