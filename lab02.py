danh_sach_sach = []

def xep_loai_danh_gia(danh_gia):
    if danh_gia == "5":
        return "Tốt"
    elif danh_gia == "4":
        return "Khá Tốt"
    elif danh_gia == "3":
        return "Tốt"
    elif danh_gia == "2":
        return "Trung bình"
    else:
        return "Kém"

def nhap_thong_tin_sach():
    
    so_luong = int(input("Nhập số lượng sách thêm: "))
    for i in range(0, so_luong):
        print(f"Nhập thông tin sách: {i + 1}")
        ten_sach = input("Nhập tên sách: ")
        tac_gia = input("Nhập tên tác giả: ")
        gia_ban = input("Nhập giá sách: ")
        danh_gia = input("Nhập số sao(1/2/3/4/5): ")
        xep_loai = xep_loai_danh_gia(danh_gia)
          
        thong_tin_sach = {
            "ten_sach" : ten_sach,
            "tac_gia" : tac_gia,
            "gia_ban" : gia_ban,
            "danh_gia" : danh_gia,
            "xep_loai" : xep_loai
        }
        danh_sach_sach.append(thong_tin_sach)
        
def hien_thi_danh_sach():
    print("{:<15} {:<20}".format("","=====DANH SÁCH SÁCH====="))
    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format("STT","Tên sách","Tác giả","Giá sách","Đánh giá","Xếp loại"))
    for i,sach in enumerate(danh_sach_sach):
        print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i+1,sach.get("ten_sach", ""),sach.get("tac_gia", ""), sach.get("gia_ban", ""), sach.get("danh_gia", ""), sach.get("xep_loai")))
        
while True:
    print("Menu chương trình")
    print("1. Thêm sách")
    print("2. Hiển thị danh sách")
    print("3. Thoát")
    
    chon = input("Chọn chức năng: ")
    
    if chon == "1":
        nhap_thong_tin_sach()
    if chon == "2":
        hien_thi_danh_sach()
    if chon == "3":
        break
        
