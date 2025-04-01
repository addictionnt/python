while True:
    print("-----------------------------------------")
    print("1. Hiển thị danh sách sách")
    print("2. Tìm kiếm sách theo mã sách")
    print("3. Tìm kiếm sách theo tên")
    print("4. Tìm kiếm sách theo tác giả")
    print("5. Thêm sách mới")
    print("6. Cập nhật thông tin sách")
    print("7. Xoá sách")
    print("8. Lọc sách theo yêu cầu")
    print("9. Tính tổng số lượng sách")
    print("10. Danh sách sách > 100000")
    print("11. Thoát")
    print("-----------------------------------------")
    lua_chon = int(input("Nhập lựa chọn của bạn: "))
    if lua_chon == 1:
        print("Thực hiện chức năng: 1. Hiển thị danh sách sách")
    elif lua_chon == 2:
        print("Thực hiện chức năng: 2. Tìm kiếm sách theo mã sách")
    elif lua_chon == 3:
        print("Thực hiện chức năng: 3. Tìm kiếm sách theo tên")
    elif lua_chon == 4:
        print("Thực hiện chức năng: 4. Tìm kiếm sách theo tác giả")
    elif lua_chon == 5:
        print("Thực hiện chức năng: 5. Thêm sách mới")
    elif lua_chon == 6:
        print("Thực hiện chức năng: 6. Cập nhật thông tin sách")
    elif lua_chon == 7:
        print("Thực hiện chức năng: 7. Xoá sách")
    elif lua_chon == 8:
        print("Thực hiện chức năng: 8. Lọc sách theo yêu cầu")
    elif lua_chon == 9:
        print("Thực hiện chức năng: 9. Tính tổng số lượng sách")
    elif lua_chon == 10:
        print("Thực hiện chức năng: Danh sách sách > 100000")
    elif lua_chon == 11:
        print("Thoát")
        break
    else:
        print("Lựa chọn không phù hợp, yêu cầu thực hiện lại!")