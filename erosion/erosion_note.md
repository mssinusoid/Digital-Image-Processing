**object**: sets of foreground pixels 

**structuring elements** (SE's): theo mình đang hiểu thì nó giống như một cửa sổ hình chữ nhật, phủ lên object cần xử lý (chỗ nào phủ lên object thì chứa một giá trị vs như True, chỗ nào không phủ thì chứa một giá trị- vs như False)
### Erosion
Co ảnh -> tức là mình muốn làm ảnh nhỏ đi, nhưng không phải là zoom to zoom nhỏ, mà là làm giảm số lượng pixel biểu diễn object. (Chứ còn ảnh đầu vào có kích thước bao nhiêu thì đầu ra vẫn y thế nha)
Với A và B là set trong $Z^{2}$, phép co của A bởi B kí hiệu là $$A\ominus B=\left\{  z| \left( B\right) _{z}\subseteq A\right\} $$
trong đó, 
- A là set các foreground pixels
- B là phần tử cấu trúc (structuring element)
- z là các giá trị foreground.

Nhưng như thế mới chỉ thu được foreground (object) đã co thôi, mình cần đầu ra là một ảnh cơ (có cả foreground + background) $$\begin{aligned}I\ominus B=\left\{  z| \left( B\right) _{z}\subseteq A~and~A\subseteq I\right\} \cup \left\{  A^{c}| A^{c}\subseteq I\right\} \end{aligned}$$
Vậy là mấy cái trên chỉ dùng được cho ảnh nhị phân thôi, còn ảnh xám thì phải có kiểu khác