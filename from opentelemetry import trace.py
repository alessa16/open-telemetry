from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

# Configure tracer provider with exporter
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(_name_)
tracer_provider = trace.get_tracer_provider()
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
tracer_provider.add_span_processor(span_processor)

# Start a span
with tracer.start_as_current_span("example_span"):
    print("Hello, OpenTelemetry!")