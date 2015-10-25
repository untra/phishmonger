from basemodel import BaseModel
class Response(BaseModel):
    AWAITING = 0
    SENT = 1
    OPENED = 2
    CLICKED = 3
    POSTED = 4

    def requiredFields(self):
        super(Response, self).fields() + ['target_id', 'campaign_id', 'status']

    def fields(self):
        print super(Response, self).fields()
        super(Response, self).fields().update({
        })
