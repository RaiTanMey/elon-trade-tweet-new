#!/usr/bin/env python3
"""
Close all open positions via Simmer SDK
Jalankan sekali untuk tutup semua posisi Polymarket
"""

import os
import sys
import json
from datetime import datetime

try:
    from simmer_sdk import SimmerClient
except ImportError:
    print("❌ Error: pip install simmer-sdk")
    sys.exit(1)

def main():
    # Cek API key
    api_key
