from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# PDF Report Generator

def generate_report(filename):
    # Create a PDF document
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    # Styles for the document
    styles = getSampleStyleSheet()
    blue_heading = ParagraphStyle(name='BlueHeading', fontSize=18, spaceAfter=12, textColor=colors.HexColor('#0066CC'))
    red_accent = ParagraphStyle(name='RedAccent', fontSize=12, spaceAfter=6, textColor=colors.HexColor('#FF3333'))
    white_background = colors.HexColor('#FFFFFF')

    # Document content
    content = []
    content.append(Paragraph('Cover Page', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Habit Tracking Web Application Report', styles['Normal']))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Student: Zeumo yemele brandon cyrian', styles['Normal']))
    content.append(Paragraph('Teacher: Mr. Tchoua', styles['Normal']))
    content.append(Spacer(1, 24))

    content.append(Paragraph('Table of Contents', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('1. Executive Summary
2. Project Overview
3. Problem Statement
4. Proposed Solution
5. Database Architecture
6. System Architecture
7. Features and Functionality
8. UI/UX Design
9. Installation Guide
10. Code Implementation
11. Testing and Deployment
12. Conclusion and Future Enhancements', styles['Normal']))
    content.append(Spacer(1, 24))

    # Executive Summary
    content.append(Paragraph('Executive Summary', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('This report outlines...', styles['Normal']))
    content.append(Spacer(1, 24))

    # Project Overview
    content.append(Paragraph('Project Overview', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The Habit Tracking Web Application...', styles['Normal']))
    content.append(Spacer(1, 24))

    # Problem Statement
    content.append(Paragraph('Problem Statement', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Many individuals struggle... ', styles['Normal']))
    content.append(Spacer(1, 24))

    # Proposed Solution
    content.append(Paragraph('Proposed Solution', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Our solution is to develop...', styles['Normal']))
    content.append(Spacer(1, 24))

    ## Database Architecture (4 pages)
    for i in range(4):
        content.append(Paragraph('Database Architecture - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Detailed explanation of the database architecture...', styles['Normal']))
        content.append(Spacer(1, 24))

    ## System Architecture (3 pages)
    for i in range(3):
        content.append(Paragraph('System Architecture - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Overview of the system architecture...', styles['Normal']))
        content.append(Spacer(1, 24))

    ## Features and Functionality (3 pages)
    for i in range(3):
        content.append(Paragraph('Features and Functionality - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Description of key features...', styles['Normal']))
        content.append(Spacer(1, 24))

    ## UI/UX Design (3 pages)
    for i in range(3):
        content.append(Paragraph('UI/UX Design - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Explanation of UI/UX design...', styles['Normal']))
        content.append(Spacer(1, 24))

    ## Installation Guide (2 pages)
    for i in range(2):
        content.append(Paragraph('Installation Guide - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Steps to install...', styles['Normal']))
        content.append(Spacer(1, 24))

    ## Code Implementation (2 pages)
    for i in range(2):
        content.append(Paragraph('Code Implementation - Page {0}'.format(i + 1), blue_heading))
        content.append(Spacer(1, 12))
        content.append(Paragraph('Overview of the code implementation...', styles['Normal']))
        content.append(Spacer(1, 24))

    # Testing and Deployment
    content.append(Paragraph('Testing and Deployment', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Details of testing conducted...', styles['Normal']))
    content.append(Spacer(1, 24))

    # Conclusion and Future Enhancements
    content.append(Paragraph('Conclusion and Future Enhancements', blue_heading))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Final thoughts and potential future work...', styles['Normal']))

    # Build the PDF
    pdf.build(content)

# Create the report
generate_report('Habit_Tracking_Report.pdf')