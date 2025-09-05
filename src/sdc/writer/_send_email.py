from email.mime.multipart import MIMEMultipart

from kasperl.writer import SendEmail as KSendEmail


class SendEmail(KSendEmail):

    def _attach_item(self, message: MIMEMultipart, item) -> bool:
        """
        Attaches the item to the message.

        :param message: the message to attach to
        :type message: MIMEMultipart
        :param item: the item to attach
        :return: whether data type has handled
        :rtype: bool
        """
        return False
