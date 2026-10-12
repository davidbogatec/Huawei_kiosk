import cloudscraper
from flask import Flask, Response, jsonify

app = Flask(__name__)
KIOSK_URL = "https://uni002eu5.fusionsolar.huawei.com/rest/pvms/web/kiosk/v1/station-kiosk/file?kk=yhw9diq4M41czjCh9yd8ehp4BLi7QbHA"

@app.route('/kiosk', methods=['GET'])
def get_kiosk_data():
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(KIOSK_URL, timeout=15)
        if response.status_code == 200:
            return Response(response.text, mimetype='application/json')
        else:
            return jsonify({"error": f"Huawei returned {response.status_code}"}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500
