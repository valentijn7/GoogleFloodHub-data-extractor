# src/main.py

import sys
import extract


def main():
    print("BEWARE: as of November 2024, the API contains no data issued before July 2024\n")
    
    try:
        country, a, b = extract.validate_args(sys.argv)
        _, _, forecasts = extract.extract_country_data_for_time_delta("../key.txt",
                                                                      country,
                                                                      (a, b))
        extract.validate_forecasts(forecasts, (a, b), country)
    except Exception as exc:
        extract.handle_exception(exc)


if __name__ == '__main__':
    main()