###-----------------------------GET-USER-BY-EMAIL-------------------------###
def get_user_by_email(username):
    return User.query.filter(User.username == username).first()