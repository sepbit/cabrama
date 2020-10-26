"""
Cabrama - Câmbio no Brasil para Mastodon
Copyright (C) 2020  Vitor Guia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import unittest
from sepbit.cabrama.bcb import mask_money, cotacao


class BcbTest(unittest.TestCase):
    """
    Test bcb module
    """

    def test_mask_money(self):
        """
        Test mask_money function
        """
        self.assertEqual(mask_money('5,61140000'), '5,61')


    def test_cotacao(self):
        """
        Test cotacao function
        """
        self.assertTrue(cotacao())


if __name__ == '__main__':
    unittest.main()
