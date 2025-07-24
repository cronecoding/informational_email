import smtplib
from email.message import EmailMessage
from email.utils import make_msgid

# Your Workspace email
EMAIL_ADDRESS = "inkwellglobalreport@inkwell.report"
EMAIL_PASSWORD = "rnhwclvcxttdathd"  # Paste the 16-char app password

# Email content
subject = "Informational Interview Request from Inkwell Global Report"
body = """
Dear [Name or Team],

I'm reaching out on behalf of Inkwell Global Report. We admire the work your organization is doing and would love to connect for a brief conversation to learn more about your current priorities, what analysis needs you have, and how you are currently solving them.

Would someone on your team be available for a short call or email exchange in the coming weeks? If I have reached out to the wrong person, I'd be grateful if you could point me in the right direction.

Warm regards,  
Rebecca Kimble, MD, MPH  
Founder & Research Lead 
bkimble@inkwell.report

Inkwell Global Report  
https://www.inkwell.report


"""

# List of contacts
contacts = {
    #Content producers
    "Tiffani Bova": "info@tiffanibova.com",
    "Dr. Jen Gunter": "drjengunter@gmail.com",
    "Politics Girl (YouTube)": "contact@politicsgirl.com",
    "SecondThought": "contact@secondthought.com",
    
    # Think Tanks
    "RAND Corporation": "jobs@rand.org",
    "Brookings Institution": "HROffice@brookings.edu",
    "Urban Institute": "events@urban.org",
    "NORC at the University of Chicago": "cotton-david@norc.org",
    "NORC at the University of Chicago": "ahn-roy@norc.org"
    "RTI International": "communications@rti.org",
    "Mathematica": "info@mathematica-mpr.com",
    "KFF (Kaiser Family Foundation)": "contact@kff.org",
    "Center for American Progress": "info@americanprogress.org",
    "Pew Research Center": "info@pewresearch.org",
    "Raquel Wojnar, Communications Manager, Population Reference Bureau": "communications@prb.org",

    # Government / Private Sector Firms
    "Booz Allen Hamilton": "helpdesk@bah.com",
    "ICF International": "info@icf.com",
    "Deloitte (Public Sector)": "contact@deloitte.com",
    "McKinsey & Company": "inquiries@mckinsey.com",
    "Abt Associates": "info@abtassoc.com",
    "Mike Tosh, Partner, State and Local Government, Guidehouse": "mtosh@guidehouse.com",
    "David Smith, Associate Director, Tech Solutions, Guidehouse": "dsmith@guidehouse.com",
    "Sue Bembers, GSA contractor POC, The Lewin Group": "sue.bembers@lewin.com",
    "Westat": "info@westat.com",
    "Manatt Health": "info@manatt.com",
    "Palladium": "info@thepalladiumgroup.com",

    # Global Health / NGOs
    "PATH": "media@path.org",
    "FHI 360": "partneringwithus@fhi360.org",
    "Vital Strategies": "info@vitalstrategies.org",
    "Management Sciences for Health (MSH)": "communications@msh.org",
    "Chemonics International": "info@chemonics.com",
    "Jhpiego": "info@jhpiego.org",
    "PSI (Population Services International)": "info@psi.org",
    "Clinton Health Access Initiative (CHAI)": "info@clintonhealthaccess.org",
    "Results for Development (R4D)": "info@r4d.org",
    "EGPAF (Elizabeth Glaser Pediatric AIDS Foundation)": "info@pedaids.org",

    # Data-Focused Nonprofits
    "DataKind": "partners@datakind.org",
    "Stefaan Verhulst, Co-Founder and Director of the Data Program, The GovLab": "stefaan@thegovlab.org",
    "Open Data Watch": "info@opendatawatch.com",
    "Development Gateway": "info@developmentgateway.org",
    "Global Health Council": "info@globalhealth.org",
    "The Center for Open Data Enterprise": "contact@odenterprise.org",
    "Center for Data Innovation": "info@datainnovation.org",
    "Code for America": "info@codeforamerica.org",
    "Human Rights Data Analysis Group (HRDAG)": "info@hrdag.org",

    # Environmental Policy
    "Environmental Defense Fund": "media@edf.org",
    "Annie Tastet, Media and Communications Specialist, Resources for the Future": "media@rff.org",
    "Earth Innovation Institute": "info@earthinnovation.org",
    "World Wildlife Fund": "wwfimpact@wwfus.org",
    "Conservation International": "info@conservation.org",

    # Philanthropic Foundations
    "Robert Wood Johnson Foundation": "media@rwjf.org",
    "Rockefeller Foundation": "media@rockfound.org",
    "Gates Foundation": "media@gatesfoundation.org",
    "Ford Foundation": "pressline@fordfoundation.org"
    "Wellcome Trust": "info@wellcome.org"
}

def send_emails():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for org, email in contacts.items():
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg.set_content(body.replace("[Name or Team]", org))
            msg["Reply-To"] = EMAIL_ADDRESS
            msg["Message-ID"] = make_msgid()
            msg["X-Mailer"] = "Python SMTP Script"

            try:
                smtp.send_message(msg)
                print(f"✅ Email sent to {org} at {email}")
            except Exception as e:
                print(f"❌ Failed to send to {org} ({email}): {e}")

if __name__ == "__main__":
    send_emails()