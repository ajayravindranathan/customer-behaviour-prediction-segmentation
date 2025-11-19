import pandas as pd
import numpy as np
import boto3
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

n_customers = 10000

# Customer Profile
customer_ids = [f"CUST{str(i).zfill(6)}" for i in range(1, n_customers + 1)]
age = np.random.randint(18, 85, n_customers)
geography = np.random.choice(['Urban', 'Suburban', 'Rural'], n_customers, p=[0.45, 0.35, 0.2])
billing_preference = np.random.choice(['Large Font', 'Paperless', 'Standard Paper'], n_customers, p=[0.15, 0.55, 0.3])
vulnerability = np.random.choice(['Yes', 'No'], n_customers, p=[0.12, 0.88])
tenure_months = np.random.randint(1, 240, n_customers)
payment_method = np.random.choice(['Direct Debit', 'Cheque', 'Cash', 'Card'], n_customers, p=[0.65, 0.15, 0.08, 0.12])

# Product & Service
product_broadband = np.random.choice([0, 1], n_customers, p=[0.2, 0.8])
product_tv = np.random.choice([0, 1], n_customers, p=[0.4, 0.6])
product_voice = np.random.choice([0, 1], n_customers, p=[0.35, 0.65])
product_tier = np.random.choice(['Copper', 'Fibre', 'Fibre Plus'], n_customers, p=[0.3, 0.55, 0.15])
contract_lifecycle = np.random.choice(['In Contract', 'Out of Contract', 'Month to Month'], n_customers, p=[0.45, 0.35, 0.2])
average_monthly_spend = np.random.lognormal(3.8, 0.5, n_customers).round(2)

# Behavioural & Engagement (pre-migration)
contact_frequency_pre_migration = np.random.poisson(2.5, n_customers)
number_of_complaints = np.random.poisson(0.8, n_customers)
number_of_faults = np.random.poisson(1.2, n_customers)
late_payments = np.random.poisson(0.6, n_customers)
missed_payments = np.random.poisson(0.3, n_customers)

# Generate labels with realistic correlations
# Label 1: Number of calls post-migration (higher if more pre-migration issues)
base_calls = np.random.poisson(1.5, n_customers)
calls_boost = (contact_frequency_pre_migration * 0.3 + number_of_faults * 0.4 + number_of_complaints * 0.5).astype(int)
number_of_calls_post_migration = np.maximum(0, base_calls + calls_boost + np.random.randint(-1, 2, n_customers))

# Label 2: Churn after migration (binary)
churn_prob = 0.05 + (number_of_complaints * 0.02) + (number_of_faults * 0.015) + \
             (late_payments * 0.01) + (missed_payments * 0.02) + \
             ((contract_lifecycle == 'Out of Contract').astype(int) * 0.08) + \
             ((tenure_months < 12).astype(int) * 0.05)
churn_prob = np.clip(churn_prob, 0, 0.5)
churn_after_migration = (np.random.random(n_customers) < churn_prob).astype(int)

# Label 3: Change in spend (can be positive, negative, or zero)
spend_change_base = np.random.normal(0, 15, n_customers)
# Positive change if adopted more products, negative if churned or had issues
spend_change_adjustment = (product_broadband + product_tv + product_voice - 1.5) * 5 - \
                          (number_of_complaints * 3) - (churn_after_migration * 20) + \
                          ((contract_lifecycle == 'In Contract').astype(int) * 5)
change_in_spend = (spend_change_base + spend_change_adjustment).round(2)

# Label 4: Change in products (net change: -2 to +2)
product_change_prob = 0.15 + (number_of_calls_post_migration * 0.02) + \
                      ((contract_lifecycle == 'Month to Month').astype(int) * 0.05)
product_change_prob = np.clip(product_change_prob, 0, 0.4)
change_in_products = np.where(
    np.random.random(n_customers) < product_change_prob,
    np.random.choice([-2, -1, 1, 2], n_customers, p=[0.1, 0.3, 0.45, 0.15]),
    0
)

# Create DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    # Customer Profile
    'age': age,
    'geography': geography,
    'billing_preference': billing_preference,
    'vulnerability': vulnerability,
    'tenure_months': tenure_months,
    'payment_method': payment_method,
    # Product & Service
    'product_broadband': product_broadband,
    'product_tv': product_tv,
    'product_voice': product_voice,
    'product_tier': product_tier,
    'contract_lifecycle': contract_lifecycle,
    'average_monthly_spend': average_monthly_spend,
    # Behavioural & Engagement
    'contact_frequency_pre_migration': contact_frequency_pre_migration,
    'number_of_complaints': number_of_complaints,
    'number_of_faults': number_of_faults,
    'late_payments': late_payments,
    'missed_payments': missed_payments,
    # Reinforcement (Labels for propensity models)
    'number_of_calls_post_migration': number_of_calls_post_migration,
    'churn_after_migration': churn_after_migration,
    'change_in_spend': change_in_spend,
    'change_in_products': change_in_products
})

# Save locally
csv_filename = f'customer_propensity_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
df.to_csv(csv_filename, index=False)
print(f"Generated {len(df)} customer records")
print(f"Saved locally as: {csv_filename}")

# Upload to S3
s3_client = boto3.client('s3')
bucket_name = 'post-migration-propensity-data'
s3_key = f'raw-data/{csv_filename}'

try:
    s3_client.upload_file(csv_filename, bucket_name, s3_key)
    print(f"Successfully uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"Error uploading to S3: {e}")

# Display summary statistics
print("\n=== DATA SUMMARY ===")
print(f"Total customers: {len(df)}")
print(f"\nLabel distributions:")
print(f"- Avg calls post-migration: {df['number_of_calls_post_migration'].mean():.2f}")
print(f"- Churn rate: {df['churn_after_migration'].mean()*100:.1f}%")
print(f"- Avg spend change: ${df['change_in_spend'].mean():.2f}")
print(f"- Customers with product changes: {(df['change_in_products'] != 0).sum()}")
print(f"\nSample data (first 5 rows):")
print(df.head())
