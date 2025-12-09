# Don't Be Dumb Budgeting

A personal finance management application built for CS 3200 Database Design at Northeastern University.

# Video Demo

https://www.dropbox.com/scl/fi/ro9x1vjx5j1upcc3dixup/ProjectVideo.mp4?rlkey=d7t5e4x74blulxjwtu23hwfu5&st=fg08zq2v&dl=0

## Project Overview

"Don't Be Dumb Budgeting" is a full-stack web application that helps users manage their personal finances. The app supports multiple user personas with many helpful budgeting features.

## Features

### Dashboard
- Financial overview with income, expenses, net position, and savings metrics
- Monthly trends bar charts (last 6 months) for income and expenses
- Pie charts for expense breakdown by category and income by source
- Recent transactions list
- Quick action buttons for navigation

### Budget Tracker
- **Totals Tab**: Financial overview with budget progress bars
- **Budget Manager Tab**: Set total budget, category budgets, and custom budgets
- **Income Tab**: Track and add income with search and export to CSV
- **Expenditures Tab**: Track and add expenses with category selection and budget assignment
- **All Transactions Tab**: View all transactions with search and export functionality

### Savings Goals
- Create and track savings goals with target amounts and deadlines
- Add/remove money from savings goals
- Progress bars showing goal completion

### Other Financial Data
- **Debt Management**: Track loans with payment progress, make payments
- **Investments**: Track investment portfolio with balances and return rates
- **Subscriptions**: Manage recurring subscriptions with pay functionality
- **Bills**: Track bills with pay/unpay functionality and due dates

### AI Insights
- AI-powered financial analysis and recommendations

## User Personas

The application supports 4 distinct user personas:

1. **Alex (College Student)** - Basic budgeting for students with limited income
2. **Jamie (Professional)** - Comprehensive finance tracking for working professionals
3. **Jordan (Club Treasurer)** - Organization/club treasury management
4. **Sarah (Family Manager)** - Family budget management with dependents tracking

## Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: Flask REST API (Python)
- **Database**: MySQL
- **Containerization**: Docker & Docker Compose
- **Visualization**: Plotly

## Project Structure
```
dont-be-dumb-app/
├── app/                             # Streamlit Frontend
│   └── src/
│       ├── pages/
│       │   ├── 00_User_Home.py      # Dashboard
│       │   ├── 10_Budget_Tracker.py # Budget management
│       │   ├── 12_Savings.py        # Savings goals
│       │   ├── 13_Other.py          # Debt, investments, subscriptions, bills
│       │   ├── 20_AI_Insights.py    # AI recommendations
│       │   ├── 25_Dependents.py     # Family dependents
│       │   ├── 30_Users.py          # User selection
│       │   └── 40_About.py          # About page
│       ├── modules/
│       │   └── nav.py               # Navigation components
│       └── Home.py                  # Landing page
├── api/                             # Flask REST API
│   └── backend/
│       ├── bills/                   # Bill routes
│       ├── budgets/                 # Budget routes
│       ├── insights/                # AI insights routes
│       ├── investments/             # Investment routes
│       ├── loans/                   # Loan/debt routes
│       ├── savings/                 # Savings routes
│       ├── subscriptions/           # Subscription routes
│       ├── transactions/            # Transaction routes
│       ├── users/                   # User routes
│       ├── db_connection/           # Database connection
│       └── rest_entry.py            # Flask app entry point
├── database-files/                  # SQL initialization scripts
│   └── 01_budget_db.sql             # Database schema and test data
├── docker-compose.yaml              # Docker configuration
└── README.md
```

## Database Schema

The application uses 10 tables with 65+ attributes:

- **User** - User accounts and profiles
- **Account** - Financial accounts (checking, savings, credit)
- **Transaction** - Income and expense transactions
- **Budget** - Budget limits (total, category, custom)
- **Category** - Transaction categories
- **Saving** - Savings goals
- **Loan** - Debt/loan tracking
- **Investment** - Investment portfolio
- **Subscription** - Recurring subscriptions
- **Bill** - Bill tracking

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Git

### Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd dont-be-dumb-app
```

2. Set up the environment file:
```bash
   cp api/.env.template api/.env
```
   Edit `api/.env` and set a password for `MYSQL_ROOT_PASSWORD`

3. Start the application:
```bash
   docker compose up -d --build
```

4. Wait, then access:
   - **Streamlit App**: http://localhost:8501
   - **Flask API**: http://localhost:4000
   - **MySQL**: localhost:3200

### Stopping the Application
```bash
docker compose down
```

### Rebuilding the Database

To reset the database with fresh test data:
```bash
docker compose down -v && docker compose up -d --build
```

## API Endpoints

### Users
- `GET /users/` - Get all users
- `GET /users/<id>` - Get user by ID
- `GET /users/<id>/accounts` - Get user's accounts

### Transactions
- `GET /transactions/user/<id>` - Get user's transactions
- `GET /transactions/user/<id>/income` - Get income transactions
- `GET /transactions/user/<id>/expenses` - Get expense transactions
- `POST /transactions/` - Create transaction
- `DELETE /transactions/<id>` - Delete transaction

### Budgets
- `GET /budgets/user/<id>/list` - Get user's budgets
- `GET /budgets/user/<id>/totals` - Get financial totals
- `POST /budgets/` - Create budget
- `PUT /budgets/<id>` - Update budget
- `DELETE /budgets/<id>` - Delete budget

### Savings
- `GET /savings/user/<id>` - Get user's savings goals
- `POST /savings/` - Create savings goal
- `PUT /savings/<id>/add` - Add money to goal
- `PUT /savings/<id>/remove` - Remove money from goal
- `DELETE /savings/<id>` - Delete savings goal

### Loans
- `GET /loans/user/<id>` - Get user's loans
- `POST /loans/` - Create loan
- `PUT /loans/<id>/pay` - Make loan payment
- `DELETE /loans/<id>` - Delete loan

### Bills
- `GET /bills/user/<id>` - Get user's bills
- `POST /bills/` - Create bill
- `PUT /bills/<id>/pay` - Mark bill as paid
- `PUT /bills/<id>/unpay` - Mark bill as unpaid
- `DELETE /bills/<id>` - Delete bill

### Subscriptions
- `GET /subscriptions/user/<id>` - Get user's subscriptions
- `POST /subscriptions/` - Create subscription
- `DELETE /subscriptions/<id>` - Delete subscription

### Investments
- `GET /investments/user/<id>` - Get user's investments
- `POST /investments/` - Create investment
- `DELETE /investments/<id>` - Delete investment

## Authors

- Ryan Porto
- Amogh Athimamula
- Adam Ancheta
- Shravan Ganta 

- Northeastern University, CS 3200 Database Design, Fall 2025

## Acknowledgments

- Built with Streamlit, Flask, MySQL, and Docker
