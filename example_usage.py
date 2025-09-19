#!/usr/bin/env python3
"""
Example usage of the Scooter Demand Model

This script demonstrates different ways to use the scooter demand model
with various parameters and customizations.
"""

from scooter_demand_model import (
    generate_synthetic_data, 
    fit_hierarchical_model, 
    calculate_residuals, 
    plot_demand_heatmap,
    print_model_summary
)
import matplotlib.pyplot as plt


def example_basic_usage():
    """Basic usage example with default parameters."""
    print("=== Basic Usage Example ===")
    
    # Generate data
    df = generate_synthetic_data(n_neigh=100, seed=42)
    print(f"Generated data for {len(df)} neighborhoods")
    
    # Fit model
    model, trace = fit_hierarchical_model(df)
    
    # Calculate residuals
    df = calculate_residuals(df, trace)
    
    # Print summary
    print_model_summary(trace)
    
    # Create plot
    plot_demand_heatmap(df, save_path="example_basic_heatmap.png")


def example_custom_parameters():
    """Example with custom parameters."""
    print("\n=== Custom Parameters Example ===")
    
    # Generate data with more neighborhoods
    df = generate_synthetic_data(n_neigh=300, seed=123)
    print(f"Generated data for {len(df)} neighborhoods")
    
    # Fit model with more samples
    model, trace = fit_hierarchical_model(df, n_samples=30000)
    
    # Calculate residuals
    df = calculate_residuals(df, trace)
    
    # Print summary
    print_model_summary(trace)
    
    # Create custom plot
    plt.figure(figsize=(14, 10))
    sc = plt.scatter(df['x'], df['y'], c=df['residuals'], 
                    cmap='RdYlBu_r', s=100, edgecolor='k', alpha=0.7)
    plt.colorbar(sc, label='Demand Residual')
    plt.title("Custom Heatmap: 300 Neighborhoods", fontsize=16, fontweight='bold')
    plt.xlabel("X Coordinate", fontsize=12)
    plt.ylabel("Y Coordinate", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("example_custom_heatmap.png", dpi=300, bbox_inches='tight')
    plt.show()


def example_analysis():
    """Example showing how to analyze results."""
    print("\n=== Analysis Example ===")
    
    # Generate and fit model
    df = generate_synthetic_data(n_neigh=150, seed=456)
    model, trace = fit_hierarchical_model(df)
    df = calculate_residuals(df, trace)
    
    # Analyze results
    print(f"Total neighborhoods: {len(df)}")
    print(f"Underserved neighborhoods (residual < -5): {(df['residuals'] < -5).sum()}")
    print(f"Over-served neighborhoods (residual > 5): {(df['residuals'] > 5).sum()}")
    print(f"Average residual: {df['residuals'].mean():.3f}")
    print(f"Residual standard deviation: {df['residuals'].std():.3f}")
    
    # Find most underserved neighborhoods
    most_underserved = df.nsmallest(5, 'residuals')[['neighborhood', 'residuals', 'infrastructure']]
    print("\nMost underserved neighborhoods:")
    print(most_underserved)
    
    # Find most over-served neighborhoods
    most_overserved = df.nlargest(5, 'residuals')[['neighborhood', 'residuals', 'infrastructure']]
    print("\nMost over-served neighborhoods:")
    print(most_overserved)


if __name__ == "__main__":
    # Run examples
    example_basic_usage()
    example_custom_parameters()
    example_analysis()
    
    print("\n=== All Examples Complete ===")
    print("Check the generated PNG files for visualizations!")