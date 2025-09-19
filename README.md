# Scooter Demand Hierarchical Model

A Bayesian hierarchical spatial model for analyzing scooter demand across neighborhoods, identifying underserved areas through residual analysis using Laplace approximation.

## 🚀 Overview

This project implements a sophisticated statistical model to analyze scooter demand patterns across urban neighborhoods. By combining infrastructure data with neighborhood-level random effects, the model identifies areas where observed demand significantly differs from predicted demand, highlighting potential expansion opportunities or service gaps.

### Key Features

- **Hierarchical Modeling**: Captures both infrastructure effects and neighborhood-specific variations
- **Bayesian Inference**: Uses Laplace approximation for fast, approximate posterior estimation
- **Residual Analysis**: Identifies underserved neighborhoods through demand residuals
- **Visualization**: Generates intuitive heatmaps showing demand patterns
- **Synthetic Data**: Includes realistic data generation for demonstration purposes

## 📊 Methodology

### Core Concepts

**Hierarchical Modeling**: The model uses a two-level structure:
- **Level 1**: Neighborhood-specific random effects capture unobserved heterogeneity
- **Level 2**: Fixed effects model the relationship between infrastructure and demand

**Laplace Approximation**: Provides fast approximate Bayesian inference by:
- Approximating the posterior distribution with a multivariate normal
- Avoiding computationally expensive MCMC sampling
- Maintaining reasonable accuracy for many applications

**Residual Analysis**: Demand residuals (observed - predicted) reveal:
- **Negative residuals**: Underserved neighborhoods (demand lower than expected)
- **Positive residuals**: Over-served neighborhoods (demand higher than expected)

### Model Specification

The model assumes a Poisson likelihood for demand counts:

```
log(λᵢ) = α + β × infrastructureᵢ + uᵢ
yᵢ ~ Poisson(λᵢ)
uᵢ ~ Normal(0, σ²)
```

Where:
- `λᵢ` is the expected demand for neighborhood `i`
- `α` is the baseline intercept
- `β` captures the infrastructure effect
- `uᵢ` are neighborhood random effects
- `yᵢ` is the observed demand count

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/scooter-demand-model.git
   cd scooter-demand-model
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Run

### Basic Usage

Run the complete analysis with default parameters:

```bash
python scooter_demand_model.py
```

This will:
1. Generate synthetic data for 200 neighborhoods
2. Fit the hierarchical model using Laplace approximation
3. Calculate demand residuals
4. Generate a heatmap visualization
5. Save results to `neighborhood_demand_results.csv`

### Programmatic Usage

```python
from scooter_demand_model import generate_synthetic_data, fit_hierarchical_model, calculate_residuals, plot_demand_heatmap

# Generate data
df = generate_synthetic_data(n_neigh=100, seed=42)

# Fit model
model, trace = fit_hierarchical_model(df)

# Calculate residuals
df_with_residuals = calculate_residuals(df, trace)

# Visualize results
plot_demand_heatmap(df_with_residuals)
```

## 📈 Output

### Generated Files

- **`scooter_demand_heatmap.png`**: Heatmap visualization showing demand residuals
- **`neighborhood_demand_results.csv`**: Complete dataset with predictions and residuals

### Visualization

The heatmap displays:
- **Blue areas**: Underserved neighborhoods (negative residuals)
- **Red areas**: Over-served neighborhoods (positive residuals)
- **Coordinate system**: Spatial layout of neighborhoods
- **Colorbar**: Scale of residual values

### Model Summary

The script outputs key model parameters:
- **Intercept (α)**: Baseline log-demand
- **Infrastructure Effect (β)**: Impact of infrastructure on demand
- **Neighborhood Effect Std (σ)**: Variability in neighborhood effects

## 🔧 Dependencies

### Core Requirements

- **numpy** (≥1.21.0): Numerical computing
- **pandas** (≥1.3.0): Data manipulation
- **pymc** (≥5.0.0): Bayesian modeling
- **pytensor** (≥2.0.0): Computational backend
- **matplotlib** (≥3.5.0): Visualization

### Optional Dependencies

For enhanced functionality with real geographic data:
- **geopandas**: Geospatial data processing
- **folium**: Interactive mapping
- **shapely**: Geometric operations

## 🎯 Next Steps & Improvements

### Immediate Enhancements

1. **Real Data Integration**:
   - Replace synthetic coordinates with actual neighborhood boundaries
   - Use real scooter usage data and infrastructure metrics
   - Incorporate temporal patterns (daily/weekly seasonality)

2. **Spatial Correlation**:
   - Add spatial correlation between neighborhood random effects
   - Implement Intrinsic Conditional Autoregressive (ICAR) models
   - Account for spatial clustering of demand patterns

3. **Enhanced Visualization**:
   - Overlay heatmap on real city maps using `geopandas` and `folium`
   - Create interactive dashboards with `plotly` or `streamlit`
   - Add confidence intervals to residual estimates

### Advanced Features

4. **Model Extensions**:
   - Zero-inflated Poisson models for sparse demand data
   - Negative binomial models for overdispersed counts
   - Time-varying coefficients for dynamic demand patterns

5. **Validation & Testing**:
   - Cross-validation procedures
   - Model comparison metrics (WAIC, LOO-CV)
   - Sensitivity analysis for prior specifications

6. **Deployment**:
   - REST API for real-time demand prediction
   - Automated model retraining pipeline
   - Integration with fleet management systems

## 📚 Technical Details

### Algorithm Complexity

- **Time Complexity**: O(n²) for Laplace approximation, where n is the number of neighborhoods
- **Space Complexity**: O(n²) for storing covariance matrices
- **Convergence**: Typically converges within 20,000 iterations

### Model Assumptions

1. **Poisson Distribution**: Demand counts follow Poisson distribution
2. **Log-Linear Relationship**: Infrastructure effects are multiplicative
3. **Normal Random Effects**: Neighborhood effects are normally distributed
4. **Independence**: Neighborhoods are conditionally independent given random effects

### Limitations

- **No Spatial Correlation**: Current model assumes independent neighborhood effects
- **Synthetic Data**: Demonstration uses simulated rather than real data
- **Static Model**: No temporal dynamics or seasonality
- **Laplace Approximation**: May be less accurate than full MCMC for complex posteriors

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Install development dependencies: `pip install -r requirements-dev.txt`
4. Make your changes and add tests
5. Run tests: `pytest`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PyMC Team**: For the excellent Bayesian modeling framework
- **NumPy/Pandas Communities**: For foundational data science tools
- **Urban Planning Research**: For inspiration on spatial demand modeling

## 📞 Contact

For questions, suggestions, or collaboration opportunities:
- **Issues**: [GitHub Issues](https://github.com/yourusername/scooter-demand-model/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/scooter-demand-model/discussions)

---

**Note**: This is a demonstration project using synthetic data. For production use with real scooter data, additional validation, testing, and domain expertise are recommended.