Ý tưởng: Thông thường phân ngưỡng là mình chọn ra một giá trị, rồi những pixel nào có giá trị nhỏ hơn hoặc bằng ngưỡng thì cho về 0, những pixel nào có giá trị lớn hơn ngưỡng thì đưa về 255 (với trường hợp 8 bit). Nhưng đấy là chọn ngưỡng thủ công, làm sao biết được chọn ngưỡng bằng bao nhiêu thì ảnh kết quả sẽ tốt nhất (nhìn rõ nhất ?) -> việc Otsu làm.

Giả dụ ngưỡng được chọn là $T(k) = k, 0 < k < L-1$. Việc phân ngưỡng chia ảnh thành 2 class $c_{1}$ và $c_{2}$. $c_{1}$ chứa các pixel có intensity dưới hoặc bằng ngưỡng (trong đoạn `[0, k]`), $c_{2}$ chứa các pixel trong đoạn `[k+1, L-1]`.
Tương ứng với đó:
- $P_{1}$ là xác suất để một pixel rơi vào class $c_{1}$ (tức bằng tổng số pixel thuộc class $c_{1}$ trên tổng số pixel), tương tự với $P_{2}$. ($P_{1} + P_{2} = 1$)
- $m_{1}$ là mean intensity trong class $c_{1}$ (tức bằng tổng tất cả intensity của các pixel trong $c_{1}$ trên tổng số pixel trong $c_{1}$)
- $m_{G}$ là avarage intensity của cả ảnh (tức bằng tổng tất cả intensity của các pixel trên cả ảnh trên tổng số pixel có trong ảnh)

>[!note] Phương sai giữa hai class (between-class variance)
>$$\sigma ^{2}_{B} = P_{1}(m_{1} - m_{G})^{2} + P_{2}(m_{2} - m_{G})^{2}$$
>xong qua 7749 phép biến đổi toán học sẽ ra được: $$\sigma ^{2}_{B} = P_{1}P_{2}(m_{1} - m_{2})^{2} = \dfrac{(m_{G}P_{1} - m)^{2}}{P_{1}[1-P_{1}]}$$

- - -

1. Tính xác suất phân phối của của các mức xám. Vd có L-1 mức xám thì tính xem mức xám có giá trị 0 chiếm bao nhiêu phần, mức xám có giá trị 1 chiếm bao nhiêu phần,..., mức xám L-1 chiếm bao nhiêu phần.
$$p_{i} = \dfrac{\text{số pixel có mức xám i}}{\text{tổng số pixel}}$$
2. Tính tổng tính luỹ của $P_{1}(k)$ với $k = 0, 1, 2,..., L-1$: $$P_{1}(k) = \sum_{i=0}^{k}p_{i}$$
3. Tính trung bình tích luỹ $m(k)$ với $k = 0, 1, 2,..., L-1$:
$$m(k) = \sum_{i=0}^{k}ip_{i}$$
intensity tích luỹ trung bình
4. Tính trung bình toàn cục (global mean) $m_{G}$ 
$$m_{G} = \sum_{i=0}^{L-1}ip_{i}$$

5. Tính phương sai giữa hai class $\sigma ^{2}_{B}(k)$ với k $k = 0, 1, 2,..., L-1$
$$\sigma ^{2}_{B}(k) = \dfrac{[m_{G}P_{1}(k) - m(k)]^{2}}{P_{1}(k)-[1-P_{1}(k)]}$$
mà **ý tưởng của Otsu là tối đa sự sai khác giữa hai class ()**
=> chọn k* là k tối ưu làm phương sai lớn nhất. Nếu có nhiều giá trị k khiến phương sai cực đại thì chọn trung bình của các k làm cho phương sai cực đại.