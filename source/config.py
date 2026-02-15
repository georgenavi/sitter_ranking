from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

INPUT_FILE = INPUT_DIR / "reviews.csv"
OUTPUT_FILE = OUTPUT_DIR / "sitters.csv"

MAX_ALPHABET_SIZE = 26
MAX_PROFILE_SCORE = 5.0
FULL_WEIGHT_THRESHOLD = 10

FLOAT_PRECISION_EPSILON = 1e-12