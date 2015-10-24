import requests
import time

class message:
    def __init__(self, to, subject, html):
        self.to = to
        self.subject = subject
        self.html = html

    def send(self):
        return requests.post(
            "https://api.mailgun.net/v3/sandboxbbe9ae6f185c4349978fde92ee4a1f42.mailgun.org/messages",
            auth=("api", "key-826d0e14eed794810322d8b6dd02e8cc"),
            data={"from": "Mailgun Sandbox <phish@phishy.com>",
                  "to": self.to,
                  "subject": self.subject,
                  "html": self.html
        })

# def main():
#     to = ["Alex <antsankov@gmail.com>"]
#     subject = time.ctime()
#     html = "<html><a href='http://www.google.com/' target='_blank'>Our phihsing path goes here!</a></html>"
#     message_test = message(to,subject,html)
#     message_test.send()
#
# if __name__ == "__main__":
#     main()
