#!/usr/bin/env python3
"""Send DCMD directly from Python to test write-back"""

import sys

sys.path.insert(0, "sparkplugb_env/")

import paho.mqtt.client as mqtt
import sparkplug_b_pb2
import time


def send_dcmd(control_tag_value=True):
    """Send DCMD message directly"""
    print(f"📤 Sending DCMD: Control Tag = {control_tag_value}")

    # Create client
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    except:
        client = mqtt.Client()

    client.username_pw_set("ignition", "EIeng123!!3030")
    client.connect("172.30.230.43", 1883, 60)

    # Create DCMD payload
    payload = sparkplug_b_pb2.Payload()
    # DCMD messages don't have sequence numbers

    metric = payload.metrics.add()
    metric.name = "LDS01/LeakSensorFaultRow"
    metric.datatype = 11  # Boolean
    metric.boolean_value = control_tag_value

    # Publish DCMD
    topic = "spBv1.0/SIN01/DCMD/00325/ROWA"
    binary_data = payload.SerializeToString()

    client.publish(topic, binary_data)

    print(f"✅ DCMD sent!")
    print(f"   Topic: {topic}")
    print(f"   Payload: {binary_data.hex()}")
    print(f"   Length: {len(binary_data)} bytes")

    client.disconnect()


def main():
    print("🚀 Direct DCMD Sender")
    print("=" * 30)

    print("💡 Make sure your coordinated_sparkplug.py is running!")
    print()

    choice = input("Send Control Tag = True or False? (t/f): ").strip().lower()
    value = choice in ["t", "true", "1"]

    send_dcmd(value)

    print("\n🔍 Check your coordinated script console for write-back response!")


if __name__ == "__main__":
    main()
