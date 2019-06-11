# Music Genres Identification (MGI)

### Bài tập nhận diện thể loại bài hát thông qua file nhạc

- Họ tên sinh viên: Dương Quang Khải
- MSSV: 16020242

MGI bao gồm web app dùng để upload file nhạc và trả lại cho người dùng thể loại bài hát mà hệ thống nhận diện được. Độ chính xác của mô hình đạt ~73%

### Cách chạy
#### Hiện tại phần mềm đã thử nghiệm chạy thành công với Ubuntu 18.04

- Mở terminal và gõ những dòng sau
```sh
	cd music_genres_identification/web
	node app.js
```

- Mở trình duyệt với địa chỉ: 
```sh
	http://locahost:3000
```

- Upload 1 file nhạc lên. <b>Lưu ý: Chỉ up file định dạng mp3</b>. Xong ấn nút <b>Show me </b>
- Chờ khoảng từ 30-40s để hệ thống chạy nhận diện. Kết quả sẽ được trả về ngay khi xong.


