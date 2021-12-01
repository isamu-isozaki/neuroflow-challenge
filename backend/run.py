"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: Runs the app
Created:  2021-12-01T16:18:09.893Z
Modified: !date!
Modified By: Isamu Isozaki
"""

from neuroflow.app import create_app
from waitress import serve
import sys
app = create_app()

if __name__ == "__main__":
    try:
        if app.config['ENV'] == 'development':
            app.run(debug=True, host='0.0.0.0', port=app.config['PORT'])

        elif app.config['ENV'] == 'production':
            # app = Talisman(app)
            serve(
                app,
                host='0.0.0.0',
                port=app.config['PORT'],
                max_request_body_size=10737418240
            )
    except Exception as e:
        logging.info(e)
