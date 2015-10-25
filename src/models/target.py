from basemodel import BaseModel
class Target(BaseModel):
    def requiredFields():
        super + ['fname', 'lname', 'email', 'group']

    def fields():
        super.update({
            'fname' : (is_string, ),
            'lname' : (is_string, ),
            'email' : (is_string, ),
            'group' : (is_string, ),
            'tel' : (is_string, ),
        })
