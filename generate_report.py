from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

# Constants for colors
HEADING_COLOR = '#0066CC'
HIGHLIGHT_COLOR = '#FF3333'
BACKGROUND_COLOR = colors.whitesmoke

# Create our PDF
def generate_report():
    pdf_filename = "HabitTracking_Report.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    # Custom style for headings
    heading_style = ParagraphStyle(name='HeadingStyle', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor(HEADING_COLOR))

    # Content list
    content = []

    # Cover Page
    content.append(Paragraph('Habit Tracking Web Application Report', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Student Name: Zeumo yemele brandon cyrian', styles['Normal']))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Teacher Name: Mr. Tchoua', styles['Normal']))
    content.append(Spacer(1, 12))
    content.append(Paragraph('GitHub Link: <a href="https://github.com/antoinemben12/HabitTracking.git">https://github.com/antoinemben12/HabitTracking.git</a>', styles['Normal']))
    content.append(PageBreak())

    # Table of Contents
    content.append(Paragraph('Table of Contents', heading_style))
    content.append(Spacer(1, 12))
    toc = ["1. Project Overview", "2. Problem Statement", "3. Database Schema Documentation", "4. System Architecture", "5. Features and Functionality", "6. UI/UX Description", "7. Installation Guide", "8. Code Highlights", "9. Conclusion"]
    for item in toc:
        content.append(Paragraph(item, styles['Normal']))
    content.append(PageBreak())

    # Project Overview
    content.append(Paragraph('1. Project Overview', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('This report outlines the Habit Tracking Web Application designed to assist users in managing their habits effectively.', styles['Normal']))
    content.append(PageBreak())

    # Problem Statement
    content.append(Paragraph('2. Problem Statement', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The application addresses the need for users to track their habits in a user-friendly platform.', styles['Normal']))
    content.append(PageBreak())

    # Database Schema Documentation
    content.append(Paragraph('3. Database Schema Documentation', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The database consists of 4 main tables:', styles['Normal']))
    content.append(Spacer(1, 12))
    db_tables = {
        'users': 'Stores user information including id, name, and email.',
        'habits': 'Tracks different habits with user associations and status.',
        'habit_logs': 'Logs instances of habit completion for a user.',
        'reminders': 'Manages reminders set by users for their habits.'
    }

    for table, description in db_tables.items():
        content.append(Paragraph(f' - {table}: {description}', styles['Normal']))
    content.append(PageBreak())

    # System Architecture
    content.append(Paragraph('4. System Architecture', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The system utilizes a client-server architecture with a structured database.', styles['Normal']))
    content.append(PageBreak())

    # Features and Functionality
    content.append(Paragraph('5. Features and Functionality', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Main features include user registration, habit tracking, notifications, and reporting.', styles['Normal']))
    content.append(PageBreak())

    # UI/UX Description
    content.append(Paragraph('6. UI/UX Description', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The user interface is designed to be intuitive and responsive.', styles['Normal']))
    content.append(PageBreak())

    # Installation Guide
    content.append(Paragraph('7. Installation Guide', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('To install the application, follow these steps: ...', styles['Normal']))
    content.append(PageBreak())

    # Code Highlights
    content.append(Paragraph('8. Code Highlights', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('Key snippets of the application code, demonstrating features.', styles['Normal']))
    content.append(PageBreak())

    # Conclusion
    content.append(Paragraph('9. Conclusion', heading_style))
    content.append(Spacer(1, 12))
    content.append(Paragraph('The Habit Tracking Web Application is poised to enhance user productivity significantly.', styles['Normal']))

    # Build the PDF
    document.build(content)

# Run the report generation
if __name__ == '__main__':
    generate_report()