"""Test end-to-end data processing pipeline."""

import pytest
import csv
from pathlib import Path
from source.csv_reader import load_sitters
from source.csv_writer import save_sitters


@pytest.fixture
def sample_reviews(tmp_path):
    """Create sample CSV with various scenarios."""
    input_file = tmp_path / "reviews.csv"

    with open(input_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sitter_email', 'sitter', 'rating'])

        # Veteran: 10 reviews alternating 5.0 and 4.5
        for i in range(10):
            rating = 5.0 if i % 2 == 0 else 4.5
            writer.writerow(['veteran@example.com', 'Veteran Sitter', rating])

        # Newbie: 1 perfect review
        writer.writerow(['newbie@example.com', 'Newbie Sitter', 5.0])

        # Nobody: no rating
        writer.writerow(['nobody@example.com', 'Nobody Sitter', ''])

    return input_file, tmp_path


class TestDataPipeline:
    """Validates complete data flow through the system."""

    def test_load_aggregate_and_save(self, sample_reviews):
        """
        Test complete pipeline: load → aggregate → save.
        Ensures data flows correctly through all components.
        """
        input_file, tmp_path = sample_reviews
        output_file = tmp_path / "output.csv"

        # Step 1: Load and verify aggregation
        sitters = load_sitters(input_file)

        assert len(sitters) == 3, "Should load 3 unique sitters"

        # Verify veteran sitter (10 ratings)
        veteran = sitters["veteran@example.com"]
        assert veteran.name == "Veteran Sitter"
        assert len(veteran.ratings) == 10
        assert veteran.average_rating() == 4.75

        # Verify newbie sitter (1 rating)
        newbie = sitters["newbie@example.com"]
        assert len(newbie.ratings) == 1
        assert newbie.ratings[0] == 5.0

        # Verify sitter with no ratings
        nobody = sitters["nobody@example.com"]
        assert len(nobody.ratings) == 0

        # Step 2: Save results
        save_sitters(list(sitters.values()), output_file)
        assert output_file.exists(), "Output file should be created"

        # Step 3: Verify output format and content
        with open(output_file) as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3, "Output should contain 3 sitters"

        # Verify veteran ranks first (10 ratings at 4.75 avg)
        assert rows[0]["email"] == "veteran@example.com"
        assert float(rows[0]["search_score"]) == pytest.approx(4.75, abs=0.01)

        # Verify all required columns exist
        required_columns = ["email", "name", "profile_score", "ratings_score", "search_score"]
        for row in rows:
            for col in required_columns:
                assert col in row, f"Column '{col}' should exist in output"
                assert row[col], f"Column '{col}' should not be empty"