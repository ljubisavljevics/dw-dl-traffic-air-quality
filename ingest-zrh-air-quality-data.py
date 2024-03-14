import pandas as pd
from datetime import datetime, timedelta


def ingest_data():
    """
    Load the air pollution measurement data from the URL specified and filter
    the DataFrame to include only the data from yesterday. The data is loaded
    into a DataFrame, and then the date of yesterday is calculated. Subsequently,
    the rows where the 'Datum' column equals yesterday's date are filtered. Finally,
    yesterday's data is saved to a CSV file named 'zrh-YYYY-MM-DD.csv', where
    'YYYY-MM-DD' represents yesterday's date.

    Returns:
    None

    (docstring generated by ChatGPT 3.5)
    """

    # load the growing file
    df = pd.read_csv(
        'https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download/ugz_ogd_air_h1_2024.csv',
        parse_dates=['Datum'])

    # Calculate the date of yesterday
    one_day_before_today = datetime.now().date() - timedelta(days=1)

    # Filter rows where 'Datum' equals to yesterday
    filtered_df = df[df['Datum'].dt.date == one_day_before_today]

    # save yesterday's data to file
    filtered_df.to_csv(f'data/zrh-{one_day_before_today}.csv')


if __name__ == "__main__":
    ingest_data()
