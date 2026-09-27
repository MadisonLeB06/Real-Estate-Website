# Real Estate Website

A web application designed to help users find homes that fit within their estimated budget.

Instead of only providing the estimated price range for what the user could purchase, the goal of this project it to connect the affordability calculations with real estate listings. Using the given information from user, they will receive an estimated home-buying range, and then be able to filter properties within that range. Making it easier for the user to navigate through what their searching for to find an affordable home.

> **Note:** Affordability calculations provided by this application are estimates only and should not be considered financial advice or mortgage approval. Actual affordability and loan eligibility can vary based on lenders and individual circumstances. Please keep this in mind when using the website.

## Project Overview

The application will calculate an estimated recommended and maximum home price using financial information provided by the user.

The affordability calculation takes into account:

- Annual gross income
- Monthly debt
- Down payment
- Interest rate
- Loan term
- Property taxes
- Homeowners insurance
- Private mortgage insurance (PMI)
- HOA fees
- Debt-to-income (DTI) ratios

After calculating the user's estimated affordability range, the application will allow the user to search real estate listings based on that budget.

## Features

### Affordability Calculator

- [x] Create the formula to calculate the price range
- [ ] Accept affordability information through the web interface
- [ ] Allow optional values to use reasonable defaults
- [ ] Display a breakdown of the affordability calculation

### Property Search

- [ ] Integrate a real estate listing API
- [ ] Search for homes by location
- [ ] Filter listings by recommended and maximum price
- [ ] Search for homes within the calculated affordability range
- [ ] Filter by bedrooms and bathrooms etc
- [ ] Display property information and images

### User Features

- [ ] Create user accounts
- [ ] User authentication
- [ ] Save financial preferences
- [ ] Save favorite properties
- [ ] View previously saved properties
- [ ] Save financial information to edit later on if needed

## Planned Tech Stack

**Backend**
- Python
- FastAPI

**Frontend**
- React
- JavaScript

**Database**
- SQL / PostgreSQL

**External Services**
- Real estate listing API (TBD)

The technologies used may change as the project develops.

## How Affordability Calculator Works

The calculator uses the user's gross monthly income, existing debt, housing expenses, down payment, mortgage interest rate, and loan term to estimate an affordable home price.

Two estimates are provided:

**Recommended Budget** - A more conservative estimate intended to represent a reasonable housing budget based on housing and debt-to-income limits.

**Maximum Budget** - A higher estimate based on a maximum debt-to-income threshold.

These values can then be used as price filters when searching for available properties.

## Project Status

**Currently in development, more will be added.**
