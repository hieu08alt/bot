# bot

**Setup Bot:**
- Setup ban đầu:
1. Tạo tài khoản Discord và tạo bot *(search google)*
2. Tải Python: "https://www.python.org/downloads/" (nên xài Python 3.7)
3. Tải Discordpy: vô Command Prompt gõ `pip install discord.py`
4. Tải ide để code :/

- Setup Bot:
1. Mở file config.json
2. Bỏ Token của bot vào trong key `"TOKEN"`
3. ghi tên author bot vào key `"author"`
4. bỏ thời gian vào key `"mute_time"` *(đơn vị: second)*
5. bỏ id của channel cần thông báo mute vào key `"id_channel_send"`

Demo
```json
{
  "TOKEN": "JIasdoisadpojsandjasio",
  "author": "hieudeptrai#8265",
  "mute_time": 900,
  "id_channel_send": 930811651014418472
}
```

**Lưu ý**
- Chạy file: `main.py` để có bot hoạt động. vô Command Prompt ghi `python3 main.py` *(Lưu ý phải chuyển đến thư mục chứa file main)*
- Có thể thay đổi hoặc thêm những từ **NÓI TỤC** bằng những từ khác. Nhưng bạn phải đảm bảo là mỗi từ một dòng, cấm ghi 2 hoặc nhiều từ ở lên ghi 1 dòng.
- Có 2 file Bad Word là `bad_word.txt` và `bad_word1.txt`
+ File `bad_word.txt` là file chính, khi phát hiện từ nói tục thì lật tức mute
+ FIle `bad_word1.txt` là file phụ, nó sẽ được thêm kí tự trắng ở cuối từ nhằm đảm bảo bot không mute nhầm *(nhưng mà giảm tính bảo mật)*
- Nếu bạn muốn bot chạy 24/7 thì bạn cần một nơi để host. Thì cái đấy bạn từ tìm hiểu nhé.
