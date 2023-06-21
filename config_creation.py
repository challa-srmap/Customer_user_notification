import configparser
def config_password(linkedin_password,email_password):
    config = configparser.ConfigParser()
    config.add_section('Passwords')
    config.set('Passwords', "linkedin_password", linkedin_password)
    config.set('Passwords', 'email_password', email_password)

    with open("config.ini", "w") as configfile:
        config.write(configfile)
