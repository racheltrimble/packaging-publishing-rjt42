import unittest
from cancer_prediction_rjt42 import CancerModel

class TestCancerModel(unittest.TestCase):

    def test_diagnosis_target_translation_and_inverse(self):
        model = CancerModel()
        for diagnosis, code in [("Benign", 1) , ("Malignant", 0)]:
            target = model.diagnosis_to_target(diagnosis)
            self.assertEqual (target, code)
            diagnosis_test = model.target_to_diagnosis(target)
            self.assertEqual (diagnosis, diagnosis_test)
