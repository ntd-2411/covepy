Bài1: Python là ngôn ngữ thông dịch, vì lí do nằm ở cách thực thi mã 
- Không cần biên dịch trước: bạn viết mã Python và chạy trực tiếp, không phải qua bước chuyển mã sang dạng máy hiểu như các ngôn ngữ biên dịch ví dụ như C, C++
- Mã được chạy thông qua trình thông dịch: python sử dụng trình thông dịch như CPython để đọc từng dòng mã và thực hiện ngay tại thời điểm chạy 
- Tính linh hoạt cao:Vì không cần biên dịch trước, bạn có thể thử nghiệm nhanh, sửa mã linh hoạt - rất phù hợp với phát triển ứng dụng, khao học dữ liệu, AI 

Bài 2
1, Các kiểu dữ liệu trong Python 
int:	Số nguyên	Ví dụ: 5, -10
float:	Số thực (dấu phẩy động)	Ví dụ: 3.14, -0.5
complex:	Số phức	Ví dụ: 2 + 3j
str:	Chuỗi ký tự	Ví dụ: "Hello", 'Python'
bool:	Boolean (True/False)	Ví dụ: True, False
list:	Danh sách có thể thay đổi	Ví dụ: [1, "a", 3.5]
tuple:	Danh sách không thay đổi	Ví dụ: (1, 2, 3)
set:	Tập hợp không trùng lặp	VÍ dụ: {1, 2, 3}
dict:	Từ điển (key-value)	Ví dụ: {"name": "Đỗ", "age": 20}
2, Các toán tử trong Python 
-Toán tử số học
+, -, *, /, //, %, **

-Toán tử so sánh
==, !=, >, <, >=, <=

-Toán tử logic
and, or, not

-Toán tử gán
=, +=, -=, *=, //=, v.v.

-Toán tử kiểm tra thành viên
in, not in

-Toán tử định danh
is, is not
3, Mệnh đề điều kiện và vòng lặp
- Mệnh đề điều kiện
if x > 0:
    print("Số dương")
elif x == 0:
    print("Số 0")
else:
    print("Số âm")
- Vòng lặp
while loop: Lặp khi điều kiện còn đúng
i = 0
while i < 5:
    print(i)
    i += 1
for loop: Lặp qua chuỗi, danh sách, range
for i in range(5):
    print(i)
- Kiểu dữ liệu True / False (Boolean)
Chỉ có hai giá trị: True và False
Dùng trong điều kiện, vòng lặp, kiểm tra logic
Một số giá trị được coi là False: 0, "", [], {}, None
print(bool(0))       # False
print(bool("Hello")) # True