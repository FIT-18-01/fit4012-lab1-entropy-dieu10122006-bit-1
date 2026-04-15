# Run Log – FIT4012 Lab 1

## Entropy / Redundancy Program

### Test Results
- [x] Đã chạy với input `aaaa`
  - Entropy: 0.000000
  - Redundancy: 8.000000
  - Nhận xét: String có ký tự lặp lại hoàn toàn → entropy nhỏ nhất, redundancy lớn nhất

- [x] Đã chạy với input `abcd`
  - Entropy: 2.000000
  - Redundancy: 6.000000
  - Nhận xét: 4 ký tự khác nhau hoàn toàn → entropy = log2(4) = 2

- [x] Đã chạy với input `hello world`
  - Entropy: 2.845351
  - Redundancy: 5.154649
  - Nhận xét: Có khoảng trắng, ký tự lặp lại → entropy trung bình

## Modulo Inverse Program

### Test Results
- [x] Đã chạy với `3 7`
  - Kết quả: 5
  - Kiểm tra: 3 * 5 mod 7 = 1 ✓
  - gcd(3, 7) = 1 (inverse tồn tại)

- [x] Đã chạy với `10 17`
  - Kết quả: 12
  - Kiểm tra: 10 * 12 mod 17 = 1 ✓
  - gcd(10, 17) = 1 (inverse tồn tại)

- [x] Đã chạy với `6 9`
  - Kết quả: Không tồn tại
  - gcd(6, 9) = 3 ≠ 1 (inverse không tồn tại)

## Điều em học được từ bài lab

Bài lab này giúp hiểu sâu hơn hai khái niệm quan trọng trong lý thuyết thông tin và mật mã học:

1. **Entropy Shannon**: Đo độ bất định hay độ đa dạng của dữ liệu. Entropy cao khi ký tự phân bố đều, thấp khi có sự lặp lại.

2. **Redundancy (Dư thừa thông tin)**: Phần thông tin "dư" không cần thiết. Redundancy cao có nghĩa dữ liệu có thể được nén được (giống như string toàn `a`).

3. **Modular Inverse với Extended Euclidean**: Thuật toán tìm nghịch đảo modulo là nền tảng cho mật mã RSA. Điều kiện tồn tại là gcd(a, m) = 1.

Khó khăn lớn nhất: Hiểu được tại sao modular inverse chỉ tồn tại khi a và m nguyên tố cùng nhau (coprime).

Điều giúp hiểu rõ: Xem trực tiếp kết quả của công thức entropy trên các input khác nhau, và thấy được cách verify modular inverse bằng phép nhân modulo.
