#!/usr/bin/env python3
"""
Close all open positions via Simmer SDK
Run sekali untuk tutup semua posisi
"""

import os
import sys
import json
from datetime import datetime

try:
    from simmer_sdk import SimmerClient
except ImportError:
    print("❌ Install: pip install simmer-sdk")
    sys.exit(1)

def main():
    api_key = os.environ.get("SIMMER_API_KEY")
    if not api_key:
        print("❌ SIMMER_API_KEY environment variable not set")
        sys.exit(1)

    client = SimmerClient(api_key=api_key
