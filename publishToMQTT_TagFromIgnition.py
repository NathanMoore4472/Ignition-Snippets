# MAKE SURE RPC CLIENT IS ENABLED (IN SETS) AND THE CREDIETIALS ARE SET IN THE BROKER SETTINGS

from org.eclipse.tahu.message import SparkplugBPayloadEncoder
from org.eclipse.tahu.message.model import SparkplugBPayload, Metric
from java.util import Date, ArrayList
import base64

# Create payload
payload = SparkplugBPayload()

# Try to initialize the metrics list manually
payload.setMetrics(ArrayList())

# Set timestamp
payload.setTimestamp(Date())

# Create metric
metric = Metric()
metric.setName("LDS01/LeakSensorFaultRow")
metric.setValue(True)
metric.setDataType(MetricDataType.Boolean)

# Add to payload
payload.addMetric(metric)

# Encode and publish
encoder = SparkplugBPayloadEncoder()
byte_array = encoder.getBytes(payload, True)

system.cirruslink.transmission.publish('mqttserver', 'spBv1.0/SIN01/DCMD/00325/ROWA', byte_array, 1, 0)


# PURE JSON VERSION, NO PROTOBUF ENCODING


import json

# Create JSON payload
payload = {
    'timestamp': system.date.now().getTime(),
    'metrics': [
        {
            'name': 'LDS01/LeakSensorFaultRow',
            'timestamp': system.date.now().getTime(),
            'dataType': 'Boolean',
            'value': False
        }
    ]
}

# Convert to JSON string and then to bytes
json_string = json.dumps(payload)
byte_array = json_string.encode('utf-8')

# Publish to a custom topic (NOT a Sparkplug B topic)
system.cirruslink.transmission.publish(
    'mqttserver', 
    'spBv1.0/SIN01/DCMD/00325/ROWA',  # Use your own topic structure
    byte_array, 
    1,  # QoS
    0   # Retained
)

# SIMPLIFED VERSION FOR PROTOBUF
from org.eclipse.tahu.message import SparkplugBPayloadEncoder
from org.eclipse.tahu.message.model import SparkplugBPayload, Metric, MetricDataType
from java.util import ArrayList

payload = SparkplugBPayload()
payload.setMetrics(ArrayList())

# Use MetricBuilder
metric = Metric.MetricBuilder("LDS01/LeakSensorFaultRow", MetricDataType.Boolean, True).createMetric()
payload.addMetric(metric)

byte_array = SparkplugBPayloadEncoder().getBytes(payload, True)
system.cirruslink.transmission.publish('mqttserver', 'spBv1.0/SIN01/DCMD/00325/ROWA', byte_array, 1, 0)

