from cleaning.cleaning import clean_temperature_data, clean_food_data
import unittest
import pandas as pd
import numpy as np

class TestCleaning(unittest.TestCase):

    def setUp(self):
        self.food_df = pd.DataFrame(data =
            {
                "Date": ["1/2001", "2/2002", "3/2003"],
                "Food Price Index": [104.3, 108.1, 107.2],
                "Meat Price Index": [445.0, 392.0, 722.0],
                "Dairy Price Index": [652.0, 678.0, 655.0],
                "Cereals Price Index": [752.0, 784.0, 763.0],
                "Oils Price Index": [158.0, 187.0, 216.0],
                "Sugar Price Index": [315.0, 337.0, 353.0]
            }
        )


    def test_clean_temperature_data(self):
        pass


    def test_clean_food_data(self):
        clean_food_df = pd.DataFrame(data =
            {
                "Date": ["1/2001", "2/2002", "3/2003"],
                "Meat Price Index": [445.0, 392.0, 722.0],
                "Dairy Price Index": [652.0, 678.0, 655.0],
                "Cereals Price Index": [752.0, 784.0, 763.0],
                "Oils Price Index": [158.0, 187.0, 216.0],
                "Sugar Price Index": [315.0, 337.0, 353.0]
            }
        )
        self.assertEquals(clean_food_df.shape, clean_food_data(self.food_df).shape)
        self.assertEquals(clean_food_df.columns.tolist(), clean_food_data(self.food_df).columns.tolist())
