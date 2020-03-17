## Import libraries
import os
from typing import List
from requests import Response, post

## MailgunException
class MailgunException(Exception):
    def __int__(self, message: str):
        self.message = message

## Mailgun Class
class Mailgun:
    ## Class variables
    FROM_TITLE = 'Pricing Service'
    FROM_EMAIL = f'do-not-reply@sandbox40d22620718a4cac9946ecbc2b135a1b.mailgun.org'

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        """
        This method sends out an email to supplied email
        :param email: The email address to send the notification to - Default is my current email address
        :param subject: The subject of the email
        :param text: The message
        :param html: Any HTML that will markup the email message
        :return:
        """
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)

        if api_key is None:
            raise MailgunException('Failed to load Mailgun API key.')

        if domain is None:
            raise MailgunException('Failed to load Mailgun domain.')

        response = post(
            f'{domain}/messages',
            auth=('api', api_key),
            data={'from': f'{cls.FROM_TITLE} {cls.FROM_EMAIL}',
                  'to': email,
                  'subject': subject,
                  'text': text,
                  'html': html})

        if response.status_code != 200:
            print(response.status_code)
            raise MailgunException('An error occurred while sending e-mail.')

        return response