# SYS-IB  MASTER PROJECT CONTEXT

## PURPOSE OF THIS DOCUMENT

This document is the authoritative source of truth for the SYS-IB project.

A new developer, AI agent, Claude Code session, ChatGPT session, or future contributor should be able to read only this document and immediately understand:

* Project vision
* Current state
* Architecture
* Completed work
* Development rules
* Next steps
* Long-term roadmap

This project is being developed incrementally and must remain reproducible at every stage.

---

# PROJECT OVERVIEW

Project Name:

SYS-IB

Goal:

Build a professional automated stock trading platform capable of running up to 20 independent trading strategies.

Each strategy operates independently and may use a dedicated Alpaca paper trading account.

The platform must support:

* Strategy creation
* Backtesting
* Paper trading
* Portfolio monitoring
* Risk management
* AI-assisted learning and improvement

---

# CORE DEVELOPMENT PRINCIPLES

1. Backend First

No UI-first development.

Every feature must first exist as:

* Database model
* API endpoint
* Testable backend service

Only then may a UI be added.

---

2. Reproducible Development

Manual configuration should be minimized.

Prefer:

* scripts
* docker
* automated setup

Avoid:

* manual editing
* undocumented steps
* environment-specific hacks

---

3. Modular Architecture

No component should directly depend on another component's internal implementation.

Services communicate through defined interfaces.

---

4. AI-Friendly Development

The system is designed to allow future AI agents to:

* analyze trades
* suggest improvements
* generate pull requests

without requiring knowledge of the entire codebase.

---

# REPOSITORY

GitHub Repository:

https://github.com/salmog/sys-ib

Branch Strategy:

main

* production-ready only

develop

* active integration branch

feature/*

* one feature per branch

Never commit directly to main.

---

# DEVELOPMENT ENVIRONMENT

Primary Development Machine:

MacBook

Project Path:

/Users/salmog/test/sys-ib

Python:

3.9.6

Virtual Environment:

venv-sys-ib

---

# CURRENT PROJECT STRUCTURE

sys-ib/

backend/
frontend/
database/
docker/
docs/
scripts/
tests/

---

# CURRENT BACKEND

Framework:

FastAPI

Entry Point:

backend/app/main.py

Working Endpoints:

GET /health

returns:

{
"status": "ok"
}

GET /db-test

returns:

{
"db": "connected"
}

---

# DATABASE

Database:

PostgreSQL 15

Docker Container:

sysib-postgres

Database:

sysib_db

User:

sysib

Password:

sysib123

Connection String:

postgresql://sysib:sysib123@localhost:5432/sysib_db

---

# COMPLETED MILESTONES

Completed:

 Repository created

 Branching strategy defined

 SSH authentication configured

 FastAPI backend running

 Strategy API created

 PostgreSQL Docker setup created

 SQLAlchemy installed

 psycopg2 installed

 Database session layer created

 Database connection verified

 /db-test endpoint operational

---

# VERIFIED WORKING

The following has been tested successfully:

docker-compose up

PostgreSQL container startup

Database login

SQLAlchemy connection

FastAPI integration

GET /db-test

---

# CURRENT SYSTEM STATE

Working:

 Backend

 API

 PostgreSQL

 SQLAlchemy

Not Yet Built:

 Database models

 Persistence layer

 Alembic

 Backtesting

 Scanner

 PatternPY integration

 Risk engine

 Execution engine

 Learning engine

 Frontend

---

# TRADING PHILOSOPHY

Primary strategy concept:

Weekly Retest Breakout

Requirements:

* Long-term uptrend
* Strong structure
* Clear support
* Breakout confirmation
* Retest entry
* Risk-based sizing

Risk:

Maximum 1% account risk per trade.

Position sizing is always calculated from:

Risk Amount / Stop Distance

No strategy may bypass the risk engine.

---

# SUPPORT ZONE MODEL

Support is represented by:

Upper Line
Lower Line

Stop Loss:

Lower Support - 1 ATR

Support zones must eventually include:

* confidence
* timeframe
* touch count
* source

---

# MULTI-TIMEFRAME MODEL

Monthly  Weekly

Weekly  Daily

Daily  4H

4H  2H

2H  1H

1H  30m

30m  15m

15m  5m

5m  1m

---

# PATTERNPY INTEGRATION

PatternPY is a signal provider only.

PatternPY never makes trading decisions.

Outputs:

* support
* resistance
* channels
* triangles
* wedges
* cup and handle
* head and shoulders
* double tops
* double bottoms

All outputs must be stored.

Decision logic remains inside SYS-IB.

---

# LEARNING ENGINE

The learning engine is considered a first-class component.

Purpose:

Learn from completed trades.

Every trade must eventually support:

Create Learning Package

Button:

[Analyze Trade]

When pressed:

1. Collect trade data
2. Collect indicators
3. Collect PatternPY output
4. Collect candle history
5. Collect screenshots
6. Package into ZIP
7. Transfer to Mac via SCP
8. AI analyzes package
9. Generate recommendations

---

# LEARNING PACKAGE CONTENTS

Required:

trade.json

strategy.json

risk.json

market.json

patternpy.json

orders.json

decision_log.json

candles_before_entry.csv

candles_during_trade.csv

candles_after_exit.csv

chart screenshots

---

# REQUIRED FUTURE UI SECTIONS

1. Strategy Factory

Create strategies.

AI-assisted.

Generate standardized strategy definitions.

---

2. Backtesting

Compare against:

SPY

QQQ

---

3. Scanner Dashboard

Show funnel:

Universe



Trend



Structure



Breakout



Retest



Orders



Positions

---

4. Active Trading Dashboard

Show:

Open trades

Pending orders

P&L

Risk

Reasoning

Strategy status

---

5. Portfolio Risk Dashboard

Cross-strategy risk monitoring.

---

6. Pattern Explorer

PatternPY visualizations.

---

7. Learning Center

Trade analysis.

Recommendations.

Performance review.

---

# AUTOMATION REQUIREMENTS

Strong preference for:

scripts

docker

one-command setup

reproducible deployment

Future developers should always ask:

"Can this be automated?"

before introducing manual work.

---

# IMMEDIATE NEXT STEPS

1. Create database models

2. Create tables

3. Persist strategies

4. Replace in-memory storage

5. Add Alembic

6. Create trade model

7. Create learning package model

8. Build learning engine foundation

9. Build backtesting engine

10. Build scanner engine

---

# INSTRUCTIONS FOR THE NEXT AI AGENT

The project is currently at:

Prototype API  Real Backend Transition

The database connection has already been completed and verified.

Do NOT:

* redesign the project
* introduce major architecture changes
* start frontend work
* start trading logic

Continue from:

Create SQLAlchemy models and database tables.

Always work in small reproducible steps.

Always provide:

* exact file path
* complete file contents
* exact commands
* expected output

The user is a beginner and should never be required to infer missing steps.

