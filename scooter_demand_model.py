#!/usr/bin/env python3
"""
Hierarchical Spatial Model for Scooter Demand Analysis

This script implements a Bayesian hierarchical model to analyze scooter demand
across neighborhoods, identifying underserved areas through residual analysis.

Author: Generated for scooter demand modeling project
License: MIT
"""

import numpy as np
import pandas as pd
import pymc as pm
import pytensor.tensor as pt
import matplotlib.pyplot as plt
from typing import Tuple, Dict, Any


def generate_synthetic_data(n_neigh: int = 200, seed: int = 2025) -> pd.DataFrame:
    """
    Generate synthetic scooter demand data for neighborhoods.
    
    Args:
        n_neigh: Number of neighborhoods to simulate
        seed: Random seed for reproducibility
        
    Returns:
        DataFrame with neighborhood data including coordinates, infrastructure,
        and observed demand
    """
    np.random.seed(seed)
    
    # Synthetic spatial coordinates (e.g. lat/lon in arbitrary units)
    coords = np.random.uniform(0, 50, size=(n_neigh, 2))
    
    # Synthetic infrastructure score (scale 0-1)
    infra_score = np.random.beta(2, 5, size=n_neigh)
    
    # True neighborhood-level random effects (latent demand factors)
    true_neigh_effect = np.random.normal(0, 0.5, size=n_neigh)
    
    # Baseline intercept and effect of infrastructure on demand
    alpha_true = 1.0
    beta_infra_true = 2.0
    
    # Generate expected log-demand per neighborhood
    log_demand = alpha_true + beta_infra_true * infra_score + true_neigh_effect
    
    # Convert to expected counts (e.g. rides per day)
    expected_demand = np.exp(log_demand)
    
    # Simulate observed demand counts (Poisson)
    observed_demand = np.random.poisson(expected_demand)
    
    # Create DataFrame
    df = pd.DataFrame({
        'neighborhood': np.arange(n_neigh),
        'x': coords[:, 0],
        'y': coords[:, 1],
        'infrastructure': infra_score,
        'observed_demand': observed_demand
    })
    
    return df


def fit_hierarchical_model(df: pd.DataFrame, n_samples: int = 20000) -> Tuple[pm.Model, Any]:
    """
    Fit a Bayesian hierarchical model for scooter demand.
    
    Args:
        df: DataFrame with neighborhood data
        n_samples: Number of samples for variational inference
        
    Returns:
        Tuple of (model, trace) containing the fitted model and posterior samples
    """
    n_neigh = len(df)
    
    with pm.Model() as model:
        # Priors
        alpha = pm.Normal("alpha", mu=0, sigma=5)
        beta_infra = pm.Normal("beta_infra", mu=0, sigma=3)
        sigma_neigh = pm.HalfNormal("sigma_neigh", sigma=1)
        
        # Neighborhood random effects
        neigh_eff = pm.Normal("neigh_eff", mu=0, sigma=sigma_neigh, shape=n_neigh)
        
        # Expected log demand
        log_lambda = alpha + beta_infra * df['infrastructure'].values + neigh_eff
        
        # Poisson likelihood
        demand_obs = pm.Poisson("demand_obs", mu=pt.exp(log_lambda), 
                               observed=df['observed_demand'].values)
        
        # Fit model using Laplace approximation or fallback to ADVI
        try:
            print("Attempting Laplace approximation...")
            approx = pm.fit(method='laplace', n=n_samples)
        except Exception as e:
            print(f"Laplace method not available ({e}), falling back to fullrank_advi")
            approx = pm.fit(method='fullrank_advi', n=n_samples)
        
        trace = approx.sample(1000)
    
    return model, trace


def calculate_residuals(df: pd.DataFrame, trace: Any) -> pd.DataFrame:
    """
    Calculate demand residuals (observed - predicted) for each neighborhood.
    
    Args:
        df: DataFrame with neighborhood data
        trace: Posterior samples from the fitted model
        
    Returns:
        DataFrame with residuals added
    """
    # Extract posterior mean neighborhood effects
    posterior_neigh_eff = trace.posterior["neigh_eff"].mean(dim=["chain", "draw"]).values
    
    # Calculate posterior predicted demand mean per neighborhood
    posterior_alpha = trace.posterior["alpha"].mean().values
    posterior_beta_infra = trace.posterior["beta_infra"].mean().values
    posterior_log_lambda = (posterior_alpha + 
                           posterior_beta_infra * df['infrastructure'].values + 
                           posterior_neigh_eff)
    posterior_lambda = np.exp(posterior_log_lambda)
    
    # Calculate residuals = observed - posterior mean predicted demand
    residuals = df['observed_demand'] - posterior_lambda
    
    # Add residuals to DataFrame
    df['residuals'] = residuals
    df['predicted_demand'] = posterior_lambda
    
    return df


def plot_demand_heatmap(df: pd.DataFrame, save_path: str = None) -> None:
    """
    Create a heatmap visualization of demand residuals.
    
    Args:
        df: DataFrame with neighborhood data and residuals
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(12, 10))
    
    # Create scatter plot with residuals as color
    sc = plt.scatter(df['x'], df['y'], c=df['residuals'], 
                    cmap='coolwarm', s=80, edgecolor='k', alpha=0.8)
    
    # Add colorbar
    cbar = plt.colorbar(sc, label='Demand Residual (Observed - Predicted)')
    cbar.ax.tick_params(labelsize=12)
    
    # Customize plot
    plt.title("Heatmap of Demand Residuals: Negative = Underserved Neighborhoods", 
              fontsize=14, fontweight='bold')
    plt.xlabel("X Coordinate", fontsize=12)
    plt.ylabel("Y Coordinate", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add text box with interpretation
    textstr = ('Negative residuals (blue): Underserved neighborhoods\n'
               'Positive residuals (red): Over-served neighborhoods')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()


def print_model_summary(trace: Any) -> None:
    """
    Print a summary of the fitted model parameters.
    
    Args:
        trace: Posterior samples from the fitted model
    """
    print("\n" + "="*50)
    print("MODEL SUMMARY")
    print("="*50)
    
    # Extract posterior means and standard deviations
    alpha_mean = trace.posterior["alpha"].mean().values
    alpha_std = trace.posterior["alpha"].std().values
    beta_mean = trace.posterior["beta_infra"].mean().values
    beta_std = trace.posterior["beta_infra"].std().values
    sigma_mean = trace.posterior["sigma_neigh"].mean().values
    sigma_std = trace.posterior["sigma_neigh"].std().values
    
    print(f"Intercept (α): {alpha_mean:.3f} ± {alpha_std:.3f}")
    print(f"Infrastructure Effect (β): {beta_mean:.3f} ± {beta_std:.3f}")
    print(f"Neighborhood Effect Std (σ): {sigma_mean:.3f} ± {sigma_std:.3f}")
    print("\nInterpretation:")
    print(f"- Each unit increase in infrastructure score increases log-demand by {beta_mean:.3f}")
    print(f"- Neighborhood random effects have standard deviation of {sigma_mean:.3f}")


def main():
    """
    Main function to run the complete scooter demand analysis.
    """
    print("Scooter Demand Hierarchical Model Analysis")
    print("="*50)
    
    # Generate synthetic data
    print("Generating synthetic neighborhood data...")
    df = generate_synthetic_data(n_neigh=200, seed=2025)
    print(f"Generated data for {len(df)} neighborhoods")
    
    # Fit hierarchical model
    print("\nFitting Bayesian hierarchical model...")
    model, trace = fit_hierarchical_model(df)
    print("Model fitting completed!")
    
    # Calculate residuals
    print("\nCalculating demand residuals...")
    df = calculate_residuals(df, trace)
    
    # Print model summary
    print_model_summary(trace)
    
    # Create visualization
    print("\nGenerating demand heatmap...")
    plot_demand_heatmap(df, save_path="scooter_demand_heatmap.png")
    
    # Save results
    df.to_csv("neighborhood_demand_results.csv", index=False)
    print("\nResults saved to 'neighborhood_demand_results.csv'")
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()