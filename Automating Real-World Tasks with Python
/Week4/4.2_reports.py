#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])

    info = "<br/>"
    for d in additional_info:
        info += "name: {}<br/>weight: {}<br/><br/>".format(
            d["name"], d["weight"])

    report_info = Paragraph(info, styles["BodyText"])
    report.build([report_title, report_info])
