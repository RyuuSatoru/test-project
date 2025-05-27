# 🧠 test-project

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

### 1. Tải project
```python
!git clone [https://github.com/RyuuSatoru/test-similar.git](https://github.com/RyuuSatoru/test-similar.git)
%cd test-similar
