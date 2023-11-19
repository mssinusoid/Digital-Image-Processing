# Công thức 
$s_{k} = T(r_{k}) = (L-1)\sum ^{k}_{j=0}p_{r}\left( r_{j}\right)$

trong đó:
- s : giá trị của pixel sau khi cân bằng
- r : giá trị của pixel trước khi cân bằng
- $p_{r}(r_{k})$ : xác suất xuất hiện pixel mang giá trị $r_{k}$ trong ảnh chưa cân bằng (bằng thương của số pixel có giá trị giá trị $r_{k}$ trên tổng số pixel cấu thành nên ảnh (M là số hàng, N là số cột, MxN sẽ ra tổng số pixel)) $$p_{r} \left( r_{k}\right) =\dfrac{n_{k}}{MN}$$
- Vậy $\sum ^{k}_{j=0}p_{r}\left( r_{j}\right)$ là xác suất tích luỹ của các pixel có giá trị từ 0 cho đến $r_{k}$ 

# Giải thích một số hàm được dùng
np.histogram(gray, np.arange(256))
---
trả về histogram (lần lượt số lượng pixel tại các điểm trong bin) và bin_egdes (các mức cường độ của pixel)

`def histogram(a, bins=10, range=None, density=None, weights=None)`
- a: Mảng một chiều chứa các giá trị pixel của ảnh. Tuy nhiên nếu đưa vào mảng nhiều chiều thì vẫn ok vì nó tự làm phẳng (flatten).
- bins = np.arange(256): bin edges là mảng các giá trị nguyên thuộc khoảng [0, 255]

plt.hist(gray.flatten(), bins)
---
vẽ histo của ảnh, nhưng ảnh đưa vào phải được làm phẳng (đưa về dạng một chiều) chứ không có tự làm phẳng như np.histogram

hist = cv2.calcHist([img],[0],None,[256],ranges=[0,256])
---
trả về một mảng of histogram **points** (tức là vừa có toạ độ x, vừa có toạ độ y?)

image=[img] : list các ảnh
channels=[0]: list các kênh
mask=None: tính hết, không chừa miếng nào
histSize= [256] : số bins
ranges=[0,256]: dải giá trị là từ 0 đến 255, ừ, không gồm 256 đâu

equ = s[img]
---
Qua `equ = np.zeros_like(img)` thì equ bây giờ đã là một ma trận có kích thước bằng ảnh ban đầu toàn chứa giá trị 0

s là một mảng gồm 256 phần tử tương ứng với 256 giá trị của ảnh gốc ánh xạ sang

-> giả sử `img[x, y]` có giá trị `100`, thì `equ[x, y]` có giá trị `s[100]`, cái 100 trong s[100] nó vừa là giá trị, nó vừa là chỉ số ấy, hiểu hong? vì r ban đầu



