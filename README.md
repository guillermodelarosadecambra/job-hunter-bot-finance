# Finance Job Hunter Bot

Automated Python bot that scans finance, trading and commodities job opportunities across multiple platforms and sends alerts when relevant roles appear.

---

# Project Structure

## config.py
Main configuration file.

Contains:
- target roles
- locations
- companies
- job sources
- keywords for filtering

This file allows modifying the behaviour of the bot without changing the core code.

---

## main.py
Main execution script of the bot.

Responsibilities:
- run job scrapers
- collect job listings
- apply filters
- check duplicates
- trigger notifications

This file acts as the **central controller of the application**.

---

## jobs_database.csv
Local storage of previously detected jobs.

Purpose:
- avoid duplicate alerts
- keep track of already processed listings

---

# Folders

## scrapers/
Contains all modules responsible for collecting job listings from different platforms.

Examples:
- LinkedIn
- Indeed
- eFinancialCareers
- company career pages

Each scraper extracts job data such as:
- title
- company
- location
- link

---

## filters/
Contains logic to filter job listings based on predefined criteria.

Filters include:
- target roles
- junior level keywords
- excluded senior positions
- location filtering

---

## notifications/
Handles the alert system.

Responsible for sending notifications when new jobs are detected.

Possible channels:
- Telegram
- Email
- other messaging services

---

## database/
Folder reserved for storing structured data if the project grows.

Currently used for:
- job tracking
- potential future databases
