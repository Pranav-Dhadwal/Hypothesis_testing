import numpy as np
import pandas as pd


def generate_customer_data(n_rows: int, purchase_lift: float):

    # Customer IDs
    customer_id = np.arange(1, n_rows + 1)

    # Age
    age = np.random.randint(18, 65, n_rows)

    # Device
    device = np.random.choice(
        ["Mobile", "Desktop", "Other"],
        size=n_rows,
        p=[0.6, 0.15, 0.25]
    )

    # Session duration (minutes)
    session_duration = np.random.normal(10, 2, n_rows)

    # Younger users browse slightly longer
    session_duration += np.where(age < 30, 3, 0)

    session_duration = np.clip(session_duration, 1, None)

    # Pages viewed depends on session duration
    pages_viewed = (
        session_duration *
        np.random.uniform(1.5, 2.5, n_rows)
    ).astype(int)

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

        "device": device,

        "session_duration": session_duration.round(2),

        "pages_viewed": pages_viewed,

        "previous_orders": previous_orders,

        "experiment_group": experiment_group,

        "purchase_prob": purchase_prob.round(3),

        "purchased": purchased

    })

    return df