from regipy.registry import RegistryHive
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Load the NTUSER.DAT registry hive
hive = RegistryHive("NTUSER.DAT")
suspicious_data = []

# Access the registry key
key = hive.get_key(r'\SOFTWARE\Microsoft\Windows\CurrentVersion\Run')
if key:
    for value in key.iter_values():
        suspicious_data.append(
            f"Key: {key.name}, Value: {value.name}, Data: {value.value}"
        )
    print(suspicious_data)

# Function to generate PDF report
def generate_pdf_report(suspicious_data, llm_analysis, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter
    y_pos = height - 50

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y_pos, "Windows Registry Analysis Report")
    y_pos -= 50

    # Suspicious Data Section
    c.setFont("Helvetica", 12)
    c.drawString(100, y_pos, "Suspicious Registry Entries:")
    y_pos -= 20

    # Draw each suspicious registry entry
    for entry in suspicious_data:
        # Start a new line at the current y position
        text = c.beginText(100, y_pos)
        text.setFont("Helvetica", 12)
        text.setTextOrigin(100, y_pos)
        text.textLines(entry)

        # Draw the text and adjust the y position
        c.drawText(text)
        y_pos -= 20  # Move down by 20 for each new line

        # Check if the y position is too low for another line, then start a new page
        if y_pos < 100:
            c.showPage()
            y_pos = height - 50  # Reset y position for new page

    # Manual Analysis Section
    c.setFont("Helvetica", 12)
    c.drawString(100, y_pos, "Manual Analysis:")
    y_pos -= 20

    text = c.beginText(100, y_pos)
    text.setFont("Helvetica", 12)
    text.textLines(llm_analysis.strip())
    c.drawText(text)

    c.save()

# Manual analysis of suspicious data
llm_analysis = """
The following registry entries were found to be potentially suspicious:

1. ExampleProgram: This program is located in a non-standard directory and may indicate an unwanted application.
2. SuspiciousApp: The path points to a known malicious folder, suggesting it might be part of malware.

Further investigation and dynamic analysis are recommended to confirm the behavior of these executables.
"""

# Generate the PDF report
generate_pdf_report(suspicious_data, llm_analysis, "Registry_Report.pdf")
