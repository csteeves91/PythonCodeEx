import re
class dictionary_operations():
    
    Id = { 'Id_1': {"Name": 'XYZ',"Contact_Number":{"Work" : '666-666-666'}},
              'Id_2': {"Name":'PQR', "Contact_Number": {"Work":'888-888-8888',"Home":'111-111-1111'}},
              'Id_3': {"Name": 'ABC',"Contact_Number":{"Work": '777-777-7777', "Cell": '222-222-2222'}}}

    for i_id, i_info in Id.items():
        print("ID:", i_id)
        
        print('Name:',i_info['Name'])
        print('Contact_Number:')
        for i_type, i_num in i_info['Contact_Number'].items():
            print(i_type,":", i_num)
        
        print()
            

    Id['Id_4']={"Name":'QWE','Contact_Number':{'Work':'567-890-1234'}}
    
    for i_id, i_info in Id.items():
        print("ID:", i_id)
        
        print('Name:',i_info['Name'])
        print('Contact_Number:')
        for i_type, i_num in i_info['Contact_Number'].items():
            print(i_type,":", i_num)
        
        print()

       
    txt = input("Please input a number:")
    i = re.match("\d\d\d-\d\d\d-\d\d\d\d",txt)
    
    if i:
       Id['Id_2']['Contact_Number']['Home']= txt
       for i_id, i_info in Id.items():
                print("ID:", i_id)
        
                print('Name:',i_info['Name'])
                print('Contact_Number:')
                for i_type, i_num in i_info['Contact_Number'].items():
                    print(i_type,":", i_num)
        
                print()
           
    else:
        
            print("\nInvalid number, reenter")
            
            
    del Id['Id_3']['Contact_Number']['Work']
    del Id['Id_3']['Contact_Number']['Cell']
    for i_id, i_info in Id.items():
                print("ID:", i_id)
        
                print('Name:',i_info['Name'])
                print('Contact_Number:')
                for i_type, i_num in i_info['Contact_Number'].items():
                    print(i_type,":", i_num)
        
                print()