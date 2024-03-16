class Page:
    def __init__(self,heading,body):
        self.heading = heading
        self.body = body
    def create_page(self):
        html = f"<h1>{self.heading}</h1> <p>{self.body}</p>"
        return html

class Contact(Page):
    def __init__(self,heading,body,email_id):
        self.heading = heading
        self.body = body
        self.email_id = email_id
    
    def create_contact_button(self):
        return f"<button>{self.email_id},Contact Now!</button>"

contact_page = Contact("Contact us","Please give us your feedback","rktaakash@gmail.com")
print(contact_page.create_contact_button())