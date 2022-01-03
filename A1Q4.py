def sum_of_dice_rolls():
   d6=[1,2,3,4,5,6]
   total1=[0]
   total2=[0]
   total3=[0]
   total4=[0]
   total5=[0]
   total6=[0]
   totals = [total1,total2,total3,total4,total5,total6]
   count2=[0]
   count3=[0]
   count4=[0]
   count5=[0]
   count6=[0]
   count7=[0]
   count8=[0]
   count9=[0]
   count10=[0]
   count11=[0]
   count12=[0]
   rolls2=[0]
   rolls3=[0]
   rolls4=[0]
   rolls5=[0]
   rolls6=[0]
   rolls7=[0]
   rolls8=[0]
   rolls9=[0]
   rolls10=[0]
   rolls11=[0]
   rolls12=[0]
   for i in d6:
       if d6 == ' ':
           break
       for j in d6:
           if d6 == ' ':
               break
           for k in d6:
               if d6 == ' ':
                   break
               for l in d6:
                   if d6 == ' ':
                       break
                   total1 = l+k
                   total2 = l+j
                   total3 = l+i
                   total4 = k+j
                   total5 = k+i
                   total6 = j+i
                   if 2 in totals:
                       count2+1
                       rolls2+1
                   else:
                       count2=count2
                   if 3 in totals:
                       count3+1
                       rolls3+1
                   else:
                       count3=count3
                   if 4 in totals:
                       count4+1
                       rolls4+1
                   else:
                       count4=count4
                   if 5 in totals:
                       count5+1
                       rolls5+1
                   else:
                       count5=count3
                   if 6 in totals:
                       count6+1
                       rolls6+1
                   else:
                       count6=count3    
                   if 7 in totals:
                       count7+1
                       rolls7+1
                   else:
                       count7=count7
                   if 8 in totals:
                       count8+1
                       rolls8+1
                   else:
                       count8=count8    
                   if 9 in totals:
                       count9+1
                       rolls9+1
                   else:
                       count9=count9  
                   if 10 in totals:
                       count10+1
                       rolls10+1
                   else:
                       count10=count10   
                   if 11 in totals:
                       count11+1
                       rolls11+1
                   else:
                       count11=count11   
                   if 12 in totals:
                       count12+1
                       rolls12+1
                   else:
                       count12=count12
   print('sum 2 is:', count2) 
   print('percentage is:', count2/1296)                 
   print('sum 3 is:', count3) 
   print('percentage is:', count2/1296)   
   print('sum 4 is:', count4) 
   print('percentage is:', count2/1296)
   print('sum 5 is:', count5) 
   print('percentage is:', count2/1296)
   print('sum 6 is:', count6) 
   print('percentage is:', count2/1296)
   print('sum 7 is:', count7) 
   print('percentage is:', count2/1296)
   print('sum 8 is:', count8) 
   print('percentage is:', count2/1296)
   print('sum 9 is:', count9) 
   print('percentage is:', count2/1296)
   print('sum 10 is:', count10) 
   print('percentage is:', count2/1296)
   print('sum 11 is:', count11) 
   print('percentage is:', count2/1296)
   print('sum 12 is:', count12) 
   print('percentage is:', count2/1296)
   grossh = 0
   grossl = 999999
   highest = [rolls2,rolls3,rolls4,rolls5,rolls6,rolls7,rolls8,rolls9,rolls10,rolls11,rolls12]
   for i in highest:
       if i > grossh:
           grossh=i
       else:
           continue
   for i in highest:
       if i < grossl:
           grossl=i
       else:
           continue
   print('highest grossing number', grossh)
   print("lowest grossing number", grossl)