from flask import Flask
from dotenv import load_dotenv
import controllers.users

## Olen käyttänyt tehhtävässä apuna tekoälyä

app = Flask(__name__)

app.add_url_rule('/api/users', view_func=controllers.users.get_all_users)

if __name__ == '__main__':
    load_dotenv()
    app.run()
