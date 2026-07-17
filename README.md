# Restaurant Table Booking & Online Delivery Analysis

Cognifyz Technologies — Data Science Internship — **Level 2, Task 1**

A Flask dashboard analyzing a global restaurant dataset (9,551 restaurants) to uncover patterns in table booking, online delivery, and pricing.

## What it does

- **Table booking & online delivery rates** — calculates the percentage of restaurants offering each service.
- **Rating comparison** — compares average customer ratings for restaurants with vs. without table booking.
- **Price range vs. delivery** — analyzes how online delivery availability varies across price tiers (Cheap → Very Expensive).

## Key findings

| Metric | Value |
|---|---|
| Restaurants offering table booking | 12.12% |
| Restaurants offering online delivery | 25.66% |
| Avg. rating (with table booking) | 3.44 |
| Avg. rating (without table booking) | 2.56 |
| Highest online delivery adoption | Moderate price range (41.31%) |

Restaurants with table booking tend to have noticeably higher average ratings — likely correlated with more established, higher-service establishments.

## Tech stack

- **Backend:** Flask, Pandas
- **Frontend:** Jinja2 templates, Chart.js
- **Deployment:** Vercel (serverless Python)

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## Deploy

Push to GitHub and import the repo into Vercel — `vercel.json` handles the routing automatically.
