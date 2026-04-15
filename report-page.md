# Report 1 Page – FIT4012 Lab 1

## 1. Mục tiêu
Bài lab nhằm giúp sinh viên hiểu và cài đặt hai khái niệm cơ bản:
1. **Entropy Shannon** và **Redundancy (dư thừa thông tin)**: Đo độ bất định và tính dư thừa của dữ liệu.
2. **Modular Inverse** bằng thuật toán **Extended Euclidean**: Nền tảng cho mật mã RSA.

## 2. Cách làm
- Đọc hiểu chương trình entropy mẫu: Tính xác suất từng ký tự và áp dụng công thức H(X) = -Σ p(x) log₂(p(x)).
- Bổ sung hàm tính redundancy: Redundancy = log₂(N) - H(X), trong đó N là kích thước bảng chữ cái.
- Hoàn thiện hàm mod_inverse(): Sử dụng thuật toán Extended Euclidean để tìm x sao cho (a·x) mod m = 1.
- Chạy thử trên nhiều test case và ghi lại kết quả.

## 3. Kết quả chính

### 3.1 Entropy và Redundancy
| Input | Entropy | Redundancy | Nhận xét |
|---|---:|---:|---|
| aaaa | 0.0000 | 8.0000 | Lặp lại hoàn toàn → entropy min, redundancy max |
| abcd | 2.0000 | 6.0000 | Phân bố đều 4 ký tự → entropy = log₂(4) |
| hello world | 2.8454 | 5.1546 | Có khoảng trắng, ký tự lặp → entropy trung bình |

### 3.2 Modulo Inverse
| a | m | Kết quả mong đợi | Kết quả chương trình | Kiểm tra | Status |
|---:|---:|---|---|---|---|
| 3 | 7 | 5 | 5 | 3·5 mod 7 = 1 | ✓ Pass |
| 10 | 17 | 12 | 12 | 10·12 mod 17 = 1 | ✓ Pass |
| 6 | 9 | Không tồn tại | Không tồn tại | gcd(6,9)=3≠1 | ✓ Pass |

## 4. Kết luận

**Các khái niệm chính:**
- **Entropy**: Thước đo độ bất định của dữ liệu. Entropy cao khi ký tự phân bố đều; thấp khi có sự lặp lại.
- **Redundancy**: Phần thông tin "dư thừa" có thể nén được. Dữ liệu có redundancy cao có ít thông tin mới.
- **Modular Inverse**: Tồn tại khi gcd(a,m)=1 (a và m nguyên tố cùng nhau). Là cơ sở của mật mã RSA.

**Khó khăn lớn nhất:** Hình dung tại sao modular inverse chỉ tồn tại khi gcd(a,m)=1, và hiểu mối liên hệ giữa extended Euclidean với việc tìm nghịch đảo.

**Điều giúp hiểu rõ hơn:** 
- Chạy thực tế trên các input khác nhau và thấy entropy giảm khi dữ liệu có xu hướng → giúp hình dung công thức.
- Verify kết quả modular inverse bằng (a·x) mod m = 1 → thấy rõ định nghĩa và cách kiểm chứng.

**Ứng dụng thực tế:** Entropy dùng trong nén dữ liệu và lý thuyết thông tin. Modular inverse dùng trong mật mã publickey RSA.
