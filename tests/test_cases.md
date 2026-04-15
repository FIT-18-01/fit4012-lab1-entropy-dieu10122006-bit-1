# Test cases – FIT4012 Lab 1

Đánh dấu [x] khi đã chạy và kiểm tra kết quả.

## 1. Entropy / Redundancy
- [x] Input: `aaaa` -> entropy = 0.0, redundancy = 8.0 (entropy thấp, redundancy cao)
- [x] Input: `abcd` -> entropy = 2.0, redundancy = 6.0 (entropy cao hơn `aaaa`)
- [x] Input: `hello world` -> entropy = 2.8454, redundancy = 5.1546 (entropy và redundancy được tính hợp lệ)

## 2. Modulo inverse
- [x] `a=3, m=7` -> nghịch đảo modulo là 5 ✓ PASS
- [x] `a=10, m=17` -> nghịch đảo modulo là 12 ✓ PASS  
- [x] `a=6, m=9` -> không tồn tại nghịch đảo modulo ✓ PASS

## 3. Ghi chú
Tất cả các test cases đã chạy thành công và kết quả đúng như mong đợi.
Entropy giảm khi ký tự trở nên đa dạng hơn.
Redundancy là độ dư thừa của thông tin (phần thông tin "dư" không cần thiết).
Modular inverse tồn tại khi gcd(a, m) = 1.
