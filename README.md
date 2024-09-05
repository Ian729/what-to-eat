# Restaurant Picker with Gaode Map API

This Python script uses the Gaode (Amap) API to find nearby restaurants and randomly selects one for your next meal. The script can be scheduled using `crontab` to remind you where to eat lunch or dinner.

## Features

- Retrieves nearby restaurants based on your current location.
- Sorts restaurants by rating.
- Randomly selects a restaurant from the list.
- Can be scheduled to run automatically using `crontab`.

## Requirements

- Python 3.x
- `requests` library

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/restaurant_picker.git
cd restaurant_picker
```

### 2. Create a Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

### 4. Install Dependencies

Install the required dependencies:

```bash
pip install requests
```

Alternatively, you can install dependencies from a `requirements.txt` file (if available):

```bash
pip install -r requirements.txt
```

### 5. Get a Gaode API Key

Sign up for a Gaode developer account and create a new project to obtain an API key. You can sign up [here](https://lbs.amap.com/).

### 6. Set Environment Variables

You need to set two environment variables:

- `GAODE_API_KEY`: Your Gaode API key.
- `MY_LOCATION`: Your current location in `longitude,latitude` format.

Example:

```bash
export GAODE_API_KEY=your_api_key
export MY_LOCATION=116.397128,39.916527  # Example for Beijing
```

### 7. Crontab Setup

To run this script automatically for lunch and dinner reminders, you can set up a cron job.

Edit your `crontab`:

```bash
crontab -e
```

Add the following lines to run the script at 12 PM and 6 PM every day:

```bash
0 12 * * * /bin/bash -c "source /path_to_project/venv/bin/activate && python /path_to_project/restaurant_picker.py >> ~/restaurant_picker.log 2>&1"
0 18 * * * /bin/bash -c "source /path_to_project/venv/bin/activate && python /path_to_project/restaurant_picker.py >> ~/restaurant_picker.log 2>&1"
```

Replace `/path_to_project/` with the full path to your project directory.

### 8. Test the Script

Run the script manually to test if it works correctly:

```bash
python restaurant_picker.py
```

The script will fetch nearby restaurants and randomly suggest one based on ratings.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to update the repository link, license, or any other project-specific information.