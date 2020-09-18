from prometheus_client.exposition import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client.multiprocess import MultiProcessCollector
from prometheus_client.registry import CollectorRegistry


def metrics_monoprocessing():
    registry = generate_latest()
    return registry, 200, {'Content-Type': CONTENT_TYPE_LATEST}


def metrics_multiprocessing():
    registry = CollectorRegistry()
    MultiProcessCollector(registry)
    registry = generate_latest(registry)
    return registry, 200, {'Content-Type': CONTENT_TYPE_LATEST}
