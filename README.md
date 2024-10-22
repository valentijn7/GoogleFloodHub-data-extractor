# GoogleFloodHub-data-extractor

This repository contains a script to query the [Google FloodHub](https://sites.research.google/floods/l/0/0/3) (beta) API. As of October 2024, the API is focused on real-time forecasts and grants access to data issued at the earliest in July of 2024. Later, this is expected to be complemented with historical data spanning several decades.

When encountering a bug (or when the API itself is updated), please contact [toldenburg@rodekruis.nl](mailto:toldenburg@rodekruis.nl).

## Set-up

1. Clone the repository
    ```sh
    git clone [repo URL]
    cd GoogleFloodHub-data-extractor
    ```
2. (Optional) Install the required dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Add a .txt with your API key
    ```
    echo "[YOUR_KEY]" > key.txt
    ```

When not in possession of a valid key, contact [toldenburg@rodekruis.nl](mailto:toldenburg@rodekruis.nl) or, perhaps preferably, [pphung@redcross.nl](mailto:pphung@redcross.nl).

## Manual

To run, navigate to `src/` and execute `main.py` with arguments:
- country: the country name of interest;
- starting date: the first issue date of interest; and
- ending date: the final issue date of interest.

The data is subsequently stored in the `data/` folder.

Example usage:

```
python3 main.py Mali 01-10-2024 07-10-2024
```


## Dependencies

See `requirements.txt`. Note: only very basic functionality is used.


## License

This project is licensed under the MIT License.
