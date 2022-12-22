import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # confirmation_num = event['queryStringParameters']['confirmation_num']
    # conf_table = boto3.resource('dynamodb').Table('book-history')
    # item = conf_table.get_item(Key={'confirmation_num': confirmation_num})['Item']
    # match_users = item['match_users']
    
    
    addr = event['queryStringParameters']['email_addr']
    subject, body = event['queryStringParameters']['subject'], event['queryStringParameters']['body']
    
    BODY_HTML = """<!DOCTYPE html>
      <html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
      <head>
      <title></title>
      <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
      <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
      <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
      <!--[if !mso]><!-->
      <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Shrikhand" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Cormorant+Garamond" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css"/>
      <link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css"/>
      <!--<![endif]-->
      <style>
      		* {{
      			box-sizing: border-box;
      		}}
      
      		body {{
      			margin: 0;
      			padding: 0;
      		}}
      
      		a[x-apple-data-detectors] {{
      			color: inherit !important;
      			text-decoration: inherit !important;
      		}}
      
      		#MessageViewBody a {{
      			color: inherit;
      			text-decoration: none;
      		}}
      
      		p {{
      			line-height: inherit
      		}}
      
      		.desktop_hide,
      		.desktop_hide table {{
      			mso-hide: all;
      			display: none;
      			max-height: 0px;
      			overflow: hidden;
      		}}
      
      		@media (max-width:670px) {{
      
      			.desktop_hide table.icons-inner,
      			.social_block.desktop_hide .social-table {{
      				display: inline-block !important;
      			}}
      
      			.icons-inner {{
      				text-align: center;
      			}}
      
      			.icons-inner td {{
      				margin: 0 auto;
      			}}
      
      			.fullMobileWidth,
      			.row-content {{
      				width: 100% !important;
      			}}
      
      			.mobile_hide {{
      				display: none;
      			}}
      
      			.stack .column {{
      				width: 100%;
      				display: block;
      			}}
      
      			.mobile_hide {{
      				min-height: 0;
      				max-height: 0;
      				max-width: 0;
      				overflow: hidden;
      				font-size: 0px;
      			}}
      
      			.desktop_hide,
      			.desktop_hide table {{
      				display: table !important;
      				max-height: none !important;
      			}}
      		}}
      	</style>
      </head>
      <body style="margin: 0; background-color: #50d250; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
      <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #50d250;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #50d250; background-image: url('https://travel-with-me-public.s3.amazonaws.com/images/waves_header.png'); background-position: top center; background-repeat: repeat;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="text-align:center;width:100%;padding-top:80px;">
      <h2 style="margin: 0; color: #d14f90; direction: ltr; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; font-size: 24px; font-weight: 400; letter-spacing: 1px; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder"></span></h2>
      </td>
      </tr>
      </table>
      <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="text-align:center;width:100%;padding-bottom:30px;">
      <h1 style="margin: 0; color: #d14f90; direction: ltr; font-family: 'Shrikhand', Impact, Charcoal, sans-serif; font-size: 36px; font-weight: 400; letter-spacing: 1px; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder" style="color: #000000;">TravelwithMe</span></h1>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e9e1bb; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="image_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-bottom:50px;">
      <div align="center" class="alignment" style="line-height:10px"><img alt="Image" src="https://media3.giphy.com/media/J2mRBHugc9MtceuzTR/giphy.gif?cid=20eb4e9dbmy3qn0e9wvn5debt2lfs4vlhq12gl1vwo8wfor6&rid=giphy.gif&ct=g" style="display: block; height: auto; border: 0; width: 293px; max-width: 100%;" title="Image" width="293"/></div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fceedf; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="text-align:center;width:100%;">
      <h3 style="margin: 0; color: #4c4c4c; direction: ltr; font-family: 'Shrikhand', Impact, Charcoal, sans-serif; font-size: 30px; font-weight: 400; letter-spacing: 1px; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">Incoming Friend<strong>!</strong></h3>
      </td>
      </tr>
      </table>
      <table border="0" cellpadding="0" cellspacing="0" class="divider_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:15px;padding-left:5px;padding-right:5px;padding-top:5px;">
      <div align="center" class="alignment">
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="50%">
      <tr>
      <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px dotted #4C4C4C;"><span> </span></td>
      </tr>
      </table>
      </div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fcdfdf; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-right: 15px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
      <table border="0" cellpadding="0" cellspacing="0" class="image_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;">
      <div align="center" class="alignment" style="line-height:10px"><img alt="Image" class="fullMobileWidth" src="https://media3.giphy.com/media/VduFvPwm3gfGO8duNN/giphy.gif?cid=20eb4e9dtdk0lfv12019w4mgoeej88z4wpsjnj8ovnuj2f79&rid=giphy.gif&ct=g" style="display: block; height: auto; border: 0; width: 248px; max-width: 100%;" title="Image" width="248"/></div>
      </td>
      </tr>
      </table>
      </td>
      <td class="column column-2" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 15px; padding-right: 15px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
      <table border="0" cellpadding="0" cellspacing="0" class="text_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:15px;">
      <div style="font-family: sans-serif">
      <div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #4c4c4c; line-height: 1.2; font-family: Bitter, Georgia, Times, Times New Roman, serif;">
        <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"><span style="font-size:16px;">This is an email sent from someone registered on TravelwithMe that is willing to be your travel partner.</span></p>
        <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"> </p>
        <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"><span style="font-size:16px;">You are receiving this email because our system found that you two have the most matching MBTI types and shared travel duration.</span></p>
        <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"> </p>
        <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"><span style="font-size:16px;">Here's the message this traveler left:</span></p>
      </div>
      </div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fcdfdf; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="text_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:40px;">
      <div style="font-family: 'Times New Roman', Georgia, serif">
      <div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #4c4c4c; line-height: 1.2; font-family: Bitter, Georgia, Times, Times New Roman, serif;">
      <p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px; letter-spacing: normal;"><span style="font-size:20px;">{rec_body}</span></p>
      </div>
      </div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="divider_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;">
      <div align="center" class="alignment">
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 5px solid #419C41;"><span> </span></td>
      </tr>
      </table>
      </div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-7" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-image: url('https://travel-with-me-public.s3.amazonaws.com/images/Ondas_footer.png'); background-position: top center; background-repeat: repeat;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="social_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:70px;text-align:center;">
      <div align="center" class="alignment">
      <table border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;" width="208px">
      </table>
      </div>
      </td>
      </tr>
      </table>
      <table border="0" cellpadding="0" cellspacing="0" class="text_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
      <div style="font-family: sans-serif">
      <div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #9a56b2; line-height: 1.2; font-family: Bitter, Georgia, Times, Times New Roman, serif;">
      <p style="margin: 0; text-align: center; font-size: 16px; mso-line-height-alt: 19.2px;"><span style="font-size:16px;">Copyright © 2022 TravelwithMe</span></p>
      </div>
      </div>
      </td>
      </tr>
      </table>
      <table border="0" cellpadding="0" cellspacing="0" class="text_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
      <tr>
      <td class="pad" style="padding-bottom:30px;padding-left:20px;padding-right:20px;">
      <div style="font-family: sans-serif">
      <div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #9a56b2; line-height: 1.2; font-family: Bitter, Georgia, Times, Times New Roman, serif;">
      <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:13px;"><a href="https://www.example.com" rel="noopener" style="text-decoration: underline; color: #d14f90;" target="_blank">ABOUT US</a> | <a href="https://www.example.com" rel="noopener" style="text-decoration: underline; color: #d14f90;" target="_blank">UNSUBSCRIBE</a></span></p>
      </div>
      </div>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-8" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tbody>
      <tr>
      <td>
      <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
      <tbody>
      <tr>
      <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
      <table border="0" cellpadding="0" cellspacing="0" class="icons_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="pad" style="vertical-align: middle; padding-bottom: 5px; padding-top: 5px; color: #9d9d9d; font-family: inherit; font-size: 15px; text-align: center;">
      <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
      <tr>
      <td class="alignment" style="vertical-align: middle; text-align: center;">
      <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
      <!--[if !vml]><!-->
      <table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
      <!--<![endif]-->
      </table>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table>
      </td>
      </tr>
      </tbody>
      </table><!-- End -->
      </body>
      </html>
    """.format(rec_body=body)

    SUBJECT = subject
    BODY_TEXT = ("Amazon SES \r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
    ses = boto3.client('ses',region_name='us-east-1')
    try:
        response = ses.send_email(
            Destination={'ToAddresses': [addr]},
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': SUBJECT,
                },
            },
            Source="ruichen.yang@nyu.edu",
            ConfigurationSetName="ConfigSet",
        )
    except ClientError as e:
        response = str(e.response['Error']['Message'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent!')
    }
