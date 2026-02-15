# Sitter Ranking System
A Python-based system for ranking pet sitters based on customer reviews using a weighted scoring algorithm.

The ranking algorithm intelligently balances profile quality with customer ratings, gradually shifting weight from profile scores to ratings as sitters accumulate more reviews:

- **0 reviews**: 100% profile score (based on name diversity)
- **1-9 reviews**: Weighted blend transitioning from profile to ratings
- **10+ reviews**: 100% ratings score (average of all reviews)

## Installation
```bash
# Clone repository
git clone https://github.com/georgenavi/sitter_ranking.git
cd sitter_ranking

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if any added later)
pip3 install -r requirements.txt
```

## Usage
```bash
# Place reviews.csv in data/input/
# Run the script
python3 -m source.run
# Results will be in data/output/sitters.csv
```

## Development Setup
```bash
# Clone repository
git clone https://github.com/georgenavi/sitter_ranking.git
cd sitter_ranking

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip3 install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=source --cov-report=html
```

## Project Structure
```
rover_challenge/
├── source/          # Source code
├── data/
│   ├── input/      # Input CSV files
│   └── output/     # Generated results
└── tests/          # Unit tests
```