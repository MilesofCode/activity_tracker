from sqlalchemy import MetaData, Table, Column, Integer,  Float, create_engine, Date, Insert
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
metadata = MetaData()


def list_table():
    holder = []
    metadata.reflect(engine)
    for tables in metadata.tables.keys():
        holder.append(tables)
    return holder


def return_table(table_name):
    metadata.reflect(engine)
    return metadata.tables[table_name]


def create_table(table_name="Miles"):
    personal_table = Table(
            table_name,
            metadata,
            Column("id", Integer, primary_key=True),
            Column("Date", Date),
            Column("Calories", Integer),
            Column("Push-ups", Integer),
            Column("Sit-ups", Integer),
            Column("Pull-ups", Integer),
            Column("Miles ran", Float),
        )
    metadata.create_all(engine)


# Insert data in table
def insert_data(data, table_name="Miles"):
    print(type(data))
    print(data)
    with engine.connect() as conn:
        result = conn.execute(Insert(return_table(table_name)),
                              [
                                  # {"Date": dt.datetime.strptime(data["date"], "%Y/%m/%d"),
                                  {"Date": data["date"],
                                   "Calories": data["calories"],
                                   "Push-ups": data["push_ups"],
                                   "Sit-ups": data["sit_ups"],
                                   "Pull-ups": data["pull_ups"],
                                   "Miles ran": data["miles_ran"]}
                              ])
        conn.commit()

