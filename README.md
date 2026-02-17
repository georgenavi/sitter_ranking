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
python3 -m run
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
├── source/         # Source code
├── data/
│   ├── input/      # Input CSV files
│   └── output/     # Generated results
└── tests/          # Unit tests
```

## Discussion Question

- The reviews and service provider data has several use-cases across the business - it serves as input to machine learning models, ad-hoc exploration by analysts and fed into reports used by business users. What considerations would you make and how would you model this data for its different needs?

### Data Architecture Strategy 
#### Layer 1: Raw / Source Layer

Ingest data in its original form without transformation. This preserves fidelity for reprocessing, auditing, and handling schema evolution. Partitioned by ingestion date for efficient querying.
#### Layer 2: Cleaned & Conformed Layer (Single Source of Truth)

Standardized, deduplicated, and validated records — review text, ratings, attributes of sitters/users/dogs, timestamps, relationships. This layer serves as the foundation for everything downstream and prevents logic divergence between teams.
#### Layer 3: Purpose-Specific Serving Layer

**For ML Models**:
Point-in-time feature sets that prevent data leakage. Include engineered features like rating velocity, profile completeness scores, and temporal patterns. Versioned snapshots enable reproducible model training and consistent inference. Store both historical feature sets (for training) and current features (for real-time predictions).

**For Analysts**:
Flexible, denormalized views combining reviews with users profiles and temporal dimensions. Pre-joined relationships reduce query complexity. Include both granular review-level data for deep dives and intermediate aggregations for exploratory analysis. Optimized for ad-hoc SQL queries and varying aggregation patterns.

**For Business Reports**:
Pre-aggregated metrics updated on fixed schedules (daily/weekly). Includes key performance indicators: average ratings by provider, review volume trends, ranking scores, and distribution statistics. Simple table structures aligned with business questions. Optimized for fast retrieval and dashboard rendering.
### Key Design Considerations
Temporal Consistency: Layer 2 maintains complete history with timestamps, allowing Layer 3 to reconstruct past states. Critical for ML models to avoid future data leakage and for analysts to perform historical comparisons. 

Shared Logic: Business rules (like the weighted scoring algorithm) are implemented once in Layer 2 or standardized Layer 3 processes. This ensures ML models, analysts, and reports all use identical definitions for metrics like "search_score."

Quality Gates: Validation occurs at Layer 2 ingestion: checking data types, required fields, value ranges (ratings 0-5), and referential integrity. Rejected records are quarantined for review. This prevents bad data from polluting downstream use cases.

Schema Evolution: Layer 1 captures schema changes without breaking pipelines. Layer 2 handles backwards compatibility through versioning. Layer 3 views can adapt independently based on their specific needs.

Governance: PII in review text (names, contact info) should be masked or tokenized before serving to analysts or ML; only authorized pipelines access raw text.