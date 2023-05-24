dl_sensors_drop = "DROP TABLE IF EXISTS sensors;"
dl_metrics_drop = "DROP TABLE IF EXISTS metrics;"
dl_samples_drop = "DROP TABLE IF EXISTS samples;"
dl_cycles_drop = "DROP TABLE IF EXISTS cycles;"

dl_sensors_create = """
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY,
        type TEXT,
        number INTEGER,
        sampling_rate INTEGER
    );
"""

dl_metrics_create = """
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY,
        name TEXT,
        unit TEXT
    );
"""

dl_cycles_create = """
    CREATE TABLE IF NOT EXISTS cycles (
        id INTEGER PRIMARY KEY,
        cycle_number INTEGER,
        start_date TEXT,
        start_time INTEGER
    );
"""

dl_samples_create = """
    CREATE TABLE IF NOT EXISTS samples (
        sensor_id INTEGER,
        cycle_id INTEGER,
        sample_number INTEGER,
        metric_id INTEGER,
        value NUMERIC
    );
"""

dl_sensors_insert = """
    INSERT INTO sensors (type, number, sampling_rate) VALUES (%s, %s, %s);
"""

dl_metrics_insert = """
    INSERT INTO metrics (name, unit) VALUES (%s, %s);
"""

dl_cycles_insert = """
    INSERT INTO CYCLES (cycle_number, start_date, start_time) VALUES (%s, %s, %s);
"""

dl_samples_insert = """
    INSERT INTO samples (sensor_id, cycle_id, sample_number, metric_id, value) VALUES (%s, %s, %s, %s);
"""

dl_drop_table_queries = [dl_sensors_drop, dl_metrics_drop, dl_cycles_drop, dl_samples_drop]
dl_create_table_queries = [dl_sensors_create, dl_metrics_create, dl_cycles_create, dl_samples_create]