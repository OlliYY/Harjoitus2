from flask import jsonify

from repositories.repository_factory import users_repository_factory


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.
def get_all_users():
    repo = users_repository_factory()
    users = repo.get_all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
        })
    return jsonify(users_json)