import os

from update_utils.update_markets import update_markets
from update_utils.update_goldsky import update_goldsky
from update_utils.process_live import process_live

if __name__ == "__main__":
    print("Updating markets")
    update_markets()
    print("Updating goldsky")
    update_goldsky()
    if os.getenv("SKIP_PROCESS_LIVE", "").strip() in {"1", "true", "TRUE", "yes", "YES"}:
        print("Skipping live processing (SKIP_PROCESS_LIVE=1)")
    else:
        print("Processing live")
        process_live()
