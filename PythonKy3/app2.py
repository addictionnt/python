from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)

DATA_FILE = "luu_tru.json"

def luu_du_lieu(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Dữ liệu đã được lưu vào {DATA_FILE}")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu: {e}")
        flash(f"Lỗi khi lưu dữ liệu: {e}", "danger")

def doc_du_lieu():
    if not os.path.exists(DATA_FILE):
        print(f"File {DATA_FILE} không tồn tại. Tạo file mới.")
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Dữ liệu đã được đọc từ {DATA_FILE}")
        return data
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu: {e}")
        flash(f"Lỗi khi đọc dữ liệu: {e}", "danger")
        return {}

danh_sach_luu_tru = doc_du_lieu()

@app.route('/')
def trang_chu():
    return render_template('trang_chu.html')

@app.route('/them-tai-khoan', methods=['GET', 'POST'])
def them_tai_khoan_nguoi_dung():
    if request.method == 'POST':
        ma_nguoi_dung = request.form['ma_nguoi_dung']
        if ma_nguoi_dung in danh_sach_luu_tru:
            flash("Mã người dùng đã tồn tại!", "danger")
            return render_template('them_tai_khoan.html', error="Mã người dùng đã tồn tại!")
        ten_dang_nhap = request.form['ten_dang_nhap']
        mat_khau = request.form['mat_khau']
        kiem_tra_mat_khau = request.form['kiem_tra_mat_khau']
        if mat_khau != kiem_tra_mat_khau:
            flash("Mật khẩu không trùng khớp!", "danger")
            return render_template('them_tai_khoan.html', error="Mật khẩu không trùng khớp!")
        ho_ten = request.form['ho_ten']
        ngay_sinh = request.form['ngay_sinh']
        dia_chi = request.form['dia_chi']

        nguoi_dung_moi = {
            "ten_dang_nhap": ten_dang_nhap,
            "mat_khau": mat_khau,
            "thong_tin": {
                "ho_ten": ho_ten,
                "ngay_sinh": ngay_sinh,
                "dia_chi": dia_chi
            },
            "tai_khoan_luu_tru": {}
        }
        danh_sach_luu_tru[ma_nguoi_dung] = nguoi_dung_moi
        luu_du_lieu(danh_sach_luu_tru)
        flash("Thêm tài khoản thành công!", "success")
        return redirect(url_for('danh_sach_nguoi_dung'))
    return render_template('them_tai_khoan.html', error=None)

@app.route('/danh-sach-nguoi-dung')
def danh_sach_nguoi_dung():
    return render_template('danh_sach_nguoi_dung.html', danh_sach=danh_sach_luu_tru)

@app.route('/xoa-tai-khoan/<ma_nguoi_dung>', methods=['POST'])
def xoa_tai_khoan_nguoi_dung(ma_nguoi_dung):
    if ma_nguoi_dung in danh_sach_luu_tru:
        del danh_sach_luu_tru[ma_nguoi_dung]
        luu_du_lieu(danh_sach_luu_tru)
        flash("Xóa tài khoản thành công!", "success")
    else:
        flash("Mã người dùng không tồn tại!", "danger")
    return redirect(url_for('danh_sach_nguoi_dung'))

@app.route('/sua-tai-khoan/<ma_nguoi_dung>', methods=['GET', 'POST'])
def sua_tai_khoan_nguoi_dung(ma_nguoi_dung):
    if ma_nguoi_dung not in danh_sach_luu_tru:
        flash("Mã người dùng không tồn tại!", "danger")
        return redirect(url_for('danh_sach_nguoi_dung'))
    if request.method == 'POST':
        ten_dang_nhap = request.form['ten_dang_nhap']
        mat_khau = request.form['mat_khau']
        kiem_tra_mat_khau = request.form['kiem_tra_mat_khau']
        if mat_khau != kiem_tra_mat_khau:
            flash("Mật khẩu không trùng khớp!", "danger")
            return render_template('sua_tai_khoan.html', ma_nguoi_dung=ma_nguoi_dung, thong_tin=danh_sach_luu_tru[ma_nguoi_dung])
        ho_ten = request.form['ho_ten']
        ngay_sinh = request.form['ngay_sinh']
        dia_chi = request.form['dia_chi']

        danh_sach_luu_tru[ma_nguoi_dung]["ten_dang_nhap"] = ten_dang_nhap
        danh_sach_luu_tru[ma_nguoi_dung]["mat_khau"] = mat_khau
        danh_sach_luu_tru[ma_nguoi_dung]["thong_tin"]["ho_ten"] = ho_ten
        danh_sach_luu_tru[ma_nguoi_dung]["thong_tin"]["ngay_sinh"] = ngay_sinh
        danh_sach_luu_tru[ma_nguoi_dung]["thong_tin"]["dia_chi"] = dia_chi
        luu_du_lieu(danh_sach_luu_tru)
        flash("Cập nhật tài khoản thành công!", "success")
        return redirect(url_for('danh_sach_nguoi_dung'))
    return render_template('sua_tai_khoan.html', ma_nguoi_dung=ma_nguoi_dung, thong_tin=danh_sach_luu_tru[ma_nguoi_dung])

@app.route('/them-tai-khoan-luu-tru', methods=['GET', 'POST'])
def them_tai_khoan_luu_tru():
    if request.method == 'POST':
        ma_nguoi_dung = request.form['ma_nguoi_dung']
        if ma_nguoi_dung not in danh_sach_luu_tru:
            flash("Mã người dùng không tồn tại!", "danger")
            return render_template('them_tai_khoan_luu_tru.html', error="Mã người dùng không tồn tại!")
        ma_tai_khoan = request.form['ma_tai_khoan']
        tai_khoan = request.form['tai_khoan']
        mat_khau = request.form['mat_khau_tk']
        ghi_chu = request.form['ghi_chu']

        if "tai_khoan_luu_tru" not in danh_sach_luu_tru[ma_nguoi_dung]:
            danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"] = {}
        danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan] = {
            "tai_khoan": tai_khoan,
            "mat_khau": mat_khau,
            "ghi_chu": ghi_chu
        }
        luu_du_lieu(danh_sach_luu_tru)
        flash("Thêm tài khoản lưu trữ thành công!", "success")
        return redirect(url_for('danh_sach_tai_khoan_luu_tru', ma_nguoi_dung=ma_nguoi_dung))
    return render_template('them_tai_khoan_luu_tru.html', error=None)

@app.route('/danh-sach-tai-khoan-luu-tru/<ma_nguoi_dung>')
def danh_sach_tai_khoan_luu_tru(ma_nguoi_dung):
    if ma_nguoi_dung not in danh_sach_luu_tru:
        flash("Mã người dùng không tồn tại!", "danger")
        return redirect(url_for('danh_sach_nguoi_dung'))
    danh_sach_tai_khoan = danh_sach_luu_tru[ma_nguoi_dung].get("tai_khoan_luu_tru", {})
    return render_template('danh_sach_tai_khoan_luu_tru.html', ma_nguoi_dung=ma_nguoi_dung, danh_sach_tai_khoan=danh_sach_tai_khoan)

@app.route('/xoa-tai-khoan-luu-tru/<ma_nguoi_dung>/<ma_tai_khoan>', methods=['POST'])
def xoa_tai_khoan_luu_tru(ma_nguoi_dung, ma_tai_khoan):
    if ma_nguoi_dung not in danh_sach_luu_tru:
        flash("Mã người dùng không tồn tại!", "danger")
        return redirect(url_for('danh_sach_nguoi_dung'))
    if "tai_khoan_luu_tru" in danh_sach_luu_tru[ma_nguoi_dung] and ma_tai_khoan in danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"]:
        del danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan]
        luu_du_lieu(danh_sach_luu_tru)
        flash("Xóa tài khoản lưu trữ thành công!", "success")
    else:
        flash("Mã tài khoản không tồn tại!", "danger")
    return redirect(url_for('danh_sach_tai_khoan_luu_tru', ma_nguoi_dung=ma_nguoi_dung))

@app.route('/sua-tai-khoan-luu-tru/<ma_nguoi_dung>/<ma_tai_khoan>', methods=['GET', 'POST'])
def sua_tai_khoan_luu_tru(ma_nguoi_dung, ma_tai_khoan):
    if ma_nguoi_dung not in danh_sach_luu_tru:
        flash("Mã người dùng không tồn tại!", "danger")
        return redirect(url_for('danh_sach_nguoi_dung'))
    if "tai_khoan_luu_tru" not in danh_sach_luu_tru[ma_nguoi_dung] or ma_tai_khoan not in danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"]:
        flash("Mã tài khoản không tồn tại!", "danger")
        return redirect(url_for('danh_sach_tai_khoan_luu_tru', ma_nguoi_dung=ma_nguoi_dung))
    if request.method == 'POST':
        tai_khoan = request.form['tai_khoan']
        mat_khau = request.form['mat_khau_tk']
        ghi_chu = request.form['ghi_chu']

        danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan]["tai_khoan"] = tai_khoan
        danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan]["mat_khau"] = mat_khau
        danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan]["ghi_chu"] = ghi_chu
        luu_du_lieu(danh_sach_luu_tru)
        flash("Cập nhật tài khoản lưu trữ thành công!", "success")
        return redirect(url_for('danh_sach_tai_khoan_luu_tru', ma_nguoi_dung=ma_nguoi_dung))
    return render_template('sua_tai_khoan_luu_tru.html', ma_nguoi_dung=ma_nguoi_dung, ma_tai_khoan=ma_tai_khoan, thong_tin=danh_sach_luu_tru[ma_nguoi_dung]["tai_khoan_luu_tru"][ma_tai_khoan])

@app.route('/chi-tiet-tai-khoan/<ma_nguoi_dung>')
def chi_tiet_tai_khoan(ma_nguoi_dung):
    if ma_nguoi_dung not in danh_sach_luu_tru:
        flash("Mã người dùng không tồn tại!", "danger")
        return redirect(url_for('danh_sach_nguoi_dung'))
    thong_tin_tai_khoan = danh_sach_luu_tru[ma_nguoi_dung]
    return render_template('chi_tiet_tai_khoan.html', ma_nguoi_dung=ma_nguoi_dung, thong_tin_tai_khoan=thong_tin_tai_khoan)

if __name__ == '__main__':
    app.run(debug=True)
