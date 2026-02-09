#!/usr/bin/env python3
"""
Kidney Stone Detection Application - Entry Point
================================================

Run this script to start the Flask web application.

Usage:
    python run.py [--host HOST] [--port PORT] [--debug]

Examples:
    python run.py                    # Run on localhost:5000
    python run.py --port 8080        # Run on localhost:8080
    python run.py --host 0.0.0.0     # Run on all interfaces
"""

import os
import sys
import argparse

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app.main import app, init_detector


def main():
    parser = argparse.ArgumentParser(description='Kidney Stone Detection Web Application')
    parser.add_argument('--host', default='0.0.0.0', help='Host to run on (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=5000, help='Port to run on (default: 5000)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    # Initialize the detector
    model_path = os.path.join(os.path.dirname(__file__), 'src', 'app', 'models', 'best.pt')
    if os.path.exists(model_path):
        init_detector(model_path)
    else:
        print(f"Warning: Model not found at {model_path}")
        print("Please ensure best.pt is in src/app/models/")
    
    print(f"""
╔════════════════════════════════════════════════════════════════╗
║       🏥 Kidney Stone Detection System                         ║
║       Powered by YOLOv8 with Multi-Level Explainability        ║
╠════════════════════════════════════════════════════════════════╣
║   🌐 Local:   http://localhost:{args.port:<5}                        ║
║   🌐 Network: http://{args.host}:{args.port:<5}                        ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host=args.host, port=args.port, debug=args.debug, threaded=True)


if __name__ == '__main__':
    main()
