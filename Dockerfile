# Dựa trên image cơ bản nào
FROM python:3

# Khai báo thư mục làm việc
WORKDIR /Users/apple/Desktop/mai/BulletSv

# Copy toàn bộ file mã nguồn và các file khác vào image
COPY . .

# Cài đặt Flask
RUN pip install -r requirements.txt