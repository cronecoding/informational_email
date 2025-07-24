contacts = {
    "Raquel Wojnar, Communications Manager, Population Reference Bureau": "communications@prb.org",
    "Mike Tosh, Partner, State and Local Government, Guidehouse": "mtosh@guidehouse.com",
    "David Smith, Associate Director, Tech Solutions, Guidehouse": "dsmith@guidehouse.com",
    "Sue Bembers, GSA contractor POC, The Lewin Group": "sue.bembers@lewin.com",
    "FHI 360": "partneringwithus@fhi360.org",
    "DataKind": "partners@datakind.org",
    "Stefaan Verhulst, Co-Founder and Director of the Data Program, The GovLab": "stefaan@thegovlab.org",
    "The Center for Open Data Enterprise": "contact@odenterprise.org",
    "Annie Tastet, Media and Communications Specialist, Resources for the Future": "media@rff.org",
    "World Wildlife Fund": "wwfimpact@wwfus.org",
    "Ford Foundation": "pressline@fordfoundation.org"
}
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

I'm reaching out on behalf of Inkwell Global Report. We admire the work your organization is doing and would love to connect for brief chat. We are looking to gather information about your current priorities, what research needs you have, and how you are currently solving them.

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
    "Raquel Wojnar, Communications Manager, Population Reference Bureau": "communications@prb.org",
    "Mike Tosh, Partner, State and Local Government, Guidehouse": "mtosh@guidehouse.com",
    "David Smith, Associate Director, Tech Solutions, Guidehouse": "dsmith@guidehouse.com",
    "Sue Bembers, GSA contractor POC, The Lewin Group": "sue.bembers@lewin.com",
    "FHI 360": "partneringwithus@fhi360.org",
    "DataKind": "partners@datakind.org",
    "Stefaan Verhulst, Co-Founder and Director of the Data Program, The GovLab": "stefaan@thegovlab.org",
    "The Center for Open Data Enterprise": "contact@odenterprise.org",
    "Annie Tastet, Media and Communications Specialist, Resources for the Future": "media@rff.org",
    "World Wildlife Fund": "wwfimpact@wwfus.org",
    "Ford Foundation": "pressline@fordfoundation.org"
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
