#!/usr/bin/env python
"""Entry point to run the DocRAG FastAPI application."""

import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Starting DocRAG FastAPI on http://localhost:{port}")
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=False)
