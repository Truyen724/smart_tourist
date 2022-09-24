# chương trình cung hoàng đạo với hàm 

def hoang_dao(ngay,thang):
        if((ngay >= 21 and thang == 3) or (ngay <= 19 and thang == 4)):
                print( "bạn thuộc nguyên tố lửa, cung Bạch Dương" )   
                return "FIRE"       
        elif((ngay >= 20 and thang == 4) or (ngay <= 20 and thang == 5)):
                print( " bạn thuộc nguyên tố đất, cung Kim Ngưu" )  
                return "EARTH" 
        elif((ngay >= 21 and  thang == 5) or (ngay <= 21 and thang == 6)):
                print( " bạn thuộc nguyên tố khí,Cung Song Tử ")             
                return "AIR"
        elif((ngay >= 22 and  thang == 6) or (ngay <= 22 and thang == 7)):
                print( "bạn thuộc nguyên tố nước, Cung Cự Giải" )   
                return "WATER"
        elif((ngay >= 23 and  thang == 7) or (ngay <= 22 and thang == 8)):
                print( "bạn thuộc nguyên tố lửa, Cung Sư Tử" )    
                return "FIRE"       
        elif((ngay >= 23 and thang == 8) or (ngay <= 22  and thang == 9)):
                print( " bạn thuộc nguyên tố đất, Cung Xử Nữ" )  
                return "EARTH" 
        elif((ngay >= 23 and  thang == 9) or (ngay <= 23 and thang == 10)):
                print( " bạn thuộc nguyên tố khí, Cung Thiên Bình ")             
                return "AIR"
        elif((ngay >= 24 and  thang == 10) or (ngay <= 2 and  thang == 11)):
                print( "bạn thuộc nguyên tố nước, Cung Bọ Cạp" )   
                return "WATER"                                                              
        elif((ngay >= 22 and  thang == 11) or (ngay <= 2 and thang == 12)):
        
                print( "bạn thuộc nguyên tố lửa, Cung Nhân Mã" )    
                return "FIRE"                           
        elif((ngay >= 22 and  thang == 12) or (ngay >= 1 and thang == 1)):
        
                print( " bạn thuộc nguyên tố đất, Cung Ma Kết" )  
                return "EARTH"                      
        elif((ngay >= 20 and thang == 1) or (ngay <= 18  and thang == 2)):
        
                print( " bạn thuộc nguyên tố khí, Cung Bảo Bình ")             
                return "AIR"   
        else:
                print( " bạn thuộc nguyên tố khí, Cung Song Ngư ")  
                return "WATER" 
