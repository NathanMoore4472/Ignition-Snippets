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
