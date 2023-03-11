def transform(self,x ,y):
    if self.perspective_mode == '2d':
        return self.transform_2D(x, y)  
    else:
        return self.transform_perspective(x, y) 
    
def transform_2D(self, x, y):
    return int(x), int(y)
    
def transform_perspective(self, x, y):
    y_lin = y * self.perspective_point_y / self.height
    if y_lin > self.perspective_point_y:
        y_lin = self.perspective_point_y
        
    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - y_lin
    factor_y = diff_y / self.perspective_point_y
    factor_y = factor_y ** 3
        
    x_tr = self.perspective_point_x + diff_x * factor_y
    y_tr = self.perspective_point_y - factor_y * self.perspective_point_y
    
    return int(x_tr), int(y_tr)