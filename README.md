# LeadScraper

A Python application that scrapes job listings from RemoteOK and automatically adds them to an Airtable database.

## Description

LeadScraper is a tool designed to help job seekers automate the process of finding remote job opportunities. It:

1. Scrapes the latest job listings from RemoteOK.com
2. Extracts job title, company name, and job link
3. Automatically adds these job listings to your Airtable database
4. Tags all jobs with "Python" for easy filtering

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mdishmam/LeadScraper
   cd LeadScraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

LeadScraper requires Airtable credentials to function. Follow these steps to set up your environment:

1. Copy the example environment file:
   ```
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Airtable credentials:
   ```
   AIRTABLE_TOKEN=your_airtable_api_key
   BASE_ID=your_airtable_base_id
   TABLE_NAME=your_table_name
   ```

### Getting Airtable Credentials

- **AIRTABLE_TOKEN**: Your Airtable API key. You can find this in your Airtable account settings.
- **BASE_ID**: The ID of your Airtable base. This can be found in the API documentation section of your Airtable workspace.
- **TABLE_NAME**: The name of the table where you want to store job listings.

## Usage

Run the script with:

```
python main.py
```

The script will:
1. Scrape the latest job listings from RemoteOK
2. Add the first 5 job listings to your Airtable database
3. Each job will include the title, company name, and a link to the job posting

## Customization

You can modify the script to:

- Change the number of jobs to add (edit line 50 in main.py)
- Add different tags (edit line 43 in main.py)
- Scrape different websites (would require modifying the scrape_jobs function)

## Dependencies

- beautifulsoup4: For parsing HTML
- requests: For making HTTP requests
- python-dotenv: For loading environment variables
- Other supporting libraries

## License

[Add your license information here]