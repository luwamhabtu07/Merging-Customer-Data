
import unittest
from merge import merge

class TestMergeFunction(unittest.TestCase):
    def test_normal_case(self):
        data1=[101,104,107,0,0,0]
        merge(data1,3,[102,105,108],3)
        self.assertEqual(data1,[101,102,104,105,107,108])

    def test_only_data1(self):
        data1=[103]
        merge(data1,1,1,[],0)
        self.assertEqual(data1,[103])

    def test_only_data2(self):
        data1=[0]
        merge(data1,0,[103], 1)
        self.assertEqual(data1,[103])

    def test_duplicates(self):
        data1=[100,100,0,0]
        merge(data1,2,[100,100], 2)
        self.assertEqual(data1,[100,100,100,100])

    def test_data2_smaller(self):
        data1=[105,106,107,0,0,0]
        merge(data1,3,[101,102,103], 3)
        self.assertEqual(data1, [101,102,103,105,106,107])

    def test_data1_empty(self):
        data1 = [0,0,0]
        merge(data1,0, [101,102,103],3)
        self.assertEqual(data1, [101,102,103])

if __name__ == '__main__':
    unittest.main()
    
    
        
