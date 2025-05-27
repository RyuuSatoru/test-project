# 🧠 Test-project

**Trợ lý truy vấn dữ liệu đa phương tiện**
Dự án AI này hỗ trợ truy vấn thông minh trên nhiều định dạng dữ liệu như video, ảnh, âm thanh, và văn bản — tất cả được xử lý trước, chuẩn hóa, và phản hồi qua mô hình ngôn ngữ lớn (LLM).

> 🎯 *Mục tiêu: Trích xuất và phân tích dữ liệu đa phương tiện để hỗ trợ tìm kiếm thông tin bằng ngôn ngữ tự nhiên.*

---

## 🚀 Tính năng chính

- ✅ Tự động nhận diện loại dữ liệu cần xử lý từ prompt người dùng.
- 🧩 Hỗ trợ 4 loại dữ liệu: `video`, `image`, `audio`, và `document`.
- 📚 Kết hợp thông tin ngữ cảnh vào prompt đầu vào.
- 🤖 Gửi prompt đầy đủ đến LLM (như Gemini / GPT) để phản hồi.
- 🧪 Chạy hoàn toàn được trên Google Colab hoặc máy cục bộ.
- 🛠 Dễ mở rộng và chỉnh sửa: mọi phần xử lý chia thành các module riêng.

---

## 📓 Dùng trên Google Colab

Bạn có thể chạy toàn bộ project này chỉ trong vài bước đơn giản:
Link Google Colab
```python
https://colab.research.google.com/github/RyuuSatoru/test-project/blob/main/project.ipynb
```

### Bước 1: Tải project
### Bước 2: Cài thư viện
### Bước 3: Tiền xử lý dữ liệu media
### Bước 4: Khởi chạy truy vấn (có UI nhập prompt)

## 💻 Dùng trên máy cục bộ (Local Machine)
```python
git clone https://github.com/RyuuSatoru/test-project.git
cd test-project
pip install -r requirements.txt
python Run-test.py
python Run.py
```
## 📍 Ghi chú
Nếu repo là private, bạn cần dùng SSH key hoặc GitHub token để git clone.
Dữ liệu văn bản (document.json) hiện đang bảo trì, có thể bỏ qua khi chỉ dùng media.

## 💡 Tác giả
Dự án xây dựng bởi Kagami , định hướng phát triển trợ lý ảo thông minh ứng dụng vào lĩnh vực tìm kiếm thông tin từ video/audio theo ngôn ngữ tự nhiên.
