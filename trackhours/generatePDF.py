from reportlab.lib import colors

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus import TableStyle


def extend_item(query):
    doc = SimpleDocTemplate("table_grids.pdf", pagesize=letter)
    story = []
    te_dhenat_e_mija = [['Name', 'Start', 'End', 'delta', ]]

    for item in query:
        element = [item.day, item.start_time,
                   item.end_time, item.delta_time,
                   ]
        tblStyle = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ('VALIGN', (0, 0), (0, -1), 'MIDDLE'), ])


        data_col_width = [114, 180, 180, 55,]

        te_dhenat_e_mija.append(element)
        data = te_dhenat_e_mija

        tbl = Table(data, colWidths=data_col_width)
        tbl.setStyle(tblStyle)

        story.append(tbl)


        doc.build(story)
