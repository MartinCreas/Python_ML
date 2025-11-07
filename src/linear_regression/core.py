"""Core utilities for simple linear regression experiments."""

from typing import Any


def fit_linear_regression(X: Any, y: Any):
    """Fit a scikit-learn LinearRegression model.

    Args:
        X: array-like feature matrix
        y: array-like target vector

    Returns:
        Fitted LinearRegression instance
    """
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(X, y)
    return model
