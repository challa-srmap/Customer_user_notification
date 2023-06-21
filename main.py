import decryption
import scraping_linkedin
import sending_email
import time
import pandas as pd

import datetime


def scrape_and_send():
    # LinkedIn credentials
    linkedin_email = "caditya02@gmail.com"
    linkedin_password = decryption.get_linkedinpassword()

    # Email credentials
    email_sender = "adityakoundinya_challa@srmap.edu.in"
    email_password = decryption.get_emailpassword()

    recipients_list = ["caditya02@gmail.com", "adityachalla73@gmail.com"]

    unread = scraping_linkedin.scrape_linkedin(linkedin_email, linkedin_password)
    df = pd.read_csv("user_info.csv")
    temp = df.loc[df['Email']==linkedin_email]
    prev_un_mess = temp['Unread messages'][0]
    prev_un_not = temp['Unread notifications'][0]
    current_time = datetime.datetime.now()
    # email message
    message = f"You have the following Unread in LinkedIn\nUnread Messages: {unread[0]}\n" \
                  f"LinkedIn Unread Notifications: {unread[1]}\nPlease read them. You previously had {prev_un_mess} unread messages and {prev_un_not} unread notfications."
    subject = "LinkedIn Unread Messages and Notifications"
    sending_email.send(email_sender,email_password, recipients_list,message,subject)
    line = [[linkedin_email,current_time,unread[0],unread[1],prev_un_mess,prev_un_not]]
    df_new_data = pd.DataFrame(line, columns = ['Email','Date and time','Unread messages', 'Unread notifications','previous messages','previous notifications'])
    print(df_new_data)
    df = df._append(df_new_data,ignore_index=True)
    df.to_csv('user_info.csv')


while True:
    scrape_and_send()
    time.sleep(60*3*3)
