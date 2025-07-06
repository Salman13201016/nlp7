from sqlalchemy import create_engine, text

try:
    engine = create_engine("mysql+pymysql://root:@localhost:3306/food_panda")

    with engine.connect() as connection:
        print("Connected to DB")

        # টেবিলগুলো দেখুন
        result = connection.execute(text("SHOW TABLES"))
        tables = result.fetchall()
        print("Tables in DB:")
        for table in tables:
            print(table[0])

        # ডাটা নিয়ে আসা (SELECT)
        query = text("SELECT * FROM categories LIMIT 5")
        result = connection.execute(query)
        rows = result.fetchall()
        print("\nCategories (upto 5 rows):")
        for row in rows:
            print(row)

except Exception as e:
    print("Error:", e)
