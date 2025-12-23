#!/usr/bin/env python
"""Entry point to run the DocRAG Flask web application."""

import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.flask_app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Starting DocRAG Flask app on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
