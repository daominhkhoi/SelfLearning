import os

def rename_jpg_files_sequentially():
    """
    Đổi tên tất cả các file .jpg trong thư mục hiện tại thành 1.jpg, 2.jpg, ...
    """
    current_directory = "."
    jpg_files = []

    # Thu thập tất cả các file .jpg trong thư mục hiện tại
    for filename in os.listdir(current_directory):
        if filename.lower().endswith(".jpg"):
            jpg_files.append(filename)

    # Sắp xếp các file để đảm bảo thứ tự đổi tên nhất quán
    jpg_files.sort()

    print(f"Tìm thấy {len(jpg_files)} file .jpg để đổi tên.")

    # Đổi tên các file
    for i, old_name in enumerate(jpg_files):
        new_name = f"{i + 1}.jpg" # Tên mới: 1.jpg, 2.jpg, v.v.
        old_path = os.path.join(current_directory, old_name)
        new_path = os.path.join(current_directory, new_name)

        # Xử lý trường hợp tên file mới đã tồn tại
        if os.path.exists(new_path) and old_path != new_path:
            print(f"Cảnh báo: File '{new_name}' đã tồn tại. Không thể đổi tên '{old_name}' để tránh ghi đè.")
            continue # Bỏ qua file này để tránh ghi đè

        try:
            os.rename(old_path, new_path)
            print(f"Đã đổi tên '{old_name}' thành '{new_name}'")
        except OSError as e:
            print(f"Lỗi khi đổi tên '{old_name}' thành '{new_name}': {e}")

if __name__ == "__main__":
    rename_jpg_files_sequentially()
