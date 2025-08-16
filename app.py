import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from shopify_insights import get_brand_context, is_shopify_site

app = Flask(__name__)
CORS(app)

# logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
log = logging.getLogger("brand-insights")

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "bad request"}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "not found"}), 404

@app.errorhandler(500)
def internal(e):
    return jsonify({"error": "internal server error"}), 500

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Shopify Brand Insights API is live", "health": "ok"}), 200

@app.route("/api/brand-context", methods=["POST"])
def brand_context():
    try:
        data = request.get_json(silent=True) or {}
        website_url = data.get("website_url") or request.args.get("website_url")

        if not website_url:
            return jsonify({"error": "website_url is required"}), 400

        log.info(f"Requested site: {website_url}")

        ok, reason = is_shopify_site(website_url)
        if not ok:
            log.warning(f"Shopify check failed: {reason}")
            return jsonify({"error": f"website not reachable or not Shopify-like: {reason}"}), 401

        context = get_brand_context(website_url)
        return jsonify(context), 200

    except Exception as e:
        log.exception("Unhandled error")
        return jsonify({"error": "internal server error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)