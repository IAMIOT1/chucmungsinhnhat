import http.server
import socketserver
import webbrowser

PORT = 8000

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Trả về 204 No Content nếu trình duyệt yêu cầu favicon.ico để tránh rác log 404
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return
        super().do_GET()

def run_server():
    # Cho phép sử dụng lại cổng nhanh nếu bạn bật/tắt script liên tục
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        print(f"✨ Server thiệp sinh nhật đang chạy tại: http://localhost:{PORT}")
        print("Đang tự động mở trình duyệt...")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã tắt Server thành công.")

if __name__ == "__main__":
    run_server()