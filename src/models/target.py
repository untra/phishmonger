from basemodel import BaseModel
class Target(BaseModel):
    def requiredFields(self):
        super(Target, self).fields() + ['fname', 'lname', 'email', 'group', 'tel']

    def fields(self):
        print super(Target, self).fields()
        super(Target, self).fields().update({
            'fname' : (is_string, cannot_be_empty, cannot_be_none),
            'lname' : (is_string, cannot_be_empty, cannot_be_none),
            'email' : (is_string, cannot_be_empty, cannot_be_none),
            'group' : (is_string, cannot_be_empty, cannot_be_none),
            'tel' : (is_string, ),
        })
