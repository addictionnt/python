list = []

def nhap_thong_tin_sach(list):
    
    soLuong = int(input("Nhập số lượng sách thêm: "))
    for i in range(0, soLuong):
        print(f"Nhập thông tin sách: {i + 1}")
        tenSach = input("Nhập tên sách: ")
        tacGia = input("Nhập tên tác giả: ")
        giaBan = input("Nhập giá sách: ")
        danhGia = input("Nhập số sao(1/2/3/4/5): ")
        
        def tu_danh_gia(danhGia):
            if danhGia == "5":
                return "Tốt"
            elif danhGia == "4":
                return "Khá Tốt"
            elif danhGia == "3":
                return "Tốt"
            elif danhGia == "2":
                return "Trung bình"
            else:
                return "Kém"
        
        xepLoai = tu_danh_gia(danhGia)
          
        Sach = {
            "ten_sach" : tenSach,
            "tac_gia" : tacGia,
            "gia_ban" : giaBan,
            "danh_gia" : danhGia,
            "xep_loai" : xepLoai
        }
        list.append(Sach)
        
def hien_thi_danh_sach(list):
    print("{:<15} {:<20}".format("","=====DANH SÁCH SÁCH====="))
    print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format("STT","Tên sách","Tác giả","Giá sách","Đánh giá","Xếp loại"))
    for i,sach in enumerate(list):
        print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i+1,sach.get("ten_sach", ""),sach.get("tac_gia", ""), sach.get("gia_ban", ""), sach.get("danh_gia", ""), sach.get("xep_loai")))
        
while True:
    print("Menu chương trình")
    print("1. Thêm sách")
    print("2. Hiển thị danh sách")
    print("3. Thoát")
    
    chon = input("Chọn chức năng: ")
    
    if chon == "1":
        nhap_thong_tin_sach(list)
    if chon == "2":
        hien_thi_danh_sach(list)
    if chon == "3":
        break
        