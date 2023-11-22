**Arithmetic Mean Filter** 
là bộ lọc đơn giản nhất trong các bộ lọc trung bình (giống với Box filter kernels): thay thế pixel trung tâm bằng trung bình cộng tất cả các giá trị pixel của ảnh được phủ bởi bộ lọc 

Giá trị phục hồi (restored) của ảnh $\widehat{f}$ tại điểm $(x, y)$ được tính bằng: $$\begin{aligned}\widehat{f}\left( x,y\right) =\dfrac{1}{mn} \sum_{\left( r,c\right) \in S_{xy}} g\left( r,c\right)\end{aligned}$$
trong đó:
- $S_{xy}$ là tập hợp các toạ độ của ảnh bị phủ bởi bộ lọc  
- mn là số pixel của tập $S_(xy)$ vì của sổ lọc là một hình chữ nhật có kích thước mxn, tâm tại điểm (x, y)
- $g(x, y)$ là ảnh ban đầu chưa được phục hồi (corrupted image)