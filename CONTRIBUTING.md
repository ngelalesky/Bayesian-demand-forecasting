# Contributing to Scooter Demand Model

Thank you for your interest in contributing to the Scooter Demand Model project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of Bayesian statistics and hierarchical modeling

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/scooter-demand-model.git
   cd scooter-demand-model
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular

### Testing

- Write tests for new functionality
- Ensure existing tests pass
- Aim for good test coverage

### Documentation

- Update README.md for significant changes
- Add docstrings to new functions
- Include examples in docstrings where helpful

## 📝 How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Use the issue template
3. Provide clear reproduction steps
4. Include system information (OS, Python version, etc.)

### Suggesting Enhancements

1. Open an issue with the "enhancement" label
2. Describe the proposed feature clearly
3. Explain the use case and benefits
4. Consider implementation complexity

### Submitting Code

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clean, well-documented code
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   python -m pytest  # If tests exist
   python scooter_demand_model.py  # Run main script
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Reference any related issues
   - Provide a detailed description of changes
   - Include screenshots for UI changes

## 🎯 Areas for Contribution

### High Priority

- **Real Data Integration**: Replace synthetic data with real scooter usage data
- **Spatial Correlation**: Add spatial correlation between neighborhood effects
- **Enhanced Visualization**: Interactive maps and better plotting
- **Model Validation**: Cross-validation and model comparison tools

### Medium Priority

- **Performance Optimization**: Faster model fitting and sampling
- **Additional Models**: Zero-inflated Poisson, Negative Binomial variants
- **API Development**: REST API for model predictions
- **Documentation**: Tutorials and advanced examples

### Low Priority

- **Testing Framework**: Comprehensive test suite
- **CI/CD Pipeline**: Automated testing and deployment
- **Docker Support**: Containerized deployment
- **Web Interface**: User-friendly web application

## 📋 Pull Request Process

1. **Ensure your PR**:
   - Has a clear, descriptive title
   - Includes a detailed description
   - References related issues
   - Passes all tests
   - Follows code style guidelines

2. **Review Process**:
   - Maintainers will review your PR
   - Address any feedback promptly
   - Make requested changes in new commits

3. **After Approval**:
   - Your PR will be merged
   - You'll be credited in the project

## 🏷️ Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add: new feature description
Fix: bug description
Update: change description
Remove: removal description
Docs: documentation changes
Test: test additions or changes
```

Examples:
- `Add: spatial correlation model for neighborhood effects`
- `Fix: handle edge case in residual calculation`
- `Update: improve heatmap visualization colors`
- `Docs: add installation instructions for Windows`

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**:
   - Operating system and version
   - Python version
   - Package versions (from `pip list`)

2. **Reproduction**:
   - Clear steps to reproduce the issue
   - Expected vs. actual behavior
   - Error messages (if any)

3. **Additional Context**:
   - Screenshots (if applicable)
   - Related issues or discussions

## 💡 Feature Requests

When suggesting features:

1. **Problem Statement**: What problem does this solve?
2. **Proposed Solution**: How should it work?
3. **Alternatives**: What other approaches were considered?
4. **Additional Context**: Any other relevant information

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: For sensitive or private matters

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to the Scooter Demand Model project!