# Tests for the Unit 1 Assessment 1 programming examples.

import unittest

from assessment_1_examples import (
    calculate_order_total,
    format_recent_alerts,
    lab_access_message,
    learner_profile,
)


class AssessmentExamplesTests(unittest.TestCase):
    def test_variables_keep_their_expected_types(self) -> None:
        name, age, is_student = learner_profile()
        self.assertIsInstance(name, str)
        self.assertIsInstance(age, int)
        self.assertIsInstance(is_student, bool)

    def test_sequence_calculates_vat_before_total(self) -> None:
        self.assertEqual(calculate_order_total(50.00), 60.00)

    def test_selection_approves_only_safe_lab_access(self) -> None:
        self.assertEqual(lab_access_message(True, True), "Lab access approved")
        self.assertEqual(lab_access_message(True, False), "Lab access blocked")

    def test_iteration_formats_every_alert(self) -> None:
        self.assertEqual(
            format_recent_alerts(["camera zone", "training complete"]),
            ["KORA alert: camera zone", "KORA alert: training complete"],
        )


if __name__ == "__main__":
    unittest.main()
