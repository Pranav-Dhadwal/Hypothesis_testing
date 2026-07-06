import numpy as np
import pandas as pd


def generate_customer_data(n_rows: int, purchase_lift: float):

    # Customer IDs
    customer_id = np.arange(1, n_rows + 1)

    # Age
    age = np.random.randint(18, 65, n_rows)

    gender = np.random.choice(
        ['Male', 'Female'],
        size=n_rows,
        p=[0.45, 0.55]
    )

    # Country
    country = np.random.choice(
        ["India", "USA", "UK", "Germany", "Canada", "Australia"],
        size=n_rows,
        p=[0.40, 0.20, 0.12, 0.10, 0.10, 0.08]
    ) 

    # traffic source 
    traffic_prob = {
    "India":    [0.30,0.45,0.15,0.10],
    "USA":      [0.50,0.20,0.20,0.10],
    "UK":       [0.45,0.25,0.20,0.10],
    "Germany":  [0.40,0.25,0.25,0.10],
    "Canada":   [0.45,0.20,0.25,0.10],
    "Australia":[0.42,0.23,0.25,0.10]
    }

    traffic_source = [
        np.random.choice(
            ["Organic","Ads","Email","Social"],
            p=traffic_prob[c]
        )
        for c in country
    ]

    # Device prob so it depends on country 
    device_prob = {
        "India":    [0.75, 0.15, 0.10],
        "USA":      [0.45, 0.45, 0.10],
        "UK":       [0.55, 0.35, 0.10],
        "Germany":  [0.50, 0.40, 0.10],
        "Canada":   [0.50, 0.40, 0.10],
        "Australia":[0.55, 0.35, 0.10]
    }

    # device
    device = [
        np.random.choice(
            ["Mobile","Desktop","Other"],
            p=device_prob[c]
        )
        for c in country
    ]
    # Session duration (minutes)
    session_duration = np.random.normal(10, 2, n_rows)

    # Younger and female users browse slightly longer
    session_duration += np.where(age < 30, 3, 0)

    session_duration *= np.where(
        gender == "Female",
        1.12,
        1.00
    )

    session_duration = np.clip(session_duration, 1, None)

    # Session duration influences browsing
    pages_viewed = (
        session_duration *
        np.random.uniform(1.5, 2.5, n_rows)
    ).astype(int)

    # Slightly higher engagement for female customers
    pages_viewed += np.where(
        gender == "Female",
        np.random.binomial(1, 0.6, n_rows),
        0
    )

    pages_viewed = np.clip(pages_viewed, 1, None)

    # Previous orders
    previous_orders = np.random.poisson(2, n_rows)

    # Experiment Groups
    experiment_group = np.random.choice(
        ["A", "B"],
        size=n_rows
    )

    # Purchase probability
    purchase_prob = (
        0.20
        + previous_orders * 0.03
        + session_duration * 0.01
        + pages_viewed * 0.005
    )

    # Apply recommendation lift only to Group B
    purchase_prob += np.where(
        experiment_group == "B",
        purchase_lift / 100,
        0
    )

    purchase_prob = np.clip(purchase_prob, 0, 1)

    # Final purchase decision
    purchased = np.random.rand(n_rows) < purchase_prob

    df = pd.DataFrame({

        "customer_id": customer_id,

        "age": age,

        "gender": gender,

        "country": country,

        "device": device,

        "traffic_source" : traffic_source,

        "session_duration": session_duration.round(2),

        "pages_viewed": pages_viewed,

        "previous_orders": previous_orders,

        "experiment_group": experiment_group,

        "purchase_prob": purchase_prob.round(3),

        "purchased": purchased

    })

    return df