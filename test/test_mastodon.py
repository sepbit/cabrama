'''
Cabrama - Câmbio no Brasil para Mastodon
Copyright (C) 2020-2022 Vitor Guia

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
'''

import unittest
from os import environ
from sepbit.sistamapy.statuses import Statuses


class MastodonTest(unittest.TestCase):
    '''
    Test Mastodon integration 
    '''

    def test_statuses(self):
        toot = Statuses(
            environ['INSTANCE'],
            environ['TOKEN'],
        )
        
        '''
        Test statuses function
        '''
        result = toot.post({
            'status': 'teste',
            'language': 'por',
            'visibility': 'public'
        })

        self.assertTrue(result)

        '''
        Test delete function
        '''
        self.assertTrue(
            toot.delete( result['id'] )
        )


if __name__ == '__main__':
    unittest.main()
