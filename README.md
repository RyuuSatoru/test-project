🧠 test-project
Trợ lý truy vấn dữ liệu đa phương tiện
Dự án AI này hỗ trợ truy vấn thông minh trên nhiều định dạng dữ liệu như video, ảnh, âm thanh, và văn bản — tất cả được xử lý trước, chuẩn hóa, và phản hồi qua mô hình ngôn ngữ lớn (LLM).

🎯 Mục tiêu: Trích xuất và phân tích dữ liệu đa phương tiện để hỗ trợ tìm kiếm thông tin bằng ngôn ngữ tự nhiên.

🚀 Tính năng chính
✅ Tự động nhận diện loại dữ liệu cần xử lý từ prompt người dùng.

🧩 Hỗ trợ 4 loại dữ liệu: video, image, audio, và document.

📚 Kết hợp thông tin ngữ cảnh vào prompt đầu vào.

🤖 Gửi prompt đầy đủ đến LLM (như Gemini / GPT) để phản hồi.

🧪 Chạy hoàn toàn được trên Google Colab hoặc máy cục bộ.

🛠 Dễ mở rộng và chỉnh sửa: mọi phần xử lý chia thành các module riêng.

📓 Dùng trên Google Colab
Bạn có thể chạy toàn bộ project này chỉ trong vài bước đơn giản:

1. Tải project
!git clone [https://github.com/RyuuSatoru/test-similar.git](https://github.com/RyuuSatoru/test-similar.git)
%cd test-similar

2. Cài thư viện
!pip install -q --progress-bar off -r requirements.txt

3. Tiền xử lý dữ liệu media
!python Run-test.py 2>/dev/null

4. Khởi chạy truy vấn (có UI nhập prompt)
Mở file project.ipynb, chạy các ô để nhập prompt và nhận phản hồi từ LLM.

💻 Dùng trên máy cục bộ (Local Machine)
git clone [https://github.com/RyuuSatoru/test-similar.git](https://github.com/RyuuSatoru/test-similar.git)
cd test-similar
pip install -r requirements.txt
python Run-test.py
python Run.py

📍 Ghi chú

Nếu repo là private, bạn cần dùng SSH key hoặc GitHub token để git clone.

Dữ liệu văn bản (document.json) hiện đang bảo trì, có thể bỏ qua khi chỉ dùng media.

💡 Tác giả
Dự án xây dựng bởi nhà nghiên cứu AI chuyên sâu, định hướng phát triển trợ lý ảo thông minh ứng dụng vào lĩnh vực tìm kiếm thông tin từ video/audio theo ngôn ngữ tự nhiên.
