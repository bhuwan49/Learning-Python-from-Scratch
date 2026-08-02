import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
# import sys
# import os

# (Optional) External module with ticker list – not used by default
# parent_dir = os.path.dirname(os.getcwd())
# if parent_dir not in sys.path:
#     sys.path.append(parent_dir)
# try:
#     import tickers as ti
# except ImportError:
#     print("Module 'tickers' not found; using GitHub source.")
#     ti = None

# =============================================================================
# 1. FETCH S&P 500 CONSTITUENTS FROM GITHUB (NO SCRAPING, NO API KEY)
# =============================================================================
url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv"
try:
    sp500 = pd.read_csv(url)
    tickers = sp500['Symbol'].tolist()
    # Replace '.' with '-' for yfinance compatibility (e.g., BRK.B -> BRK-B)
    tickers = [ticker.replace('.', '-') for ticker in tickers]
    print(f"✅ Loaded {len(tickers)} tickers from GitHub.")
except Exception as e:
    print(f"❌ Error fetching S&P 500 list from GitHub: {e}")
    sys.exit(1)

# (Fallback) If you prefer Wikipedia with a proper User‑Agent, uncomment the block below
# and comment the GitHub block above.
#
# url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
# headers = {'User-Agent': 'Mozilla/5.0 ...'}
# response = requests.get(url, headers=headers, timeout=10)
# sp500_table = pd.read_html(response.text)[0]
# tickers = sp500_table['Symbol'].tolist()
# tickers = [t.replace('.', '-') for t in tickers]

# =============================================================================
# 2. DOWNLOAD PRICE DATA
# =============================================================================
num_of_years = 1
start = dt.date.today() - dt.timedelta(days=int(365.25 * num_of_years))
end = dt.date.today()

# For testing, limit to first 100 tickers to avoid long downloads.
# Remove this line to fetch all ~500 stocks.
tickers_subset = tickers[:35]

print(f"Downloading data for {len(tickers_subset)} tickers...")
dataset = yf.download(
    tickers_subset,
    start=start,
    end=end,
    auto_adjust=True,
    progress=False
)["Close"]

# Drop columns that are entirely NaN
dataset = dataset.dropna(axis=1, how='all')

# Calculate log returns
stocks_returns = np.log(dataset / dataset.shift(1)).dropna()

# =============================================================================
# 3. CORRELATION MATRIX
# =============================================================================
corr_matrix = stocks_returns.corr()
print("\nCorrelation Matrix (head):\n", corr_matrix.head())

# =============================================================================
# 4. HEATMAP VISUALIZATION
# =============================================================================
def visualize_correlation_matrix(df_corr):
    data = df_corr.values
    plt.rcParams["figure.figsize"] = (15, 10)
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)

    ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_xticklabels(df_corr.columns, rotation=90)
    ax.set_yticklabels(df_corr.index)

    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()

visualize_correlation_matrix(corr_matrix)

# =============================================================================
# 5. TOP ABSOLUTE CORRELATIONS
# =============================================================================
def get_redundant_pairs(df):
    pairs_to_drop = set()
    for i in range(df.shape[1]):
        for j in range(i + 1, df.shape[1]):   # avoids diagonal & duplicates
            pairs_to_drop.add((df.columns[i], df.columns[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=25):
    au_corr = df.abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

print("\nTop Absolute Correlations")
# top absolute correlations except self-correlations (diagonal)

print(get_top_abs_correlations(corr_matrix, n=25))




#####------------------------------------DESCRIPTION-------------------------------------######

"""
Here is a simple, step‑by‑step explanation of what this code does, from start to finish,
in plain English.

------------------Overall Goal---------------------------

This program analyzes 500 of the biggest US companies (S&P 500) 
to find out which pairs of stocks move up and down together most strongly. 
It helps answer questions like: “If Apple goes up, does Microsoft usually go up too?”

---------------------------------------------------------------
---------------------------------------------------------------


-----------------------------Group 1: The Toolbox (Imports)----------------

python

import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import sys
import os
These lines load up all the helper tools the program needs:

datetime → to handle dates (today, last year).

numpy & pandas → to do math and organise data into tables.

matplotlib → to draw charts and heatmaps.

yfinance → to download stock prices from Yahoo Finance.

sys & os → to manage file paths (not heavily used here).

-------------------------------------------------------------------------
-------------------------------------------------------------------------


--------------------------Group 2: Getting the Guest List (Tickers)--------------------

python

url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv"
sp500 = pd.read_csv(url)
tickers = sp500['Symbol'].tolist()
tickers = [ticker.replace('.', '-') for ticker in tickers]
The program goes to a reliable online CSV file (hosted on GitHub) that contains the official list of S&P 500 companies.

It reads that file and pulls out the stock symbols (e.g., AAPL, MSFT).

Why the replace? Yahoo Finance uses a dash (-) instead of a dot (.). So BRK.B becomes BRK-B, so Yahoo can recognise it.

Group 3: Setting the Time Frame
python
num_of_years = 1
start = dt.date.today() - dt.timedelta(days=int(365.25 * num_of_years))
end = dt.date.today()
It decides to look back exactly 1 year from today.

start = today minus 365 days.
end = today.

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------



-----------------------Group 4: Downloading the Prices (Speed Limit)---------------


python

tickers_subset = tickers[:100]
dataset = yf.download(tickers_subset, start=start, end=end, auto_adjust=True, progress=False)["Close"]
Because downloading 500 stocks all at once can be slow, the code only takes the first 100 (you can remove this limit later).

It asks Yahoo Finance for the daily closing prices of these 100 stocks over the past year.

auto_adjust=True makes sure the prices are adjusted for stock splits and dividends, so they are accurate for comparisons.

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------


--------------------Group 5: Cleaning and Calculating Daily Moves (Returns)----------------
python

dataset = dataset.dropna(axis=1, how='all')
stocks_returns = np.log(dataset / dataset.shift(1)).dropna()
Cleaning: If any stock has no data at all for the whole year, it is removed.

Calculating Returns: We don't care about the actual dollar price (e.g., $100 vs $200). We care about percentage change each day.
This line calculates the daily percentage return (using a mathematical trick called "log returns") for every stock.
Example: If a stock went from $100 to $101, the return is +1%.

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------


--------------Group 6: The Correlation Table (The Main Measure)-----------------------



python

corr_matrix = stocks_returns.corr()
This creates a giant table (100 rows × 100 columns).

Each cell contains a number between -1 and +1:

+1 → the two stocks move perfectly in the same direction every single day.

0 → no relationship at all; they move randomly compared to each other.

-1 → they move in exactly opposite directions.

It prints the top-left corner of this table so you can see a preview.

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------


---------------Group 7: Drawing the Heatmap (Visualising the Table)-------------------

python

def visualize_correlation_matrix(df_corr):
    # ... (draws a colourful grid)
visualize_correlation_matrix(corr_matrix)
Numbers are hard to read, so the program draws a colourful heatmap.

Green means positive correlation (move together).
Red means negative correlation (move opposite).
The darker the colour, the stronger the relationship.

This helps you instantly spot which stocks are "close friends" or "enemies" just by looking at the colours.

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

----------------------Group 8: Finding the Top "Best Friend" Pairs--------------------

python

def get_redundant_pairs(df): ...
def get_top_abs_correlations(df, n=25): ...
print(get_top_abs_correlations(corr_matrix, n=25))
The correlation table contains duplicates:
Correlation(Apple, Microsoft) is the same as Correlation(Microsoft, Apple). Also, a stock correlated with itself (diagonal) is always 1, which is useless.

First function (get_redundant_pairs): It removes these duplicate and self-pairs to clean up the list.

Second function (get_top_abs_correlations): It sorts all the remaining pairs by how strong the relationship is (ignoring whether it's positive or negative, just looking at the absolute number) and picks the top 25 strongest pairs.

Finally, it prints that shortlist. This is the most valuable output – it tells you exactly which two stocks have moved most similarly (or most oppositely) over the last year.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------


Summary (In One Sentence)
This program automatically downloads the latest S&P 500 list, fetches their stock prices for the past year, calculates how closely each pair of stocks moves together, shows you a colourful heatmap, and finally prints the top 25 most tightly linked stock pairs.


 
"""
