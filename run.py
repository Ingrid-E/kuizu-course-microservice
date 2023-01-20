from app import create_app
import os
from flask_cors import CORS

app = create_app()
CORS(app)

if __name__ == '__main__':
    port = os.getenv('PORT', default=3001)
    app.run(host="0.0.0.0", port=port)
