from basemodel import BaseModel
class Campaign(BaseModel):
    def requiredFields(self):
        super(Campaign, self).fields() + ['date_started', 'date_sent', 'date_concluded', 'targets', 'sent', 'opened', 'clicked', 'posted', 'responses']

    def fields(self):
        print super(Campaign, self).fields()
        super(Campaign, self).fields().update({

        })
