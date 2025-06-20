#!/usr/bin/env python3
"""
AI Engineer Portfolio - Entry Point
Professional portfolio showcasing AI engineering expertise and projects.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the main application
from app.main import setup_portfolio

if __name__ in {"__main__", "__mp_main__"}:
    # Get configuration from environment
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    reload = os.getenv("RELOAD", "false").lower() == "true"
    
    # Setup and run the portfolio
    setup_portfolio()
    
    # Import NiceGUI after setup
    from nicegui import ui
    
    # Run the application
    ui.run(
        host=host,
        port=port,
        reload=reload,
        title="AI Engineer Portfolio",
        favicon="🤖",
        dark=None,  # Let user choose theme
        show=False  # Don't auto-open browser in production
    )