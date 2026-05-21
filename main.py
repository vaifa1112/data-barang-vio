from utils.extract import scrape_all_products
from utils.transform import transform_data
from utils.load import save_to_csv


def main():

    print("=" * 50)
    print("START ETL PIPELINE")
    print("=" * 50)

    raw_df = scrape_all_products()

    print(f"[INFO] Raw Data: {len(raw_df)}")

    clean_df = transform_data(raw_df)

    print(f"[INFO] Clean Data: {len(clean_df)}")

    save_to_csv(clean_df)

    print("=" * 50)
    print("ETL PIPELINE SUCCESS")
    print("=" * 50)


if __name__ == "__main__":
    main()