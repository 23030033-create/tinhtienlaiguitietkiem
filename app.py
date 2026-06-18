https://guitietkiem-8lekvwbqmlbsgruwlh7x2a.streamlit.app/
https://sharpe-ratio-app-p4ybxr4g8avwdcbfl8ftnb.streamlit.app/
https://colab.research.google.com/
Không dùng CHAT GPT
C=500.000.000
i=5%
n=3
A=c*(i*n+1)
print (A)
a=500000000
b=0.05
c=3 
d=a*(b*c+1)
print(d)
a=500000000
b=0.05
c=3/12
d=a*(b*c+1)
print(d)
a=500
b=5/100
n=3
c=a*(b*n+1)
print(c)
C = 500000000
i = 0.05 / 12
n = 3
An = C * (i * n + 1)
print("Tong so tien nhan duoc la:", An)
C=500000000
i=0.05/12
n=3
An=C*(i*n+1)
print(An)
506250000.0
c=500000000
i=0.05
n=0.25
an=c*(i*n+1)
print("tong tien =", an)
Code tính tiền phòng trọ
A=float(input("Nhập số tiền phòng: "))
a=float(input("Nhập số điện đầu tháng: "))
b=float(input("Nhập số điện cuối tháng: "))
c=float(input("Nhập đơn giá 1 số điện: "))
B=(b-a)*c
x=float(input("Nhập số nước đầu tháng: "))
y=float(input("Nhập số nước cuối tháng: "))
z=float(input("Nhập đơn giá 1 số nước: "))
C=(y-x)*z
D=A+B+C 
print(f"Tổng số tiền phòng trọ của 1 tháng: {D:,.2f} đồng")
Streamlit
https://github.com/
import streamlit as st

# Tiêu đề ứng dụng
st.title("🏠 TÍNH TIỀN PHÒNG TRỌ HÀNG THÁNG")

# Nhập tiền phòng
A = st.number_input(
    "Nhập số tiền phòng (đồng)",
    min_value=0.0,
    value=3000000.0
)

# Nhập chỉ số điện
st.subheader("⚡ Tiền điện")
a = st.number_input(
    "Nhập số điện đầu tháng",
    min_value=0.0,
    value=100.0
)

b = st.number_input(
    "Nhập số điện cuối tháng",
    min_value=0.0,
    value=150.0
)

c = st.number_input(
    "Nhập đơn giá 1 số điện (đồng)",
    min_value=0.0,
    value=3500.0
)

# Nhập chỉ số nước
st.subheader("💧 Tiền nước")
x = st.number_input(
    "Nhập số nước đầu tháng",
    min_value=0.0,
    value=20.0
)

y = st.number_input(
    "Nhập số nước cuối tháng",
    min_value=0.0,
    value=30.0
)

z = st.number_input(
    "Nhập đơn giá 1 số nước (đồng)",
    min_value=0.0,
    value=15000.0
)

# Nút tính toán
if st.button("Tính tiền phòng trọ"):
    B = (b - a) * c
    C = (y - x) * z
    D = A + B + C

    st.success(f"Tổng tiền điện: {B:,.0f} đồng")
    st.success(f"Tổng tiền nước: {C:,.0f} đồng")
    st.success(f"Tổng tiền phòng trọ của 1 tháng: {D:,.0f} đồng")
requirements.txt
streamlit
https://streamlit.io/cloud
https://tinh-tien-tro-mjhmxovp8bueaxvqspjuna.streamlit.app/
https://nwwlrrnd9awcac3zwnls66.streamlit.app/
https://tinhtientro-6tllrwajzwjte5zqeebbip.streamlit.app/
https://tinhtientro-auvbxsfegp8q9hu5eo89uf.streamlit.app/
https://tinhtientro-mlk8dyj5kkousn7nxkvwsb.streamlit.app/
@All thứ 5 ngày 11/6 lớp mình nghỉ học nhé. Thầy sẽ dạy bù sau. Cảm ơn các em nhé!
@All thứ 5 tuần này (ngày 11/6) lớp mình nghỉ học nhé. Thầy sẽ dạy bù sau, cảm ơn các em nhé!
@All ngày mai thứ 5 (ngày 18/7) bạn nào có laptop mang theo đi học nhé, thầy hướng dẫn thiết kế và xây dựng app về tài chính.
https://github.com/
import streamlit as st
st.image("logo.jpg")
# Tiêu đề app
st.title("APP TÍNH TIỀN GỬI TIẾT KIỆM_ĐỀ TÀI 2_TS. VŨ ĐỨC BÌNH")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng gửi",
    min_value=1,
    value=12
)

# Đổi % sang số thập phân
i = i / 100

# Nút tính toán
if st.button("Tính toán"):
    
    # Lãi đơn
    A = C * (1 + i * n / 12)

    # Lãi kép
    B = C * (1 + i / 12) ** n

    st.subheader("Kết quả")

    st.success(
        f"Tổng tiền nhận được theo lãi đơn: {A:,.4f} triệu đồng"
    )

    st.success(
        f"Tổng tiền nhận được theo lãi kép: {B:,.4f} triệu đồng"
    )
