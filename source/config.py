from pathlib import Path

# Получаем корень проекта
PROJECT_ROOT = Path(__file__).parent.parent

# Папки с данными
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# Файлы
INPUT_FILE = INPUT_DIR / "reviews.csv"
OUTPUT_FILE = OUTPUT_DIR / "sitters.csv"

# Константы для расчётов
MAX_ALPHABET_SIZE = 26
MAX_PROFILE_SCORE = 5.0
FULL_WEIGHT_THRESHOLD = 10

FLOAT_PRECISION_EPSILON = 1e-12