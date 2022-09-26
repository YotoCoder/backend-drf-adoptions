class Crypto:
    
    @staticmethod
    def encrip_email(email):
        pos = email.index("@")
        multiplier = len(email[1:pos - 1])*"*"
        user = email[:1] + multiplier + email[pos-1]
        domain = email[pos:(len(email))]
        total_email = user+domain
        
        return str(total_email)