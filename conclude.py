import os
import json
import pdb
import time
import re
import requests

total_time = 0
total_output_length = 0
total_success = 0
with open("gsm8k_out.jsonl", "r") as f:
    num = total_success = 0
    for line in f:
        num += 1
        entry = json.loads(line)
        total_time += entry["time"]
        total_output_length += entry["output_length"]
        total_success += entry["result"]
    
    average_time = total_time / num
    average_output_length = total_output_length / num
    average_success = total_success / num
    print(f"Average time: {average_time}")
    print(f"Average output length: {average_output_length}")
    print(f"Average success: {average_success * 100}%")
        
