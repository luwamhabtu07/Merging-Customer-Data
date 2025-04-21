# Customer Data Merge Problem

## ✅ Clarifying Questions
- Are all elements in `customerData1` and `customerData2` integers?
- Can both arrays be empty?
- Can there be duplicate customer IDs?

## ✅ Flowchart
See `diagram.png`.

## ✅ Time and Space Complexity

- **Time:** O(m + n) — we traverse both arrays once.
- **Space:** O(1) — in-place merge, no extra arrays used.

## ✅ Test Coverage
- ✅ Normal case
- ✅ Edge case: one array empty
- ✅ Edge case: all zeros
- ✅ Edge case: all duplicates

## ✅ Run Tests
```bash
python3 test_merge.py
