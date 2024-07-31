import pandas as pd
import requests


df = pd.read_excel("database.xlsx")
sys_link = pd.read_csv("sysNo-link.csv")

def create_html_with_download_button(link, output_html_path):
    html_template = f"""
<!DOCTYPE html>
<html>
<head>
</head>
<body style="font-family: Poppins, Arial; font-size: 20px; color: #3e3e3e; background-color: #e4e4e4;">
    <div style="max-width: 80%; margin: 0 auto; background-color: #ffffff;">
        <div style="padding: 20px;">
            <div style="text-align: center; width: 100%; margin: 0 auto; padding-top: 20px;">
                <img src="https://github.com/SbusIdeas/Faisure-images/blob/main/faisure-logo.jpeg?raw=true" alt="Faisure" width="25%"><br>
                <h3>Payslip for July 2024</h3>
            </div>
            <hr style="border-color: #f02121">

            <div class="content">
            <p>Dear KZN Pensioner</p>

            <p>KZN Municipal Pension Fund payslips are now available electronically.</p>

            <p>This email contains a secure link to your payslip for July 2024, which you can download.</p>

            <p>We take the security of your information seriously. For this reason, your statement is encrypted with password protection.</p>

            <p>Once you click on the download button below, you will be asked for a password. To open and view your payslip, please use the first six digits of your identity number as your password. Do not enter any spaces or separators.</p>

            <p>Please note that this payslip is in PDF format and requires PDF reader software for it to be viewed.</p>

            <p>You can download your payslip by clicking on the link below.</p>

                <div style="text-align: center;">
                    <a href="{link}" style="text-decoration: none;">
                        <button style="padding: 5px; background-color: #6d95ac; color: #ffffff; border-radius: 13px; border: 1px solid #6d95ac; font-size: 20px;">Click Here To Download Your Payslip</button>
                    </a>
                </div>

                <p>Sincerely,</p>
                <p><b>Fairsure Fund Administration</p>

                <div style="width: 60%; margin: 0 0;">
                    <img src="https://github.com/SbusIdeas/Faisure-images/blob/main/faisure-banner.png?raw=true" alt="faisure banner" style="width: 100%; height: auto;">
                </div>
            </div>
        </div>

        <footer style="background-color: #f06126; font-size: 20px;">
            <div style="width: 50%; text-align: center; margin: 0 auto; padding: 10px 0;">
                <span style="color: #ffffff;">Fairsure Administration</span><br><br>
                <span style="color: #ffffff;">2nd Floor Building B</span><br>
                <span style="color: #ffffff;">Loftus Park Centre</span><br>
                <span style="color: #ffffff;">416 Kirkness Street</span><br>
                <span style="color: #ffffff;">Acardia</span><br>
                <span style="color: #ffffff;">Pretoria</span><br>
                <span style="color: #ffffff;">0002</span><br><br>
            </div>
        </footer>
    </div>
    </body>
    </html>
    """
    
    with open(output_html_path, 'w') as html_file:
        html_file.write(html_template)
    
    return html_template

# Post details
sender_email = "fairsurecomms@inter-net.co.za"
company_name = "Fairsure"
subject = "Fairsure Communications"

j = 0
for i in range(df.shape[0]):
    row = df.loc[i]
    sys_no = row["System No"]
    member_email = row["EMAIL ADDRESS"]
    link = sys_link[ sys_link["sysNo"] == sys_no]["link"].iloc[0]

    member_html_template = create_html_with_download_button(link, f"html_templates/{sys_no}.html")

    resp = requests.post(
        "https://api.brevo.com/v3/smtp/email", 
        headers={
            'accept': 'application/json',
            'api-key': '<api key>',
            'content-type': 'application/json'
        },
        json={
            "sender":{  
                "name":subject,
                "email": sender_email
            },
            "to":[
                {
                    "email": member_email.lower(),
                    "name": company_name
                }
            ],
            "subject":subject,
            "htmlContent":member_html_template
                }
        )

    j += 1
    
    if resp.status_code != 201:
        print(f"""
    code: {resp.status_code}
    system number: {sys_no}
    email: {member_email}
""")

print(j)



    


