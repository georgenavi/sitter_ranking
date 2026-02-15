# Sitter Ranking System

## Installation
```bash
# Clone repository
git clone https://github.com/georgenavi/rover_challenge.git
cd rover_challenge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if any added later)
pip3 install -r requirements.txt
```

## Development Setup
```bash
# Install dependencies
pip3 install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=source --cov-report=html
```

## Usage
```bash
# Place reviews.csv in data/input/
# Run the script
python3 -m source.run
# Results will be in data/output/sitters.csv
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