import smtplib
from string import Template

signature= 'Thanks and regards \n'\
           'Satish'


class MailSender:
    def __init__(self, server, from_address, to_addresses, cc_addresses, subject, body):
        self.server = server
        self.from_address = from_address
        self.to_addresses = to_addresses
        self.cc_addresses = cc_addresses
        self.subject = subject
        self.body = body
        self.body = self._create_msg()

    def _create_msg(self):
        with open('./mailer/mail.template') as f:
            data = f.read()
        template = Template(data)
        return template.substitute(from_address=self.from_address, to_addresses=', '.join(self.to_addresses),
                                   cc_addresses=', '.join(self.cc_addresses), subject=self.subject,
                                   body='\n'.join([self.body, signature]))

    def send_mail(self):
        server = smtplib.SMTP(self.server)
        print self.body
        server.sendmail(self.from_address, self.to_addresses, self.body)
        server.quit()