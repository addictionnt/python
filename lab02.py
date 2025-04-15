def them_sach():
    global so_luong, ten_sach_1, tac_gia_sach_1, nam_xuat_ban_sach_1, ma_sach_1, danh_gia_sach_1, gia_ban_sach_1, ten_sach_2, tac_gia_sach_2, nam_xuat_ban_sach_2, ma_sach_2, danh_gia_sach_2, gia_ban_sach_2, ten_sach_3, tac_gia_sach_3, nam_xuat_ban_sach_3, ma_sach_3, danh_gia_sach_3, gia_ban_sach_3

    so_luong = int(input("Nhập số lượng sách: "))
    if so_luong > 3:
        print("Chỉ cho phép tối đa 3 sách.")
        so_luong = 3

    for i in range(1, so_luong + 1):
        print(f"\n--- Nhập thông tin sách {i} ---")
        ten = input("Nhập tên sách: ")
        ma = input("Nhập mã sách: ")
        tac_gia = input("Nhập tên tác giả: ")
        nam = input("Nhập năm xuất bản sách: ")
        sao = input("Nhập số sao được đánh giá: ")
        gia = int(input("Nhập giá sách: "))
        if i == 1:
            ten_sach_1 = ten
            tac_gia_sach_1 = tac_gia
            nam_xuat_ban_sach_1 = nam
            ma_sach_1 = ma
            danh_gia_sach_1 = sao
            gia_ban_sach_1 = gia
        elif i == 2:
            ten_sach_2 = ten
            tac_gia_sach_2 = tac_gia
            nam_xuat_ban_sach_2 = nam
            ma_sach_2 = ma
            danh_gia_sach_2 = sao
            gia_ban_sach_2 = gia
        elif i == 3:
            ten_sach_3 = ten
            tac_gia_sach_3 = tac_gia
            nam_xuat_ban_sach_3 = nam
            ma_sach_3 = ma
            danh_gia_sach_3 = sao    
            gia_ban_sach_3 = gia

def hien_thi_sach():
    if so_luong == 0:
        print("Chưa có dữ liệu sách . Vui lòng nhập trước.")
        return

    print("\n========= DANH SÁCH SÁCH HIỆN CÓ TRONG THƯ VIỆN ========")
    print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format("STT", "Tên sách", "Tên tác giả", "Năm xuất bản", "Mã sách", "Đánh giá(sao)", "Giá bán"))

    for i in range(1, so_luong + 1):
        if i == 1:
            print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format(i, ma_sach_1, ten_sach_1, tac_gia_sach_1, nam_xuat_ban_sach_1, danh_gia_sach_1, gia_ban_sach_1))
        elif i == 2:
            print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format(i, ma_sach_2, ten_sach_2, tac_gia_sach_2, nam_xuat_ban_sach_2, danh_gia_sach_2, gia_ban_sach_2))
        elif i == 3:
            print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15}".format(i, ma_sach_3, ten_sach_3, tac_gia_sach_3, nam_xuat_ban_sach_3, danh_gia_sach_3, gia_ban_sach_3))

def tim_sach_dat_nhat():
    if so_luong == 0:
        print("Chưa có dữ liệu sách. Vui lòng nhập trước.")
        return

    max_gia = gia_ban_sach_1
    ten_max = ten_sach_1

    if so_luong >= 2 and gia_ban_sach_2 > max_gia:
        max_gia = gia_ban_sach_2
        ten_max = ten_sach_2
    if so_luong == 3 and gia_ban_sach_3 > max_gia:
        max_gia = gia_ban_sach_3
        ten_max = ten_sach_3
        
    print("Sách đắt nhất là: " , ten_max, " với giá: ", max_gia)      
    
def dat_sach():
    ma_sach_mua = input("Nhập mã sách cần mua: ")
    so_luong_mua = int(input("Nhập số lượng mua: "))
    if ma_sach_mua == ma_sach_1:
        thanh_toan = gia_ban_sach_1 * so_luong_mua
    elif ma_sach_mua == ma_sach_2:
        thanh_toan = gia_ban_sach_3 * so_luong_mua
    elif ma_sach_mua == ma_sach_3:       
        thanh_toan = gia_ban_sach_3 * so_luong_mua
           
    print("Tổng số tiền cần thanh toán: ", thanh_toan)  
while True:
    print("\n===== MENU CHƯƠNG TRÌNH =====")
    print("1. Thêm sách")
    print("2. Danh sách sách hiện có")
    print("3. Tìm sách đắt nhất")
    print("4. Mua sách")
    print("5. Thoát chương trình")
    chon = input("Chọn chức năng (1–5): ")
    if chon == "1":
        them_sach()
    elif chon == "2":
        hien_thi_sach()
    elif chon == "3":
        tim_sach_dat_nhat()
    elif chon == "4":
        dat_sach()
    elif chon == "5":
        print("Kết thúc chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")