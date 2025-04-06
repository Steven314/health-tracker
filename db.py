import duckdb
import datetime

class DailyRecord:
    def __init__(self, date: datetime.date, caffeine: int, weight: float, stress: int, sleep_rhr: int, sleep_duration: float, sleep_battery: int, running: bool, weight_lifting: bool):
        self.date           = date
        self.caffeine       = caffeine
        self.weight         = weight
        self.stress         = stress
        self.sleep_rhr      = sleep_rhr
        self.sleep_duration = sleep_duration
        self.sleep_battery  = sleep_battery
        self.running        = running
        self.weight_lifting = weight_lifting

    def __str__(self):
        return f"Date: {self.date}"

class Database:
    def __init__(self, location: str):
        self.location = location
        self.dbcon = duckdb.connect(
            database = location,
            read_only = False
        )

        self.dbcon.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_records (
                date DATE,
                caffeine INT,
                weight FLOAT,
                stress INT,
                sleep_rhr INT,
                sleep_duration FLOAT,
                sleep_battery INT,
                running BOOL,
                weight_lifting BOOL
            )
            """
        )

    def __del__(self):
        self.dbcon.close()

    def add_record(self, record: DailyRecord):
        self.dbcon.execute(
            """
            INSERT INTO daily_records
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.date,
                record.caffeine,
                record.weight,
                record.stress,
                record.sleep_rhr,
                record.sleep_duration,
                record.sleep_battery,
                record.running,
                record.weight_lifting
            )
        )

    def replace_record(self, record: DailyRecord):
        self.dbcon.execute(
            """
            UPDATE daily_records
            SET caffeine = ?, weight = ?, stress = ?, sleep_rhr = ?, sleep_duration = ?, sleep_battery = ?, running = ?, weight_lifting = ?
            WHERE date = ?
            """,
            (
                record.caffeine,
                record.weight,
                record.stress,
                record.sleep_rhr,
                record.sleep_duration,
                record.sleep_battery,
                record.running,
                record.weight_lifting,
                record.date
            )
        )

