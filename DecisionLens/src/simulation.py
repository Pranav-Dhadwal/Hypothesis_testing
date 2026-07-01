import os
import numpy as np
import pandas as pd

n_users = 10000
np.random.seed(42)
data_file = os.path.join('DecisionLens', 'data', 'stimulated_data.csv')

# Base product views (normal Poisson)
base_product_views = np.random.poisson(lam=2, size=n_users) + 1
# Create a mask for explorers (5% probability)
explorer_mask = np.random.choice([0, 1], size=n_users, p=[0.95, 0.05])
# Generate extra product views for explorers (higher lambda)
explorer_product_views = np.random.poisson(lam=7, size=n_users)
# Final product views: add extra where mask is 1
final_product_views = base_product_views + (explorer_mask * explorer_product_views)

df = pd.DataFrame({
    'user_id': np.arange(1, n_users + 1),
    'age': np.random.randint(18, 65, size=n_users),
    'gender': np.random.choice(['Male', 'Female'], size=n_users, p=[0.4, 0.6]),
    'country': np.random.choice(['India', 'USA', 'UK', 'Germany', 'Brazil'], size=n_users, p=[0.5, 0.3, 0.1, 0.05, 0.05]),
    'device': np.random.choice(['Mobile', 'Desktop', 'Tablet', 'Other'], size=n_users, p=[0.6, 0.2, 0.1, 0.1]),
    'session_duration': np.round(np.random.lognormal(mean=1.0, sigma=0.5, size=n_users),2),
    'pages_viewed': final_product_views,
    'previous_orders': np.random.poisson(lam=2, size=n_users),
    'traffic_source': np.random.choice(['Organic', 'Ads', 'Email', 'Social'], size=n_users, p=[0.4, 0.3, 0.2, 0.1]),
    'experiment_group': np.random.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])
})

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.size)
# print(df.shape)
# print(df.dtypes)
# print(df.columns)
# print(df.memory_usage())

df.to_csv(data_file, index=False)

with open(data_file, 'r') as f:
    if f.read() == '':
        print('Data File is Empty')
    else :
        print("Data Available")
